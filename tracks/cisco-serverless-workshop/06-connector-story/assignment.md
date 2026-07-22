---
slug: connector-story
id: buau85hegypi
type: challenge
title: Challenge 3 — Connectors & federated sources
teaser: See how connectors let you federate Meraki and internal sources without rip-and-replace.
tabs:
- id: nalu5qy1vqsy
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

> **Module 2 — Federated Data Sources** · one **Serverless Search** project

# Federate sources with connectors

**Time:** ~15–20 minutes

## Why federation (not rip-and-replace)

- **Keep systems in place** — Meraki, DNA Center, and ITSM stay authoritative
- **Unify the query layer** — connectors sync content and events into Serverless Search; **ES|QL** joins them at query time
- **Add sources incrementally** — start with high-value indices (like this lab's Meraki-style events) before expanding

## Tasks

1. Browse **Connectors** in Kibana (UI tour — no production connector required in lab).
2. Pick **two** connector types relevant to Cisco environments (e.g. ServiceNow, SharePoint, MongoDB, GitHub).
3. Write **3 bullets**: what stays in existing Cisco/cloud systems vs. what gets indexed for search in Elastic.
4. Tie Module 1 search patterns to Module 3 **Agent Builder** tools on the same indices.

## Verification

Click **Check** when connectors + federated bullets are in your notes.
