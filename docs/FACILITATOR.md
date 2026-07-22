# Facilitator guide — Cisco Serverless workshops

**Audience:** Cisco-facing AEs, SEs, partners  
**Duration:** ~90 minutes per workshop (75 min hands-on + 15 min Q&A)

## Environment

**Recommended:** single track **`cisco-serverless-workshop`** — dual Serverless projects on one `es3-api` VM:

| Port | Project | Modules |
|------|---------|---------|
| **8080** | Serverless Search (vector) | AI Search + Federated |
| **8090** | Serverless Observability (complete) | Agent Builder |

Legacy single-project tracks (`cisco-w1-*`, `cisco-w2-*`, `cisco-w3-*`) use one project each.

All variants use **`ESS_CLOUD_API_KEY`**. Optional **`LLM_PROXY_PROD`** for Agent Builder LLM (Module 3).

**Startup:** allow **5–6 minutes** on combined track (two projects + seeds).

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
