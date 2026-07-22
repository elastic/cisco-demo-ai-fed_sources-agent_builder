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
    sites = [
        ("Branch-4471-Dallas", "MR-AP-4471", "Q2XX-4471-ABCD"),
        ("Branch-2201-Austin", "MR-AP-2201", "Q2XX-2201-EFGH"),
        ("Branch-1108-Chicago", "MR-AP-1108", "Q2XX-1108-IJKL"),
        ("Branch-3302-Seattle", "MR-AP-3302", "Q2XX-3302-MNOP"),
        ("Branch-5504-NYC", "MR-AP-5504", "Q2XX-5504-QRST"),
    ]
    # Seed ~24h of Meraki connector events so dashboard timelines look alive.
    events: list[dict] = []
    for hour in range(24, 0, -1):
        for idx, (site, device, serial) in enumerate(sites):
            ts = now - timedelta(hours=hour, minutes=(idx * 7) % 50)
            # Branch 4471 goes offline near "now"; others flap online/offline lightly.
            if site.endswith("Dallas") and hour <= 1:
                etype, detail = "device.offline", "AP lost cloud connectivity; last seen on switch port Gi1/0/24"
            elif hour % 5 == idx % 5:
                etype, detail = "device.offline", "Brief cloud disconnect; monitoring"
            else:
                etype, detail = "device.online", "AP healthy / reconnected"
            events.append(
                {
                    "@timestamp": ts.isoformat(),
                    "source": "meraki_connector",
                    "device_name": device,
                    "device_serial": serial,
                    "site": site,
                    "event_type": etype,
                    "detail": detail,
                }
            )
    # Anchor docs used by challenge queries
    events.append(
        {
            "@timestamp": (now - timedelta(minutes=12)).isoformat(),
            "source": "meraki_connector",
            "device_name": "MR-AP-4471",
            "device_serial": "Q2XX-4471-ABCD",
            "site": "Branch-4471-Dallas",
            "event_type": "device.offline",
            "detail": "AP lost cloud connectivity; last seen on switch port Gi1/0/24",
        }
    )
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

    net_sites = [
        ("Branch-4471-Dallas", "edge-dfw-01", "dist-dfw-02"),
        ("Branch-2201-Austin", "edge-aus-01", "dist-aus-02"),
        ("Branch-1108-Chicago", "edge-ord-01", "dist-ord-02"),
        ("Branch-3302-Seattle", "edge-sea-01", "dist-sea-02"),
        ("Branch-5504-NYC", "edge-nyc-01", "dist-nyc-02"),
    ]
    net_events: list[dict] = []
    for hour in range(24, 0, -1):
        for idx, (site, edge, dist) in enumerate(net_sites):
            ts = now - timedelta(hours=hour, minutes=(idx * 11) % 45)
            if site.endswith("Dallas") and hour <= 1:
                net_events.append(
                    {
                        "@timestamp": ts.isoformat(),
                        "message": "BGP neighbor 10.0.0.1 changed state from Established to Idle",
                        "event_type": "bgp.session_down",
                        "host.name": edge,
                        "cisco.product": "IOS-XE",
                        "cisco.site": site,
                    }
                )
            elif hour % 6 == idx:
                net_events.append(
                    {
                        "@timestamp": ts.isoformat(),
                        "message": f"DNA Assurance health score dropped on switch {dist}",
                        "event_type": "dna.assurance.alert",
                        "host.name": dist,
                        "cisco.product": "DNA Center",
                        "cisco.site": site,
                    }
                )
            else:
                net_events.append(
                    {
                        "@timestamp": ts.isoformat(),
                        "message": f"BGP neighbor session Established on {edge}",
                        "event_type": "bgp.session_up",
                        "host.name": edge,
                        "cisco.product": "IOS-XE",
                        "cisco.site": site,
                    }
                )
    net_events.append(
        {
            "@timestamp": (now - timedelta(minutes=8)).isoformat(),
            "message": "BGP neighbor 10.0.0.1 changed state from Established to Idle",
            "event_type": "bgp.session_down",
            "host.name": "edge-dfw-01",
            "cisco.product": "IOS-XE",
            "cisco.site": "Branch-4471-Dallas",
        }
    )
    nlines: list[str] = []
    for i, ev in enumerate(net_events):
        nlines.append(json.dumps({"index": {"_index": "cisco-network-events", "_id": f"net-{i}"}}))
        nlines.append(json.dumps(ev))
    bulk(es_url, header, nlines)

    print(
        "Search workshop indices ready: cisco-network-kb, cisco-internal-runbooks, "
        f"cisco-meraki-events ({len(events)} docs), cisco-network-events ({len(net_events)} docs)"
    )

    # Dashboards + workflows + Cisco NOC Copilot agent (best-effort — indices already seeded)
    for mod_name in ("seed_cisco_dashboards", "seed_cisco_workflows", "seed_cisco_agent"):
        try:
            mod = __import__(mod_name)
            rc = mod.main()
            if rc != 0:
                print(f"warn: {mod_name} returned non-zero", file=sys.stderr)
        except Exception as exc:  # noqa: BLE001
            print(f"warn: {mod_name} skipped: {exc}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
