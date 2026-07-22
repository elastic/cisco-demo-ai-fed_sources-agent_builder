---
slug: cross-source-esql
id: c061wrpybn4c
type: challenge
title: Challenge 2 — Cross-Source ES|QL
teaser: Join KB guidance with live Meraki offline events.
tabs:
- id: 1dmkewx72at2
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
timelimit: 2100
enhanced_loading: null
---

> **Module 2 — Federated Data Sources** · one **Serverless Search** project

# Cross-source ES|QL

**Scenario:** Meraki AP **MR-AP-4471** went offline — find the event **and** the recovery runbook.

**Time:** ~25–35 minutes

## Query 1 — Events

```esql
FROM cisco-meraki-events
| WHERE event_type == "device.offline" AND device_name LIKE "*4471*"
| KEEP @timestamp, device_name, site, event_type, detail
| SORT @timestamp DESC
| LIMIT 5
```

## Query 2 — Runbook

```esql
FROM cisco-network-kb
| WHERE product == "Meraki" AND MATCH(content, "offline")
| KEEP title, product, category
| LIMIT 5
```

## Tasks

1. Run both queries; capture **timestamp + site** for the offline event.
2. Paste **one** runbook title that applies to recovery.
3. Optional third query — internal runbooks:

```esql
FROM cisco-internal-runbooks
| WHERE MATCH(content, "escalation")
| KEEP title, team, severity
| LIMIT 5
```

## Verification

Click **Check** after both primary queries succeed.

