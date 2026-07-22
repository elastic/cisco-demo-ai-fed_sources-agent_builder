---
slug: build-investigation-agent
id: gyebeza3rkxx
type: challenge
title: Challenge 8 — Build the NOC investigation agent
teaser: Wire Agent Builder to your Serverless Search indices — then ask about Branch
  4471.
tabs:
- id: a1webiqejm77
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
timelimit: 2100
enhanced_loading: null
---

> **Module 3 — Act** · one **Elastic Serverless Search** project

# Build the NOC investigation agent

## Background

You’ve found runbooks, federated indices, and triaged the inject by hand. Now give a **Serverless Search–backed** agent the same tools.

**Time:** ~25–35 minutes

## Suggested agent charter

| | |
|--|--|
| **Name** | Cisco NOC Copilot |
| **Goal** | Given an alert summary, correlate Search indices (BGP + Meraki) with KB runbooks, suggest steps, draft an escalation note |
| **Data** | `cisco-network-events`, `cisco-meraki-events`, `cisco-network-kb` (+ optional internal runbooks) |

## Your task

1. Open **Agent Builder** → create or explore a **new agent** (use lab-safe read-only tools where prompted).
2. Add capabilities that reference **ES|QL** over `cisco-network-events`, `cisco-meraki-events`, and `cisco-network-kb`.
3. Test with:

> Branch 4471 reports Meraki offline and BGP flapping on `edge-dfw-01`. Summarize timeline and next steps.

4. Capture **notes or a screenshot** of one successful tool invocation.

## Optional — Splunk O11Y A2A workflow

Open **Workflows** → **Cisco Branch 4471 — Splunk O11Y A2A RCA** (`cisco-branch-4471-splunk-o11y-a2a-rca`).
It gathers Meraki + BGP ES|QL context, calls a Splunk Observability A2A bridge (set `consts.splunk_o11y_a2a_url`), then synthesizes RCA with Agent Builder. Run it manually with the defaults for this lab.

## Reference

Workshop assets include **`agent-builder-cisco-playbook.md`** for tool ideas.

## Success criteria

- Agent exists with Search-backed capabilities
- Test prompt returns actionable steps grounded in lab indices

## Verification

Click **Check** after a test prompt returns actionable steps.
