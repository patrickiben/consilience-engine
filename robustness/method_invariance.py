#!/usr/bin/env python3
"""Method-invariance (false-floor) robustness check for the unsupervised class-recovery claim.

The anti-circularity argument in the manuscript is that unsupervised clustering of the z-scored
four-lens separation profiles recovers the a-priori entity classes (adjusted Rand index 0.25
nervous, 0.55 immune), reported under k-means with k = 3. The false-floor question: does that
recovery survive alternative defensible clustering choices, or is it a k-means-k=3 artifact?

This script reproduces the exact feature matrix and labels used by the primary analysis
(same component ordering, lens order [InterPro, expression, STRING, GO-BP], StandardScaler
z-scoring), then recomputes the adjusted Rand index over a grid of clusterings
(k-means, Ward and average agglomerative, Gaussian mixture) at k in {2, 3, 4}, each with the
label-permutation null. It writes method_invariance.json next to this file and then ASSERTS the
published claim (recovery holds broadly, k-means-k=3 baselines near 0.25 / 0.55), exiting non-zero
if a regression breaks it. Inputs are shipped in robustness/data/ so this runs offline in CI.
"""
import json
import sys
from pathlib import Path

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.metrics import adjusted_rand_score

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
B = 2000  # permutation draws per cell

# a-priori kinds, identical to the primary analysis (ari_null.py / circularity_control.py)
NEURO_KIND = {
 "Astrocyte": "cell", "Oligodendrocyte": "cell", "Microglia": "cell", "OPC": "cell", "BBB-endothelium": "cell",
 "Pericyte-mural": "cell", "ChoroidPlexus-ependyma": "cell", "Cerebellar-neuron": "cell", "SpinalMotor-neuron": "cell",
 "NeuralStem-radialglia": "cell", "Schwann-periphglia": "cell",
 "Glu-mGluR": "family", "Glu-iGluR": "family", "Glu-transport": "family", "Scaffold": "family", "GABA": "family",
 "Glycine": "family", "Histamine": "family", "Purinergic": "family", "TraceAmine-TAAR": "family", "VoltageChannel": "family",
 "Gap-junction": "family", "Opioid-peptide": "family", "Serotonin": "family", "ANS": "family", "Cholinergic-core": "family",
 "Neuropeptide": "family", "Reward-DA": "family",
 "SynapticVesicle": "module", "Neurotrophin": "module", "Plasticity-core": "module", "IEG-transcription": "module",
 "Mitochondrial": "module", "Neurodegeneration": "module", "TransSynaptic-adhesion": "module", "Axon-guidance": "module",
 "Circadian": "module", "Neurosteroid": "module", "Gasotransmitter": "module", "JAKSTAT-cytokine": "module",
 "Neuroimmune": "module", "Morphogen-patterning": "module", "Enteric-NS": "module", "mTOR-epilepsy": "module",
 "Endocannabinoid": "module", "Vision-photo": "module", "Olfaction": "module", "Nociception": "module", "HPA": "module"}


def build_Xy(seps, kind, exprkey):
    comps = [c for c in seps if c in kind]
    lenses = ["InterPro", exprkey, "STRING", "GO-BP"]
    X = np.array([[seps[c][l] for l in lenses] for c in comps])
    y = np.array([kind[c] for c in comps])
    Xz = StandardScaler().fit_transform(X)
    return comps, Xz, y


def cluster_labels(Xz, algo, k):
    if algo == "kmeans":
        return KMeans(n_clusters=k, n_init=10, random_state=0).fit_predict(Xz)
    if algo == "agg_ward":
        return AgglomerativeClustering(n_clusters=k, linkage="ward").fit_predict(Xz)
    if algo == "agg_average":
        return AgglomerativeClustering(n_clusters=k, linkage="average").fit_predict(Xz)
    if algo == "gmm":
        return GaussianMixture(n_components=k, covariance_type="full", n_init=5,
                               random_state=0).fit_predict(Xz)
    raise ValueError(algo)


def ari_with_null(y, labels, rng, B=B):
    obs = adjusted_rand_score(y, labels)
    null = np.array([adjusted_rand_score(rng.permutation(y), labels) for _ in range(B)])
    z = (obs - null.mean()) / null.std() if null.std() > 0 else float("nan")
    p = (1 + int(np.sum(null >= obs))) / (B + 1)
    return float(obs), float(null.mean()), float(null.std()), float(z), float(p)


def run_grid(name, seps, kind, exprkey):
    comps, Xz, y = build_Xy(seps, kind, exprkey)
    rng = np.random.default_rng(1)
    cells = []
    print(f"\n=== {name}: n={len(comps)} components (lens order [InterPro,{exprkey},STRING,GO-BP], z-scored) ===")
    print(f"{'algo':<12}{'k':>2}   {'ARI':>7} {'z':>6} {'p_perm':>8}  sig")
    for algo in ["kmeans", "agg_ward", "agg_average", "gmm"]:
        for k in [2, 3, 4]:
            labels = cluster_labels(Xz, algo, k)
            obs, nm, nsd, z, p = ari_with_null(y, labels, rng)
            sig = (p < 0.05 and obs > 0)
            cells.append({"algo": algo, "k": k, "ARI": round(obs, 3),
                          "null_mean": round(nm, 4), "null_sd": round(nsd, 4),
                          "z": round(z, 1), "p_perm": round(p, 4), "significant": sig})
            star = " *" if (algo == "kmeans" and k == 3) else ""
            print(f"{algo:<12}{k:>2}   {obs:>7.3f} {z:>6.1f} {p:>8.4f}  {'yes' if sig else 'no'}{star}")
    aris = np.array([c["ARI"] for c in cells])
    baseline = next(c for c in cells if c["algo"] == "kmeans" and c["k"] == 3)
    summary = {
        "n": len(comps),
        "baseline_kmeans_k3_ARI": baseline["ARI"], "baseline_kmeans_k3_z": baseline["z"],
        "baseline_kmeans_k3_p": baseline["p_perm"],
        "grid_ARI_min": round(float(aris.min()), 3), "grid_ARI_max": round(float(aris.max()), 3),
        "grid_ARI_median": round(float(np.median(aris)), 3),
        "n_cells": len(cells), "n_significant": int(sum(c["significant"] for c in cells)),
        "fraction_significant": round(float(np.mean([c["significant"] for c in cells])), 3),
    }
    print(f"  -> grid ARI [{summary['grid_ARI_min']}, {summary['grid_ARI_max']}], "
          f"{summary['n_significant']}/{summary['n_cells']} cells significant")
    return {"cells": cells, "summary": summary}


def verdict(res):
    s = res["summary"]
    holds = (s["fraction_significant"] >= 0.6) and (s["grid_ARI_min"] > 0.0)
    return "HOLDS_BROADLY" if holds else "FRAGILE"


def main():
    nm = json.load(open(DATA / "lens_map.json"))
    res_n = run_grid("NEURO (nervous)", {c: nm[c]["seps"] for c in nm}, NEURO_KIND, "snRNA")
    im = json.load(open(DATA / "immune_lens_map.json"))
    res_i = run_grid("IMMUNE", im["seps"], im["kind"], "blood-expr")
    v_n, v_i = verdict(res_n), verdict(res_i)
    out = {
        "description": "Method-invariance (false-floor) grid for the unsupervised class-recovery ARI: "
                       "KMeans / Agglomerative-ward / Agglomerative-average / GaussianMixture at k in {2,3,4}, "
                       "label-permutation null (B=2000). Reproduces the primary Xz/y.",
        "permutation_draws": B, "neuro": res_n, "immune": res_i,
        "verdict_neuro": v_n, "verdict_immune": v_i,
        "type_classification": "Type N (nonequivalent) per Del Giudice and Gangestad (2021): the clustering "
                               "algorithm is a defensible but non-interchangeable analytic choice, so the grid "
                               "is reported as a multiverse rather than a single pick.",
    }
    json.dump(out, open(HERE / "method_invariance.json", "w"), indent=1)

    print("\n================ VERDICT ================")
    print(f"NEURO : {v_n}  (baseline k-means k=3 ARI={res_n['summary']['baseline_kmeans_k3_ARI']}, "
          f"grid min={res_n['summary']['grid_ARI_min']}, sig {res_n['summary']['n_significant']}/{res_n['summary']['n_cells']})")
    print(f"IMMUNE: {v_i}  (baseline k-means k=3 ARI={res_i['summary']['baseline_kmeans_k3_ARI']}, "
          f"grid min={res_i['summary']['grid_ARI_min']}, sig {res_i['summary']['n_significant']}/{res_i['summary']['n_cells']})")

    # assertions: the manuscript claim must hold, or CI goes red
    bn, bi = res_n["summary"]["baseline_kmeans_k3_ARI"], res_i["summary"]["baseline_kmeans_k3_ARI"]
    problems = []
    if v_n != "HOLDS_BROADLY":
        problems.append(f"nervous recovery no longer holds broadly ({v_n})")
    if v_i != "HOLDS_BROADLY":
        problems.append(f"immune recovery no longer holds broadly ({v_i})")
    if not (0.20 <= bn <= 0.30):
        problems.append(f"nervous k-means-k3 baseline ARI {bn} drifted out of [0.20, 0.30]")
    if not (0.50 <= bi <= 0.60):
        problems.append(f"immune k-means-k3 baseline ARI {bi} drifted out of [0.50, 0.60]")
    if problems:
        print("\nFAIL: " + "; ".join(problems))
        sys.exit(1)
    print("\nOK: unsupervised class-recovery holds across the clustering multiverse; baselines within tolerance.")


if __name__ == "__main__":
    main()
