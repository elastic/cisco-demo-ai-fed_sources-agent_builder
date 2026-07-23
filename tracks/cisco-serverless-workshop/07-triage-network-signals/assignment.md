---
slug: triage-network-signals
id: swavmv7lb4sv
type: challenge
title: Challenge 7 — Triage with Agent + A2A Workflow
teaser: Re-run the inject — Cisco Agent for Elastic signals, Workflow A2A for Splunk
  O11Y.
notes:
- type: text
  contents: |
    **While Elastic Serverless Search provisions (~3–4 min)** — use **← →** in the deck.

    <iframe src="https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html?v3=1" width="100%" height="720" frameborder="0"
      style="border-radius:8px;border:1px solid #2a3140;display:block;min-height:560px;background:#0b0d12">
    </iframe>

    Fullscreen: https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html
tabs:
- id: vxxwmin01a0h
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
timelimit: 600
enhanced_loading: null
---

> **Module 3 — Act** · one **Elastic Serverless Search** project

# Triage with Agent + A2A Workflow

> **Thesis:** Live triage = `Cisco NOC Copilot` on Elastic indices **plus** Workflow A2A for Splunk O11Y — same Branch 4471 inject, two automation surfaces.

> **Tip:** If Discover, Dashboards, or ES|QL show no data, expand the time picker to **Last 24 hours** (Branch 4471 workshop events are seeded across the day).

## Background

Pager: *"BGP session down on edge router + Meraki AP offline at Branch 4471."*

**Time:** ~5 minutes with Agent + Workflow
*Without AI this beat was usually 15–20 minutes.*

## Your task

Open [button label="Elastic Serverless Search"](tab-0) — one Kibana tab; switch Agents ↔ Workflows in the left nav.

### 1 — Agent triage (Elastic)

**Agents** → `Cisco NOC Copilot` and paste:

```text
Triage Branch 4471 now.
1) BGP session_down from cisco-network-events (host, site, message)
2) Meraki device.offline for *4471* from cisco-meraki-events
3) One KB runbook title to open next
Return a 5-line pager update.
```

### 2 — A2A augment (Splunk stub)

Left nav → **Workflows** → **Cisco Branch 4471 — Splunk O11Y A2A RCA** → **Run** (defaults). Confirm stub detectors still align with the Agent's Elastic timeline (BGP before / with Meraki cloud disconnect).

### 3 — One decision

In notes: *Primary action = transport/ISP on edge-dfw-01; AP RMA is secondary.*

## Success criteria

- Agent returns BGP + Meraki triage card
- A2A workflow run shows matching stub Splunk evidence
- Decision note written

## Verification

Click **Check** when the success criteria are met.

> If Check says **Something went wrong while checking**, wait until Kibana is fully loaded, wait ~30 seconds, then click **Check** again. That message means the lab host was not ready — not that your work failed.

