---
slug: build-investigation-agent
id: qfltmwdse48m
type: challenge
title: Challenge 2 — Build an Investigation Agent
teaser: Configure Agent Builder for Cisco NOC workflow.
tabs:
- id: kuaglcxsbnhc
  title: Elastic Serverless
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

# Build an investigation agent

**Time:** ~25–35 minutes

## Suggested agent charter

**Name:** Cisco NOC Copilot
**Goal:** Given an alert summary, pull correlated logs (BGP + Meraki), suggest runbook steps, draft escalation note.

## Tasks

1. Open **Agent Builder** → create or explore a **new agent** (use lab-safe read-only tools where prompted).
2. Add capabilities that reference **logs** and **ES|QL** (or Observability AI Assistant if bundled).
3. Test with prompt:

> Branch 4471 reports Meraki offline and BGP flapping on `edge-dfw-01`. Summarize timeline and next steps.

4. Capture **screenshot or notes** of one successful tool invocation.

## Reference

Download **`agent-builder-cisco-playbook.md`** from workshop assets (synced on push) for tool ideas.

## Verification

Click **Check** after a test prompt returns actionable steps.

