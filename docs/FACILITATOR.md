# Facilitator guide — Cisco Serverless workshops

**Audience:** Cisco-facing AEs, SEs, partners  
**Duration:** ~90 minutes per workshop (75 min hands-on + 15 min Q&A)

## Environment

All three workshops use a single **`es3-api`** virtual machine (`elastic/es3-api-v2`) that:

1. Creates a **per-learner Serverless project** via Cloud API (`ESS_CLOUD_API_KEY`)
2. Proxies Kibana on **port 8080**
3. Runs a **Python seed** (`WORKSHOP_SEED` in `config.yml`)

| Workshop | Project type | Seed script |
|----------|--------------|-------------|
| W1 AI Search | `elasticsearch` / `vector` | `seed_cisco_kb.py` |
| W2 Federated | `elasticsearch` / `general_purpose` | `seed_federated_sources.py` |
| W3 Agent Builder | `observability` / `complete` | `seed_cisco_observability.py` |

**Startup:** allow **3–4 minutes** before learners open the Serverless tab.

## Timing template

| Segment | Minutes |
|---------|---------|
| Intro + arc | 5 |
| Challenge 1 | 15–20 |
| Challenge 2 | 25–35 |
| Challenge 3 | 15–20 |
| Q&A | 15 |

Track time limit: **90 minutes** (`timelimit: 5400`).

## Instruqt push

After content changes:

```bash
cd tracks/<slug> && instruqt track push --force
```

Tell learners to **start a new session** to pick up instruction updates.

## Troubleshooting

- **Missing API key:** confirm `ESS_CLOUD_API_KEY` in track sandbox secrets.
- **Empty indices:** check `/tmp/workshop-seed.log` on `es3-api` during setup.
- **Agent Builder LLM errors:** verify `LLM_PROXY_PROD` for Workshop 3.
