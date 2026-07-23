---
slug: cross-source-esql
id: gl5yueeob0if
type: challenge
title: Challenge 5 — Correlate event + runbook with the Agent
teaser: Cisco NOC Copilot joins Meraki offline events with KB recovery — federation
  in one ask.
tabs:
- id: jrkldkgtlnoi
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
- id: mjjonxzx1bpa
  title: ES|QL
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
timelimit: 600
enhanced_loading: null
---

> **Module 2 — Federate** · one **Elastic Serverless Search** project

# Correlate event + runbook with the Agent

> **Thesis:** Cross-index correlation is the Agent's job. You verify once with ES\|QL; the Agent does the join narrative.

## Background

**Scenario:** Meraki AP **MR-AP-4471** went offline. Find the **event** and the **recovery runbook** in the same Serverless Search project — then let `Cisco NOC Copilot` explain the link.

**Time:** ~5–8 minutes with the Agent
*Without AI this beat was usually 25–35 minutes.*

## Your task

### 1 — Agent correlation (primary)

Open [button label="Cisco Agent"](tab-0) and paste:

```text
MR-AP-4471 went offline. Using ES|QL:
1) Find the latest device.offline event in cisco-meraki-events (timestamp, site, detail)
2) Find the matching Meraki offline runbook in cisco-network-kb
3) Optionally note an escalation owner from cisco-internal-runbooks
Return a short incident card: when / where / runbook title / first two steps.
```

### 2 — Verify with ES|QL (optional but recommended)

On [button label="ES|QL"](tab-1), skim that the agent used the right indices (or paste the Meraki offline query yourself). If you get **0 results**, set the time picker to **Last 24 hours**, then re-run:

```esql
FROM cisco-meraki-events
| WHERE event_type == "device.offline" AND device_name LIKE "*4471*"
| KEEP @timestamp, device_name, site, event_type, detail
| SORT @timestamp DESC
| LIMIT 5
```

### 3 — A2A reminder

In notes: *Next we already augment this Elastic card with Splunk O11Y via workflow `cisco-branch-4471-splunk-o11y-a2a-rca` (Challenge 2 / 7).*

## Success criteria

- Agent returns timestamp + site + Meraki runbook title
- First recovery steps captured

## Verification

Click **Check** when the success criteria are met.

> If Check says **Something went wrong while checking**, wait until Kibana is fully loaded, wait ~30 seconds, then click **Check** again. That message means the lab host was not ready — not that your work failed.

