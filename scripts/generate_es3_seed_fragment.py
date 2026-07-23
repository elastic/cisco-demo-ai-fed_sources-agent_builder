#!/usr/bin/env python3
"""Emit bash fragment that materializes Cisco seed assets under /tmp (Instruqt-safe)."""
from __future__ import annotations

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
ASSETS = ROOT / "assets" / "shared"
DASHBOARDS = ASSETS / "dashboards"
WORKFLOWS = ASSETS / "workflows"


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def embed_dir(files: list[Path], dest_dir: str, marker_prefix: str) -> str:
    blocks = []
    for f in files:
        token = f"{marker_prefix}_{f.stem.upper().replace('-', '_')}"
        blocks.append(
            f"base64 -d <<'{token}' > {dest_dir}/{f.name}\n{b64(f)}\n{token}"
        )
    return "\n".join(blocks)


def main() -> None:
    kb = ASSETS / "cisco-knowledge-base.json"
    seed_kb = SCRIPTS / "seed_cisco_kb.py"
    seed_fed = SCRIPTS / "seed_federated_sources.py"
    seed_dash = SCRIPTS / "seed_cisco_dashboards.py"
    seed_wf = SCRIPTS / "seed_cisco_workflows.py"
    seed_agent = SCRIPTS / "seed_cisco_agent.py"
    dash_files = sorted(DASHBOARDS.glob("*.json"))
    wf_files = sorted(WORKFLOWS.glob("*.yaml")) + sorted(WORKFLOWS.glob("*.yml"))
    for p in (kb, seed_kb, seed_fed, seed_dash, seed_wf, seed_agent):
        if not p.is_file():
            raise SystemExit(f"missing {p}")
    if not dash_files:
        raise SystemExit(f"no dashboard JSON under {DASHBOARDS}")
    if not wf_files:
        raise SystemExit(f"no workflow YAML under {WORKFLOWS}")

    print(
        f"""# Workshop seed — files embedded (Instruqt runs setup from /tmp without siblings)
set -euo pipefail

WORKSHOP_SEED="${{WORKSHOP_SEED:-}}"
if [ -z "$WORKSHOP_SEED" ]; then
  echo "No WORKSHOP_SEED — skipping data seed"
  echo "done"
  exit 0
fi

echo "Materializing Cisco seed assets under /tmp..."
mkdir -p /tmp/dashboards /tmp/workflows
base64 -d <<'CISCO_KB_JSON' > /tmp/cisco-knowledge-base.json
{b64(kb)}
CISCO_KB_JSON
base64 -d <<'CISCO_SEED_KB_PY' > /tmp/seed_cisco_kb.py
{b64(seed_kb)}
CISCO_SEED_KB_PY
base64 -d <<'CISCO_SEED_FED_PY' > /tmp/seed_federated_sources.py
{b64(seed_fed)}
CISCO_SEED_FED_PY
base64 -d <<'CISCO_SEED_DASH_PY' > /tmp/seed_cisco_dashboards.py
{b64(seed_dash)}
CISCO_SEED_DASH_PY
base64 -d <<'CISCO_SEED_WF_PY' > /tmp/seed_cisco_workflows.py
{b64(seed_wf)}
CISCO_SEED_WF_PY
base64 -d <<'CISCO_SEED_AGENT_PY' > /tmp/seed_cisco_agent.py
{b64(seed_agent)}
CISCO_SEED_AGENT_PY
{embed_dir(dash_files, "/tmp/dashboards", "CISCO_DASH")}
{embed_dir(wf_files, "/tmp/workflows", "CISCO_WF")}

export ES_URL="${{ES_URL:-$(jq -r --arg region "${{REGIONS:-aws-us-east-1}}" '.[$region].endpoints.elasticsearch // empty' /tmp/project_results.json)}}"
export KIBANA_URL="${{KIBANA_URL:-$(jq -r --arg region "${{REGIONS:-aws-us-east-1}}" '.[$region].endpoints.kibana // empty' /tmp/project_results.json)}}"
export ES_PASSWORD="${{ES_PASSWORD:-$(jq -r --arg region "${{REGIONS:-aws-us-east-1}}" '.[$region].credentials.password // empty' /tmp/project_results.json)}}"
export ES_USERNAME="${{ES_USERNAME:-admin}}"
export ES_API_KEY="${{ES_API_KEY:-$(jq -r --arg region "${{REGIONS:-aws-us-east-1}}" '.[$region].credentials.api_key // empty' /tmp/project_results.json)}}"
export ELASTICSEARCH_API_KEY="${{ELASTICSEARCH_API_KEY:-$ES_API_KEY}}"
export KIBANA_API_KEY="${{KIBANA_API_KEY:-$ES_API_KEY}}"

SEED="/tmp/$WORKSHOP_SEED"
if [ ! -f "$SEED" ]; then
  echo "ERROR: seed script not found after embed: $SEED"
  ls -la /tmp/seed_*.py /tmp/cisco-knowledge-base.json /tmp/dashboards /tmp/workflows 2>/dev/null || true
  exit 1
fi

echo "Running workshop seed: $WORKSHOP_SEED"
# Soft-fail: a seed warning must not leave the Instruqt host unhealthy —
# otherwise Challenge Check returns "Something went wrong while checking".
if python3 "$SEED" > /tmp/workshop-seed.log 2>&1; then
  tail -30 /tmp/workshop-seed.log || true
else
  echo "WARN: seed reported errors — lab may still be usable; see /tmp/workshop-seed.log"
  tail -80 /tmp/workshop-seed.log || true
fi

echo "done"
"""
    )


if __name__ == "__main__":
    main()
