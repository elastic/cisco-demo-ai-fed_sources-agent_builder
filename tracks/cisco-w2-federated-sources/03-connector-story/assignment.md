---
slug: connector-story
id: 2bbgtwukwviu
type: challenge
title: Challenge 6 — Plan federation with Agent + Workflows
teaser: Connectors feed Search; the Cisco Agent + A2A workflow are the query/augment
  layer.
tabs:
- id: q843byadyys5
  title: Connectors
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
- id: ok9j73nf9faa
  title: Cisco Agent
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
timelimit: 480
enhanced_loading: null
---

# Plan federation with Agent + Workflows

> **Thesis:** Connectors keep Meraki/ITSM authoritative. `Cisco NOC Copilot` + Workflows/A2A are how you **query and augment** — not replace — those systems.

## Background

Lab indices simulate a connector-fed world. Production uses **Elastic connectors** into the same Serverless Search project.

**Time:** ~3–5 minutes with the Agent
*Without AI this beat was usually 15–20 minutes.*

## Your task

### 1 — Tour Connectors (30 seconds)

Open [button label="Connectors"](tab-0). Skim types (no production connector required).

### 2 — Agent writes the federation plan

Open [button label="Cisco Agent"](tab-1) and paste:

```text
Draft a federation plan for Cisco on Elastic Serverless Search.

Lab already has: cisco-meraki-events, cisco-network-kb, cisco-internal-runbooks, cisco-network-events.
Production uses Elastic connectors (not rip-and-replace).
We also run workflow cisco-branch-4471-splunk-o11y-a2a-rca for stubbed Splunk O11Y A2A augmentation.

Output under 150 words:
1. Two connector types relevant to Cisco + why
2. Three bullets: what stays authoritative vs what gets indexed
3. How Cisco NOC Copilot tools + the A2A workflow divide labor (Search query vs peer-platform augment)
```

Copy into notes.

## Success criteria

- Two connector types chosen
- Federation bullets written
- Agent explains Agent vs A2A workflow roles

## Verification

Click **Check** when the success criteria are met.

