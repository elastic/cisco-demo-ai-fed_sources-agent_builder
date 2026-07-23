---
slug: map-data-silos
id: gz3biuxritlc
type: challenge
title: Challenge 4 — Map silos the Agent will query
teaser: Four Search indices = four silos — inventory them, then ask the Cisco Agent
  who owns each.
notes:
- type: text
  contents: |
    **While Elastic Serverless Search provisions (~3–4 min)** — use **← →** in the deck.

    <iframe src="https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html?v3=1" width="100%" height="720" frameborder="0"
      style="border-radius:8px;border:1px solid #2a3140;display:block;min-height:560px;background:#0b0d12">
    </iframe>

    Fullscreen: https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html
tabs:
- id: jkxucfktzf3f
  title: Indices
  type: service
  hostname: es3-api
  path: /app/management/data/index_management/indices
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
- id: 4f5xmxfcc2sl
  title: Cisco Agent
  type: service
  hostname: es3-api
  path: /app/agent_builder
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
timelimit: 600
enhanced_loading: null
---

> **Module 2 — Federate** · one **Elastic Serverless Search** project

# Map silos the Agent will query

> **Thesis:** Federation is not rip-and-replace. `Cisco NOC Copilot` only gets smarter when you map which silos feed Serverless Search.

## Background

Branch 4471 needs more than a KB. Setup seeded four indices in **one** Serverless Search project.

| Index | Simulates | Owner persona |
|-------|-----------|---------------|
| `cisco-network-kb` | Public / TAC docs | TAC / GSE |
| `cisco-internal-runbooks` | Internal wiki | NOC lead |
| `cisco-meraki-events` | Meraki connector sync | NetOps |
| `cisco-network-events` | BGP / DNA-style signals | Network eng |

**Time:** ~5 minutes with the Agent
*Without AI this beat was usually 15–20 minutes.*

## Your task

### 1 — Confirm indices

Open [button label="Indices"](tab-0). Confirm all **four** indices exist.

### 2 — Spot-check Meraki fields

Open Discover on `cisco-meraki-events` (or ask the agent which fields matter). Set time to **Last 24 hours** if the table is empty. Note `event_type`, `device_name`, `site`.

### 3 — Ask the Agent to map ownership

Open [button label="Cisco Agent"](tab-1) and paste:

```text
We have four indices: cisco-network-kb, cisco-internal-runbooks, cisco-meraki-events, cisco-network-events.
For each: (1) what real Cisco system it maps to, (2) who owns it, (3) why Cisco NOC Copilot needs ES|QL access.
Return a compact table. End with one sentence on how Splunk O11Y A2A (workflow cisco-branch-4471-splunk-o11y-a2a-rca) augments — not replaces — these silos.
```

## Success criteria

- All four indices confirmed
- Agent returns ownership/mapping table
- Notes mention A2A as augmentation (not rip-and-replace)

## Verification

Click **Check** when the success criteria are met.

