#!/usr/bin/env python3
"""Upsert Cisco NOC Copilot into Agent Builder (Serverless Search)."""
from __future__ import annotations

import gzip
import json
import os
import sys
import urllib.error
import urllib.request

AGENT_ID = "cisco-noc-copilot"
AGENT_NAME = "Cisco NOC Copilot"

INSTRUCTIONS = """You are Cisco NOC Copilot on Elastic Serverless Search for Branch 4471 workshops.

Priorities:
1) Query Elastic indices with tools before answering (cisco-network-kb, cisco-meraki-events, cisco-network-events, cisco-internal-runbooks).
2) Prefer WAN/BGP root-cause hypotheses when Meraki cloud disconnect coincides with edge BGP Idle.
3) When Splunk Observability confirmation is needed, tell the analyst to run workflow cisco-branch-4471-splunk-o11y-a2a-rca (lab uses a stubbed A2A response). Never invent live Splunk telemetry.
4) Cite index names and runbook titles. Keep answers NOC-ready and concise.
"""

TOOL_IDS = [
    "platform.core.search",
    "platform.core.list_indices",
    "platform.core.get_index_mapping",
    "platform.core.get_document_by_id",
    "platform.core.execute_esql",
    "platform.core.generate_esql",
]


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


def agent_payload() -> dict:
    # Prefer execute_esql when present; creation still succeeds if some tool IDs are unknown
    # on older builds — we retry with a smaller built-in set on 400.
    return {
        "id": AGENT_ID,
        "name": AGENT_NAME,
        "description": (
            "Cisco NOC investigation agent for Branch 4471 — Meraki + BGP + KB on "
            "Elastic Serverless Search; points analysts at the Splunk O11Y A2A workflow for peer-platform evidence."
        ),
        "labels": ["cisco", "noc", "workshop", "serverless-search"],
        "avatar_color": "#049BFB",
        "avatar_symbol": "CN",
        "configuration": {
            "instructions": INSTRUCTIONS,
            "tools": [{"tool_ids": TOOL_IDS}],
        },
    }


def create_or_update(base: str, header: str) -> int:
    body = json.dumps(agent_payload()).encode()
    code, resp = request("GET", f"{base}/api/agent_builder/agents/{AGENT_ID}", header)
    if code == 200:
        # PUT accepts description/configuration/tags only (not id/name)
        update = {
            "description": agent_payload()["description"],
            "configuration": agent_payload()["configuration"],
            "labels": agent_payload()["labels"],
        }
        code2, resp2 = request(
            "PUT", f"{base}/api/agent_builder/agents/{AGENT_ID}", header, json.dumps(update).encode()
        )
        if code2 in (200, 201):
            print(f"agent updated: {AGENT_ID}")
            return 0
        print(f"warn: agent update HTTP {code2}: {resp2[:400]}", file=sys.stderr)
        return 1

    code2, resp2 = request("POST", f"{base}/api/agent_builder/agents", header, body)
    if code2 in (200, 201):
        print(f"agent created: {AGENT_ID} ({AGENT_NAME})")
        return 0

    # Retry with minimal built-in tools if some tool IDs are unavailable
    if code2 == 400 and "tool" in resp2.lower():
        minimal = agent_payload()
        minimal["configuration"]["tools"] = [
            {
                "tool_ids": [
                    "platform.core.search",
                    "platform.core.list_indices",
                    "platform.core.get_index_mapping",
                    "platform.core.get_document_by_id",
                ]
            }
        ]
        code3, resp3 = request(
            "POST", f"{base}/api/agent_builder/agents", header, json.dumps(minimal).encode()
        )
        if code3 in (200, 201):
            print(f"agent created (minimal tools): {AGENT_ID}")
            return 0
        print(f"warn: agent create retry HTTP {code3}: {resp3[:400]}", file=sys.stderr)
        return 1

    print(f"warn: agent create HTTP {code2}: {resp2[:400]}", file=sys.stderr)
    return 1


def main() -> int:
    base = kibana_base()
    header = auth_header()
    if not base or not header:
        print("ERROR: KIBANA_URL and API key required for agent seed", file=sys.stderr)
        return 1
    return create_or_update(base, header)


if __name__ == "__main__":
    sys.exit(main())
