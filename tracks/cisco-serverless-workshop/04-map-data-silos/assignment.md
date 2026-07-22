---
slug: map-data-silos
id: rbxysyvajdld
type: challenge
title: Challenge 1 — Map Cisco Data Silos
teaser: Inventory federated indices and their business owner.
tabs:
- id: eiq1xiymq56h
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
timelimit: 1200
enhanced_loading: null
---

> **Module 2 — Federated Data Sources** · one **Serverless Search** project

# Map data silos

**Story:** Cisco IT has **Meraki Dashboard events**, **internal Confluence runbooks**, and **cisco.com KB** — three silos.

**Time:** ~15–20 minutes

## Seeded indices (lab)

| Index | Simulates | Owner persona |
|-------|-----------|---------------|
| `cisco-network-kb` | Public KB / docs | TAC / GSE |
| `cisco-internal-runbooks` | Internal wiki | NOC lead |
| `cisco-meraki-events` | Connector sync (Meraki) | NetOps |
| `cisco-network-events` | Network telemetry (BGP/DNA-style) | NOC / automation |

## Tasks

1. Open **Index Management** and confirm all **four** indices exist.
2. Open **Discover** on **`cisco-meraki-events`** — note fields `source`, `device_serial`, `event_type`.
3. In notes, map each index to a **real** Cisco system your customer uses.

## Verification

Click **Check** when you have documented all four indices.

