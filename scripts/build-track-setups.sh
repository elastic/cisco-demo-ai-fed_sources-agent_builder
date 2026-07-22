#!/usr/bin/env bash
# Concatenate es3-setup-base + embedded Cisco seed into each track's setup-es3-api
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BASE="$ROOT/scripts/es3-setup-base.sh"
CLEANUP_SRC="$ROOT/scripts/es3-cleanup.sh"
SEED_FRAG="$(mktemp)"
python3 "$ROOT/scripts/generate_es3_seed_fragment.py" > "$SEED_FRAG"

for track in cisco-w1-ai-search cisco-w2-federated-sources cisco-w3-agent-builder; do
  out="$ROOT/tracks/$track/track_scripts/setup-es3-api"
  mkdir -p "$(dirname "$out")"
  {
    echo '#!/bin/bash'
    tail -n +2 "$BASE"
    echo ""
    cat "$SEED_FRAG"
  } > "$out"
  chmod +x "$out"
  # Keep loose copies for local inspection; runtime uses embedded /tmp files
  cp -f "$ROOT/scripts/seed_federated_sources.py" "$ROOT/tracks/$track/track_scripts/" 2>/dev/null || true
  cp -f "$ROOT/scripts/seed_cisco_kb.py" "$ROOT/tracks/$track/track_scripts/" 2>/dev/null || true
  cp "$CLEANUP_SRC" "$ROOT/tracks/$track/track_scripts/cleanup-es3-api"
  chmod +x "$ROOT/tracks/$track/track_scripts/cleanup-es3-api"
  echo "Built $out ($(wc -c < "$out") bytes)"
done
rm -f "$SEED_FRAG"
