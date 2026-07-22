---
slug: map-data-silos
id: n3olmdtkd0e1
type: challenge
title: Challenge 4 — Map silos the Agent will query
teaser: "Four Search indices = four silos — inventory them, then ask the Cisco Agent who owns each."
tabs:
- id: tab-idx-04
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
- id: tab-agent-04
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

Open Discover on `cisco-meraki-events` (or ask the agent which fields matter). Note `event_type`, `device_name`, `site`.

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

