#!/usr/bin/env python3
"""Build single combined Cisco Instruqt track from the three module tracks."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMBINED = ROOT / "tracks" / "cisco-serverless-workshop"
DEVELOPER = "peter.simkins@elastic.co"

# (source track, source challenge dir, dest challenge dir, kibana port, deep link path)
CHALLENGES = [
    ("cisco-w1-ai-search", "01-explore-cisco-kb", "01-explore-cisco-kb", 8080, "/app/search"),
    ("cisco-w1-ai-search", "02-hybrid-retrieval", "02-hybrid-retrieval", 8080, "/app/elasticsearch/query"),
    ("cisco-w1-ai-search", "03-customer-talk-track", "03-customer-talk-track", 8080, "/app/search"),
    (
        "cisco-w2-federated-sources",
        "01-map-data-silos",
        "04-map-data-silos",
        8080,
        "/app/management/data/index_management/indices",
    ),
    (
        "cisco-w2-federated-sources",
        "02-cross-source-esql",
        "05-cross-source-esql",
        8080,
        "/app/elasticsearch/query",
    ),
    (
        "cisco-w2-federated-sources",
        "03-connector-story",
        "06-connector-story",
        8080,
        "/app/enterprise_search/content/connectors",
    ),
    (
        "cisco-w3-agent-builder",
        "01-triage-network-signals",
        "07-triage-network-signals",
        8090,
        "/app/discover",
    ),
    (
        "cisco-w3-agent-builder",
        "02-build-investigation-agent",
        "08-build-investigation-agent",
        8090,
        "/app/agent_builder",
    ),
    (
        "cisco-w3-agent-builder",
        "03-exec-demo-close",
        "09-exec-demo-close",
        8090,
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
    "07": "Module 3 — Agent Builder",
    "08": "Module 3 — Agent Builder",
    "09": "Module 3 — Agent Builder",
}


def strip_instruqt_ids(text: str) -> str:
    text = re.sub(r"^id: .+\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"^- id: .+\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"^tabs:\n  title:", "tabs:\n- title:", text, flags=re.MULTILINE)
    return text


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    if COMBINED.exists():
        shutil.rmtree(COMBINED)
    COMBINED.mkdir(parents=True)

    for src_slug, src_ch, dest_ch, port, kibana_path in CHALLENGES:
        src = ROOT / "tracks" / src_slug / src_ch
        dest = COMBINED / dest_ch
        assignment = strip_instruqt_ids((src / "assignment.md").read_text(encoding="utf-8"))
        parts = assignment.split("---", 2)
        front, body = parts[1], parts[2].lstrip()
        module = MODULE_BY_DEST[dest_ch[:2]]
        body = f"> **{module}** (Serverless tab port **{port}**)\n\n{body}"
        if port == 8090:
            body = body.replace(
                "1. Wait for **Elastic Serverless** to finish loading (~3–4 min on first start).",
                "1. **Module 3** uses Observability on port **8090** — same lab VM, different Kibana project (~5–6 min total startup at track begin).",
                1,
            )
        front = re.sub(r"^  port: \d+", f"  port: {port}", front, flags=re.MULTILINE)
        front = re.sub(r"^  path: .+", f"  path: {kibana_path}", front, flags=re.MULTILINE)
        tab_title = "Elastic Serverless (Observability)" if port == 8090 else "Elastic Serverless (Search)"
        front = re.sub(r"^- title: Elastic Serverless.*", f"- title: {tab_title}", front, flags=re.MULTILINE)
        write(dest / "assignment.md", f"---{front}---\n\n{body}")
        for script in ("check-es3-api", "solve-es3-api"):
            shutil.copy2(src / script, dest / script)

    kb = ROOT / "assets" / "shared" / "cisco-knowledge-base.json"
    if kb.is_file():
        write(COMBINED / "workshop-assets" / "data" / "cisco-knowledge-base.json", kb.read_text(encoding="utf-8"))
    for name in ("seed_cisco_kb.py", "seed_federated_sources.py", "seed_cisco_observability.py"):
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
teaser: One lab — Serverless Search + Observability for Cisco NOC demos (3 modules, 9 challenges).
description: |
  Combined Cisco workshop for Elastic sellers and SEs. Provisions **two** Serverless projects per learner:
  **Search** (8080) for AI Search and Federated Sources modules, **Observability** (8090) for Agent Builder.

  **Duration:** ~4.5 hours total (3 × ~90 min modules) — skipping enabled for partial runs.

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
    REGIONS: aws-us-east-1
    DUAL_PROJECT: "true"
  memory: 8192
  cpus: 2
  allow_external_ingress:
  - http
  - https
  - high-ports
secrets:
- name: ESS_CLOUD_API_KEY
- name: LLM_PROXY_PROD
""",
    )

    shutil.copy2(ROOT / "scripts" / "es3-setup-dual-cisco.sh", COMBINED / "track_scripts" / "setup-es3-api")
    shutil.copy2(ROOT / "scripts" / "es3-cleanup-dual-cisco.sh", COMBINED / "track_scripts" / "cleanup-es3-api")
    (COMBINED / "track_scripts" / "setup-es3-api").chmod(0o755)
    (COMBINED / "track_scripts" / "cleanup-es3-api").chmod(0o755)

    print(f"Built combined track at {COMBINED} ({len(CHALLENGES)} challenges)")


if __name__ == "__main__":
    main()
