#!/usr/bin/env python3
"""Teeth check: demonstrate the test suite is NOT vacuous. Inject known bugs into the separation
metric and confirm the *committed* property/metamorphic tests catch each one. If a bug slips through,
the suite has no teeth. Run: python scripts/teeth_check.py"""
import sys, os, itertools
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tests"))
from consilience import engine
import test_properties, test_metamorphic

_orig = engine.separation

def bug_omit_between(sim, g, ag):
    """forgets to subtract the group-to-rest term (separation = within only)"""
    w = [sim.get(engine._key(a, b), 0.0) for a, b in itertools.combinations(g, 2)]
    return float(np.mean(w)) if w else 0.0

def bug_sign_flip(sim, g, ag):
    """returns the negated separation"""
    return -_orig(sim, g, ag)

def bug_missing_default(sim, g, ag):
    """uses 0.5 for missing pairs instead of 0 (breaks the whole-set = 0 invariant)"""
    s = set(g); rest = [x for x in ag if x not in s]
    w = [sim.get(engine._key(a, b), 0.5) for a, b in itertools.combinations(g, 2)]
    b = [sim.get(engine._key(a, b), 0.5) for a in g for b in rest]
    return (float(np.mean(w)) - float(np.mean(b))) if w and b else 0.0

BUGS = {"omit between-subtraction": bug_omit_between,
        "sign flip": bug_sign_flip,
        "missing-pairs default 0.5": bug_missing_default}

# the committed tests that should catch a broken metric
TESTS = [test_properties.test_whole_set_is_zero,
         test_properties.test_separation_bounded,
         test_properties.test_positive_scaling_preserves_sign,
         test_metamorphic.test_adding_noise_gene_does_not_increase_separation,
         test_metamorphic.test_missing_pair_equals_explicit_zero]

def run_suite():
    for t in TESTS:
        t()   # raises on any falsifying example

# sanity: the correct engine passes
run_suite()
print("baseline: correct engine passes all invariants")

missed = []
for name, buggy in BUGS.items():
    engine.separation = buggy
    try:
        run_suite()
        caught = False
    except BaseException:
        caught = True
    finally:
        engine.separation = _orig
    print(f"  {'CAUGHT ' if caught else 'MISSED '} injected bug: {name}")
    if not caught:
        missed.append(name)

if missed:
    print(f"FAIL: {len(missed)} injected bug(s) slipped through -> suite is vacuous: {missed}")
    sys.exit(1)
print(f"OK: all {len(BUGS)} injected bugs caught -> the invariant suite has teeth")
