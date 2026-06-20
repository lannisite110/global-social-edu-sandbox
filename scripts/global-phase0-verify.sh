#!/usr/bin/env bash
# Phase 0 gateway 冒烟（需 backend）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CORE="${CORE:-$ROOT/../web3-edu-platform-core}"

cd "$CORE" && make register-plugins PLUGINS_DIR="$ROOT/.."

for pid in edu.global.sandbox.election edu.global.sandbox.religion edu.global.sandbox.welfare edu.global.sandbox.regulatory edu.global.sandbox.logistics; do
  code=$(curl -sf -o /tmp/g.json -w '%{http_code}' \
    -X POST "http://127.0.0.1:8080/api/v1/labs/${pid}/simulate" \
    -H 'Content-Type: application/json' \
    -d '{"user_prompt":"global phase0","params":{},"allowed_chain_ids":["fabric-local"]}' || echo "000")
  if [ "$code" = "202" ] || [ "$code" = "200" ]; then
    echo "  OK $pid HTTP $code"
  else
    echo "  FAIL $pid HTTP $code"
    exit 1
  fi
done
echo "==> global phase0 gateway smoke PASSED"
