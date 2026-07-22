# Facilitator guide — Cisco Serverless workshops

**Audience:** Cisco-facing AEs, SEs, partners  
**Duration:** ~90 minutes per module (~4.5 h full track)

## Environment (Search only)

**Do not position Observability or Security** in this Cisco motion. All labs use **one Serverless Search** project per learner:

- VM: **`es3-api`** (`elastic/es3-api-v2`)
- Kibana proxy: port **8080**
- Seed: **`seed_federated_sources.py`** → `cisco-network-kb`, `cisco-internal-runbooks`, `cisco-meraki-events`, `cisco-network-events`

Secrets: **`ESS_CLOUD_API_KEY`** (required), **`LLM_PROXY_PROD`** (optional, Module 3 Agent Builder).

**Startup:** ~3–4 minutes before opening the Search tab.

## Lifecycle (Serverless project spin-down)

| Trigger | Behavior |
|---------|----------|
| Setup | Creates **one** Search Serverless project; stores `ES_DEPLOYMENT_ID` + `ES_PROJECT_TYPE` |
| Cleanup (`cleanup-es3-api`) | Deletes that project via Cloud API |
| Idle | **5 minutes** (`idle_timeout: 300`) → sandbox stops → cleanup runs |
| Extend | At most **10 minutes** (`extend_ttl: 600`) |
| Track limit | **~4.5 h** wall clock (`timelimit: 16200`); cleanup on expiry / Stop |

Tell learners: leave the tab idle >5 minutes and the lab (and Cloud project) tear down. Hit **Stop** when finished so cleanup runs immediately.

## Combined vs legacy tracks

| Track | Use when |
|-------|----------|
| `cisco-serverless-workshop` | Default — full story in one lab |
| `cisco-w1-ai-search` / `w2` / `w3` | Module-only enablement |

## Push after edits

```bash
cd tracks/cisco-serverless-workshop && instruqt track push --force
```

Learners need a **new session** after instruction updates.
