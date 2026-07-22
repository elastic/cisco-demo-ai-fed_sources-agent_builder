---
slug: map-data-silos
type: challenge
title: Challenge 1 — Map Cisco Data Silos
teaser: Inventory federated indices and their business owner.
tabs:
- title: Elastic Serverless
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
---

# Map data silos

**Story:** Cisco IT has **Meraki Dashboard events**, **internal Confluence runbooks**, and **cisco.com KB** — three silos.

**Time:** ~15–20 minutes

## Seeded indices (lab)

| Index | Simulates | Owner persona |
|-------|-----------|---------------|
| `cisco-network-kb` | Public KB / docs | TAC / GSE |
| `cisco-internal-runbooks` | Internal wiki | NOC lead |
| `cisco-meraki-events` | Connector sync (Meraki) | NetOps |

## Tasks

1. Open **Index Management** and confirm all **three** indices exist.
2. Open **Discover** on **`cisco-meraki-events`** — note fields `source`, `device_serial`, `event_type`.
3. In notes, map each index to a **real** Cisco system your customer uses.

## Verification

Click **Check** when you have documented all three indices.

