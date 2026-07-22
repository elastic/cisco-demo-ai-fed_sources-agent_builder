#!/usr/bin/env bash
# Concatenate es3-setup-base + seed hook into each track's track_scripts/setup-es3-api
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BASE="$ROOT/scripts/es3-setup-base.sh"
SEED="$ROOT/scripts/es3-setup-seed.sh"
CLEANUP_SRC="$ROOT/scripts/es3-cleanup.sh"

for track in cisco-w1-ai-search cisco-w2-federated-sources cisco-w3-agent-builder; do
  out="$ROOT/tracks/$track/track_scripts/setup-es3-api"
  mkdir -p "$(dirname "$out")"
  {
    echo '#!/bin/bash'
    cat "$BASE" | tail -n +2
    echo ""
    cat "$SEED" | tail -n +2
  } > "$out"
  chmod +x "$out"
  cp "$CLEANUP_SRC" "$ROOT/tracks/$track/track_scripts/cleanup-es3-api"
  chmod +x "$ROOT/tracks/$track/track_scripts/cleanup-es3-api"
  echo "Built $out"
done
