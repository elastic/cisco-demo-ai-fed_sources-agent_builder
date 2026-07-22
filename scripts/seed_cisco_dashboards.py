#!/usr/bin/env python3
"""Install Cisco workshop dashboards into Kibana (Serverless Search).

Uses POST/PUT /api/dashboards with Elastic-Api-Version 2023-10-31
(markdown + vis data_table + ES|QL) — same pattern as Adaptive Metrics Instruqt labs.
"""
from __future__ import annotations

import gzip
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

API_VERSION = os.environ.get("KIBANA_DASHBOARDS_API_VERSION", "2023-10-31")

DASHBOARDS = (
    ("cisco-noc-ops", "cisco-noc-ops.json"),
    ("cisco-kb-library", "cisco-kb-library.json"),
)


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
    password = os.environ.get("ES_PASSWORD") or os.environ.get("ELASTICSEARCH_PASSWORD") or ""
    if password:
        import base64

        return "Basic " + base64.b64encode(f"{user}:{password}".encode()).decode()
    return ""


def kibana_base() -> str:
    return (
        os.environ.get("KIBANA_URL")
        or os.environ.get("ES_KIBANA_URL")
        or ""
    ).rstrip("/")


def request(method: str, url: str, header: str, body: bytes | None = None) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": header,
            "kbn-xsrf": "true",
            "Content-Type": "application/json",
            "Elastic-Api-Version": API_VERSION,
            "Accept-Encoding": "identity",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.status, decode(resp.read())
    except urllib.error.HTTPError as e:
        return e.code, decode(e.read())


def dashboard_paths() -> list[Path]:
    roots = [
        Path("/tmp/dashboards"),
        Path(__file__).resolve().parents[1] / "assets" / "shared" / "dashboards",
        Path("/track/assets/shared/dashboards"),
    ]
    return roots


def load_spec(filename: str) -> dict:
    for root in dashboard_paths():
        path = root / filename
        if path.is_file():
            return json.loads(path.read_text(encoding="utf-8"))
    raise FileNotFoundError(f"dashboard JSON not found: {filename}")


def ensure_data_view(base: str, header: str, view_id: str, title: str, time_field: str | None) -> None:
    body: dict = {
        "data_view": {
            "id": view_id,
            "name": title,
            "title": title,
            "allowNoIndex": True,
        }
    }
    if time_field:
        body["data_view"]["timeFieldName"] = time_field
    code, resp = request(
        "POST",
        f"{base}/api/data_views/data_view",
        header,
        json.dumps(body).encode(),
    )
    if code in (200, 201):
        print(f"data view ok: {view_id}")
    elif code == 409 or "already exists" in resp.lower():
        print(f"data view exists: {view_id}")
    else:
        print(f"warn: data view {view_id} HTTP {code}: {resp[:240]}", file=sys.stderr)


def upsert_dashboard(base: str, header: str, dash_id: str, spec: dict) -> None:
    payload = dict(spec)
    payload.pop("time_from", None)
    payload.pop("time_to", None)
    payload["id"] = dash_id
    raw = json.dumps(payload).encode()

    code, resp = request("PUT", f"{base}/api/dashboards/{dash_id}", header, raw)
    if code in (200, 201):
        print(f"dashboard upserted: {dash_id} ({payload.get('title')})")
        return

    # Fallback create
    create_body = dict(payload)
    create_body.pop("id", None)
    code2, resp2 = request("POST", f"{base}/api/dashboards", header, json.dumps(create_body).encode())
    if code2 in (200, 201):
        print(f"dashboard created: {dash_id} via POST ({payload.get('title')}) — HTTP {code} on PUT: {resp[:160]}")
        return
    raise RuntimeError(
        f"dashboard {dash_id} failed PUT {code}: {resp[:400]} | POST {code2}: {resp2[:400]}"
    )


def main() -> int:
    base = kibana_base()
    header = auth_header()
    if not base or not header:
        print("ERROR: KIBANA_URL and API key/password required for dashboards", file=sys.stderr)
        return 1

    # Best-effort data views (ES|QL panels do not require them, but Discover benefits)
    ensure_data_view(base, header, "cisco-meraki-events", "cisco-meraki-events", "@timestamp")
    ensure_data_view(base, header, "cisco-network-events", "cisco-network-events", "@timestamp")
    ensure_data_view(base, header, "cisco-network-kb", "cisco-network-kb", None)
    ensure_data_view(base, header, "cisco-internal-runbooks", "cisco-internal-runbooks", None)

    for dash_id, filename in DASHBOARDS:
        try:
            spec = load_spec(filename)
            upsert_dashboard(base, header, dash_id, spec)
        except Exception as exc:  # noqa: BLE001 — seed should not hard-fail the whole lab
            print(f"ERROR installing {dash_id}: {exc}", file=sys.stderr)
            return 1

    print("Cisco dashboards ready: cisco-noc-ops, cisco-kb-library")
    return 0


if __name__ == "__main__":
    sys.exit(main())
