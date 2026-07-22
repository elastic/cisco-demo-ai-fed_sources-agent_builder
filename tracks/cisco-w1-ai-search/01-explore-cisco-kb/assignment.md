---
slug: explore-cisco-kb
id: ewxzjpdnweuu
type: challenge
title: Challenge 1 — Explore the Cisco Knowledge Base
teaser: Navigate Search and Discover on seeded Cisco runbooks.
tabs:
- id: cja7sibzacwr
  title: Elastic Serverless
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

