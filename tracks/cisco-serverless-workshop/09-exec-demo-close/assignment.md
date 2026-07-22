---
slug: exec-demo-close
id: hjwatcfnabka
type: challenge
title: Challenge 9 — Close the loop with the Cisco Agent
teaser: 'Agent recap: Find → Federate → Act, with Workflows/A2A called out as the
  augment path.'
tabs:
- id: ueyhge9zn0wv
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

> **Module 3 — Act** · one **Elastic Serverless Search** project

# Close the loop with the Cisco Agent

> **Thesis:** Same Serverless Search project the whole way — Agent Builder for Elastic action, Workflows/A2A for peer-platform augment.

> **Tip:** If Discover, Dashboards, or ES|QL show no data, expand the time picker to **Last 24 hours** (Branch 4471 workshop events are seeded across the day).

## Background

You stayed on **Elastic Serverless Search**: created `Cisco NOC Copilot`, mapped silos, correlated events, and ran stubbed Splunk O11Y A2A.

**Time:** ~2–3 minutes with the Agent
*Without AI this beat was usually 15–20 minutes.*

## Your task

Open [button label="Cisco Agent"](tab-0) and paste:

```text
Write a close-out for my team after the Cisco Elastic Serverless Search workshop.

Include:
1. 90-second Find → Federate → Act recap (spoken bullets)
2. How Cisco NOC Copilot (Agent Builder) + workflow cisco-branch-4471-splunk-o11y-a2a-rca (A2A stub) divided labor
3. One concrete outcome from today
4. One next experiment on Serverless Search (connector POC, more agent tools, or real A2A bridge URL)
5. One sentence on AI time compression (manual write-ups → agent paste prompts)

Splunk evidence in this lab is workshop_demo stub only.
```

Copy the write-up into notes.

## Success criteria

- Agent returns Find → Federate → Act recap naming Agent Builder + A2A workflow
- One outcome + one next experiment included

## Verification

Click **Check** when your recap is complete.

