---
slug: triage-network-signals
id: zbkbtyqzlwbq
type: challenge
title: Challenge 1 — Triage Network Signals
teaser: Discover BGP and Meraki signals in Observability.
tabs:
- id: ikqpcg2bzcec
  title: Elastic Serverless
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

# Triage network signals

**Story:** Pager: *"BGP session down on edge router + Meraki AP offline at Branch 4471."*

**Time:** ~15–20 minutes

## Tasks

1. Open **Discover** → data view **`logs-cisco.network-*`** (or index **`logs-cisco.network-default`**).
2. Filter **`event.category: network`** or search `BGP` and `Meraki`.
3. Identify **one** `bgp.session_down` and **one** `meraki.device.offline` event; note hostname/site.
4. Skim **Agent Builder** in the menu — what tools/skills would you expose to a NOC agent?

## Verification

Click **Check** when you have found both event types.

