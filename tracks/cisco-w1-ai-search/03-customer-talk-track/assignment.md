---
slug: customer-talk-track
id: 3gvfy9uno5vx
type: challenge
title: Challenge 3 — Share the story with your peers
teaser: Practice explaining hybrid search to a teammate in 60 seconds.
tabs:
- id: l0jonvx0zquw
  title: Elastic Serverless
  type: service
  hostname: es3-api
  path: /app/search
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

# Explain it to your team

**Time:** ~15–20 minutes

## Story outline (for a peer or skip-level)

| Beat | Your line |
|------|-----------|
| Pain | Cisco teams search **Meraki, IOS-XE, DNA Center, Talos** in silos |
| Outcome | **One Serverless Search** project — hybrid + semantic on runbooks |
| Proof | Live query: BGP down + Meraki offline in **under 10 seconds** |
| What's new | Vector Search + ES|QL + connectors path (Module 2) |
| Next | Federated sources + Agent Builder (Modules 2–3) |

## Tasks

1. Re-run your **best** search from Challenge 2 as a **show-and-tell** moment.
2. Draft a **60-second** explanation (notes or voice memo outline) for a teammate.
3. Name **one** internal team (NOC, platform, or GSE) that would benefit from **unified doc search**.

## Verification

Click **Check** when your story outline table is complete.
