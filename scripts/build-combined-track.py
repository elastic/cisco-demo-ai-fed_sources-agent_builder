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
DECK_CACHE_BUST = "v2"
LOADING_PAGE = f"https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html?{DECK_CACHE_BUST}=1"
SLIDES_PAGE = f"https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html"
LOADING_NOTE_CHALLENGES = frozenset(
    {"01-explore-cisco-kb", "04-map-data-silos", "07-triage-network-signals"}
)

# (source track, source challenge dir, dest challenge dir, deep link path)
CHALLENGES = [
    ("cisco-w1-ai-search", "01-explore-cisco-kb", "01-explore-cisco-kb", "/app/agent_builder"),
    ("cisco-w1-ai-search", "02-hybrid-retrieval", "02-hybrid-retrieval", "/app/workflows"),
    ("cisco-w1-ai-search", "03-customer-talk-track", "03-customer-talk-track", "/app/agent_builder"),
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
        "/app/agent_builder",
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
        "/app/agent_builder",
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
    "01": "Module 1 — Find",
    "02": "Module 1 — Find",
    "03": "Module 1 — Find",
    "04": "Module 2 — Federate",
    "05": "Module 2 — Federate",
    "06": "Module 2 — Federate",
    "07": "Module 3 — Act",
    "08": "Module 3 — Act",
    "09": "Module 3 — Act",
}

TITLE_BY_DEST = {
    "01-explore-cisco-kb": "Challenge 1 — Create the Cisco Agent & find the runbook",
    "02-hybrid-retrieval": "Challenge 2 — Augment with Splunk O11Y A2A (Workflow)",
    "03-customer-talk-track": "Challenge 3 — Agent drafts the peer story",
    "04-map-data-silos": "Challenge 4 — Map silos the Agent will query",
    "05-cross-source-esql": "Challenge 5 — Correlate event + runbook with the Agent",
    "06-connector-story": "Challenge 6 — Plan federation with Agent + Workflows",
    "07-triage-network-signals": "Challenge 7 — Triage with Agent + A2A Workflow",
    "08-build-investigation-agent": "Challenge 8 — Harden Cisco NOC Copilot",
    "09-exec-demo-close": "Challenge 9 — Close the loop with the Cisco Agent",
}


def strip_instruqt_ids(text: str) -> str:
    text = re.sub(r"^id: .+\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"^- id: .+\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"^tabs:\n  title:", "tabs:\n- title:", text, flags=re.MULTILINE)
    return text


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def inject_loading_notes(front: str, dest_ch: str) -> str:
    if dest_ch not in LOADING_NOTE_CHALLENGES or "notes:" in front:
        return front
    block = f"""notes:
- type: text
  contents: |
    **While Elastic Serverless Search provisions (~3–4 min)** — use **← →** in the deck.

    <iframe src="{LOADING_PAGE}" width="100%" height="720" frameborder="0"
      style="border-radius:8px;border:1px solid #2a3140;display:block;min-height:560px;background:#0b0d12">
    </iframe>

    Fullscreen: {SLIDES_PAGE}

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
        body = f"> **{module}** · one **Elastic Serverless Search** project\n\n{body}"
        front = re.sub(r"^  port: \d+", f"  port: {PORT}", front, flags=re.MULTILINE)
        # Only rewrite the first tab path (challenges may include a second dashboard tab).
        front = re.sub(r"^  path: .+", f"  path: {kibana_path}", front, count=1, flags=re.MULTILINE)
        front = re.sub(
            r"^- title: Elastic Serverless.*",
            f"- title: {TAB_TITLE}",
            front,
            count=1,
            flags=re.MULTILINE,
        )
        front = re.sub(
            r"^title: .+$",
            f"title: {TITLE_BY_DEST[dest_ch]}",
            front,
            count=1,
            flags=re.MULTILINE,
        )
        front = inject_loading_notes(front, dest_ch)
        write(dest / "assignment.md", f"---{front}---\n\n{body}")
        check_src = ROOT / "scripts" / "instruqt-check-es3.sh"
        for script in ("check-es3-api", "solve-es3-api"):
            if check_src.is_file():
                shutil.copy2(check_src, dest / script)
            else:
                shutil.copy2(src / script, dest / script)
            (dest / script).chmod(0o755)

    kb = ROOT / "assets" / "shared" / "cisco-knowledge-base.json"
    if kb.is_file():
        write(COMBINED / "workshop-assets" / "data" / "cisco-knowledge-base.json", kb.read_text(encoding="utf-8"))
    dash_src = ROOT / "assets" / "shared" / "dashboards"
    if dash_src.is_dir():
        for df in dash_src.glob("*.json"):
            write(COMBINED / "workshop-assets" / "dashboards" / df.name, df.read_text(encoding="utf-8"))
    wf_src = ROOT / "assets" / "shared" / "workflows"
    if wf_src.is_dir():
        for wf in list(wf_src.glob("*.yaml")) + list(wf_src.glob("*.yml")):
            write(COMBINED / "workshop-assets" / "workflows" / wf.name, wf.read_text(encoding="utf-8"))
    for name in (
        "seed_cisco_kb.py",
        "seed_federated_sources.py",
        "seed_cisco_dashboards.py",
        "seed_cisco_workflows.py",
    ):
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
title: Cisco — Elastic Serverless Search Workshop
teaser: Find → Federate → Act with Agent Builder, Workflows, and Splunk O11Y A2A on one Serverless Search project.
description: |
  Workshop for **Cisco** network, NOC, and platform engineers exploring
  **Elastic Serverless Search**. Each learner gets **one** Search project (Search-only —
  no Observability or Security projects).

  Continuous story — Branch 4471: Meraki offline + BGP flap.
  Build **Cisco NOC Copilot** (Agent Builder), augment with **Workflows + stubbed Splunk O11Y A2A**,
  then federate indices and harden the agent — Find → Federate → Act.

  **Duration with Agent Builder / Workflows / A2A:** ~60–90 minutes hands-on (plus ~5 min provision).
  **Without AI automation (legacy pace):** ~3.5–4.5 hours of manual talk tracks, notes, and RCA writing.
  Skipping enabled.

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
# Idle 5m → stop sandbox → cleanup deletes Serverless project
idle_timeout: 300
# Wall-clock buffer (~2h) for AI-paced workshop + provision/demos
timelimit: 7200
lab_config:
  # Short extend window so abandoned sessions do not linger
  extend_ttl: 600
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
    OPTIMIZED_FOR: general_purpose
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
    cleanup = ROOT / "scripts" / "es3-cleanup.sh"
    out = COMBINED / "track_scripts" / "setup-es3-api"
    seed_frag = subprocess.check_output(
        ["python3", str(ROOT / "scripts" / "generate_es3_seed_fragment.py")],
        cwd=ROOT,
        text=True,
    )
    with out.open("w", encoding="utf-8") as f:
        f.write("#!/bin/bash\n")
        f.write(base.read_text(encoding="utf-8")[len("#!/bin/bash\n") :])
        f.write("\n")
        f.write(seed_frag)
    out.chmod(0o755)
    shutil.copy2(cleanup, COMBINED / "track_scripts" / "cleanup-es3-api")
    (COMBINED / "track_scripts" / "cleanup-es3-api").chmod(0o755)
    # Convenience copies (runtime uses embedded base64 → /tmp)
    shutil.copy2(ROOT / "scripts" / "seed_federated_sources.py", COMBINED / "track_scripts" / "seed_federated_sources.py")
    shutil.copy2(ROOT / "scripts" / "seed_cisco_kb.py", COMBINED / "track_scripts" / "seed_cisco_kb.py")

    print(f"Built combined track at {COMBINED} ({len(CHALLENGES)} challenges, Search only)")


if __name__ == "__main__":
    main()
