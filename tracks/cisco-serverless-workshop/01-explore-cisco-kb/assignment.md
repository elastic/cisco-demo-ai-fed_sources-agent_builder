---
slug: explore-cisco-kb
type: challenge
title: Challenge 1 — Create the Cisco Agent & find the runbook
teaser: Stand up Cisco NOC Copilot in Agent Builder — then ask Branch 4471.
notes:
- type: text
  contents: |
    **While Elastic Serverless Search provisions (~3–4 min)** — use **← →** in the deck.

    <iframe src="https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html?v2=1" width="100%" height="720" frameborder="0"
      style="border-radius:8px;border:1px solid #2a3140;display:block;min-height:560px;background:#0b0d12">
    </iframe>

    Fullscreen: https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html

tabs:
- title: Cisco Agent
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
timelimit: 600
enhanced_loading: null
---

> **Module 1 — Find** · one **Elastic Serverless Search** project

# Create the Cisco Agent & find the runbook

> **Thesis:** Don't start in raw Discover. Create a **Cisco Agent** in Agent Builder that queries Serverless Search — then use it for every later challenge.

## Background

NOC chat: *"Branch 4471 — Meraki AP offline, edge BGP looking ugly. Where's the recovery runbook?"*

Seeded for you: **Cisco NOC Command Center** dashboard + `cisco-network-kb`.

**Time:** ~5 minutes with Agent Builder  
*Without AI/agent tooling this beat was usually 15–20 minutes.*

## Your task

### 1 — Orient (30 seconds)

Open [button label="NOC Dashboard"](tab-1). Confirm **Branch-4471-Dallas** appears in Meraki offline and/or network panels.

### 2 — Create **Cisco NOC Copilot**

Open [button label="Cisco Agent"](tab-0) → **Agent Builder** → create a **new agent**:

| | |
|--|--|
| **Name** | `Cisco NOC Copilot` |
| **Goal** | Investigate Cisco Branch 4471: correlate Meraki + BGP signals with KB runbooks; draft next steps |
| **Tools** | ES\|QL (or index search) over `cisco-network-kb`, `cisco-meraki-events`, `cisco-network-events` (add `cisco-internal-runbooks` if offered) |

Save the agent. You will reuse it for the rest of the workshop.

### 3 — Ask the agent for runbooks

In the agent chat, paste:

```text
Branch 4471 — Meraki AP offline, edge BGP looking ugly. Where's the recovery runbook?
Use cisco-network-kb. Return both Meraki offline and BGP neighbor guidance with numbered first steps.
```

Confirm tool calls hit Search indices and you get **Meraki AP Offline Recovery** + **BGP Neighbor Down — IOS-XE Troubleshooting** (or equivalent titles).

## Success criteria

- `Cisco NOC Copilot` exists with Search-backed tools
- Agent returns Meraki + BGP recovery steps grounded in `cisco-network-kb`
- NOC dashboard shows Branch 4471 signals

## Verification

Click **Check** when the success criteria are met.

