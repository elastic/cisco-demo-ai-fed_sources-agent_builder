---
slug: explore-cisco-kb
id: 60vejxsxcumb
type: challenge
title: Challenge 1 — Explore the Cisco Knowledge Base
teaser: Navigate Search and Discover on seeded Cisco runbooks.
notes:
- type: text
  contents: |
    **While the lab provisions (~3–4 min)** — use **← →** inside the deck below.

    <iframe src="https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html?v1=1" width="100%" height="720" frameborder="0"
      style="border-radius:8px;border:1px solid #2a3140;display:block;min-height:560px;background:#0b0d12">
    </iframe>

    Fullscreen: https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html
tabs:
- id: fjicbakgrdrf
  title: Elastic Serverless Search
  type: service
  hostname: es3-api
  path: /app/search
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

> **Module 1 — AI Search** · one **Serverless Search** project

# Explore the Cisco knowledge base

**Story:** A Cisco NOC lead asks: *"Can we search Meraki, IOS-XE, and DNA Center docs in one place?"*

**Time:** ~15–20 minutes

## Tasks

1. Wait for **Elastic Serverless** to finish loading (~3–4 min on first start).
2. Open **Search** (or use global search) and confirm index **`cisco-network-kb`** is available.
3. Run a **keyword** search: `BGP neighbor idle`
4. Open **Discover** → index **`cisco-network-kb`** and filter **product: Meraki**.
5. In notes, write one sentence on how this maps to **reducing MTTR** for Cisco ops teams.

## Verification

Click **Check** when you have run at least **two** searches and viewed **Meraki** documents in Discover.

