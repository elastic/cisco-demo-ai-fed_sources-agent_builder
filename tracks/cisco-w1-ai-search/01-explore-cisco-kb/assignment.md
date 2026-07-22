---
slug: explore-cisco-kb
id: x4ssyoighgs4
type: challenge
title: Challenge 1 — Find the runbook
teaser: Branch 4471 is paging — start in Discover on your Serverless Search project.
tabs:
- id: yfkxkvh8vl0j
  title: Elastic Serverless Search
  type: service
  hostname: es3-api
  path: /app/discover
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

1. Wait until **Elastic Serverless Search** finishes provisioning (~3–4 min on first start).
2. In **Discover**, open **`cisco-network-kb`** (use the data view / index picker if needed).
3. Run a keyword search: `BGP neighbor idle`
4. Filter **product: Meraki** and open at least one recovery-oriented doc.
5. In notes, write one sentence on how unified Search reduces **MTTR** for Cisco ops.

## Success criteria

- You can see documents in **`cisco-network-kb`**
- Keyword search returns BGP-related hits
- Meraki filter shows Meraki docs
- MTTR note is written

## Verification

Click **Check** when the success criteria are met.
