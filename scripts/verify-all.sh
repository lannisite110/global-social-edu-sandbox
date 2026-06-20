#!/usr/bin/env bash
# Phase 0 验收：5 插件 rule-engine 冒烟
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CORE="${CORE:-$ROOT/../web3-edu-platform-core}"

cd "$CORE"
PYTHON="${CORE}/.venv/bin/python"
[ -x "$PYTHON" ] || { python3 -m venv "${CORE}/.venv" && "${CORE}/.venv/bin/pip" install -q -r rule-engine-py/requirements.txt pyyaml; }

echo "==> register plugins"
"$PYTHON" ci/register-plugins.py "$(dirname "$ROOT")"

echo "==> validate manifests"
for m in "$ROOT"/plugins/*/plugin.manifest.yaml; do
  MANIFEST="$m" bash ci/compliance/validate-plugin.sh
done

echo "==> compliance-check"
bash ci/compliance/compliance-check.sh "$ROOT"

echo "==> rule engine (×5)"
PYTHONPATH="$CORE/rule-engine-py:$ROOT" "$PYTHON" - <<'PY'
from plugins.registry import run_plugin, RuleInput

cases = [
    ("plugins.rules.election:evaluate", {}, "election"),
    ("plugins.rules.religion:evaluate", {"amount": 8000}, "religion"),
    ("plugins.rules.welfare:evaluate", {}, "welfare"),
    ("plugins.rules.regulatory:evaluate", {}, "regulatory"),
    ("plugins.rules.logistics:evaluate", {}, "logistics"),
]
for entry, params, name in cases:
    out = run_plugin(entry, RuleInput("demo", params, ["fabric-local"]))
    assert out.compliance_passed, f"{name}: {out.rejection_reason}"
    print(f"OK {name}")
PY

echo "==> global-social-edu-sandbox verify PASSED (5/5)"
