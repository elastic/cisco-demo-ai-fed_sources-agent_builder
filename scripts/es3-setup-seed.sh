#!/usr/bin/env bash
# Run workshop seed after es3-api provisioning (WORKSHOP_SEED env from config.yml).
set -euo pipefail

WORKSHOP_SEED="${WORKSHOP_SEED:-}"
if [ -z "$WORKSHOP_SEED" ]; then
  echo "No WORKSHOP_SEED — skipping data seed"
  echo "done"
  exit 0
fi

TS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TRACK_ROOT="$(dirname "$TS_DIR")"
SEED="$TS_DIR/$WORKSHOP_SEED"

if [ -f "$TRACK_ROOT/workshop-assets/data/cisco-knowledge-base.json" ]; then
  cp -f "$TRACK_ROOT/workshop-assets/data/cisco-knowledge-base.json" /tmp/cisco-knowledge-base.json
fi

export ES_URL="${ES_URL:-$(jq -r --arg region "${REGIONS:-aws-us-east-1}" '.[$region].endpoints.elasticsearch // empty' /tmp/project_results.json)}"
export ES_PASSWORD="${ES_PASSWORD:-$(jq -r --arg region "${REGIONS:-aws-us-east-1}" '.[$region].credentials.password // empty' /tmp/project_results.json)}"
export ES_USERNAME="${ES_USERNAME:-admin}"
export ES_API_KEY="${ES_API_KEY:-$(jq -r --arg region "${REGIONS:-aws-us-east-1}" '.[$region].credentials.api_key // empty' /tmp/project_results.json)}"

if [ ! -f "$SEED" ]; then
  echo "ERROR: seed script not found: $SEED"
  exit 1
fi

echo "Running workshop seed: $WORKSHOP_SEED"
if python3 "$SEED" > /tmp/workshop-seed.log 2>&1; then
  tail -5 /tmp/workshop-seed.log || true
else
  echo "ERROR: seed failed — /tmp/workshop-seed.log"
  tail -30 /tmp/workshop-seed.log || true
  exit 1
fi

echo "done"
