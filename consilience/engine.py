"""Core consilience engine: separation, permutation null, cross-lens consilience matrix, and the
entity-class classifier (cell type / molecular family / functional module).

Given a dict of components {name: [genes]} and one similarity dict per lens, the engine computes, for
each component in each lens, how much more similar its genes are to each other than to the rest of the
set ("separation"), with a permutation null, and assigns each component a diagnostic lens.

The empirical finding this operationalises: structure and expression separations are anti-correlated
(a component is a molecular family OR a cell type, rarely both); interaction is a near-universal
detector. See LENS_MAP for the cross-domain (nervous + immune) validation.
"""
from __future__ import annotations
import itertools, random
import numpy as np
from scipy.stats import spearmanr


def _key(a, b):
    return tuple(sorted((a, b)))


def separation(sim: dict, group_genes, all_genes) -> float:
    """mean within-group similarity minus mean group-to-rest similarity (missing pairs = 0)."""
    gg = list(group_genes)
    s = set(gg)
    rest = [g for g in all_genes if g not in s]
    within = [sim.get(_key(a, b), 0.0) for a, b in itertools.combinations(gg, 2)]
    between = [sim.get(_key(a, b), 0.0) for a in gg for b in rest]
    return (float(np.mean(within)) - float(np.mean(between))) if within and between else 0.0


def permutation_null(sim, group_genes, all_genes, draws=2000, seed=1):
    """z-score and empirical p of observed separation vs random same-size gene sets."""
    obs = separation(sim, group_genes, all_genes)
    rng = random.Random(seed)
    n = len(list(group_genes))
    null = [separation(sim, rng.sample(all_genes, n), all_genes) for _ in range(draws)]
    mu, sd = float(np.mean(null)), float(np.std(null))
    z = (obs - mu) / sd if sd > 0 else float("nan")
    p = (1 + sum(1 for x in null if x >= obs)) / (draws + 1)
    return {"observed": obs, "null_mean": mu, "z": z, "p": p}


def consilience_matrix(sims: dict) -> dict:
    """Spearman correlation of gene-pair similarities between every pair of lenses (shared pairs)."""
    names = list(sims)
    out = {}
    for a, b in itertools.combinations(names, 2):
        shared = set(sims[a]) & set(sims[b])
        if len(shared) >= 10:
            xa = [sims[a][k] for k in shared]
            xb = [sims[b][k] for k in shared]
            r = spearmanr(xa, xb).correlation
            out[f"{a}|{b}"] = float(r) if r == r else None
    return out


def classify(seps: dict, thr: float = 0.18) -> str:
    """Assign a component its diagnostic entity-class from its per-lens separations.

    seps keys expected (any subset): 'structure','expression','interaction','process'.
    """
    struct = seps.get("structure", 0.0)
    expr = seps.get("expression", 0.0)
    inter = seps.get("interaction", 0.0)
    if expr >= thr and expr >= struct:
        return "cell-type (expression)"
    if struct >= thr and struct > expr:
        return "molecular-family (structure)"
    if inter >= thr:
        return "functional-module (interaction)"
    return "weak/mixed"


def run(components: dict, sims: dict, null_draws: int = 1000, seed: int = 1) -> dict:
    """Score every component across every lens.

    components : {name: [gene symbols]}
    sims       : {lens_name: similarity_dict}
    returns    : {component: {'seps': {...}, 'best': lens, 'class': str, 'null': {lens: {...}}}}
    """
    all_genes = sorted({g for gs in components.values() for g in gs})
    report = {}
    for name, genes in components.items():
        seps = {lens: separation(sim, genes, all_genes) for lens, sim in sims.items()}
        best = max(seps, key=seps.get) if seps else None
        nulls = {lens: permutation_null(sims[lens], genes, all_genes, draws=null_draws, seed=seed)
                 for lens in sims}
        report[name] = {"seps": seps, "best": best, "class": classify(seps), "null": nulls}
    return {"components": report,
            "consilience_matrix": consilience_matrix(sims),
            "n_genes": len(all_genes), "n_components": len(components)}


def structure_expression_orthogonality(report: dict):
    """Pearson r between structure- and expression-separations across components.
    Near 0 / negative => the two diagnostic lenses are independent (the central finding)."""
    comps = report["components"]
    s = [comps[c]["seps"].get("structure", 0.0) for c in comps]
    e = [comps[c]["seps"].get("expression", 0.0) for c in comps]
    if len(s) >= 3 and np.std(s) > 0 and np.std(e) > 0:
        return float(np.corrcoef(s, e)[0, 1])
    return float("nan")
