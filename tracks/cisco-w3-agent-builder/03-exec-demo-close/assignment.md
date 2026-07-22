---
slug: exec-demo-close
id: joojvtikxray
type: challenge
title: Challenge 3 — Executive Demo Close
teaser: W1→W2→W3 arc for Cisco leadership.
tabs:
- id: pft5s8qlrfpp
  title: Elastic Serverless
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

# Executive demo close

**Time:** ~15–20 minutes

## Three-beat arc

1. **W1 AI Search** — find Meraki/BGP runbooks in seconds
2. **W2 Federated** — Meraki events + internal runbooks + KB in one ES|QL story
3. **W3 Agent Builder** — agentic triage on Search (`cisco-network-events` + federated indices)

## Tasks

1. Write a **90-second** demo script hitting all three beats (bullets only).
2. Add **one** Gartner-style proof point: unified search + agentic ops (use your own approved wording).
3. Name **next step** for a Cisco account: POV, connector phase, or Agent Builder workshop.

## Verification

Click **Check** when your demo script is complete.

