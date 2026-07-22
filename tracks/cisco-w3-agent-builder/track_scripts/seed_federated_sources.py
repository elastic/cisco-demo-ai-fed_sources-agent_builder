#!/usr/bin/env python3
"""Seed KB + internal runbooks + Meraki-style connector events for federated lab."""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Reuse KB seed
sys.path.insert(0, str(Path(__file__).resolve().parent))
import seed_cisco_kb  # noqa: E402


def auth_header() -> str:
    h, _ = seed_cisco_kb.auth_header()
    return h


def bulk(es_url: str, header: str, lines: list[str]) -> None:
    payload = "\n".join(lines) + "\n"
    code, body = seed_cisco_kb.request("POST", f"{es_url}/_bulk", header, payload.encode())
    if code not in (200, 201):
        raise RuntimeError(f"bulk failed {code}: {body[:500]}")


def ensure_index(es_url: str, header: str, name: str, mapping: dict) -> None:
    code, body = seed_cisco_kb.request(
        "PUT", f"{es_url}/{name}", header, json.dumps(mapping).encode()
    )
    if code not in (200, 201):
        print(f"warn: index {name} HTTP {code}: {body[:200]}", file=sys.stderr)


def main() -> int:
    if seed_cisco_kb.main() != 0:
        return 1

    es_url = (os.environ.get("ES_URL") or "").rstrip("/")
    header = auth_header()
    if not es_url or not header:
        return 1

    ensure_index(
        es_url,
        header,
        "cisco-internal-runbooks",
        {
            "mappings": {
                "properties": {
                    "title": {"type": "text"},
                    "content": {"type": "text"},
                    "team": {"type": "keyword"},
                    "severity": {"type": "keyword"},
                }
            }
        },
    )

    internal = [
        {
            "title": "NOC escalation — dual WAN + Meraki offline",
            "team": "Global NOC",
            "severity": "P2",
            "content": "If Meraki AP offline coincides with BGP flap, check upstream ISP and site power. Page transport team after 15 minutes. Reference public KB Meraki AP Offline Recovery.",
        },
        {
            "title": "Change window — IOS-XE BGP hold-timer",
            "team": "Core Routing",
            "severity": "P3",
            "content": "Document hold-timer changes in change ticket. Rollback if neighbor count drops below baseline.",
        },
    ]
    lines: list[str] = []
    for i, doc in enumerate(internal):
        lines.append(json.dumps({"index": {"_index": "cisco-internal-runbooks", "_id": f"runbook-{i}"}}))
        lines.append(json.dumps(doc))
    bulk(es_url, header, lines)

    ensure_index(
        es_url,
        header,
        "cisco-meraki-events",
        {
            "mappings": {
                "properties": {
                    "@timestamp": {"type": "date"},
                    "source": {"type": "keyword"},
                    "device_name": {"type": "keyword"},
                    "device_serial": {"type": "keyword"},
                    "site": {"type": "keyword"},
                    "event_type": {"type": "keyword"},
                    "detail": {"type": "text"},
                }
            }
        },
    )

    now = datetime.now(timezone.utc)
    events = [
        {
            "@timestamp": (now - timedelta(minutes=12)).isoformat(),
            "source": "meraki_connector",
            "device_name": "MR-AP-4471",
            "device_serial": "Q2XX-4471-ABCD",
            "site": "Branch-4471-Dallas",
            "event_type": "device.offline",
            "detail": "AP lost cloud connectivity; last seen on switch port Gi1/0/24",
        },
        {
            "@timestamp": (now - timedelta(minutes=45)).isoformat(),
            "source": "meraki_connector",
            "device_name": "MR-AP-2201",
            "device_serial": "Q2XX-2201-EFGH",
            "site": "Branch-2201-Austin",
            "event_type": "device.online",
            "detail": "AP reconnected after PoE bounce",
        },
    ]
    elines: list[str] = []
    for i, ev in enumerate(events):
        elines.append(json.dumps({"index": {"_index": "cisco-meraki-events", "_id": f"ev-{i}"}}))
        elines.append(json.dumps(ev))
    bulk(es_url, header, elines)

    ensure_index(
        es_url,
        header,
        "cisco-network-events",
        {
            "mappings": {
                "properties": {
                    "@timestamp": {"type": "date"},
                    "message": {"type": "text"},
                    "event_type": {"type": "keyword"},
                    "host.name": {"type": "keyword"},
                    "cisco.product": {"type": "keyword"},
                    "cisco.site": {"type": "keyword"},
                }
            }
        },
    )

    net_events = [
        {
            "@timestamp": (now - timedelta(minutes=8)).isoformat(),
            "message": "BGP neighbor 10.0.0.1 changed state from Established to Idle",
            "event_type": "bgp.session_down",
            "host.name": "edge-dfw-01",
            "cisco.product": "IOS-XE",
            "cisco.site": "Branch-4471-Dallas",
        },
        {
            "@timestamp": (now - timedelta(minutes=30)).isoformat(),
            "message": "DNA Assurance health score dropped to 6.2 on switch dist-dfw-02",
            "event_type": "dna.assurance.alert",
            "host.name": "dist-dfw-02",
            "cisco.product": "DNA Center",
            "cisco.site": "Branch-4471-Dallas",
        },
    ]
    nlines: list[str] = []
    for i, ev in enumerate(net_events):
        nlines.append(json.dumps({"index": {"_index": "cisco-network-events", "_id": f"net-{i}"}}))
        nlines.append(json.dumps(ev))
    bulk(es_url, header, nlines)

    print(
        "Search workshop indices ready: cisco-network-kb, cisco-internal-runbooks, "
        "cisco-meraki-events, cisco-network-events"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
