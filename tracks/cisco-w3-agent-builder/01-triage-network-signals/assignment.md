---
slug: triage-network-signals
id: zmj9ciywdm8k
type: challenge
title: Challenge 7 — Triage with Agent + A2A Workflow
teaser: Re-run the inject — Cisco Agent for Elastic signals, Workflow A2A for Splunk
  O11Y.
tabs:
- id: umdrmljrrqza
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
- id: nrwufnqwqg5h
  title: A2A Workflow
  type: service
  hostname: es3-api
  path: /app/workflows
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
timelimit: 600
enhanced_loading: null
---

# Triage with Agent + A2A Workflow

> **Thesis:** Live triage = `Cisco NOC Copilot` on Elastic indices **plus** Workflow A2A for Splunk O11Y — same Branch 4471 inject, two automation surfaces.

## Background

Pager: *"BGP session down on edge router + Meraki AP offline at Branch 4471."*

**Time:** ~5 minutes with Agent + Workflow
*Without AI this beat was usually 15–20 minutes.*

## Your task

### 1 — Agent triage (Elastic)

Open [button label="Cisco Agent"](tab-0) and paste:

```text
Triage Branch 4471 now.
1) BGP session_down from cisco-network-events (host, site, message)
2) Meraki device.offline for *4471* from cisco-meraki-events
3) One KB runbook title to open next
Return a 5-line pager update.
```

### 2 — A2A augment (Splunk stub)

Open [button label="A2A Workflow"](tab-1) → **Cisco Branch 4471 — Splunk O11Y A2A RCA** → **Run** (defaults). Confirm stub detectors still align with the Agent's Elastic timeline (BGP before / with Meraki cloud disconnect).

### 3 — One decision

In notes: *Primary action = transport/ISP on edge-dfw-01; AP RMA is secondary.*

## Success criteria

- Agent returns BGP + Meraki triage card
- A2A workflow run shows matching stub Splunk evidence
- Decision note written

## Verification

Click **Check** when the success criteria are met.

