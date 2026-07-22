#!/usr/bin/env python3
"""Bulk-index Cisco KB documents into cisco-network-kb."""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

INDEX = "cisco-network-kb"


def auth_header() -> tuple[str, str]:
    api_key = (os.environ.get("ES_API_KEY") or os.environ.get("ELASTICSEARCH_API_KEY") or "").strip()
    if api_key:
        return f"ApiKey {api_key}", "api_key"
    user = os.environ.get("ES_USERNAME", "admin")
    password = os.environ.get("ES_PASSWORD") or os.environ.get("ELASTICSEARCH_PASSWORD") or ""
    if password:
        import base64

        token = base64.b64encode(f"{user}:{password}".encode()).decode()
        return f"Basic {token}", "basic"
    return "", ""


def request(method: str, url: str, header: str, body: bytes | None = None) -> tuple[int, str]:
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Authorization", header)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def load_documents() -> list[dict]:
    candidates = [
        Path("/track/assets/shared/cisco-knowledge-base.json"),
        Path(__file__).resolve().parents[1] / "assets" / "shared" / "cisco-knowledge-base.json",
        Path("/tmp/cisco-knowledge-base.json"),
    ]
    for path in candidates:
        if path.is_file():
            data = json.loads(path.read_text(encoding="utf-8"))
            return data.get("documents") or []
    raise FileNotFoundError("cisco-knowledge-base.json not found")


def main() -> int:
    es_url = (os.environ.get("ES_URL") or "").rstrip("/")
    header, mode = auth_header()
    if not es_url or not header:
        print("ERROR: ES_URL and credentials required", file=sys.stderr)
        return 1

    # Serverless rejects index.number_of_shards / number_of_replicas settings.
    mapping = {
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "content": {"type": "text"},
                "product": {"type": "keyword"},
                "category": {"type": "keyword"},
                "keywords": {"type": "keyword"},
                "resolution_type": {"type": "keyword"},
                "domain_path": {"type": "keyword"},
                "doc_id": {"type": "keyword"},
            }
        },
    }
    code, body = request("PUT", f"{es_url}/{INDEX}", header, json.dumps(mapping).encode())
    if code not in (200, 201):
        print(f"Index create HTTP {code}: {body[:500]}", file=sys.stderr)

    docs = load_documents()
    lines: list[str] = []
    for doc in docs:
        doc_id = doc.get("doc_id") or doc.get("title", "doc")
        meta = {"index": {"_index": INDEX, "_id": doc_id}}
        lines.append(json.dumps(meta))
        lines.append(json.dumps(doc))
    payload = "\n".join(lines) + "\n"
    code, body = request("POST", f"{es_url}/_bulk", header, payload.encode())
    if code not in (200, 201):
        print(f"Bulk HTTP {code}: {body[:800]}", file=sys.stderr)
        return 1
    print(f"Indexed {len(docs)} documents into {INDEX} (auth={mode})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
