---
slug: hybrid-retrieval
id: ivke7lyuske8
type: challenge
title: Challenge 2 — Hybrid & Semantic Retrieval
teaser: Compare keyword vs semantic-style queries on runbooks.
tabs:
- id: qnemh8auqgbo
  title: Elastic Serverless
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

# Hybrid retrieval lab

**Story:** Engineers ask vague questions (*"AP keeps going offline"*) — keyword search alone misses intent.

**Time:** ~25–35 minutes

## Sample ES|QL (Dev Tools or ES|QL UI)

Try in **ES|QL** (adjust if your UI uses **Query**):

```esql
FROM cisco-network-kb
| WHERE MATCH(title, "offline")
   OR MATCH(content, "meraki dashboard")
| KEEP title, product, category
| LIMIT 10
```

Then try a natural-language style query in **Search**:

> Meraki access point offline cloud connectivity

## Tasks

1. Run the ES|QL query above (or equivalent **Search** UI query).
2. Find the **Meraki AP Offline Recovery** document and note **two** troubleshooting steps from the content.
3. Optional: enable **semantic** / **AI** search features if shown in your project tier.
4. In notes, compare **keyword** vs **natural language** result quality in 2–3 bullets.

## Verification

Click **Check** after you document **Meraki offline** steps and your comparison bullets.

