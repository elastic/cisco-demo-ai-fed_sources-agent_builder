---
slug: hybrid-retrieval
id: ivke7lyuske8
type: challenge
title: Challenge 2 — Augment with Splunk O11Y A2A (Workflow)
teaser: "Workflow gathers Elastic context; stubbed A2A adds Splunk O11Y evidence for Branch 4471."
tabs:
- id: tab-wf-02
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
- id: tab-agent-02
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
timelimit: 900
enhanced_loading: null
---

# Augment with Splunk O11Y A2A (Workflow)

> **Thesis:** Agent Builder answers from Elastic. **Workflows + A2A** augment that answer with peer-platform evidence (Splunk Observability) — without rip-and-replace.

## Background

Meraki/BGP live in **Elastic Serverless Search**. Detectors/APM often live in **Splunk Observability**. Lab workflow **`cisco-branch-4471-splunk-o11y-a2a-rca`** stubs an A2A investigator response so you can see the pattern end-to-end.

**Time:** ~10 minutes with Workflows + Agent  
*Without AI/A2A automation this beat was usually 30–40 minutes.*

## Your task

### 1 — Run the A2A workflow

Open [button label="A2A Workflow"](tab-0) → **Cisco Branch 4471 — Splunk O11Y A2A RCA**.

1. Skim steps: ES\|QL (`meraki_context`, `network_context`, `kb_runbooks`) → **stubbed A2A** (`data.parseJson`) → `unified_rca`.
2. **Run** with defaults (`site=Branch-4471-Dallas`, `device_hint=4471`).
3. In the execution, confirm stub evidence: `WAN_EDGE_BGP_SESSION_DOWN` on `edge-dfw-01`, `MERAKI_AP_CLOUD_DISCONNECT` on `MR-AP-4471`, WAN/BGP-first hypothesis (do not RMA the AP).

### 2 — Feed A2A into the Cisco Agent

Open [button label="Cisco Agent"](tab-1) (`Cisco NOC Copilot`) and paste:

```text
I ran workflow cisco-branch-4471-splunk-o11y-a2a-rca. Using Elastic indices plus this Splunk O11Y A2A stub summary, produce a short RCA:

- WAN_EDGE_BGP_SESSION_DOWN on edge-dfw-01 (critical, ~18m)
- MERAKI_AP_CLOUD_DISCONNECT on MR-AP-4471 (major, ~14m)
- WAN latency p95 ~420ms vs ~35ms baseline; uplink ~91%; BGP Idle to 203.0.113.1

Correlate with cisco-meraki-events and cisco-network-events for Branch 4471. Explicitly say Splunk data is workshop_demo stub. End with: WAN/BGP first — do not RMA the AP.
```

### 3 — Capture one line

In notes: *Elastic events + stubbed Splunk A2A → same root cause (ISP-A / edge-dfw-01).*

## Success criteria

- A2A workflow run completes with stub Splunk evidence
- `Cisco NOC Copilot` returns a correlated RCA citing Elastic + stubbed A2A
- Notes capture the WAN/BGP-first takeaway

## Verification

Click **Check** when the success criteria are met.

