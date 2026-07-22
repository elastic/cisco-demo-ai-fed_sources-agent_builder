---
slug: exec-demo-close
id: mymdtoqbvr6n
type: challenge
title: Challenge 3 — Close the loop & next steps
teaser: Find → Federate → Act on one Serverless Search project — what ships next?
tabs:
- id: ijvlkxyrfu2n
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
timelimit: 300
enhanced_loading: null
---

# Close the loop & next steps

## Background

You stayed on **Elastic Serverless Search** the whole workshop — easy to upgrade later (more indices, connectors, agents) without changing platform.

**Time:** ~2–3 minutes with AI Assistant  
*Without AI this beat was usually 15–20 minutes — paste prompts, don’t retype the story.*

## Your task

Open **AI Assistant** and paste:

```text
Write a close-out I can send my team after the Cisco Elastic Serverless Search workshop (Branch 4471 story).

Include:
1. 90-second Find → Federate → Act recap (spoken bullets)
2. One concrete outcome from today
3. One next experiment still on Serverless Search (wiki index, connector POC, or Agent Builder tools)
4. One sentence on how AI Assistant compressed the workshop (manual talk tracks / RCA writing → paste-and-run)

Mention stubbed Splunk O11Y A2A only as lab evidence, not production telemetry.
```

Copy the write-up into notes.

## Success criteria

- AI Assistant returns Find → Federate → Act recap
- One outcome + one next experiment included

## Verification

Click **Check** when your recap script is complete.
