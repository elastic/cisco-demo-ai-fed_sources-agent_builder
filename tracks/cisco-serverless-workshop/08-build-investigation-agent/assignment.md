---
slug: build-investigation-agent
id: uab2lwhctrov
type: challenge
title: Challenge 8 — Harden Cisco NOC Copilot
teaser: Tighten tools, retest Branch 4471, and make A2A workflow part of the agent
  story.
tabs:
- id: t2hrpwojxwav
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
- id: qxgqppe97aqs
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
timelimit: 900
enhanced_loading: null
---

> **Module 3 — Act** · one **Elastic Serverless Search** project

# Harden Cisco NOC Copilot

> **Thesis:** Challenge 1 created the agent. Now harden it: tools, prompts, and an explicit link to the A2A workflow for Splunk augmentation.

## Background

Charter check for `Cisco NOC Copilot`:

| | |
|--|--|
| **Goal** | Correlate Meraki + BGP + KB; call for A2A/Splunk evidence when peer-platform confirmation is needed |
| **Data** | `cisco-network-events`, `cisco-meraki-events`, `cisco-network-kb`, `cisco-internal-runbooks` |
| **Augment** | Workflow `cisco-branch-4471-splunk-o11y-a2a-rca` (stubbed Splunk O11Y A2A in lab) |

**Time:** ~10–15 minutes with Agent Builder
*Without AI this beat was usually 25–35 minutes.*

## Your task

### 1 — Harden tools

Open [button label="Cisco Agent"](tab-0). Ensure ES\|QL (or search) tools cover all four indices. Add a short instruction in the agent instructions/prompt:

```text
When Branch 4471 or Meraki+BGP incidents appear, summarize Elastic evidence first.
Then tell the analyst to run workflow cisco-branch-4471-splunk-o11y-a2a-rca for Splunk O11Y A2A augmentation (lab = stub).
Never invent live Splunk telemetry.
```

### 2 — End-to-end test prompt

```text
Branch 4471 reports Meraki offline and BGP flapping on edge-dfw-01.
1) Summarize Elastic timeline + KB next steps (tool calls required)
2) Tell me exactly what the Splunk O11Y A2A workflow should add
3) Draft a P2 escalation note for transport
```

Capture notes or a screenshot of one successful tool invocation.

### 3 — Optional: re-run A2A workflow

[button label="A2A Workflow"](tab-1) → Run once if you want a fresh stub payload for the escalation note.

## Reference

Workshop assets: **`agent-builder-cisco-playbook.md`**.

## Success criteria

- `Cisco NOC Copilot` has multi-index tools + A2A workflow guidance in instructions
- Test prompt returns actionable steps with tool use
- Escalation note drafted

## Verification

Click **Check** after a test prompt returns actionable steps.

