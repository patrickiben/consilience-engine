#!/usr/bin/env python3
"""Independent symbolic re-derivation of the separation metric (SymPy, exact rationals), checked
against the engine on a fixture. A second implementation in exact arithmetic catches transcription
and algebra bugs that same-code unit tests cannot. Run: python scripts/verify_symbolic.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sympy as sp
from consilience import engine

# fixture: 4 genes, group = {a, b}, rest = {c, d}, exact rational similarities
group = ["a", "b"]
rest = ["c", "d"]
S = {("a", "b"): sp.Rational(7, 10),
     ("a", "c"): sp.Rational(1, 5), ("a", "d"): sp.Rational(1, 10),
     ("b", "c"): sp.Rational(3, 10), ("b", "d"): sp.Rational(1, 10),
     ("c", "d"): sp.Rational(1, 2)}
def k(a, b): return tuple(sorted((a, b)))

# separation = mean(within-group pairs) - mean(group-to-rest pairs)
within = [S[k("a", "b")]]
between = [S[k(g, r)] for g in group for r in rest]
sym = sum(within) / sp.Integer(len(within)) - sum(between) / sp.Integer(len(between))
sym = sp.nsimplify(sym)

eng = engine.separation({engine._key(a, b): float(v) for (a, b), v in S.items()},
                        group, group + rest)
print(f"symbolic (exact) separation = {sym} = {float(sym):.12f}")
print(f"engine  (float) separation  = {eng:.12f}")
assert abs(float(sym) - eng) < 1e-12, "SymPy re-derivation DISAGREES with the engine"
print("OK: independent symbolic re-derivation matches the engine")
