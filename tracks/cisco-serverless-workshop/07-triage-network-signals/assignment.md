---
slug: triage-network-signals
id: tinsoaexxlkm
type: challenge
title: Challenge 7 — Triage the incident
teaser: Injected Branch 4471 signals — BGP + Meraki — on Serverless Search only.
notes:
- type: text
  contents: |
    **While Elastic Serverless Search provisions (~3–4 min)** — use **← →** in the deck.

    <iframe src="https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html?v2=1" width="100%" height="720" frameborder="0"
      style="border-radius:8px;border:1px solid #2a3140;display:block;min-height:560px;background:#0b0d12">
    </iframe>

    Fullscreen: https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html
tabs:
- id: 2er7ypvgiz7h
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

> **Module 3 — Act** · one **Elastic Serverless Search** project

# Triage the incident

> **Thesis:** Before you build an agent, prove you can triage the same signals the agent will see — on **Elastic Serverless Search**.

## Background

**Pager:** *"BGP session down on edge router + Meraki AP offline at Branch 4471."*

This is the end-to-end inject: events were seeded into your Serverless Search project at lab start. No Observability or Security projects required.

**Time:** ~15–20 minutes

## ES|QL — BGP signal

```esql
FROM cisco-network-events
| WHERE event_type == "bgp.session_down"
| KEEP @timestamp, host.name, cisco.site, message
| SORT @timestamp DESC
| LIMIT 5
```

## ES|QL — Meraki offline

```esql
FROM cisco-meraki-events
| WHERE event_type == "device.offline" AND device_name LIKE "*4471*"
| KEEP @timestamp, device_name, site, detail
| SORT @timestamp DESC
| LIMIT 5
```

## Your task

1. Run both queries in **ES|QL**.
2. Note **site** and **hostname/device** for the Branch 4471 scenario.
3. Open **Agent Builder** in the nav — list **two** tools/skills you would wire to these indices (you build them next).

## Success criteria

- Both queries return events
- Site + device notes captured
- Two agent tool ideas listed

## Verification

Click **Check** when both queries return events.
