---
slug: exec-demo-close
id: 9gfqp7ekvor6
type: challenge
title: Challenge 3 — Workshop wrap-up & next steps
teaser: Recap the journey — Search → Federate → Agents — and what to try next on your
  data.
tabs:
- id: iqexfd35r3ma
  title: Elastic Serverless Search
  type: service
  hostname: es3-api
  path: /app/agent_builder
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

# Workshop wrap-up & next steps

**Time:** ~15–20 minutes

## Three-beat recap

1. **Module 1 — AI Search** — find Meraki/BGP runbooks in seconds
2. **Module 2 — Federated** — Meraki events + internal runbooks + KB in one ES|QL story
3. **Module 3 — Agent Builder** — agentic triage on Search (`cisco-network-events` + federated indices)

## Tasks

1. Write a **90-second** recap script hitting all three beats (bullets only) — practice **showing your team** what you learned.
2. Note **one concrete outcome** from today (e.g. faster runbook lookup, cross-index ES|QL, agent tool idea).
3. List **one next experiment** on Cisco data: index an internal wiki, try a connector POC, or extend Agent Builder tools.

## Verification

Click **Check** when your recap script is complete.
