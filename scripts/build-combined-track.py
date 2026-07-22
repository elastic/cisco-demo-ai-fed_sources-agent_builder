#!/usr/bin/env python3
"""Build single combined Cisco Instruqt track (one Serverless Search project)."""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMBINED = ROOT / "tracks" / "cisco-serverless-workshop"
DEVELOPER = "peter.simkins@elastic.co"
PORT = 8080
TAB_TITLE = "Elastic Serverless Search"
LOADING_PAGE = "https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/instruqt.html"
LOADING_NOTE_CHALLENGES = frozenset(
    {"01-explore-cisco-kb", "04-map-data-silos", "07-triage-network-signals"}
)

# (source track, source challenge dir, dest challenge dir, deep link path)
CHALLENGES = [
    ("cisco-w1-ai-search", "01-explore-cisco-kb", "01-explore-cisco-kb", "/app/search"),
    ("cisco-w1-ai-search", "02-hybrid-retrieval", "02-hybrid-retrieval", "/app/elasticsearch/query"),
    ("cisco-w1-ai-search", "03-customer-talk-track", "03-customer-talk-track", "/app/search"),
    (
        "cisco-w2-federated-sources",
        "01-map-data-silos",
        "04-map-data-silos",
        "/app/management/data/index_management/indices",
    ),
    (
        "cisco-w2-federated-sources",
        "02-cross-source-esql",
        "05-cross-source-esql",
        "/app/elasticsearch/query",
    ),
    (
        "cisco-w2-federated-sources",
        "03-connector-story",
        "06-connector-story",
        "/app/enterprise_search/content/connectors",
    ),
    (
        "cisco-w3-agent-builder",
        "01-triage-network-signals",
        "07-triage-network-signals",
        "/app/elasticsearch/query",
    ),
    (
        "cisco-w3-agent-builder",
        "02-build-investigation-agent",
        "08-build-investigation-agent",
        "/app/agent_builder",
    ),
    (
        "cisco-w3-agent-builder",
        "03-exec-demo-close",
        "09-exec-demo-close",
        "/app/agent_builder",
    ),
]

MODULE_BY_DEST = {
    "01": "Module 1 — AI Search",
    "02": "Module 1 — AI Search",
    "03": "Module 1 — AI Search",
    "04": "Module 2 — Federated Data Sources",
    "05": "Module 2 — Federated Data Sources",
    "06": "Module 2 — Federated Data Sources",
    "07": "Module 3 — Agent Builder (Search)",
    "08": "Module 3 — Agent Builder (Search)",
    "09": "Module 3 — Agent Builder (Search)",
}


def strip_instruqt_ids(text: str) -> str:
    text = re.sub(r"^id: .+\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"^- id: .+\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"^tabs:\n  title:", "tabs:\n- title:", text, flags=re.MULTILINE)
    return text


def adapt_search_only(dest_ch: str, body: str) -> str:
    if dest_ch == "07-triage-network-signals":
        return """# Triage network signals

**Story:** Pager: *"BGP session down on edge router + Meraki AP offline at Branch 4471."*

**Time:** ~15–20 minutes

All data lives in your **Serverless Search** project (no Observability / Security required).

## ES|QL — BGP signal

```esql
FROM cisco-network-events
| WHERE event_type == "bgp.session_down"
| KEEP @timestamp, host.name, cisco.site, message
| SORT @timestamp DESC
| LIMIT 5
```

## ES|QL — Meraki offline (connector index)

```esql
FROM cisco-meraki-events
| WHERE event_type == "device.offline" AND device_name LIKE "*4471*"
| KEEP @timestamp, device_name, site, detail
| SORT @timestamp DESC
| LIMIT 5
```

## Tasks

1. Run both queries in **ES|QL**.
2. Note **site** and **hostname/device** for the Branch 4471 scenario.
3. Open **Agent Builder** in the nav — list 2 tools/skills you would wire to these indices.

## Verification

Click **Check** when both queries return events.
"""
    if dest_ch == "08-build-investigation-agent":
        body = body.replace(
            "Add capabilities that reference **logs** and **ES|QL** (or Observability AI Assistant if bundled).",
            "Add capabilities that reference **ES|QL** over `cisco-network-events`, `cisco-meraki-events`, and `cisco-network-kb`.",
        )
        body = body.replace(
            "pull correlated logs (BGP + Meraki)",
            "correlate BGP + Meraki indices and KB runbooks",
        )
    if dest_ch == "09-exec-demo-close":
        body = body.replace(
            "3. **W3 Agent Builder** — autonomous triage on **`logs-cisco.network`**",
            "3. **W3 Agent Builder** — agentic triage on Search indices (`cisco-network-events` + federated sources)",
        )
    return body


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def inject_loading_notes(front: str, dest_ch: str) -> str:
    if dest_ch not in LOADING_NOTE_CHALLENGES or "notes:" in front:
        return front
    block = f"""notes:
- type: text
  contents: |
    **While the lab provisions (~3–4 min)** — Serverless Search + Cisco seed data.

    <iframe src="{LOADING_PAGE}" width="100%" height="680" frameborder="0"
      style="border-radius:8px;border:1px solid #2a3140;display:block;min-height:520px;background:#0b0d12">
    </iframe>

"""
    return re.sub(r"(teaser: .+\n)", r"\1" + block, front, count=1)


def main() -> None:
    if COMBINED.exists():
        shutil.rmtree(COMBINED)
    COMBINED.mkdir(parents=True)

    for src_slug, src_ch, dest_ch, kibana_path in CHALLENGES:
        src = ROOT / "tracks" / src_slug / src_ch
        dest = COMBINED / dest_ch
        assignment = strip_instruqt_ids((src / "assignment.md").read_text(encoding="utf-8"))
        parts = assignment.split("---", 2)
        front, body = parts[1], parts[2].lstrip()
        module = MODULE_BY_DEST[dest_ch[:2]]
        body = adapt_search_only(dest_ch, body)
        body = f"> **{module}** · one **Serverless Search** project\n\n{body}"
        front = re.sub(r"^  port: \d+", f"  port: {PORT}", front, flags=re.MULTILINE)
        front = re.sub(r"^  path: .+", f"  path: {kibana_path}", front, flags=re.MULTILINE)
        front = re.sub(r"^- title: Elastic Serverless.*", f"- title: {TAB_TITLE}", front, flags=re.MULTILINE)
        front = inject_loading_notes(front, dest_ch)
        write(dest / "assignment.md", f"---{front}---\n\n{body}")
        for script in ("check-es3-api", "solve-es3-api"):
            shutil.copy2(src / script, dest / script)

    kb = ROOT / "assets" / "shared" / "cisco-knowledge-base.json"
    if kb.is_file():
        write(COMBINED / "workshop-assets" / "data" / "cisco-knowledge-base.json", kb.read_text(encoding="utf-8"))
    for name in ("seed_cisco_kb.py", "seed_federated_sources.py"):
        src = ROOT / "scripts" / name
        if src.is_file():
            write(COMBINED / "track_scripts" / name, src.read_text(encoding="utf-8"))

    playbook = ROOT / "assets" / "shared" / "downloads" / "agent-builder-cisco-playbook.md"
    if playbook.is_file():
        write(
            COMBINED / "workshop-assets" / "downloads" / "agent-builder-cisco-playbook.md",
            playbook.read_text(encoding="utf-8"),
        )

    write(
        COMBINED / "track.yml",
        f"""slug: cisco-serverless-workshop
title: Cisco — AI Search, Federated Sources & Agent Builder
teaser: One Serverless Search project — AI Search, federated indices, and Agent Builder for Cisco.
description: |
  Combined Cisco workshop for Elastic sellers and SEs. Provisions **one** per-learner
  **Elastic Serverless Search** project (vector-optimized) on port **8080**.

  Modules: AI Search → Federated Data Sources → Agent Builder (Search-native ES|QL + agents).
  No Observability or Security projects required.

  **Duration:** ~4.5 hours (3 × ~90 min) — skipping enabled.

  **Prerequisites:** `ESS_CLOUD_API_KEY`; optional `LLM_PROXY_PROD` for Agent Builder LLM.
icon: https://www.elastic.co/favicon.ico
tags:
- cisco
- search
- federated
- agent-builder
- serverless
- cisco-workshop-series
owner: elastic
developers:
- {DEVELOPER}
show_timer: true
skipping_enabled: true
idle_timeout: 600
timelimit: 16200
lab_config:
  extend_ttl: 1800
  sidebar_enabled: true
  feedback_recap_enabled: true
  feedback_tab_enabled: false
  loadingMessages: true
  theme:
    name: modern-dark
  hideStopButton: false
  default_layout: AssignmentRight
  default_layout_sidebar_size: 40
# false = show challenge notes (iframe) while sandbox loads — see docs/instruqt.html
enhanced_loading: false
""",
    )

    write(
        COMBINED / "config.yml",
        """version: "3"
virtualmachines:
- name: es3-api
  image: elastic/es3-api-v2
  shell: /bin/bash
  environment:
    PROJECT_TYPE: elasticsearch
    OPTIMIZED_FOR: vector
    REGIONS: aws-us-east-1
    WORKSHOP_SEED: seed_federated_sources.py
  memory: 4096
  cpus: 1
  allow_external_ingress:
  - http
  - https
  - high-ports
secrets:
- name: ESS_CLOUD_API_KEY
- name: LLM_PROXY_PROD
""",
    )

    subprocess.run(["/bin/bash", str(ROOT / "scripts" / "build-track-setups.sh")], check=True, cwd=ROOT)
    # build-track-setups only covers legacy tracks; wire combined track setup explicitly
    base = ROOT / "scripts" / "es3-setup-base.sh"
    seed = ROOT / "scripts" / "es3-setup-seed.sh"
    cleanup = ROOT / "tracks" / "cisco-w1-ai-search" / "track_scripts" / "cleanup-es3-api"
    out = COMBINED / "track_scripts" / "setup-es3-api"
    with out.open("w", encoding="utf-8") as f:
        f.write("#!/bin/bash\n")
        f.write(base.read_text(encoding="utf-8")[len("#!/bin/bash\n") :])
        f.write("\n")
        f.write(seed.read_text(encoding="utf-8")[len("#!/usr/bin/env bash\n") :])
    out.chmod(0o755)
    shutil.copy2(cleanup, COMBINED / "track_scripts" / "cleanup-es3-api")
    (COMBINED / "track_scripts" / "cleanup-es3-api").chmod(0o755)

    print(f"Built combined track at {COMBINED} ({len(CHALLENGES)} challenges, Search only)")


if __name__ == "__main__":
    main()
