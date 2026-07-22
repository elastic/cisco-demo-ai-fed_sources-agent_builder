---
slug: map-data-silos
id: n3olmdtkd0e1
type: challenge
title: Challenge 1 — Map Cisco data silos
teaser: Four indices, one Serverless Search project — who owns what?
tabs:
- id: hejyfxmigq1e
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

# Map data silos

> **Thesis:** Federation is not rip-and-replace. Authoritative systems stay; **Serverless Search** becomes the query layer.

## Background

Branch 4471 still needs more than a KB hit. Real Cisco environments split truth across **Meraki Dashboard events**, **internal Confluence runbooks**, and **public KB** — three (or more) silos. This lab seeds all four into **one Elastic Serverless Search** project.

**Time:** ~15–20 minutes

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
3. In notes, map each index to a **real** Cisco system your team uses today.

## Success criteria

- All four indices confirmed
- Meraki event fields noted
- Real-world mapping written for each index

## Verification

Click **Check** when the success criteria are met.
