---
slug: connector-story
type: challenge
title: Challenge 3 — Connectors & Consolidation Story
teaser: Position Elastic connectors vs. rip-and-replace.
tabs:
- title: Elastic Serverless Search
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

> **Module 2 — Federated Data Sources** · one **Serverless Search** project

# Connectors talk track

**Time:** ~15–20 minutes

## Federated motion (Elastic language)

- **Displace** — replace legacy search appliance
- **Consolidate** — Meraki + DNA + ITSM into Serverless Search
- **Federate** — leave Meraki/DNA in place; **connectors + ES|QL** unify the query layer

## Tasks

1. Browse **Connectors** in Kibana (UI tour — no production connector required in lab).
2. Pick **two** connector types relevant to Cisco (e.g. ServiceNow, SharePoint, MongoDB, GitHub).
3. Write **3 bullets**: what stays in Cisco cloud vs. what Elastic indexes.
4. Tie to Workshop 1 search demo and preview Workshop 3 **Agent Builder** automation.

## Verification

Click **Check** when connectors + federated bullets are in your notes.

