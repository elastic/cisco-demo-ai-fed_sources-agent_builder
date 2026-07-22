---
slug: customer-talk-track
id: d5nyfqjegzlg
type: challenge
title: Challenge 3 — Agent drafts the peer story
teaser: Cisco NOC Copilot writes the Slack/email update — Find + A2A proof included.
tabs:
- id: fwlqtizorbqn
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
timelimit: 300
enhanced_loading: null
---

> **Module 1 — Find** · one **Elastic Serverless Search** project

# Agent drafts the peer story

> **Thesis:** The Cisco Agent already saw Elastic + A2A proof — let it write the peer update. You review once and send.

> **Tip:** If Discover, Dashboards, or ES|QL show no data, expand the time picker to **Last 24 hours** (Branch 4471 workshop events are seeded across the day).

## Background

You've created `Cisco NOC Copilot`, found runbooks, and augmented with stubbed Splunk O11Y A2A. Package that for a peer or skip-level.

**Time:** ~1–2 minutes with the Agent
*Without AI this beat was usually **15–20 minutes** of hand-written talk track.*

## Your task

Open [button label="Cisco Agent"](tab-0) and paste:

```text
Write a peer / skip-level Slack or email update about what we proved on Elastic Serverless Search for Cisco Branch 4471.

Ground it in:
- Agent Builder agent `Cisco NOC Copilot` querying cisco-network-kb / Meraki / BGP indices
- Workflow `cisco-branch-4471-splunk-o11y-a2a-rca` augmenting with stubbed Splunk Observability A2A (WAN_EDGE_BGP_SESSION_DOWN + MERAKI_AP_CLOUD_DISCONNECT; WAN/BGP first)

Produce:
1. Subject line
2. 60-second spoken narrative
3. Beats table: Pain | Outcome | Proof | What's next | Ask
4. First team to engage (NOC, platform, or GSE) + why
5. One-sentence next ask

Be explicit that Splunk evidence is the A2A workshop stub.
```

Skim once; if Proof is thin, reply *Expand Proof with Branch 4471 + A2A detectors.* Copy final write-up to notes.

## Success criteria

- Agent returns full peer write-up (subject, narrative, beats, team, ask)
- Write-up mentions Agent Builder + stubbed Splunk O11Y A2A

## Verification

Click **Check** when you have the write-up in notes.

