#!/bin/bash
# Combined Cisco workshop: Serverless Search (8080) + Observability (8090).
set -euxo pipefail

resolve_api_key() {
  if [ -z "${PME_CLOUD_INSTRUQT_API_KEY:-}" ]; then
    PME_CLOUD_INSTRUQT_API_KEY="${ESS_CLOUD_API_KEY:-}"
  fi
  if [ -z "${PME_CLOUD_INSTRUQT_API_KEY:-}" ]; then
    PME_CLOUD_INSTRUQT_API_KEY=$(agent variable get PME_CLOUD_INSTRUQT_API_KEY 2>/dev/null || echo "")
  fi
  if [ -z "${PME_CLOUD_INSTRUQT_API_KEY:-}" ]; then
    ESS_KEY=$(agent variable get ESS_CLOUD_API_KEY 2>/dev/null || echo "")
    if [ -n "$ESS_KEY" ]; then PME_CLOUD_INSTRUQT_API_KEY="$ESS_KEY"; fi
  fi
  if [ -z "${PME_CLOUD_INSTRUQT_API_KEY:-}" ]; then
    echo "ERROR: ESS_CLOUD_API_KEY required" >&2
    exit 1
  fi
  export PME_CLOUD_INSTRUQT_API_KEY
}

wait_results() {
  local timeout=120 counter=0
  while [ $counter -lt $timeout ]; do
    if [ -f "/tmp/project_results.json" ]; then return 0; fi
    sleep 2
    counter=$((counter + 2))
  done
  echo "Timeout waiting for /tmp/project_results.json" >&2
  exit 1
}

create_project() {
  local ptype="$1"
  local name_suffix="$2"
  shift 2
  rm -f /tmp/project_results.json
  local args=(--operation create --project-type "$ptype" --regions "${REGIONS:-aws-us-east-1}"
    --project-name "${INSTRUQT_TRACK_SLUG}-${name_suffix}-${INSTRUQT_PARTICIPANT_ID}-$(date '+%s')"
    --api-key "${PME_CLOUD_INSTRUQT_API_KEY}" --wait-for-ready)
  case "$ptype" in
    elasticsearch)
      args+=(--optimized-for "${1:-general_purpose}")
      ;;
    observability)
      args+=(--product-tier "${1:-complete}")
      ;;
  esac
  python3 bin/es3-api.py "${args[@]}"
  wait_results
}

enrich_api_key() {
  local results_file="$1"
  local region="${REGIONS:-aws-us-east-1}"
  local es_url kibana_url password api_key http_code response_body

  es_url=$(jq -r --arg region "$region" '.[$region].endpoints.elasticsearch' "$results_file")
  kibana_url=$(jq -r --arg region "$region" '.[$region].endpoints.kibana' "$results_file")
  password=$(jq -r --arg region "$region" '.[$region].credentials.password' "$results_file")

  output=$(curl -X POST -s -u "admin:${password}" -w "\n%{http_code}" \
    "$es_url/_security/api_key" -H 'Content-Type: application/json' -d '{"name": "cisco-workshop"}')
  http_code=$(echo "$output" | tail -n1)
  response_body=$(echo "$output" | sed '$d')
  api_key=$(echo "$response_body" | jq -r '.encoded // empty')
  if [ -n "$api_key" ]; then
    jq --arg region "$region" --arg apikey "$api_key" \
      '.[$region].credentials.api_key = $apikey' "$results_file" > "${results_file}.tmp"
    mv "${results_file}.tmp" "$results_file"
  fi
  echo "$kibana_url|$password|$es_url|$api_key"
}

write_kibana_server() {
  local listen_port="$1"
  local kibana_url="$2"
  local password="$3"
  local default="${4:-}"
  local base64 kibana_host extra
  base64=$(echo -n "admin:${password}" | base64)
  kibana_host=$(echo "$kibana_url" | sed -e 's#http[s]\?://##g')
  extra=""
  if [ "$default" = "default" ]; then extra=" default_server"; fi
  cat >> /etc/nginx/conf.d/default.conf <<NGINX
server {
  listen ${listen_port}${extra};
  server_name kibana-${listen_port};
  location /nginx_status {
    stub_status on;
    allow 127.0.0.1;
    deny all;
  }
  location / {
    proxy_set_header Host '${kibana_host}';
    proxy_pass '${kibana_url}';
    proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    proxy_set_header Connection "keep-alive";
    proxy_hide_header Content-Security-Policy;
    proxy_hide_header X-Frame-Options;
    proxy_hide_header X-Content-Type-Options;
    proxy_hide_header Strict-Transport-Security;
    proxy_set_header X-Scheme \$scheme;
    proxy_set_header X-Forwarded-Proto https;
    proxy_set_header X-Forwarded-Host \$host;
    proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    proxy_set_header X-Real-IP \$remote_addr;
    proxy_set_header Authorization "Basic ${base64}";
    proxy_set_header User-Agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36";
    proxy_redirect off;
    proxy_http_version 1.1;
    client_max_body_size 20M;
    proxy_read_timeout 600;
    proxy_buffering off;
  }
}
NGINX
}

resolve_api_key
until [ -f /opt/instruqt/bootstrap/host-bootstrap-completed ]; do sleep 1; done

echo "Creating Serverless Search project (general_purpose)..."
create_project elasticsearch search general_purpose
mv /tmp/project_results.json /tmp/project_results_search.json
IFS='|' read -r SEARCH_KIBANA SEARCH_PASSWORD SEARCH_ES SEARCH_API_KEY <<< "$(enrich_api_key /tmp/project_results_search.json)"
SEARCH_DEPLOY_ID=$(jq -r --arg r "${REGIONS:-aws-us-east-1}" '.[$r].id' /tmp/project_results_search.json)

echo "Creating Serverless Observability project (complete)..."
create_project observability o11y complete
mv /tmp/project_results.json /tmp/project_results_o11y.json
IFS='|' read -r O11Y_KIBANA O11Y_PASSWORD O11Y_ES O11Y_API_KEY <<< "$(enrich_api_key /tmp/project_results_o11y.json)"
O11Y_DEPLOY_ID=$(jq -r --arg r "${REGIONS:-aws-us-east-1}" '.[$r].id' /tmp/project_results_o11y.json)

agent variable set ES_SEARCH_KIBANA_URL "$SEARCH_KIBANA"
agent variable set ES_SEARCH_URL "$SEARCH_ES"
agent variable set ES_SEARCH_DEPLOYMENT_ID "$SEARCH_DEPLOY_ID"
agent variable set ES_O11Y_KIBANA_URL "$O11Y_KIBANA"
agent variable set ES_O11Y_URL "$O11Y_ES"
agent variable set ES_O11Y_DEPLOYMENT_ID "$O11Y_DEPLOY_ID"
agent variable set ES_KIBANA_URL "$SEARCH_KIBANA"
agent variable set ES_URL "$SEARCH_ES"
agent variable set ES_DEPLOYMENT_ID "$SEARCH_DEPLOY_ID"

echo "Configure NGINX (Search :8080, Observability :8090)"
rm -f /etc/nginx/conf.d/default.conf
write_kibana_server 8080 "$SEARCH_KIBANA" "$SEARCH_PASSWORD" default
write_kibana_server 8090 "$O11Y_KIBANA" "$O11Y_PASSWORD"
systemctl restart nginx

python3 bin/serve_json.py > /tmp/server-serve-json.log 2>&1 &

TS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TRACK_ROOT="$(dirname "$TS_DIR")"
if [ -f "$TRACK_ROOT/workshop-assets/data/cisco-knowledge-base.json" ]; then
  cp -f "$TRACK_ROOT/workshop-assets/data/cisco-knowledge-base.json" /tmp/cisco-knowledge-base.json
fi

echo "Seeding Search (federated indices)..."
export ES_URL="$SEARCH_ES" ES_PASSWORD="$SEARCH_PASSWORD" ES_USERNAME=admin ES_API_KEY="$SEARCH_API_KEY"
python3 "$TS_DIR/seed_federated_sources.py" > /tmp/seed-search.log 2>&1 || { tail -30 /tmp/seed-search.log; exit 1; }

echo "Seeding Observability (Cisco network logs)..."
export ES_URL="$O11Y_ES" ES_PASSWORD="$O11Y_PASSWORD" ES_USERNAME=admin ES_API_KEY="$O11Y_API_KEY"
python3 "$TS_DIR/seed_cisco_observability.py" > /tmp/seed-o11y.log 2>&1 || { tail -30 /tmp/seed-o11y.log; exit 1; }

echo "Dual-project Cisco workshop ready (Search :8080, Observability :8090)"
echo "done"
