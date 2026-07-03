#!/usr/bin/env bash
# Reproduce example domains from a clean checkout. Override interpreter with PYTHON=...
set -euo pipefail
PY="${PYTHON:-python}"
cd "$(dirname "$0")/.."
$PY -m consilience run examples/immune.json  --out immune_report.json
$PY -m consilience run examples/cardiac.json --out cardiac_report.json
echo "done -> immune_report.json, cardiac_report.json (cache in examples/.consilience_cache/)"
