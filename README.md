# Cisco × Elastic — AI Search, Federated Sources & Agent Builder

Instruqt workshop for **Cisco** sellers and SEs on **Elastic Cloud Serverless Search** only (no Observability or Security positioning).

| Resource | Link |
|----------|------|
| Source repo | [github.com/elastic/cisco-demo-ai-fed_sources-agent_builder](https://github.com/elastic/cisco-demo-ai-fed_sources-agent_builder) |
| **Combined track (recommended)** | [`cisco-serverless-workshop`](https://play.instruqt.com/manage/elastic/tracks/cisco-serverless-workshop) |
| Companion UI demo | [cisco-elastic-search-ai](https://github.com/poulsbopete/cisco-elastic-search-ai) |

Tag: **`cisco-workshop-series`**

## One Serverless Search project

Each learner gets **one** vector-optimized **Serverless Search** project (Kibana tab port **8080**). All three modules use the same project:

| Module | Focus |
|--------|--------|
| **1 — AI Search** | `cisco-network-kb`, hybrid / ES|QL retrieval |
| **2 — Federated Data Sources** | KB + internal runbooks + Meraki connector events |
| **3 — Agent Builder** | ES|QL triage on `cisco-network-events` + Agent Builder on Search |

Startup ~**3–4 min** (single project + federated seed). Track time limit **4.5 h**; skipping enabled.

**While-you-wait:** [GitHub Pages](https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/instruqt.html) — iframe in module-start challenges + VM `/loading` during Kibana proxy.

## Workflow

```bash
python3 scripts/build-combined-track.py
cd tracks/cisco-serverless-workshop && instruqt track push --force
```
