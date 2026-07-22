---
slug: explore-cisco-kb
id: lmslgnjsb2un
type: challenge
title: Challenge 1 — Find the runbook
teaser: ES|QL plus Elastic AI Assistant — get both Branch 4471 runbooks in one ask.
notes:
- type: text
  contents: |
    **While Elastic Serverless Search provisions (~3–4 min)** — use **← →** in the deck.

    <iframe src="https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html?v2=1" width="100%" height="720" frameborder="0"
      style="border-radius:8px;border:1px solid #2a3140;display:block;min-height:560px;background:#0b0d12">
    </iframe>

    Fullscreen: https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html
tabs:
- id: wjwdvttlxyer
  title: NOC Dashboard
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
timelimit: 1500
enhanced_loading: null
---

> **Module 1 — Find** · one **Elastic Serverless Search** project

# Find the runbook

> **Thesis:** On **Elastic Serverless Search**, keyword ES|QL finds the docs — the **AI Assistant** turns them into a NOC-ready action plan.

## Background

NOC chat lights up: *"Branch 4471 — Meraki AP offline, edge BGP looking ugly. Where's the recovery runbook?"*

Setup seeded:

- **Cisco NOC Command Center** — [button label="NOC Dashboard"](tab-1)
- **Cisco Knowledge Base Library** (`cisco-kb-library`) — Dashboards list if you want the catalog

**Time:** ~15–20 minutes

## Your task

### 1 — Orient on the dashboard

Open [button label="NOC Dashboard"](tab-1) and confirm **Branch-4471-Dallas** appears in Meraki offline and/or network signal panels.

### 2 — Prove it with ES|QL

Back on [button label="ES|QL + AI Assistant"](tab-0), paste:

```esql
FROM cisco-network-kb
| WHERE MATCH(content, "BGP neighbor idle")
   OR MATCH(title, "BGP neighbor")
| KEEP title, product, category, content
| LIMIT 10
```

Then:

```esql
FROM cisco-network-kb
| WHERE product == "Meraki" AND MATCH(content, "offline")
| KEEP title, product, category, content
| LIMIT 10
```

Confirm you get **BGP Neighbor Down — IOS-XE Troubleshooting** and **Meraki AP Offline Recovery**.

### 3 — Ask the Elastic AI Assistant

Open the **AI Assistant** / **Elastic AI Agent** chat panel (right side in Discover).

Paste this prompt:

```text
Branch 4471 — Meraki AP offline, edge BGP looking ugly. Where's the recovery runbook?
```

Wait for tool calls to finish. You should get **both** runbooks with numbered steps, plus guidance on which problem to fix first (BGP vs Meraki).

## Success criteria

- NOC dashboard shows Branch 4471 signals
- Both ES|QL queries return the expected KB docs
- AI Assistant returns Meraki + BGP recovery steps grounded in `cisco-network-kb`

## Verification

Click **Check** when the success criteria are met.
