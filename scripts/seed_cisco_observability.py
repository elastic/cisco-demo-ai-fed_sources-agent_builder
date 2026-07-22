#!/usr/bin/env python3
"""Seed sample Cisco network logs for Observability / Agent Builder lab."""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

INDEX = "logs-cisco.network-default"


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


def main() -> int:
    es_url = (os.environ.get("ES_URL") or "").rstrip("/")
    header, mode = auth_header()
    if not es_url or not header:
        print("ERROR: ES_URL and credentials required", file=sys.stderr)
        return 1

    mapping = {
        "mappings": {
            "properties": {
                "@timestamp": {"type": "date"},
                "message": {"type": "text"},
                "event.category": {"type": "keyword"},
                "event.type": {"type": "keyword"},
                "host.name": {"type": "keyword"},
                "cisco.product": {"type": "keyword"},
                "cisco.site": {"type": "keyword"},
            }
        }
    }
    code, body = request("PUT", f"{es_url}/{INDEX}", header, json.dumps(mapping).encode())
    if code not in (200, 201):
        print(f"Index create HTTP {code}: {body[:400]}", file=sys.stderr)

    now = datetime.now(timezone.utc)
    events = [
        {
            "@timestamp": (now - timedelta(minutes=8)).isoformat(),
            "message": "BGP neighbor 10.0.0.1 changed state from Established to Idle",
            "event.category": "network",
            "event.type": "bgp.session_down",
            "host.name": "edge-dfw-01",
            "cisco.product": "IOS-XE",
            "cisco.site": "Branch-4471-Dallas",
        },
        {
            "@timestamp": (now - timedelta(minutes=10)).isoformat(),
            "message": "Meraki MR-AP-4471 offline — cloud connectivity lost",
            "event.category": "network",
            "event.type": "meraki.device.offline",
            "host.name": "MR-AP-4471",
            "cisco.product": "Meraki",
            "cisco.site": "Branch-4471-Dallas",
        },
        {
            "@timestamp": (now - timedelta(minutes=30)).isoformat(),
            "message": "DNA Assurance health score dropped to 6.2 on switch dist-dfw-02",
            "event.category": "network",
            "event.type": "dna.assurance.alert",
            "host.name": "dist-dfw-02",
            "cisco.product": "DNA Center",
            "cisco.site": "Branch-4471-Dallas",
        },
    ]

    lines: list[str] = []
    for i, doc in enumerate(events):
        lines.append(json.dumps({"index": {"_index": INDEX, "_id": f"log-{i}"}}))
        lines.append(json.dumps(doc))
    payload = "\n".join(lines) + "\n"
    code, body = request("POST", f"{es_url}/_bulk", header, payload.encode())
    if code not in (200, 201):
        print(f"Bulk HTTP {code}: {body[:600]}", file=sys.stderr)
        return 1

    print(f"Indexed {len(events)} logs into {INDEX} (auth={mode})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
