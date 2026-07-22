---
slug: triage-network-signals
id: ubtycyfwm7tm
type: challenge
title: Challenge 1 — Triage Network Signals
teaser: ES|QL triage on Search indices — BGP and Meraki signals.
tabs:
- id: nbrtnagypu9y
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

# Triage network signals

**Story:** Pager: *"BGP session down on edge router + Meraki AP offline at Branch 4471."*

**Time:** ~15–20 minutes

Use **Serverless Search** only — indices were seeded at track start.

## Tasks

1. Run ES|QL on **`cisco-network-events`** for `bgp.session_down`.
2. Run ES|QL on **`cisco-meraki-events`** for `device.offline` at Branch 4471.
3. Skim **Agent Builder** — what Search-backed tools would you expose to a NOC agent?

## Verification

Click **Check** when both queries return events.
