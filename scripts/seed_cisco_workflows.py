#!/usr/bin/env python3
"""Upsert Cisco workshop workflows into Kibana (Serverless Search)."""
from __future__ import annotations

import gzip
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

WORKFLOW_ID = "cisco-branch-4471-splunk-o11y-a2a-rca"
WORKFLOW_FILE = "cisco-branch-4471-splunk-o11y-a2a-rca.yaml"


def decode(raw: bytes) -> str:
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return raw.decode("utf-8", errors="replace")


def auth_header() -> str:
    api_key = (
        os.environ.get("ES_API_KEY")
        or os.environ.get("ELASTICSEARCH_API_KEY")
        or os.environ.get("KIBANA_API_KEY")
        or ""
    ).strip()
    if api_key:
        return f"ApiKey {api_key}"
    user = os.environ.get("ES_USERNAME", "admin")
    password = os.environ.get("ES_PASSWORD") or ""
    if password:
        import base64

        return "Basic " + base64.b64encode(f"{user}:{password}".encode()).decode()
    return ""


def kibana_base() -> str:
    return (os.environ.get("KIBANA_URL") or os.environ.get("ES_KIBANA_URL") or "").rstrip("/")


def request(method: str, url: str, header: str, body: bytes | None = None) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": header,
            "kbn-xsrf": "true",
            "Content-Type": "application/json",
            "Accept-Encoding": "identity",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.status, decode(resp.read())
    except urllib.error.HTTPError as e:
        return e.code, decode(e.read())


def workflow_yaml_path() -> Path:
    candidates = [
        Path("/tmp/workflows") / WORKFLOW_FILE,
        Path(__file__).resolve().parents[1] / "assets" / "shared" / "workflows" / WORKFLOW_FILE,
        Path("/track/assets/shared/workflows") / WORKFLOW_FILE,
    ]
    for p in candidates:
        if p.is_file():
            return p
    raise FileNotFoundError(WORKFLOW_FILE)


def main() -> int:
    base = kibana_base()
    header = auth_header()
    if not base or not header:
        print("ERROR: KIBANA_URL and API key required for workflows", file=sys.stderr)
        return 1

    yaml_text = workflow_yaml_path().read_text(encoding="utf-8")
    body = json.dumps({"id": WORKFLOW_ID, "yaml": yaml_text}).encode()

    code, resp = request("GET", f"{base}/api/workflows/workflow/{WORKFLOW_ID}", header)
    if code == 404:
        code2, resp2 = request("POST", f"{base}/api/workflows/workflow", header, body)
        if code2 not in (200, 201):
            print(f"warn: workflow create HTTP {code2}: {resp2[:400]}", file=sys.stderr)
            return 1
        print(f"workflow created: {WORKFLOW_ID}")
        return 0

    if code == 200:
        code2, resp2 = request("PUT", f"{base}/api/workflows/workflow/{WORKFLOW_ID}", header, body)
        if code2 not in (200, 201):
            print(f"warn: workflow update HTTP {code2}: {resp2[:400]}", file=sys.stderr)
            return 1
        print(f"workflow updated: {WORKFLOW_ID}")
        return 0

    # Workflows app may be unavailable on some project tiers
    print(f"warn: workflows API HTTP {code}: {resp[:300]}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
