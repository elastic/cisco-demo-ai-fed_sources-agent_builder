---
slug: hybrid-retrieval
id: jjqtp2sodqgk
type: challenge
title: Challenge 2 — Prove hybrid retrieval
teaser: Keyword catches codes; meaning catches intent — hybrid is what NOC actually
  needs.
tabs:
- id: iybw8yuudnwz
  title: Elastic Serverless Search
  type: service
  hostname: es3-api
  path: /app/elasticsearch/query
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

Engineers don't page with perfect keywords. They say *"AP keeps going offline"* or paste a neighbor IP. Same **Serverless Search** project — better query shapes.

**Time:** ~25–35 minutes

## Sample ES|QL

Run in the **ES|QL / Query** UI:

```esql
FROM cisco-network-kb
| WHERE MATCH(title, "offline")
   OR MATCH(content, "meraki dashboard")
| KEEP title, product, category
| LIMIT 10
```

Then try a natural-language style search in **Discover** (or Search UI if available):

> Meraki access point offline cloud connectivity

## Your task

1. Run the ES|QL query (or an equivalent Discover query).
2. Find the **Meraki AP Offline Recovery** document and note **two** troubleshooting steps.
3. Optional: try any **semantic / AI** search controls shown in your Serverless project.
4. In notes, write 2–3 bullets comparing **keyword** vs **natural-language** result quality for this incident.

## Success criteria

- ES|QL (or Discover) returns Meraki offline guidance
- Two recovery steps are captured
- Comparison bullets are written

## Verification

Click **Check** when the success criteria are met.
