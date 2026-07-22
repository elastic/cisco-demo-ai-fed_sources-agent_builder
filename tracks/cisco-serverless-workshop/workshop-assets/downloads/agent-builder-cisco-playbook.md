# Agent Builder — Cisco NOC Copilot playbook (Serverless Search)

## Create once (Challenge 1), reuse always

| | |
|--|--|
| **Name** | `Cisco NOC Copilot` |
| **Goal** | Investigate Branch 4471: correlate Meraki + BGP with KB; call for Splunk O11Y A2A when peer-platform evidence is needed |
| **Project** | Elastic Serverless Search only |

## Suggested tools / skills

- **ES|QL** (or index search) on:
  - `cisco-network-kb`
  - `cisco-meraki-events`
  - `cisco-network-events`
  - `cisco-internal-runbooks`
- Optional instruction snippet:

```text
Summarize Elastic evidence first. For Splunk Observability confirmation, tell the analyst to run
workflow cisco-branch-4471-splunk-o11y-a2a-rca (lab = stubbed A2A). Never invent live Splunk telemetry.
```

## Workflows + A2A (augment, don't replace)

| Asset | Role |
|-------|------|
| `cisco-branch-4471-splunk-o11y-a2a-rca` | ES\|QL gather → stubbed Splunk O11Y A2A → unified RCA |
| Agent Builder | Query/reason over Elastic indices; draft notes & escalations |

Production: swap the workflow stub for `http` POST to your A2A bridge (`consts.splunk_o11y_a2a_url`).

## Test prompts

1. *Branch 4471 — Meraki AP offline, edge BGP looking ugly. Where's the recovery runbook?*
2. *MR-AP-4471 offline — event card + KB first steps + escalation owner.*
3. *Correlate Elastic Meraki/BGP with Splunk O11Y A2A stub (WAN_EDGE_BGP_SESSION_DOWN). WAN/BGP first?*
4. *Draft a P2 escalation note for transport on edge-dfw-01.*

## Time picker

If Discover, Dashboards, or ES|QL look empty, set time to **Last 24 hours**. Branch 4471 seed events span the day.

## Demo guardrails

- Read-only tools in shared org labs
- Stay on **Search** — do not position Observability or Security projects in this workshop
- Label Splunk evidence as **workshop_demo stub** unless a real A2A bridge is configured
