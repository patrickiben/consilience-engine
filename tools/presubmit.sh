#!/usr/bin/env bash
# One-command pre-submission gate. Usage: PYTHON=python3 bash tools/presubmit.sh [/path/to/manuscript.md]
set -uo pipefail
PY="${PYTHON:-python3}"; ROOT="$(cd "$(dirname "$0")/.." && pwd)"; MS="${1:-}"; fail=0
run(){ echo; echo "### $1"; shift; if "$@"; then :; else fail=1; fi; }
run "absolute-path guard"                    bash "$ROOT/tools/check_paths.sh" "$ROOT"
run "property + metamorphic + engine tests"  bash -c "cd '$ROOT' && PYTHONPATH=. '$PY' -m pytest tests/ -q"
run "teeth check (suite is non-vacuous)"     bash -c "cd '$ROOT' && PYTHONPATH=. '$PY' scripts/teeth_check.py"
run "independent symbolic re-derivation"     bash -c "cd '$ROOT' && PYTHONPATH=. '$PY' scripts/verify_symbolic.py"
run "offline reproduction + numeric gate"    bash -c "cd '$ROOT' && PYTHON='$PY' bash scripts/repro.sh >/dev/null && PYTHONPATH=. '$PY' scripts/check_reports.py"
run "method-invariance multiverse (false-floor)" bash -c "cd '$ROOT' && PYTHONPATH=. '$PY' robustness/method_invariance.py >/dev/null"
if [ -n "$MS" ]; then
  run "citation integrity gate"          "$PY" "$ROOT/tools/check_citations.py" "$MS" --mailto patrickiben@gmail.com
  run "citation metadata + completeness"  "$PY" "$ROOT/tools/check_citation_metadata.py" "$MS"
  run "AI-artifact / hidden-text scrub"  "$PY" "$ROOT/tools/scrub_ai_artifacts.py" "$MS"
fi
echo; if [ "$fail" -eq 0 ]; then echo "RESULT: ALL CLEAR"; else echo "RESULT: ISSUES (above)"; fi
exit $fail
