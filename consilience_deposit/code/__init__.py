"""consilience — a keyless, domain-agnostic multi-lens consilience engine for any gene set.

Quickstart
----------
    from consilience import lenses, engine

    components = {"T-cell": ["CD3D","CD3E","CD8A","LCK","ZAP70"],
                  "TLR-family": ["TLR1","TLR2","TLR3","TLR4","TLR7","TLR9"]}
    genes = sorted({g for v in components.values() for g in v})
    ids = lenses.resolve_ids(genes)
    sims = {
        "interaction": lenses.interaction_sim(genes),
        "structure":   lenses.structure_sim(genes),
        "process":     lenses.process_sim(genes),
    }
    sims["expression"], _ = lenses.expression_sim(genes, ids, hpa_field="RNA blood cell specific nTPM")
    report = engine.run(components, sims)
    print(engine.structure_expression_orthogonality(report))
"""
from . import lenses, engine  # noqa: F401

__version__ = "0.1.0"
__all__ = ["lenses", "engine"]
