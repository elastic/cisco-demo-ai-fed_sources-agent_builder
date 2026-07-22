---
slug: hybrid-retrieval
id: kriakav00yld
type: challenge
title: Challenge 2 — Prove hybrid retrieval
teaser: Keyword catches codes; meaning catches intent — hybrid is what NOC actually
  needs.
tabs:
- id: ugajiiyeecxu
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
timelimit: 2100
enhanced_loading: null
---

> **Module 1 — Find** · one **Elastic Serverless Search** project

# Prove hybrid retrieval

> **Thesis:** Retrieval quality — not the LLM — decides whether a Cisco agent gives a useful answer. Keyword alone misses intent; meaning alone can blur exact IDs. Hybrid wins on Serverless Search.

## Background

Engineers don't page with perfect keywords. They say *"AP keeps going offline"* or paste a neighbor IP. Same **Serverless Search** project — prove keyword ES|QL, then ask the **AI Assistant** in natural language.

**Time:** ~25–35 minutes

## Your task

### 1 — Keyword path (ES|QL)

In Discover, open the **ES|QL** editor (or Query) and run:

```esql
FROM cisco-network-kb
| WHERE MATCH(title, "offline")
   OR MATCH(content, "meraki dashboard")
| KEEP title, product, category
| LIMIT 10
```

Find **Meraki AP Offline Recovery** and note **two** troubleshooting steps from the content.

### 2 — Intent path (AI Assistant)

Open the **AI Assistant** / **Elastic AI Agent** chat panel (right side in Discover).

Paste this prompt (no perfect keywords required):

```text
Meraki access point offline cloud connectivity — what runbook should I follow, and what are the first two recovery steps?
```

Wait for tool calls. Compare how the Assistant surfaces the same guidance versus the keyword ES|QL hit list.

### 3 — Capture the hybrid takeaway

In notes, write 2–3 bullets comparing **keyword ES|QL** vs **AI Assistant** result quality for this incident (precision of titles/IDs vs. speed to actionable steps).

## Success criteria

- ES|QL returns Meraki offline guidance
- AI Assistant returns recovery steps grounded in `cisco-network-kb`
- Comparison bullets are written

## Verification

Click **Check** when the success criteria are met.
