---
slug: customer-talk-track
type: challenge
title: Challenge 3 — Customer Talk Track
teaser: 60-second Elastic Serverless Search story for Cisco.
tabs:
- title: Elastic Serverless
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
---

# Customer talk track

**Time:** ~15–20 minutes

## Talk track template (fill in for your account)

| Beat | Your line |
|------|-----------|
| Pain | Cisco teams search **Meraki, IOS-XE, DNA Center, Talos** in silos |
| Outcome | **One Serverless Search** project — hybrid + semantic on runbooks |
| Proof | Live query: BGP down + Meraki offline in **under 10 seconds** |
| Elastic | Vector Search + ES|QL + connectors path (Workshop 2) |
| Next step | Federated sources + Agent Builder (Workshops 2–3) |

## Tasks

1. Re-run your **best** search from Challenge 2 as a **live demo** line.
2. Record a **60-second** pitch (notes or voice memo outline).
3. List **one** Cisco account or internal stakeholder who cares about **unified doc search**.

## Verification

Click **Check** when your talk track table is complete.

