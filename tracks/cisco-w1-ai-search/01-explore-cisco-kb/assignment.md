---
slug: explore-cisco-kb
id: x4ssyoighgs4
type: challenge
title: Challenge 1 — Find the runbook
teaser: Branch 4471 is paging — paste ES|QL against cisco-network-kb on Serverless Search.
tabs:
- id: yfkxkvh8vl0j
  title: Elastic Serverless Search
  type: service
  hostname: es3-api
  path: /app/elasticsearch/query
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

# Find the runbook

> **Thesis:** On **Elastic Serverless Search**, one project can hold Meraki, IOS-XE, and DNA-style guidance — if you can find it fast enough.

## Background

NOC chat lights up: *"Branch 4471 — Meraki AP offline, edge BGP looking ugly. Where's the recovery runbook?"*

Your lab is a single **Elastic Serverless Search** project with a seeded Cisco knowledge base. No Observability or Security projects — Search only.

**Time:** ~15–20 minutes

## Your task

Paste each query into the **ES|QL** editor and run it.

**BGP runbook**

```esql
FROM cisco-network-kb
| WHERE MATCH(content, "BGP neighbor idle")
   OR MATCH(title, "BGP neighbor")
| KEEP title, product, category, content
| LIMIT 10
```

**Meraki recovery**

```esql
FROM cisco-network-kb
| WHERE product == "Meraki" AND MATCH(content, "offline")
| KEEP title, product, category, content
| LIMIT 10
```

1. Confirm the BGP query returns **BGP Neighbor Down — IOS-XE Troubleshooting** (or similar).
2. Confirm the Meraki query returns **Meraki AP Offline Recovery** and note **two** steps from `content`.
3. In notes, write one sentence on how unified Search reduces **MTTR** for Cisco ops.

## Success criteria

- BGP query returns KB hits from **`cisco-network-kb`**
- Meraki query returns the offline recovery doc
- MTTR note is written

## Verification

Click **Check** when the success criteria are met.
