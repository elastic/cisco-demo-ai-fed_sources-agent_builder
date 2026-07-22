# Cisco × Elastic — AI Search, Federated Sources & Agent Builder

Instruqt workshop series for **Cisco** sellers and SEs. Three **~90 minute** labs on **Elastic Cloud Serverless**, following the same patterns as [metric-enablement-series](https://github.com/elastic/metric-enablement-series).

| Resource | Link |
|----------|------|
| Source repo | [github.com/elastic/cisco-demo-ai-fed_sources-agent_builder](https://github.com/elastic/cisco-demo-ai-fed_sources-agent_builder) |
| Instruqt | [play.instruqt.com/manage/elastic/tracks](https://play.instruqt.com/manage/elastic/tracks) |
| Companion UI demo | [cisco-elastic-search-ai](https://github.com/poulsbopete/cisco-elastic-search-ai) |

Filter tracks by tag **`cisco-workshop-series`**.

## Workshop order

| # | Track slug | Title | Serverless project |
|---|------------|-------|-------------------|
| 1 | `cisco-w1-ai-search` | **AI Search** | Search (vector) |
| 2 | `cisco-w2-federated-sources` | **Federated Data Sources** | Search (general purpose) |
| 3 | `cisco-w3-agent-builder` | **Agent Builder for Cisco** | Observability (complete) |

Each track has **three challenges** (~15–20 / ~25–35 / ~15–20 min). Lab UI: **Elastic Serverless** tab only (Kibana via `es3-api` nginx proxy).

## Repository layout

```
catalog/workshops.yaml
docs/FACILITATOR.md
docs/SERIES-ARC.md
assets/shared/                  # Cisco KB JSON + downloads
scripts/                        # Seed + es3 setup builders
tracks/
  cisco-w1-ai-search/
  cisco-w2-federated-sources/
  cisco-w3-agent-builder/
```

## Prerequisites (Instruqt)

- Team secret **`ESS_CLOUD_API_KEY`** with rights to create/delete Serverless projects
- Optional **`LLM_PROXY_PROD`** for Agent Builder LLM features (Workshop 3)
- ~3–4 minutes track startup for project create + data seed

## Workflow

```bash
python3 scripts/scaffold_cisco_workshop.py   # regenerate challenge markdown
./scripts/build-track-setups.sh              # rebuild setup-es3-api from es3-setup-base
cd tracks/cisco-w1-ai-search && instruqt track push --force
```

Push each track after assignment or setup changes (see `.cursor/rules/instruqt-push.mdc`).

## License

Internal Elastic enablement content.
