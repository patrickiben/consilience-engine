#!/usr/bin/env python3
"""CI gate: assert the reproduced reports match the expected deterministic headline.
Run AFTER scripts/repro.sh, which regenerates immune_report.json and cardiac_report.json."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECT = {"cardiac_report.json": -0.280, "immune_report.json": -0.265}  # deterministic structure-expression r
TOL = 0.01
fail = False
for fname, exp in EXPECT.items():
    p = os.path.join(ROOT, fname)
    if not os.path.exists(p):
        print(f"MISSING {fname}"); fail = True; continue
    r = json.load(open(p)).get("structure_expression_orthogonality")
    ok = r is not None and abs(r - exp) <= TOL
    print(f"{fname}: r={r} expected~{exp} (tol {TOL}) -> {'OK' if ok else 'FAIL'}")
    fail = fail or not ok
print("ALL OK" if not fail else "MISMATCH")
sys.exit(1 if fail else 0)
