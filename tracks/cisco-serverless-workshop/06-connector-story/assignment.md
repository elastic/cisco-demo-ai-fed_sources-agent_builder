---
slug: connector-story
id: 4nhwghz6dqsx
type: challenge
title: Challenge 6 — Plan the federation path
teaser: Connectors keep Meraki and ITSM authoritative — Serverless Search becomes
  the query layer.
tabs:
- id: lxkysevd5xw0
  title: Elastic Serverless Search
  type: service
  hostname: es3-api
  path: /app/enterprise_search/content/connectors
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
timelimit: 480
enhanced_loading: null
---

> **Module 2 — Federate** · one **Elastic Serverless Search** project

# Plan the federation path

## Background

Lab indices simulate a connector-fed world. In production, **Elastic connectors** sync Meraki-style events, wikis, and tickets into the **same Serverless Search** project you are using now.

> **Preview (Module 3):** Agent Builder will orchestrate tools over these indices. It may look unfinished until you build the agent — that is intentional.

**Time:** ~3–5 minutes with AI Assistant
*Without AI this beat was usually 15–20 minutes — paste prompts, don’t retype the story.*

## Why federation (not rip-and-replace)

- **Keep systems in place** — Meraki, DNA Center, and ITSM stay authoritative
- **Unify the query layer** — connectors sync into Serverless Search; **ES|QL** joins at query time
- **Add sources incrementally** — start with high-value indices (like this lab’s Meraki-style events)

## Your task

### 1 — Tour Connectors (30 seconds)

Open **Connectors** and skim available types (no production connector required).

### 2 — Let AI Assistant write the plan

Open **AI Assistant** (Discover or global chat) and paste:

```text
Draft a short federation plan for Cisco on Elastic Serverless Search.

Context: lab already seeded cisco-meraki-events, cisco-network-kb, cisco-internal-runbooks, cisco-network-events. Production would use Elastic connectors — not rip-and-replace Meraki/DNA/ITSM.

Output:
1. Two connector types relevant to Cisco (with one-line why each)
2. Three bullets: what stays authoritative in Cisco/cloud vs what gets indexed into Serverless Search
3. One Agent Builder tool to expose later (name + which indices)
Keep it under 150 words.
```

Copy the answer into notes.

## Success criteria

- Two connector types chosen (via Assistant output)
- Federation bullets written
- One future agent tool named

## Verification

Click **Check** when the success criteria are met.
