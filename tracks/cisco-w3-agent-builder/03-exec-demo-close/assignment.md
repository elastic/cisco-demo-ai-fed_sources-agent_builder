---
slug: exec-demo-close
id: mymdtoqbvr6n
type: challenge
title: Challenge 3 — Close the loop & next steps
teaser: Find → Federate → Act on one Serverless Search project — what ships next?
tabs:
- id: ijvlkxyrfu2n
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

# Close the loop & next steps

## Background

You stayed on **Elastic Serverless Search** the whole workshop — easy to upgrade later (more indices, connectors, agents) without changing platform.

**Time:** ~15–20 minutes

## Three-beat recap

1. **Find** — Meraki / BGP runbooks in seconds (hybrid beats keyword alone)
2. **Federate** — events + internal runbooks + KB in one ES|QL story
3. **Act** — Agent Builder triage on the same Serverless Search indices

## Your task

1. Write a **90-second** recap script hitting all three beats (bullets only) — for showing your team.
2. Note **one concrete outcome** from today (faster runbook lookup, cross-index ES|QL, or agent tool).
3. List **one next experiment** still on Serverless Search: index an internal wiki, try a connector POC, or extend Agent Builder tools.

## Success criteria

- Recap script covers Find → Federate → Act
- One outcome + one next experiment written

## Verification

Click **Check** when your recap script is complete.
