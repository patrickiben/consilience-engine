"""Metamorphic tests: for a scorer with no ground-truth oracle, assert input->output RELATIONS that
must hold (adding noise weakens a score; relabeling is invariant; extra lenses don't move the headline).
Run: pytest tests/test_metamorphic.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from consilience import engine


def _sim(pairs):
    return {engine._key(a, b): v for (a, b), v in pairs.items()}


def test_adding_noise_gene_does_not_increase_separation():
    genes = ["a", "b", "c", "d", "e"]
    sim = _sim({("a", "b"): 0.9, ("a", "c"): 0.8, ("b", "c"): 0.85,
                ("a", "d"): 0.0, ("b", "d"): 0.0, ("c", "d"): 0.0,
                ("a", "e"): 0.0, ("b", "e"): 0.0, ("c", "e"): 0.0, ("d", "e"): 0.0})
    base = engine.separation(sim, ["a", "b", "c"], genes)
    with_noise = engine.separation(sim, ["a", "b", "c", "d"], genes)
    assert with_noise <= base + 1e-9   # a zero-similarity gene dilutes, never strengthens


def test_gene_relabeling_invariant():
    genes = ["a", "b", "c", "d"]
    sim = _sim({("a", "b"): 0.7, ("a", "c"): 0.1, ("a", "d"): 0.1,
                ("b", "c"): 0.1, ("b", "d"): 0.1, ("c", "d"): 0.6})
    base = engine.separation(sim, ["a", "b"], genes)
    mp = {"a": "w", "b": "x", "c": "y", "d": "z"}
    sim2 = {engine._key(mp[k[0]], mp[k[1]]): v for k, v in sim.items()}
    assert abs(engine.separation(sim2, ["w", "x"], ["w", "x", "y", "z"]) - base) < 1e-12


def test_extra_lens_does_not_move_orthogonality():
    # >=3 components so the across-component correlation is defined
    comps = {"A": ["a", "b"], "B": ["c", "d"], "C": ["e", "f"]}
    struct = _sim({("a", "b"): 0.8})   # only A separates on structure
    expr = _sim({("c", "d"): 0.8})     # only B separates on expression
    r1 = engine.structure_expression_orthogonality(
        engine.run(comps, {"structure": struct, "expression": expr}, null_draws=50))
    r2 = engine.structure_expression_orthogonality(
        engine.run(comps, {"structure": struct, "expression": expr, "interaction": struct}, null_draws=50))
    assert r1 == r1 and abs(r1 - r2) < 1e-9   # defined, and unmoved by an extra lens


def test_missing_pair_equals_explicit_zero():
    # the missing-pairs = 0 convention: an absent pair must behave exactly like an explicit 0
    genes = ["a", "b", "c"]
    full = _sim({("a", "b"): 0.8, ("a", "c"): 0.0, ("b", "c"): 0.0})
    sparse = _sim({("a", "b"): 0.8})  # a-c and b-c ABSENT
    assert abs(engine.separation(full, ["a", "b"], genes)
               - engine.separation(sparse, ["a", "b"], genes)) < 1e-12


if __name__ == "__main__":
    test_adding_noise_gene_does_not_increase_separation()
    test_gene_relabeling_invariant()
    test_extra_lens_does_not_move_orthogonality()
    test_missing_pair_equals_explicit_zero()
    print("OK: metamorphic relations hold")
