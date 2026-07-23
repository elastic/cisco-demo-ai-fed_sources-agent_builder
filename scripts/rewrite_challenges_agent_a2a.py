#!/usr/bin/env python3
"""Rewrite workshop challenges around Agent Builder + Workflows + A2A."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CSP = """  custom_request_headers:
  - key: Content-Security-Policy
    value: 'script-src ''self'' https://kibana.estccdn.com; worker-src blob: ''self'';
      style-src ''unsafe-inline'' ''self'' https://kibana.estccdn.com; style-src-elem
      ''unsafe-inline'' ''self'' https://kibana.estccdn.com'
  custom_response_headers:
  - key: Content-Security-Policy
    value: 'script-src ''self'' https://kibana.estccdn.com; worker-src blob: ''self'';
      style-src ''unsafe-inline'' ''self'' https://kibana.estccdn.com; style-src-elem
      ''unsafe-inline'' ''self'' https://kibana.estccdn.com'"""

AGENT = "Cisco NOC Copilot"
WF = "Cisco Branch 4471 — Splunk O11Y A2A RCA"
WF_ID = "cisco-branch-4471-splunk-o11y-a2a-rca"

# Discover / Dashboards / ES|QL default to a short window; seed data spans the day.
TIME_TIP = (
    "> **Tip:** If Discover, Dashboards, or ES|QL show no data, expand the time picker "
    "to **Last 24 hours** (Branch 4471 workshop events are seeded across the day).\n"
)


def tab(title: str, path: str, tab_id: str) -> str:
    # Quote paths so YAML treats #fragments as part of the string (Instruqt tabs).
    path_yaml = path if path.startswith(('"', "'")) else f'"{path}"'
    return f"""- id: {tab_id}
  title: {title}
  type: service
  hostname: es3-api
  path: {path_yaml}
  port: 8080
{CSP}"""


def front(
    *,
    slug: str,
    title: str,
    teaser: str,
    tabs: str,
    timelimit: int,
    existing_id: str | None,
) -> str:
    id_line = f"id: {existing_id}\n" if existing_id else ""
    return f"""slug: {slug}
{id_line}type: challenge
title: {title}
teaser: "{teaser}"
tabs:
{tabs}
difficulty: intermediate
timelimit: {timelimit}
enhanced_loading: null
"""


def read_id(path: Path) -> str | None:
    if not path.is_file():
        return None
    m = re.search(r"^id: (.+)$", path.read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else None


CHECK_TIP = (
    "> If Check says **Something went wrong while checking**, wait until Kibana is "
    "fully loaded, wait ~30 seconds, then click **Check** again. That message means "
    "the lab host was not ready — not that your work failed.\n"
)


def with_time_tip(body: str) -> str:
    body = body.lstrip()
    if "Last 24 hours" not in body:
        if "## Background" in body:
            body = body.replace("## Background", f"{TIME_TIP}\n## Background", 1)
        else:
            body = f"{TIME_TIP}\n{body}"
    return body


def with_check_tip(body: str) -> str:
    if "Something went wrong while checking" in body:
        return body
    if "## Verification" in body:
        return body.replace(
            "## Verification\n\nClick **Check** when the success criteria are met.\n",
            f"## Verification\n\nClick **Check** when the success criteria are met.\n\n{CHECK_TIP}",
            1,
        )
    return body + f"\n## Verification\n\nClick **Check** when ready.\n\n{CHECK_TIP}"


def write_assignment(path: Path, fm: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = with_check_tip(with_time_tip(body))
    path.write_text(f"---\n{fm}---\n\n{body}\n", encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


CHALLENGES = {
    "01": {
        "slug": "explore-cisco-kb",
        "title": "Challenge 1 — Create the Cisco Agent & find the runbook",
        "teaser": "Stand up Cisco NOC Copilot in Agent Builder — then ask Branch 4471.",
        "timelimit": 600,
        "tabs": "\n".join(
            [
                tab("Cisco Agent", "/app/agent_builder", "tab-agent-01"),
                tab("NOC Dashboard", "/app/dashboards#/view/cisco-noc-ops", "tab-dash-01"),
            ]
        ),
        "body": f"""# Create the Cisco Agent & find the runbook

> **Thesis:** Don't start in raw Discover. Create a **Cisco Agent** in Agent Builder that queries Serverless Search — then use it for every later challenge.

## Background

NOC chat: *"Branch 4471 — Meraki AP offline, edge BGP looking ugly. Where's the recovery runbook?"*

Seeded for you: **Cisco NOC Command Center** dashboard + `cisco-network-kb`.

**Time:** ~5 minutes with Agent Builder  
*Without AI/agent tooling this beat was usually 15–20 minutes.*

## Your task

### 1 — Orient (30 seconds)

Open [button label="NOC Dashboard"](tab-1). Confirm **Branch-4471-Dallas** appears in Meraki offline and/or network panels. If panels are empty, set time to **Last 24 hours**.

### 2 — Select **{AGENT}**

Open [button label="Cisco Agent"](tab-0) → **Agent Builder**.

Setup seeds **`{AGENT}`** (`cisco-noc-copilot`). Open the agent dropdown → select **{AGENT}** (not only *Elastic AI Agent*).

If it is missing, click **+ New agent** and create:

| | |
|--|--|
| **Name** | `{AGENT}` |
| **Goal** | Investigate Cisco Branch 4471: correlate Meraki + BGP signals with KB runbooks; draft next steps |
| **Tools** | ES\\|QL / search over `cisco-network-kb`, `cisco-meraki-events`, `cisco-network-events` |

### 3 — Ask the agent for runbooks

With **{AGENT}** selected, paste:

```text
Branch 4471 — Meraki AP offline, edge BGP looking ugly. Where's the recovery runbook?
Use cisco-network-kb. Return both Meraki offline and BGP neighbor guidance with numbered first steps.
```

Confirm tool calls hit Search indices and you get **Meraki AP Offline Recovery** + **BGP Neighbor Down — IOS-XE Troubleshooting** (or equivalent titles).

## Success criteria

- `{AGENT}` exists with Search-backed tools
- Agent returns Meraki + BGP recovery steps grounded in `cisco-network-kb`
- NOC dashboard shows Branch 4471 signals

## Verification

Click **Check** when the success criteria are met.
""",
    },
    "02": {
        "slug": "hybrid-retrieval",
        "title": "Challenge 2 — Augment with Splunk O11Y A2A (Workflow)",
        "teaser": "Workflow gathers Elastic context; stubbed A2A adds Splunk O11Y evidence for Branch 4471.",
        "timelimit": 900,
        "tabs": "\n".join(
            [
                tab("A2A Workflow", "/app/workflows", "tab-wf-02"),
                tab("Cisco Agent", "/app/agent_builder", "tab-agent-02"),
            ]
        ),
        "body": f"""# Augment with Splunk O11Y A2A (Workflow)

> **Thesis:** Agent Builder answers from Elastic. **Workflows + A2A** augment that answer with peer-platform evidence (Splunk Observability) — without rip-and-replace.

## Background

Meraki/BGP live in **Elastic Serverless Search**. Detectors/APM often live in **Splunk Observability**. Lab workflow **`{WF_ID}`** stubs an A2A investigator response so you can see the pattern end-to-end.

**Time:** ~10 minutes with Workflows + Agent  
*Without AI/A2A automation this beat was usually 30–40 minutes.*

## Your task

### 1 — Run the A2A workflow

Open [button label="A2A Workflow"](tab-0) → **{WF}**.

1. Skim steps: ES\\|QL (`meraki_context`, `network_context`, `kb_runbooks`) → **stubbed A2A** (`data.parseJson`) → `unified_rca`.
2. **Run** with defaults (`site=Branch-4471-Dallas`, `device_hint=4471`).
3. In the execution, confirm stub evidence: `WAN_EDGE_BGP_SESSION_DOWN` on `edge-dfw-01`, `MERAKI_AP_CLOUD_DISCONNECT` on `MR-AP-4471`, WAN/BGP-first hypothesis (do not RMA the AP).

### 2 — Feed A2A into the Cisco Agent

Open [button label="Cisco Agent"](tab-1) → agent dropdown → select **`{AGENT}`** (seeded at lab start; create via **+ New agent** if missing). Paste:

```text
I ran workflow {WF_ID}. Using Elastic indices plus this Splunk O11Y A2A stub summary, produce a short RCA:

- WAN_EDGE_BGP_SESSION_DOWN on edge-dfw-01 (critical, ~18m)
- MERAKI_AP_CLOUD_DISCONNECT on MR-AP-4471 (major, ~14m)
- WAN latency p95 ~420ms vs ~35ms baseline; uplink ~91%; BGP Idle to 203.0.113.1

Correlate with cisco-meraki-events and cisco-network-events for Branch 4471. Explicitly say Splunk data is workshop_demo stub. End with: WAN/BGP first — do not RMA the AP.
```

### 3 — Capture one line

In notes: *Elastic events + stubbed Splunk A2A → same root cause (ISP-A / edge-dfw-01).*

## Success criteria

- A2A workflow run completes with stub Splunk evidence
- `{AGENT}` returns a correlated RCA citing Elastic + stubbed A2A
- Notes capture the WAN/BGP-first takeaway

## Verification

Click **Check** when the success criteria are met.
""",
    },
    "03": {
        "slug": "customer-talk-track",
        "title": "Challenge 3 — Agent drafts the peer story",
        "teaser": "Cisco NOC Copilot writes the Slack/email update — Find + A2A proof included.",
        "timelimit": 300,
        "tabs": tab("Cisco Agent", "/app/agent_builder", "tab-agent-03"),
        "body": f"""# Agent drafts the peer story

> **Thesis:** The Cisco Agent already saw Elastic + A2A proof — let it write the peer update. You review once and send.

## Background

You've created `{AGENT}`, found runbooks, and augmented with stubbed Splunk O11Y A2A. Package that for a peer or skip-level.

**Time:** ~1–2 minutes with the Agent  
*Without AI this beat was usually **15–20 minutes** of hand-written talk track.*

## Your task

Open [button label="Cisco Agent"](tab-0) and paste:

```text
Write a peer / skip-level Slack or email update about what we proved on Elastic Serverless Search for Cisco Branch 4471.

Ground it in:
- Agent Builder agent `{AGENT}` querying cisco-network-kb / Meraki / BGP indices
- Workflow `{WF_ID}` augmenting with stubbed Splunk Observability A2A (WAN_EDGE_BGP_SESSION_DOWN + MERAKI_AP_CLOUD_DISCONNECT; WAN/BGP first)

Produce:
1. Subject line
2. 60-second spoken narrative
3. Beats table: Pain | Outcome | Proof | What's next | Ask
4. First team to engage (NOC, platform, or GSE) + why
5. One-sentence next ask

Be explicit that Splunk evidence is the A2A workshop stub.
```

Skim once; if Proof is thin, reply *Expand Proof with Branch 4471 + A2A detectors.* Copy final write-up to notes.

## Success criteria

- Agent returns full peer write-up (subject, narrative, beats, team, ask)
- Write-up mentions Agent Builder + stubbed Splunk O11Y A2A

## Verification

Click **Check** when you have the write-up in notes.
""",
    },
    "04": {
        "slug": "map-data-silos",
        "title": "Challenge 4 — Map silos the Agent will query",
        "teaser": "Four Search indices = four silos — inventory them, then ask the Cisco Agent who owns each.",
        "timelimit": 600,
        "tabs": "\n".join(
            [
                tab(
                    "Indices",
                    "/app/management/data/index_management/indices",
                    "tab-idx-04",
                ),
                tab("Cisco Agent", "/app/agent_builder", "tab-agent-04"),
            ]
        ),
        "body": f"""# Map silos the Agent will query

> **Thesis:** Federation is not rip-and-replace. `{AGENT}` only gets smarter when you map which silos feed Serverless Search.

## Background

Branch 4471 needs more than a KB. Setup seeded four indices in **one** Serverless Search project.

| Index | Simulates | Owner persona |
|-------|-----------|---------------|
| `cisco-network-kb` | Public / TAC docs | TAC / GSE |
| `cisco-internal-runbooks` | Internal wiki | NOC lead |
| `cisco-meraki-events` | Meraki connector sync | NetOps |
| `cisco-network-events` | BGP / DNA-style signals | Network eng |

**Time:** ~5 minutes with the Agent  
*Without AI this beat was usually 15–20 minutes.*

## Your task

### 1 — Confirm indices

Open [button label="Indices"](tab-0). Confirm all **four** indices exist.

### 2 — Spot-check Meraki fields

Open Discover on `cisco-meraki-events` (or ask the agent which fields matter). Set time to **Last 24 hours** if the table is empty. Note `event_type`, `device_name`, `site`.

### 3 — Ask the Agent to map ownership

Open [button label="Cisco Agent"](tab-1) and paste:

```text
We have four indices: cisco-network-kb, cisco-internal-runbooks, cisco-meraki-events, cisco-network-events.
For each: (1) what real Cisco system it maps to, (2) who owns it, (3) why {AGENT} needs ES|QL access.
Return a compact table. End with one sentence on how Splunk O11Y A2A (workflow {WF_ID}) augments — not replaces — these silos.
```

## Success criteria

- All four indices confirmed
- Agent returns ownership/mapping table
- Notes mention A2A as augmentation (not rip-and-replace)

## Verification

Click **Check** when the success criteria are met.
""",
    },
    "05": {
        "slug": "cross-source-esql",
        "title": "Challenge 5 — Correlate event + runbook with the Agent",
        "teaser": "Cisco NOC Copilot joins Meraki offline events with KB recovery — federation in one ask.",
        "timelimit": 600,
        "tabs": "\n".join(
            [
                tab("Cisco Agent", "/app/agent_builder", "tab-agent-05"),
                tab("ES|QL", "/app/elasticsearch/query", "tab-esql-05"),
            ]
        ),
        "body": f"""# Correlate event + runbook with the Agent

> **Thesis:** Cross-index correlation is the Agent's job. You verify once with ES\\|QL; the Agent does the join narrative.

## Background

**Scenario:** Meraki AP **MR-AP-4471** went offline. Find the **event** and the **recovery runbook** in the same Serverless Search project — then let `{AGENT}` explain the link.

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

In notes: *Next we already augment this Elastic card with Splunk O11Y via workflow `{WF_ID}` (Challenge 2 / 7).*

## Success criteria

- Agent returns timestamp + site + Meraki runbook title
- First recovery steps captured

## Verification

Click **Check** when the success criteria are met.
""",
    },
    "06": {
        "slug": "connector-story",
        "title": "Challenge 6 — Plan federation with Agent + Workflows",
        "teaser": "Connectors feed Search; the Cisco Agent + A2A workflow are the query/augment layer.",
        "timelimit": 480,
        "tabs": "\n".join(
            [
                tab("Cisco Agent", "/app/agent_builder", "tab-agent-06"),
                tab(
                    "Content connectors",
                    "/app/management/data/search_connectors/connectors",
                    "tab-conn-06",
                ),
            ]
        ),
        "body": f"""# Plan federation with Agent + Workflows

> **Thesis:** Content connectors keep Meraki/ITSM authoritative. `{AGENT}` + Workflows/A2A are how you **query and augment** — not replace — those systems.

## Background

Lab indices simulate a connector-fed world. Production uses **Elastic content connectors** into the same Serverless Search project.

**Time:** ~3–5 minutes with the Agent  
*Without AI this beat was usually 15–20 minutes.*

## Your task

### 1 — Tour Content connectors (30 seconds)

Open [button label="Content connectors"](tab-1). Skim available types — no production connector required. If you see **Application not found**, open Kibana global search and type **Content connectors** (path: Stack Management → Content connectors).

### 2 — Agent writes the federation plan

Open [button label="Cisco Agent"](tab-0) (`{AGENT}`) and paste:

```text
Draft a federation plan for Cisco on Elastic Serverless Search.

Lab already has: cisco-meraki-events, cisco-network-kb, cisco-internal-runbooks, cisco-network-events.
Production uses Elastic connectors (not rip-and-replace).
We also run workflow {WF_ID} for stubbed Splunk O11Y A2A augmentation.

Output under 150 words:
1. Two connector types relevant to Cisco + why
2. Three bullets: what stays authoritative vs what gets indexed
3. How {AGENT} tools + the A2A workflow divide labor (Search query vs peer-platform augment)
```

Copy into notes.

## Success criteria

- Two connector types chosen
- Federation bullets written
- Agent explains Agent vs A2A workflow roles

## Verification

Click **Check** when the success criteria are met.
""",
    },
    "07": {
        "slug": "triage-network-signals",
        "title": "Challenge 7 — Triage with Agent + A2A Workflow",
        "teaser": "Re-run the inject — Cisco Agent for Elastic signals, Workflow A2A for Splunk O11Y.",
        "timelimit": 600,
        "tabs": "\n".join(
            [
                tab("Cisco Agent", "/app/agent_builder", "tab-agent-07"),
                tab("A2A Workflow", "/app/workflows", "tab-wf-07"),
            ]
        ),
        "body": f"""# Triage with Agent + A2A Workflow

> **Thesis:** Live triage = `{AGENT}` on Elastic indices **plus** Workflow A2A for Splunk O11Y — same Branch 4471 inject, two automation surfaces.

## Background

Pager: *"BGP session down on edge router + Meraki AP offline at Branch 4471."*

**Time:** ~5 minutes with Agent + Workflow  
*Without AI this beat was usually 15–20 minutes.*

## Your task

### 1 — Agent triage (Elastic)

Open [button label="Cisco Agent"](tab-0) and paste:

```text
Triage Branch 4471 now.
1) BGP session_down from cisco-network-events (host, site, message)
2) Meraki device.offline for *4471* from cisco-meraki-events
3) One KB runbook title to open next
Return a 5-line pager update.
```

### 2 — A2A augment (Splunk stub)

Open [button label="A2A Workflow"](tab-1) → **{WF}** → **Run** (defaults). Confirm stub detectors still align with the Agent's Elastic timeline (BGP before / with Meraki cloud disconnect).

### 3 — One decision

In notes: *Primary action = transport/ISP on edge-dfw-01; AP RMA is secondary.*

## Success criteria

- Agent returns BGP + Meraki triage card
- A2A workflow run shows matching stub Splunk evidence
- Decision note written

## Verification

Click **Check** when the success criteria are met.
""",
    },
    "08": {
        "slug": "build-investigation-agent",
        "title": "Challenge 8 — Harden Cisco NOC Copilot",
        "teaser": "Tighten tools, retest Branch 4471, and make A2A workflow part of the agent story.",
        "timelimit": 900,
        "tabs": "\n".join(
            [
                tab("Cisco Agent", "/app/agent_builder", "tab-agent-08"),
                tab("A2A Workflow", "/app/workflows", "tab-wf-08"),
            ]
        ),
        "body": f"""# Harden Cisco NOC Copilot

> **Thesis:** Challenge 1 created the agent. Now harden it: tools, prompts, and an explicit link to the A2A workflow for Splunk augmentation.

## Background

Charter check for `{AGENT}`:

| | |
|--|--|
| **Goal** | Correlate Meraki + BGP + KB; call for A2A/Splunk evidence when peer-platform confirmation is needed |
| **Data** | `cisco-network-events`, `cisco-meraki-events`, `cisco-network-kb`, `cisco-internal-runbooks` |
| **Augment** | Workflow `{WF_ID}` (stubbed Splunk O11Y A2A in lab) |

**Time:** ~10–15 minutes with Agent Builder  
*Without AI this beat was usually 25–35 minutes.*

## Your task

### 1 — Harden tools

Open [button label="Cisco Agent"](tab-0). Ensure ES\\|QL (or search) tools cover all four indices. Add a short instruction in the agent instructions/prompt:

```text
When Branch 4471 or Meraki+BGP incidents appear, summarize Elastic evidence first.
Then tell the analyst to run workflow {WF_ID} for Splunk O11Y A2A augmentation (lab = stub).
Never invent live Splunk telemetry.
```

### 2 — End-to-end test prompt

```text
Branch 4471 reports Meraki offline and BGP flapping on edge-dfw-01.
1) Summarize Elastic timeline + KB next steps (tool calls required)
2) Tell me exactly what the Splunk O11Y A2A workflow should add
3) Draft a P2 escalation note for transport
```

Capture notes or a screenshot of one successful tool invocation.

### 3 — Optional: re-run A2A workflow

[button label="A2A Workflow"](tab-1) → Run once if you want a fresh stub payload for the escalation note.

## Reference

Workshop assets: **`agent-builder-cisco-playbook.md`**.

## Success criteria

- `{AGENT}` has multi-index tools + A2A workflow guidance in instructions
- Test prompt returns actionable steps with tool use
- Escalation note drafted

## Verification

Click **Check** after a test prompt returns actionable steps.
""",
    },
    "09": {
        "slug": "exec-demo-close",
        "title": "Challenge 9 — Close the loop with the Cisco Agent",
        "teaser": "Agent recap: Find → Federate → Act, with Workflows/A2A called out as the augment path.",
        "timelimit": 300,
        "tabs": tab("Cisco Agent", "/app/agent_builder", "tab-agent-09"),
        "body": f"""# Close the loop with the Cisco Agent

> **Thesis:** Same Serverless Search project the whole way — Agent Builder for Elastic action, Workflows/A2A for peer-platform augment.

## Background

You stayed on **Elastic Serverless Search**: created `{AGENT}`, mapped silos, correlated events, and ran stubbed Splunk O11Y A2A.

**Time:** ~2–3 minutes with the Agent  
*Without AI this beat was usually 15–20 minutes.*

## Your task

Open [button label="Cisco Agent"](tab-0) and paste:

```text
Write a close-out for my team after the Cisco Elastic Serverless Search workshop.

Include:
1. 90-second Find → Federate → Act recap (spoken bullets)
2. How {AGENT} (Agent Builder) + workflow {WF_ID} (A2A stub) divided labor
3. One concrete outcome from today
4. One next experiment on Serverless Search (connector POC, more agent tools, or real A2A bridge URL)
5. One sentence on AI time compression (manual write-ups → agent paste prompts)

Splunk evidence in this lab is workshop_demo stub only.
```

Copy the write-up into notes.

## Success criteria

- Agent returns Find → Federate → Act recap naming Agent Builder + A2A workflow
- One outcome + one next experiment included

## Verification

Click **Check** when your recap is complete.
""",
    },
}

# Map challenge number → (module track slug, source challenge dir)
SRC = {
    "01": ("cisco-w1-ai-search", "01-explore-cisco-kb"),
    "02": ("cisco-w1-ai-search", "02-hybrid-retrieval"),
    "03": ("cisco-w1-ai-search", "03-customer-talk-track"),
    "04": ("cisco-w2-federated-sources", "01-map-data-silos"),
    "05": ("cisco-w2-federated-sources", "02-cross-source-esql"),
    "06": ("cisco-w2-federated-sources", "03-connector-story"),
    "07": ("cisco-w3-agent-builder", "01-triage-network-signals"),
    "08": ("cisco-w3-agent-builder", "02-build-investigation-agent"),
    "09": ("cisco-w3-agent-builder", "03-exec-demo-close"),
}

DEST = {
    "01": "01-explore-cisco-kb",
    "02": "02-hybrid-retrieval",
    "03": "03-customer-talk-track",
    "04": "04-map-data-silos",
    "05": "05-cross-source-esql",
    "06": "06-connector-story",
    "07": "07-triage-network-signals",
    "08": "08-build-investigation-agent",
    "09": "09-exec-demo-close",
}


def main() -> None:
    # Write module-track sources only; build-combined-track.py materializes the combined track.
    for num, spec in CHALLENGES.items():
        src_slug, src_ch = SRC[num]
        path = ROOT / "tracks" / src_slug / src_ch / "assignment.md"
        existing = read_id(path)
        fm = front(
            slug=spec["slug"],
            title=spec["title"],
            teaser=spec["teaser"],
            tabs=spec["tabs"],
            timelimit=spec["timelimit"],
            existing_id=existing,
        )
        write_assignment(path, fm, spec["body"])


if __name__ == "__main__":
    main()
