---
slug: customer-talk-track
id: speognshals5
type: challenge
title: Challenge 3 — Share the story with your peers
teaser: Ask AI Assistant for a full peer write-up — pain, proof, A2A, ask.
tabs:
- id: grgy8qeiguab
  title: Elastic Serverless Search
  type: service
  hostname: es3-api
  path: /app/discover
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

# Explain it to your team

> **Thesis:** If you can show Branch 4471 in the product, the AI Assistant can draft the peer write-up — you just review and send.

## Background

You've proved **Find** on one **Elastic Serverless Search** project: keyword ES|QL, AI-assisted runbooks, and stubbed Splunk O11Y A2A correlation. Now package that for a peer or skip-level — let the Assistant do the writing.

**Time:** ~1–2 minutes with AI Assistant
*Without AI this beat was usually **15–20 minutes** of hand-written talk track. Now: paste one prompt → full peer write-up in about a minute.*

## Your task

### 1 — Open AI Assistant

In Discover, open the **AI Assistant** / **Elastic AI Agent** panel.

### 2 — Paste this prompt (full write-up)

```text
Write a peer / skip-level update I can paste into Slack or email about what we just proved on Elastic Serverless Search for Cisco Branch 4471.

Ground the proof in this lab:
- Keyword ES|QL found Meraki / BGP runbooks in cisco-network-kb
- AI Assistant answered natural-language Meraki offline questions from the same index
- Workflow cisco-branch-4471-splunk-o11y-a2a-rca correlated Elastic Meraki/BGP events with a stubbed Splunk Observability A2A response (WAN_EDGE_BGP_SESSION_DOWN + MERAKI_AP_CLOUD_DISCONNECT; WAN/BGP first, do not RMA the AP)

Produce a complete write-up with these sections:
1. Subject line
2. 60-second narrative (spoken style)
3. Story beats table: Pain | Outcome | Proof | What's next | Ask
4. Recommended first team to engage (pick one of NOC, platform, or GSE) and why
5. Suggested next ask (one sentence)

Keep it crisp, seller/SE friendly, and explicit that Splunk evidence in this lab is from the A2A workshop stub.
```

### 3 — Review once

Skim the Assistant output. If a beat is thin, reply: *Expand the Proof section with Branch 4471 specifics.* Copy the final write-up into your notes.

## Success criteria

- AI Assistant returns a full peer write-up (subject, 60s narrative, beats table, team, ask)
- Write-up mentions Serverless Search proof + stubbed Splunk O11Y A2A

## Verification

Click **Check** when you have the write-up in notes.
