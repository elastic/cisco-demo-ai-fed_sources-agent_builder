---
slug: hybrid-retrieval
id: kriakav00yld
type: challenge
title: Challenge 2 — Hybrid retrieval + Splunk O11Y A2A
teaser: Keyword and AI find the runbook — A2A brings Splunk O11Y evidence into the
  same Branch 4471 story.
tabs:
- id: ugajiiyeecxu
  title: Discover + AI
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
- id: eib8uzvxelaq
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
timelimit: 2400
enhanced_loading: null
---

> **Module 1 — Find** · one **Elastic Serverless Search** project

# Hybrid retrieval + Splunk O11Y A2A

> **Thesis:** Keyword finds exact titles; AI captures intent; **A2A** pulls peer-platform evidence (Splunk Observability) so Branch 4471 isn't an Elastic-only story.

## Background

NOC reality: Meraki + BGP show up in **Elastic Serverless Search**, while detectors and APM live in **Splunk Observability**. Agent-to-agent (A2A) is how those worlds compare notes without rip-and-replace.

This lab seeds workflow **`cisco-branch-4471-splunk-o11y-a2a-rca`** with a **stubbed** Splunk O11Y A2A response (no external gateway required) so you can see the correlation pattern end-to-end.

**Time:** ~30–40 minutes

## Your task

### 1 — Keyword path (ES|QL)

On [button label="Discover + AI"](tab-0), open the **ES|QL** editor and run:

```esql
FROM cisco-network-kb
| WHERE MATCH(title, "offline")
   OR MATCH(content, "meraki dashboard")
| KEEP title, product, category
| LIMIT 10
```

Find **Meraki AP Offline Recovery** and note **two** troubleshooting steps.

### 2 — Intent path (AI Assistant)

Open the **AI Assistant** / **Elastic AI Agent** panel and paste:

```text
Meraki access point offline cloud connectivity — what runbook should I follow, and what are the first two recovery steps?
```

Compare keyword hit list vs. Assistant guidance (precision of titles vs. speed to steps).

### 3 — Elastic event context (what A2A will consume)

Still in Discover / ES|QL, run:

```esql
FROM cisco-meraki-events
| WHERE @timestamp > NOW() - 24 hours
  AND event_type == "device.offline"
  AND device_name LIKE "*4471*"
| KEEP @timestamp, site, device_name, event_type, detail
| SORT @timestamp DESC
| LIMIT 5
```

Optional BGP companion:

```esql
FROM cisco-network-events
| WHERE @timestamp > NOW() - 24 hours AND event_type == "bgp.session_down"
| KEEP @timestamp, `cisco.site`, `host.name`, event_type, message
| SORT @timestamp DESC
| LIMIT 5
```

### 4 — Splunk O11Y A2A correlation (stubbed)

Open [button label="A2A Workflow"](tab-1) → **Cisco Branch 4471 — Splunk O11Y A2A RCA**.

1. Skim the YAML: ES|QL gathers Meraki + BGP + KB, then a **`data.parseJson` stub** returns a fake Splunk O11Y A2A investigator payload (detectors, latency, log patterns).
2. **Run** the workflow with defaults (`site=Branch-4471-Dallas`, `device_hint=4471`).
3. In the execution output, find the stub evidence (e.g. `WAN_EDGE_BGP_SESSION_DOWN`, Meraki cloud disconnect) and note how it lines up with your Elastic events from step 3.

> Production swap: replace the stub step with an `http` POST to `consts.splunk_o11y_a2a_url` when you have a real A2A bridge.

### 5 — Talk-track bullets

In notes, capture **three lines**:

1. Keyword vs AI Assistant (retrieval)
2. Elastic Meraki/BGP signal for 4471
3. How stubbed Splunk O11Y A2A evidence would change the RCA (WAN/BGP first vs AP RMA)

## Success criteria

- ES|QL + AI Assistant surface Meraki offline guidance
- Meraki (and ideally BGP) events for 4471 are visible in ES|QL
- A2A workflow run shows stubbed Splunk O11Y evidence correlated to the Elastic story
- Three talk-track bullets are written

## Verification

Click **Check** when the success criteria are met.
