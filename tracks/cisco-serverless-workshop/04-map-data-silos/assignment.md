---
slug: map-data-silos
id: yjw9xwhdfyes
type: challenge
title: Challenge 4 — Map Cisco data silos
teaser: Four indices, one Serverless Search project — who owns what?
notes:
- type: text
  contents: |
    **While Elastic Serverless Search provisions (~3–4 min)** — use **← →** in the deck.

    <iframe src="https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html?v2=1" width="100%" height="720" frameborder="0"
      style="border-radius:8px;border:1px solid #2a3140;display:block;min-height:560px;background:#0b0d12">
    </iframe>

    Fullscreen: https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html
tabs:
- id: q67wcj9qcnwv
  title: Elastic Serverless Search
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
difficulty: intermediate
timelimit: 600
enhanced_loading: null
---

> **Module 2 — Federate** · one **Elastic Serverless Search** project

# Map data silos

> **Thesis:** Federation is not rip-and-replace. Authoritative systems stay; **Serverless Search** becomes the query layer.

## Background

Branch 4471 still needs more than a KB hit. Real Cisco environments split truth across **Meraki Dashboard events**, **internal Confluence runbooks**, and **public KB** — three (or more) silos. This lab seeds all four into **one Elastic Serverless Search** project.

**Time:** ~5 minutes with AI Assistant
*Without AI this beat was usually 15–20 minutes — paste prompts, don’t retype the story.*

## Seeded indices (lab)

| Index | Simulates | Owner persona |
|-------|-----------|---------------|
| `cisco-network-kb` | Public KB / docs | TAC / GSE |
| `cisco-internal-runbooks` | Internal wiki | NOC lead |
| `cisco-meraki-events` | Connector sync (Meraki) | NetOps |
| `cisco-network-events` | Network telemetry (BGP / DNA-style) | NOC / automation |

## Your task

1. Open **Index Management** and confirm all **four** indices exist.
2. Open **Discover** on **`cisco-meraki-events`** — note fields `source`, `device_serial`, `event_type`.
3. Open Dashboards → **Cisco Knowledge Base Library** (`cisco-kb-library`) and confirm runbooks by product.
4. Map each index to a **real** Cisco system your team uses today.

## Success criteria

- All four indices confirmed
- Meraki event fields noted
- KB Library dashboard opened
- Real-world mapping written for each index

## Verification

Click **Check** when the success criteria are met.
