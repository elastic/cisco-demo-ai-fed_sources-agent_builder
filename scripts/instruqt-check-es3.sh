#!/bin/bash
# Shared Instruqt check: verify Serverless Search seed is present, then pass.
# Copied into each challenge as check-es3-api / solve-es3-api (must be executable).
set -euo pipefail

RESULTS="${PROJECT_RESULTS_JSON:-/tmp/project_results.json}"
REGION="${REGIONS:-aws-us-east-1}"

if [[ ! -f "$RESULTS" ]]; then
  echo "Elastic Serverless is still provisioning (no project_results.json yet)."
  echo "Wait until Kibana loads, then click Check again."
  exit 1
fi

ES_URL=$(jq -r --arg r "$REGION" '.[$r].endpoints.elasticsearch // empty' "$RESULTS" 2>/dev/null || true)
API_KEY=$(jq -r --arg r "$REGION" '.[$r].credentials.api_key // empty' "$RESULTS" 2>/dev/null || true)
PASSWORD=$(jq -r --arg r "$REGION" '.[$r].credentials.password // empty' "$RESULTS" 2>/dev/null || true)

if [[ -z "${ES_URL:-}" ]]; then
  echo "Elasticsearch URL missing — setup may still be running. Wait and retry Check."
  exit 1
fi

auth_args=()
if [[ -n "${API_KEY:-}" && "$API_KEY" != "null" ]]; then
  auth_args=(-H "Authorization: ApiKey ${API_KEY}")
elif [[ -n "${PASSWORD:-}" && "$PASSWORD" != "null" ]]; then
  auth_args=(-u "admin:${PASSWORD}")
else
  echo "No API key/password yet — wait for setup, then retry Check."
  exit 1
fi

code=$(curl -s -o /tmp/cisco-check-count.json -w "%{http_code}" \
  "${auth_args[@]}" \
  "${ES_URL%/}/cisco-network-kb/_count" || true)

count=$(jq -r '.count // 0' /tmp/cisco-check-count.json 2>/dev/null || echo 0)

if [[ "$code" != "200" || "${count:-0}" -lt 1 ]]; then
  echo "cisco-network-kb is not ready yet (HTTP ${code}, count=${count})."
  echo "Wait for seed to finish, then click Check again."
  exit 1
fi

echo "OK — Serverless Search seed looks good (${count} KB docs). Continue when your challenge tasks are done."
exit 0
