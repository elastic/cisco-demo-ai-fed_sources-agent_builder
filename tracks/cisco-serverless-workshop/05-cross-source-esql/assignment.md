---
slug: cross-source-esql
id: xuk7t6lpqeeo
type: challenge
title: Challenge 5 — Correlate event + runbook
teaser: Same Serverless project — Meraki offline event meets recovery guidance in
  ES|QL.
tabs:
- id: gcynwtxnsbtq
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

> **Module 2 — Federate** · one **Elastic Serverless Search** project

# Correlate event + runbook

> **Thesis:** Cross-index ES|QL on Serverless Search turns “we have data somewhere” into “here’s the event and the next step.”

## Background

**Scenario:** Meraki AP **MR-AP-4471** went offline. Find the **event** and the **recovery runbook** without leaving your Serverless Search project.

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

## Optional — Internal escalation

```esql
FROM cisco-internal-runbooks
| WHERE MATCH(content, "escalation")
| KEEP title, team, severity
| LIMIT 5
```

## Your task

1. Run Query 1 and Query 2; capture **timestamp + site** for the offline event.
2. Paste **one** runbook title that applies to recovery.
3. Optional: run the internal runbooks query and note an escalation owner.

## Success criteria

- Offline event located for Branch / device 4471
- Matching Meraki runbook title recorded

## Verification

Click **Check** when both primary queries succeed.
