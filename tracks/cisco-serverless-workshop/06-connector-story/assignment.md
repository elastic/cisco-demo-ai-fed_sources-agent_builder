---
slug: connector-story
id: 2fxc00va6aop
type: challenge
title: Challenge 6 — Plan the federation path
teaser: Connectors keep Meraki and ITSM authoritative — Serverless Search becomes
  the query layer.
tabs:
- id: xppk0a6o8toc
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
timelimit: 1200
enhanced_loading: null
---

> **Module 2 — Federate** · one **Elastic Serverless Search** project

# Plan the federation path

## Background

Lab indices simulate a connector-fed world. In production, **Elastic connectors** sync Meraki-style events, wikis, and tickets into the **same Serverless Search** project you are using now.

> **Preview (Module 3):** Agent Builder will orchestrate tools over these indices. It may look unfinished until you build the agent — that is intentional.

**Time:** ~15–20 minutes

## Why federation (not rip-and-replace)

- **Keep systems in place** — Meraki, DNA Center, and ITSM stay authoritative
- **Unify the query layer** — connectors sync into Serverless Search; **ES|QL** joins at query time
- **Add sources incrementally** — start with high-value indices (like this lab’s Meraki-style events)

## Your task

1. Browse **Connectors** in Kibana (UI tour — no production connector required in this lab).
2. Pick **two** connector types relevant to Cisco environments (e.g. ServiceNow, SharePoint, MongoDB, GitHub).
3. Write **3 bullets**: what stays in existing Cisco/cloud systems vs. what gets indexed for search.
4. Note **one** Agent Builder tool you would expose later (e.g. “search Meraki offline events + KB”).

## Success criteria

- Two connector types chosen
- Federation bullets written
- One future agent tool named

## Verification

Click **Check** when the success criteria are met.
