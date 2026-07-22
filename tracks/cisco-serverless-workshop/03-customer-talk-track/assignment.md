---
slug: customer-talk-track
id: jm4lleffufhm
type: challenge
title: Challenge 3 — Share the story with your peers
teaser: Sixty seconds — pain, Serverless Search proof, what's next.
tabs:
- id: ki5dykpv5n48
  title: Elastic Serverless Search
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

> **Module 1 — Find** · one **Elastic Serverless Search** project

# Explain it to your team

## Background

You've proved **Find** on one **Elastic Serverless Search** project. Next modules add federation and an investigation agent — same project, more sources.

**Time:** ~15–20 minutes

## Story outline (for a peer or skip-level)

| Beat | Your line |
|------|-----------|
| Pain | Cisco teams search **Meraki, IOS-XE, DNA Center, Talos** in silos |
| Outcome | **One Serverless Search** project — keyword + hybrid on runbooks |
| Proof | Live query: BGP down + Meraki offline guidance in **seconds** |
| What's next | Federate events + runbooks (Module 2), then Agent Builder (Module 3) |
| Ask | Which team owns the first index we should bring in? |

## Your task

1. Re-run your **best** search from Challenge 2 as a show-and-tell moment.
2. Draft a **60-second** explanation (notes or voice-memo outline) using the table above.
3. Name **one** internal team (NOC, platform, or GSE) that would benefit first.

## Success criteria

- Story outline table is filled for your context
- One beneficiary team is named

## Verification

Click **Check** when the success criteria are met.
