#!/bin/bash
set -euo pipefail

resolve_api_key() {
  PME_CLOUD_INSTRUQT_API_KEY="${PME_CLOUD_INSTRUQT_API_KEY:-}"
  if [ -z "$PME_CLOUD_INSTRUQT_API_KEY" ]; then PME_CLOUD_INSTRUQT_API_KEY="${ESS_CLOUD_API_KEY:-}"; fi
  if [ -z "$PME_CLOUD_INSTRUQT_API_KEY" ]; then
    PME_CLOUD_INSTRUQT_API_KEY="$(agent variable get ESS_CLOUD_API_KEY 2>/dev/null || echo "")"
  fi
  if [ -z "$PME_CLOUD_INSTRUQT_API_KEY" ]; then
    echo "ERROR: ESS_CLOUD_API_KEY not set" >&2
    exit 1
  fi
  export PME_CLOUD_INSTRUQT_API_KEY
}

delete_one() {
  local ptype="$1"
  local dep_id="$2"
  [ -z "$dep_id" ] || [ "$dep_id" = "null" ] && return 0
  echo "Deleting $ptype project $dep_id"
  python3 bin/es3-api.py \
    --operation delete \
    --project-type "$ptype" \
    --regions "${REGIONS:-aws-us-east-1}" \
    --project-id "$dep_id" \
    --api-key "${PME_CLOUD_INSTRUQT_API_KEY}"
}

resolve_api_key
REG="${REGIONS:-aws-us-east-1}"

SEARCH_ID="$(agent variable get ES_SEARCH_DEPLOYMENT_ID 2>/dev/null || echo "")"
O11Y_ID="$(agent variable get ES_O11Y_DEPLOYMENT_ID 2>/dev/null || echo "")"
if [ -z "$SEARCH_ID" ] && [ -f /tmp/project_results_search.json ]; then
  SEARCH_ID="$(jq -r --arg r "$REG" '.[$r].id // empty' /tmp/project_results_search.json)"
fi
if [ -z "$O11Y_ID" ] && [ -f /tmp/project_results_o11y.json ]; then
  O11Y_ID="$(jq -r --arg r "$REG" '.[$r].id // empty' /tmp/project_results_o11y.json)"
fi

delete_one elasticsearch "$SEARCH_ID"
delete_one observability "$O11Y_ID"
echo "Done"
