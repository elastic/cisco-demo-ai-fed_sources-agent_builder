#!/usr/bin/env python3
"""Scaffold Cisco × Elastic Serverless Instruqt workshop tracks."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METRIC_SERIES = ROOT.parent / "metric-enablement-series"
SRC_KB = ROOT.parent / "cisco-elastic-search-ai" / "src" / "data" / "cisco-knowledge-base.json"
DEVELOPER = "peter.simkins@elastic.co"
TAG = "cisco-workshop-series"

CSP_HEADERS = """  custom_request_headers:
  - key: Content-Security-Policy
    value: 'script-src ''self'' https://kibana.estccdn.com; worker-src blob: ''self'';
      style-src ''unsafe-inline'' ''self'' https://kibana.estccdn.com; style-src-elem
      ''unsafe-inline'' ''self'' https://kibana.estccdn.com'
  custom_response_headers:
  - key: Content-Security-Policy
    value: 'script-src ''self'' https://kibana.estccdn.com; worker-src blob: ''self'';
      style-src ''unsafe-inline'' ''self'' https://kibana.estccdn.com; style-src-elem
      ''unsafe-inline'' ''self'' https://kibana.estccdn.com'"""

TRACKS = [
    {
        "slug": "cisco-w1-ai-search",
        "title": "Cisco W1 — AI Search on Serverless",
        "teaser": "Semantic + hybrid search over Cisco network runbooks on Elastic Serverless Search.",
        "description": """  Workshop 1 of 3 for Cisco practitioners. Per-learner **Elastic Serverless Search**
  (vector-optimized) with a pre-seeded Cisco knowledge base. Explore Search, Discover, and
  hybrid retrieval patterns for NOC and platform engineering teams. ~90 minutes.""",
        "tags": ["cisco", "search", "ai", "serverless", "elasticsearch"],
        "config_env": {
            "PROJECT_TYPE": "elasticsearch",
            "OPTIMIZED_FOR": "general_purpose",
            "REGIONS": "aws-us-east-1",
        },
        "seed_script": "seed_cisco_kb.py",
        "challenges": [
            {
                "dir": "01-explore-cisco-kb",
                "slug": "explore-cisco-kb",
                "title": "Challenge 1 — Explore the Cisco Knowledge Base",
                "teaser": "Navigate Search and Discover on seeded Cisco runbooks.",
                "path": "/app/discover",
                "minutes": 20,
                "body": """# Explore the Cisco knowledge base

**Story:** A Cisco NOC lead asks: *"Can we search Meraki, IOS-XE, and DNA Center docs in one place?"*

**Time:** ~15–20 minutes

## Tasks

1. Wait for **Elastic Serverless** to finish loading (~3–4 min on first start).
2. In **Discover**, open data view / index **`cisco-network-kb`** (use the index picker if needed).
3. Run a **keyword** search: `BGP neighbor idle`
4. Open **Discover** → index **`cisco-network-kb`** and filter **product: Meraki**.
5. In notes, write one sentence on how this maps to **reducing MTTR** for Cisco ops teams.

## Verification

Click **Check** when you have run at least **two** searches and viewed **Meraki** documents in Discover.
""",
            },
            {
                "dir": "02-hybrid-retrieval",
                "slug": "hybrid-retrieval",
                "title": "Challenge 2 — Hybrid & Semantic Retrieval",
                "teaser": "Compare keyword vs semantic-style queries on runbooks.",
                "path": "/app/elasticsearch/query",
                "minutes": 35,
                "body": """# Hybrid retrieval lab

**Story:** Engineers ask vague questions (*"AP keeps going offline"*) — keyword search alone misses intent.

**Time:** ~25–35 minutes

## Sample ES|QL (Dev Tools or ES|QL UI)

Try in **ES|QL** (adjust if your UI uses **Query**):

```esql
FROM cisco-network-kb
| WHERE MATCH(title, "offline")
   OR MATCH(content, "meraki dashboard")
| KEEP title, product, category
| LIMIT 10
```

Then try a natural-language style query in **Search**:

> Meraki access point offline cloud connectivity

## Tasks

1. Run the ES|QL query above (or equivalent **Search** UI query).
2. Find the **Meraki AP Offline Recovery** document and note **two** troubleshooting steps from the content.
3. Optional: enable **semantic** / **AI** search features if shown in your project tier.
4. In notes, compare **keyword** vs **natural language** result quality in 2–3 bullets.

## Verification

Click **Check** after you document **Meraki offline** steps and your comparison bullets.
""",
            },
            {
                "dir": "03-customer-talk-track",
                "slug": "customer-talk-track",
                "title": "Challenge 3 — Share the story with your peers",
                "teaser": "Practice explaining hybrid search to a teammate in 60 seconds.",
                "path": "/app/discover",
                "minutes": 20,
                "body": """# Explain it to your team

**Time:** ~15–20 minutes

## Story outline (for a peer or skip-level)

| Beat | Your line |
|------|-----------|
| Pain | Cisco teams search **Meraki, IOS-XE, DNA Center, Talos** in silos |
| Outcome | **One Serverless Search** project — hybrid + semantic on runbooks |
| Proof | Live query: BGP down + Meraki offline in **under 10 seconds** |
| What's new | Vector Search + ES|QL + connectors path (Module 2) |
| Next | Federated sources + Agent Builder (Modules 2–3) |

## Tasks

1. Re-run your **best** search from Challenge 2 as a **show-and-tell** moment.
2. Draft a **60-second** explanation (notes or voice memo outline) for a teammate.
3. Name **one** internal team (NOC, platform, or GSE) that would benefit from **unified doc search**.

## Verification

Click **Check** when your story outline table is complete.
""",
            },
        ],
    },
    {
        "slug": "cisco-w2-federated-sources",
        "title": "Cisco W2 — Federated Data Sources",
        "teaser": "Unify Meraki-style events, internal runbooks, and KB in one ES|QL view.",
        "description": """  Workshop 2 of 3. Same **Serverless Search** pattern with **multiple indices**
  simulating connector-fed sources (Meraki events, internal wiki, public KB). Learners
  query across sources with ES|QL and plan real **Elastic connectors**. ~90 minutes.""",
        "tags": ["cisco", "federated", "connectors", "search", "serverless"],
        "config_env": {
            "PROJECT_TYPE": "elasticsearch",
            "OPTIMIZED_FOR": "general_purpose",
            "REGIONS": "aws-us-east-1",
        },
        "seed_script": "seed_federated_sources.py",
        "challenges": [
            {
                "dir": "01-map-data-silos",
                "slug": "map-data-silos",
                "title": "Challenge 1 — Map Cisco Data Silos",
                "teaser": "Inventory federated indices and their business owner.",
                "path": "/app/management/data/index_management/indices",
                "minutes": 20,
                "body": """# Map data silos

**Story:** Cisco IT has **Meraki Dashboard events**, **internal Confluence runbooks**, and **cisco.com KB** — three silos.

**Time:** ~15–20 minutes

## Seeded indices (lab)

| Index | Simulates | Owner persona |
|-------|-----------|---------------|
| `cisco-network-kb` | Public KB / docs | TAC / GSE |
| `cisco-internal-runbooks` | Internal wiki | NOC lead |
| `cisco-meraki-events` | Connector sync (Meraki) | NetOps |

## Tasks

1. Open **Index Management** and confirm all **three** indices exist.
2. Open **Discover** on **`cisco-meraki-events`** — note fields `source`, `device_serial`, `event_type`.
3. In notes, map each index to a **real** Cisco system your customer uses.

## Verification

Click **Check** when you have documented all three indices.
""",
            },
            {
                "dir": "02-cross-source-esql",
                "slug": "cross-source-esql",
                "title": "Challenge 2 — Cross-Source ES|QL",
                "teaser": "Join KB guidance with live Meraki offline events.",
                "path": "/app/elasticsearch/query",
                "minutes": 35,
                "body": """# Cross-source ES|QL

**Scenario:** Meraki AP **MR-AP-4471** went offline — find the event **and** the recovery runbook.

**Time:** ~25–35 minutes

## Query 1 — Events

```esql
FROM cisco-meraki-events
| WHERE event_type == "device.offline" AND device_name LIKE "*4471*"
| KEEP @timestamp, device_name, site, event_type, detail
| SORT @timestamp DESC
| LIMIT 5
```

## Query 2 — Runbook

```esql
FROM cisco-network-kb
| WHERE product == "Meraki" AND MATCH(content, "offline")
| KEEP title, product, category
| LIMIT 5
```

## Tasks

1. Run both queries; capture **timestamp + site** for the offline event.
2. Paste **one** runbook title that applies to recovery.
3. Optional third query — internal runbooks:

```esql
FROM cisco-internal-runbooks
| WHERE MATCH(content, "escalation")
| KEEP title, team, severity
| LIMIT 5
```

## Verification

Click **Check** after both primary queries succeed.
""",
            },
            {
                "dir": "03-connector-story",
                "slug": "connector-story",
                "title": "Challenge 3 — Connectors & federated sources",
                "teaser": "See how connectors let you federate Meraki and internal sources without rip-and-replace.",
                "path": "/app/enterprise_search/content/connectors",
                "minutes": 20,
                "body": """# Federate sources with connectors

**Time:** ~15–20 minutes

## Why federation (not rip-and-replace)

- **Keep systems in place** — Meraki, DNA Center, and ITSM stay authoritative
- **Unify the query layer** — connectors sync content and events into Serverless Search; **ES|QL** joins them at query time
- **Add sources incrementally** — start with high-value indices (like this lab's Meraki-style events) before expanding

## Tasks

1. Browse **Connectors** in Kibana (UI tour — no production connector required in lab).
2. Pick **two** connector types relevant to Cisco environments (e.g. ServiceNow, SharePoint, MongoDB, GitHub).
3. Write **3 bullets**: what stays in existing Cisco/cloud systems vs. what gets indexed for search in Elastic.
4. Tie Module 1 search patterns to Module 3 **Agent Builder** tools on the same indices.

## Verification

Click **Check** when connectors + federated bullets are in your notes.
""",
            },
        ],
    },
    {
        "slug": "cisco-w3-agent-builder",
        "title": "Cisco W3 — Agent Builder for Cisco",
        "teaser": "Agentic investigation over Cisco network logs on Serverless Observability.",
        "description": """  Workshop 3 of 3. Per-learner **Serverless Observability** (complete tier) with
  seeded **`logs-cisco.network`** documents. Build an **Agent Builder** investigation
  story for BGP/Meraki-style incidents. ~90 minutes.""",
        "tags": ["cisco", "agent-builder", "observability", "serverless", "aiops"],
        "config_env": {
            "PROJECT_TYPE": "observability",
            "PRODUCT_TIER": "complete",
            "REGIONS": "aws-us-east-1",
        },
        "seed_script": "seed_cisco_observability.py",
        "challenges": [
            {
                "dir": "01-triage-network-signals",
                "slug": "triage-network-signals",
                "title": "Challenge 1 — Triage Network Signals",
                "teaser": "Discover BGP and Meraki signals in Observability.",
                "path": "/app/discover",
                "minutes": 20,
                "body": """# Triage network signals

**Story:** Pager: *"BGP session down on edge router + Meraki AP offline at Branch 4471."*

**Time:** ~15–20 minutes

## Tasks

1. Open **Discover** → data view **`logs-cisco.network-*`** (or index **`logs-cisco.network-default`**).
2. Filter **`event.category: network`** or search `BGP` and `Meraki`.
3. Identify **one** `bgp.session_down` and **one** `meraki.device.offline` event; note hostname/site.
4. Skim **Agent Builder** in the menu — what tools/skills would you expose to a NOC agent?

## Verification

Click **Check** when you have found both event types.
""",
            },
            {
                "dir": "02-build-investigation-agent",
                "slug": "build-investigation-agent",
                "title": "Challenge 2 — Build an Investigation Agent",
                "teaser": "Configure Agent Builder for Cisco NOC workflow.",
                "path": "/app/agent_builder",
                "minutes": 35,
                "body": """# Build an investigation agent

**Time:** ~25–35 minutes

## Suggested agent charter

**Name:** Cisco NOC Copilot  
**Goal:** Given an alert summary, pull correlated logs (BGP + Meraki), suggest runbook steps, draft escalation note.

## Tasks

1. Open **Agent Builder** → create or explore a **new agent** (use lab-safe read-only tools where prompted).
2. Add capabilities that reference **logs** and **ES|QL** (or Observability AI Assistant if bundled).
3. Test with prompt:

> Branch 4471 reports Meraki offline and BGP flapping on `edge-dfw-01`. Summarize timeline and next steps.

4. Capture **screenshot or notes** of one successful tool invocation.

## Reference

Download **`agent-builder-cisco-playbook.md`** from workshop assets (synced on push) for tool ideas.

## Verification

Click **Check** after a test prompt returns actionable steps.
""",
            },
            {
                "dir": "03-exec-demo-close",
                "slug": "exec-demo-close",
                "title": "Challenge 3 — Workshop wrap-up & next steps",
                "teaser": "Recap the journey — Search → Federate → Agents — and what to try next on your data.",
                "path": "/app/agent_builder",
                "minutes": 20,
                "body": """# Workshop wrap-up & next steps

**Time:** ~15–20 minutes

## Three-beat recap

1. **Module 1 — AI Search** — find Meraki/BGP runbooks in seconds  
2. **Module 2 — Federated** — Meraki events + internal runbooks + KB in one ES|QL story  
3. **Module 3 — Agent Builder** — agentic triage on Search (`cisco-network-events` + federated indices)

## Tasks

1. Write a **90-second** recap script hitting all three beats (bullets only) — practice **showing your team** what you learned.
2. Note **one concrete outcome** from today (e.g. faster runbook lookup, cross-index ES|QL, agent tool idea).
3. List **one next experiment** on Cisco data: index an internal wiki, try a connector POC, or extend Agent Builder tools.

## Verification

Click **Check** when your recap script is complete.
""",
            },
        ],
    },
]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def track_yml(t: dict) -> str:
    tags = "\n".join(f"- {x}" for x in t["tags"])
    return f"""slug: {t["slug"]}
title: {t["title"]}
teaser: {t["teaser"]}
description: |
{t["description"]}
icon: https://www.elastic.co/favicon.ico
tags:
{tags}
- {TAG}
owner: elastic
developers:
- {DEVELOPER}
show_timer: true
skipping_enabled: true
idle_timeout: 600
timelimit: 5400
lab_config:
  extend_ttl: 900
  sidebar_enabled: true
  feedback_recap_enabled: true
  feedback_tab_enabled: false
  loadingMessages: true
  theme:
    name: modern-dark
  hideStopButton: false
  default_layout: AssignmentRight
  default_layout_sidebar_size: 40
enhanced_loading: false
"""


def config_yml(env: dict, seed_script: str) -> str:
    env = {**env, "WORKSHOP_SEED": seed_script}
    env_lines = "\n".join(f"    {k}: {v}" for k, v in env.items())
    return f"""version: "3"
virtualmachines:
- name: es3-api
  image: elastic/es3-api-v2
  shell: /bin/bash
  environment:
{env_lines}
  memory: 4096
  cpus: 1
  allow_external_ingress:
  - http
  - https
  - high-ports
secrets:
- name: ESS_CLOUD_API_KEY
- name: LLM_PROXY_PROD
"""


def assignment(ch: dict) -> str:
    return f"""---
slug: {ch["slug"]}
type: challenge
title: {ch["title"]}
teaser: {ch["teaser"]}
tabs:
- title: Elastic Serverless
  type: service
  hostname: es3-api
  path: {ch["path"]}
  port: 8080
{CSP_HEADERS}
difficulty: intermediate
timelimit: {ch["minutes"] * 60}
---

{ch["body"]}
"""


def check_script() -> str:
    return """#!/bin/bash
echo "✓ Continue when you have completed the tasks in Instructions."
exit 0
"""


def main() -> None:
    if SRC_KB.is_file():
        shutil.copy2(SRC_KB, ROOT / "assets" / "shared" / "cisco-knowledge-base.json")
    else:
        write(ROOT / "assets" / "shared" / "cisco-knowledge-base.json", '{"documents": []}\n')

    for t in TRACKS:
        base = ROOT / "tracks" / t["slug"]
        write(base / "track.yml", track_yml(t))
        write(base / "config.yml", config_yml(t["config_env"], t["seed_script"]))

        seed_name = t["seed_script"]
        src_seed = ROOT / "scripts" / seed_name
        if src_seed.is_file():
            write(base / "track_scripts" / seed_name, src_seed.read_text(encoding="utf-8"))
        if seed_name == "seed_federated_sources.py":
            kb_seed = ROOT / "scripts" / "seed_cisco_kb.py"
            if kb_seed.is_file():
                write(base / "track_scripts" / "seed_cisco_kb.py", kb_seed.read_text(encoding="utf-8"))
        kb = ROOT / "assets" / "shared" / "cisco-knowledge-base.json"
        if kb.is_file() and seed_name in ("seed_cisco_kb.py", "seed_federated_sources.py"):
            write(
                base / "workshop-assets" / "data" / "cisco-knowledge-base.json",
                kb.read_text(encoding="utf-8"),
            )

        for ch in t["challenges"]:
            cdir = base / ch["dir"]
            write(cdir / "assignment.md", assignment(ch))
            write(cdir / "check-es3-api", check_script())
            write(cdir / "solve-es3-api", check_script())

        dl = base / "workshop-assets" / "downloads"
        write(
            dl / "cisco-workshop-overview.md",
            f"# {t['title']}\n\nSee Instructions in Instruqt for hands-on steps.\n",
        )
        playbook = ROOT / "assets" / "shared" / "downloads" / "agent-builder-cisco-playbook.md"
        if t["slug"] == "cisco-w3-agent-builder" and playbook.is_file():
            write(dl / "agent-builder-cisco-playbook.md", playbook.read_text(encoding="utf-8"))

    print("Scaffolded", len(TRACKS), "tracks under", ROOT / "tracks")


if __name__ == "__main__":
    main()
