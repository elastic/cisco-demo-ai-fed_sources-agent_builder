# Cisco × Elastic — AI Search, Federated Sources & Agent Builder

Instruqt workshop for **Cisco** sellers and SEs on **Elastic Cloud Serverless**, following patterns from [metric-enablement-series](https://github.com/elastic/metric-enablement-series).

| Resource | Link |
|----------|------|
| Source repo | [github.com/elastic/cisco-demo-ai-fed_sources-agent_builder](https://github.com/elastic/cisco-demo-ai-fed_sources-agent_builder) |
| **Combined track (recommended)** | [`cisco-serverless-workshop`](https://play.instruqt.com/manage/elastic/tracks/cisco-serverless-workshop) |
| Instruqt | [play.instruqt.com/manage/elastic/tracks](https://play.instruqt.com/manage/elastic/tracks) |
| Companion UI demo | [cisco-elastic-search-ai](https://github.com/poulsbopete/cisco-elastic-search-ai) |

Filter tracks by tag **`cisco-workshop-series`**.

## One lab, three modules

| Module | Challenges | Kibana |
|--------|------------|--------|
| **1 — AI Search** | 1–3 | Serverless **Search** (tab port **8080**) |
| **2 — Federated Data Sources** | 4–6 | Same Search project |
| **3 — Agent Builder** | 7–9 | Serverless **Observability** (tab port **8090**) |

Track startup provisions **both** Serverless projects and seeds Cisco KB/federated indices plus network logs (~**5–6 min** first load). Time limit **4.5 h** (`16200` s); **skipping** enabled so facilitators can run one module at a time.

### Legacy split tracks

These remain in the repo for partial rollout; prefer the combined track for new events:

- `cisco-w1-ai-search`
- `cisco-w2-federated-sources`
- `cisco-w3-agent-builder`

## Repository layout

```
catalog/workshops.yaml
docs/FACILITATOR.md
assets/shared/
scripts/build-combined-track.py   # regenerate tracks/cisco-serverless-workshop
tracks/cisco-serverless-workshop/ # primary
tracks/cisco-w1-ai-search/        # legacy optional
...
```

## Workflow

```bash
python3 scripts/build-combined-track.py
cd tracks/cisco-serverless-workshop && instruqt track push --force
```

After assignment or setup changes, push the combined track (see `.cursor/rules/instruqt-push.mdc`).

## License

Internal Elastic enablement content.
