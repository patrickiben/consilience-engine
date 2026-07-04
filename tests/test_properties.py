"""Property-based tests (Hypothesis) for the separation metric: invariants that must hold for ALL
inputs, not just hand-picked cases. Run: pytest tests/test_properties.py"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hypothesis import given, strategies as st, settings
from consilience import engine

GENES = [f"g{i}" for i in range(6)]
PAIRS = list(itertools.combinations(range(len(GENES)), 2))
sim_strategy = st.fixed_dictionaries(
    {p: st.floats(0, 1, allow_nan=False, allow_infinity=False) for p in PAIRS})


def _build(sim_map):
    return {engine._key(GENES[i], GENES[j]): v for (i, j), v in sim_map.items()}


@given(sim_map=sim_strategy, k=st.integers(2, len(GENES) - 1))
@settings(max_examples=200)
def test_separation_bounded(sim_map, k):
    # similarities in [0,1] => separation (mean within - mean between) in [-1, 1]
    s = engine.separation(_build(sim_map), GENES[:k], GENES)
    assert -1.0 - 1e-9 <= s <= 1.0 + 1e-9


@given(sim_map=sim_strategy, k=st.integers(2, len(GENES) - 1))
@settings(max_examples=200)
def test_group_order_invariant(sim_map, k):
    sim = _build(sim_map)
    base = engine.separation(sim, GENES[:k], GENES)
    assert abs(engine.separation(sim, list(reversed(GENES[:k])), GENES) - base) < 1e-9


@given(sim_map=sim_strategy, c=st.floats(0.01, 10, allow_nan=False, allow_infinity=False),
       k=st.integers(2, len(GENES) - 1))
@settings(max_examples=200)
def test_positive_scaling_preserves_sign(sim_map, c, k):
    sim = _build(sim_map)
    s1 = engine.separation(sim, GENES[:k], GENES)
    s2 = engine.separation({kk: v * c for kk, v in sim.items()}, GENES[:k], GENES)
    assert abs(s2 - c * s1) < 1e-6


@given(sim_map=sim_strategy)
@settings(max_examples=100)
def test_whole_set_is_zero(sim_map):
    # no "rest" to compare against => separation is defined as 0
    assert engine.separation(_build(sim_map), GENES, GENES) == 0.0


if __name__ == "__main__":
    for fn in (test_separation_bounded, test_group_order_invariant,
               test_positive_scaling_preserves_sign, test_whole_set_is_zero):
        fn()
    print("OK: property-based invariants hold")
