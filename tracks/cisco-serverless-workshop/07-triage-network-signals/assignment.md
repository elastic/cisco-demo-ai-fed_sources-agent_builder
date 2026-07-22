---
slug: triage-network-signals
type: challenge
title: Challenge 1 — Triage Network Signals
teaser: ES|QL triage on Search indices — BGP and Meraki signals.
notes:
- type: text
  contents: |
    **While the lab provisions (~3–4 min)** — use **← →** inside the deck below.

    <iframe src="https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html?v1=1" width="100%" height="720" frameborder="0"
      style="border-radius:8px;border:1px solid #2a3140;display:block;min-height:560px;background:#0b0d12">
    </iframe>

    Fullscreen: https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html

tabs:
- title: Elastic Serverless Search
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

> **Module 3 — Agent Builder (Search)** · one **Serverless Search** project

# Triage network signals

**Story:** Pager: *"BGP session down on edge router + Meraki AP offline at Branch 4471."*

**Time:** ~15–20 minutes

All data lives in your **Serverless Search** project (no Observability / Security required).

## ES|QL — BGP signal

```esql
FROM cisco-network-events
| WHERE event_type == "bgp.session_down"
| KEEP @timestamp, host.name, cisco.site, message
| SORT @timestamp DESC
| LIMIT 5
```

## ES|QL — Meraki offline (connector index)

```esql
FROM cisco-meraki-events
| WHERE event_type == "device.offline" AND device_name LIKE "*4471*"
| KEEP @timestamp, device_name, site, detail
| SORT @timestamp DESC
| LIMIT 5
```

## Tasks

1. Run both queries in **ES|QL**.
2. Note **site** and **hostname/device** for the Branch 4471 scenario.
3. Open **Agent Builder** in the nav — list 2 tools/skills you would wire to these indices.

## Verification

Click **Check** when both queries return events.
