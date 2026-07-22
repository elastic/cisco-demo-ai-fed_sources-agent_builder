---
slug: explore-cisco-kb
id: vece86m0z4wb
type: challenge
title: Challenge 1 — Find the runbook
teaser: Open the seeded NOC dashboard, then paste ES|QL to pull the recovery runbook.
notes:
- type: text
  contents: |
    **While Elastic Serverless Search provisions (~3–4 min)** — use **← →** in the deck.

    <iframe src="https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html?v2=1" width="100%" height="720" frameborder="0"
      style="border-radius:8px;border:1px solid #2a3140;display:block;min-height:560px;background:#0b0d12">
    </iframe>

    Fullscreen: https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html
tabs:
- id: gibaflgjrdxh
  title: Elastic Serverless Search
  type: service
  hostname: es3-api
  path: /app/dashboards#/view/cisco-noc-ops
  port: 8080
  custom_request_headers:
  - key: Content-Security-Policy
    value: 'script-src ''self'' https://kibana.estccdn.com; worker-src blob: ''self'';
      style-src ''unsafe-inline'' ''self'' https://kibana.estccdn.com; style-src-elem
      ''unsafe-inline'' ''self'' https://kibana.estccdn.com'
  custom_response_headers:
  - key: Content-Security-Policy
    value: 'script-src ''self'' https://kibana.estccdn.com; worker-src blob: ''self'';
      style-src ''unsafe-inline'' ''self'' https://kibana.estccdn.com; style-src-elem
      ''unsafe-inline'' ''self'' https://kibana.estccdn.com'
difficulty: intermediate
timelimit: 1200
enhanced_loading: null
---

> **Module 1 — Find** · one **Elastic Serverless Search** project

# Find the runbook

> **Thesis:** On **Elastic Serverless Search**, one project can hold Meraki, IOS-XE, and DNA-style guidance — if you can find it fast enough.

## Background

NOC chat lights up: *"Branch 4471 — Meraki AP offline, edge BGP looking ugly. Where's the recovery runbook?"*

Your lab is a single **Elastic Serverless Search** project. Setup seeded two dashboards:

- **Cisco NOC Command Center** (`cisco-noc-ops`) — this tab
- **Cisco Knowledge Base Library** (`cisco-kb-library`) — open from Dashboards if you want the catalog view

**Time:** ~15–20 minutes

## Your task

1. On the **Cisco NOC Command Center** dashboard, confirm **Branch-4471-Dallas** appears in the Meraki offline and/or network signal panels.
2. Open **ES|QL** (Query / Discover) and paste:

```esql
FROM cisco-network-kb
| WHERE MATCH(content, "BGP neighbor idle")
   OR MATCH(title, "BGP neighbor")
| KEEP title, product, category, content
| LIMIT 10
```

3. Paste the Meraki recovery query and note **two** remediation steps from the `content` field:

```esql
FROM cisco-network-kb
| WHERE product == "Meraki" AND MATCH(content, "offline")
| KEEP title, product, category, content
| LIMIT 10
```

## Success criteria

- NOC dashboard shows Branch 4471 signals
- BGP query returns a KB hit
- Meraki query returns **Meraki AP Offline Recovery** with two steps identified

## Verification

Click **Check** when the success criteria are met.
