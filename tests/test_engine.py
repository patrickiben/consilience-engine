"""Offline unit test: separation, classification, and orthogonality behave as designed (no network)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import itertools
from consilience import engine

def _clique(genes, val):
    return {tuple(sorted((a, b))): val for a, b in itertools.combinations(genes, 2)}

def test_lens_map_logic():
    comps = {"Fam": ["A1","A2","A3","A4"], "Cell": ["B1","B2","B3","B4"], "Mod": ["C1","C2","C3","C4"]}
    sims = {
        "structure":  _clique(comps["Fam"], 0.9),   # family coheres in structure
        "expression": _clique(comps["Cell"], 0.9),  # cell type coheres in expression
        "interaction": _clique(comps["Mod"], 0.9),  # module coheres in interaction
    }
    rep = engine.run(comps, sims, null_draws=50)
    assert rep["components"]["Fam"]["seps"]["structure"] > 0.5
    assert rep["components"]["Cell"]["seps"]["expression"] > 0.5
    assert "structure" in rep["components"]["Fam"]["class"]
    assert "expression" in rep["components"]["Cell"]["class"]
    assert "interaction" in rep["components"]["Mod"]["class"]
    assert engine.structure_expression_orthogonality(rep) < 0  # anti-correlated by construction

if __name__ == "__main__":
    test_lens_map_logic(); print("OK: engine logic test passed")
