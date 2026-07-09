# consilience-engine

[![reproduce](https://github.com/patrickiben/consilience-engine/actions/workflows/repro.yml/badge.svg)](https://github.com/patrickiben/consilience-engine/actions/workflows/repro.yml)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/patrickiben/consilience-engine/main)

A keyless, **domain-agnostic** multi-lens consilience engine for any gene set. Give it a set of named
components (gene groups); it pulls several public data modalities: **structure** (InterPro domains),
**expression** (Human Protein Atlas cell-type RNA), **interaction** (STRING), and **process** (GO-BP). It builds
a gene–gene similarity graph per modality, and quantifies *which data modality is required to recognise each
component*.

## The principle it operationalises

Across the nervous and immune systems, biological entity-classes have **non-overlapping diagnostic lenses**:

| entity class | revealed by | example |
|---|---|---|
| **cell type** | expression | microglia, T-cell, BBB endothelium |
| **molecular family** | structure | iGluR, TLRs, MHC, connexins |
| **functional / disease module** | interaction | inflammasome, synaptic-vesicle release |

…and **structure and expression are orthogonal** (a component is a *kind of molecule* or a *kind of cell*,
rarely both): r = −0.29 (nervous system), r = −0.27 (immune system). Interaction is a near-universal
detector. No single lens sees everything, which is why integrating them (consilience) is necessary.

## Install

```bash
pip install -e .          # from this directory
```

Requires Python ≥3.11; deps: numpy, scipy, scikit-learn, networkx. All data sources are keyless/public.

## Use (library)

```python
from consilience import lenses, engine
components = {"T-cell": ["CD3D","CD3E","CD8A","LCK","ZAP70"],
             "TLR-family": ["TLR1","TLR2","TLR3","TLR4","TLR7","TLR9"]}
genes = sorted({g for v in components.values() for g in v})
ids  = lenses.resolve_ids(genes)
sims = {"interaction": lenses.interaction_sim(genes),
        "structure":   lenses.structure_sim(genes),
        "process":     lenses.process_sim(genes)}
sims["expression"], _ = lenses.expression_sim(genes, ids, hpa_field="RNA blood cell specific nTPM")
report = engine.run(components, sims)
print("orthogonality r =", engine.structure_expression_orthogonality(report))
```

## Use (CLI): config-driven, path-independent, cached

A domain is one self-contained JSON config (components + the right expression field for the tissue):

```json
{ "name": "cardiac",
  "expression_field": "RNA single cell type specific nCPM",
  "components": { "Cardiomyocyte": ["TNNT2","MYL7", ...], "CardiacIonChannel": ["SCN5A", ...], ... } }
```

```bash
python -m consilience run examples/cardiac.json          # third domain, no code edits
python -m consilience run examples/immune.json
scripts/repro.sh                                          # one command, both example domains
```

Lens results are cached to `.consilience_cache/` (string-keyed JSON), so re-runs are **offline and
reproducible** from a clean checkout. Pick the HPA expression field for your tissue:
`RNA single nuclei brain specific nCPM` (brain) · `RNA blood cell specific nTPM` (immune) ·
`RNA single cell type specific nCPM` (pan-tissue: heart, kidney, etc.).

Offline self-test: `python tests/test_engine.py`.

## Reproduce in a container (Docker / Code Ocean)

Everything reproduces offline from shipped caches and inputs, with no network at run time:

```bash
docker build -t consilience .
docker run --rm consilience        # runs ./run
```

`run` is the one-command reproduction and the Code Ocean capsule entrypoint (see
[CODE_OCEAN.md](CODE_OCEAN.md)): absolute-path guard, unit + property + metamorphic tests, teeth
check, symbolic re-derivation, offline domain reproduction, the numeric gate, and a
**method-invariance multiverse** (`robustness/method_invariance.py`) that re-checks the unsupervised
class-recovery across four clustering algorithms and fails if the recovery stops holding. The same
steps run in the CI matrix on Python 3.11, 3.12, and 3.13.

## What you get back

For every component: per-lens **separation** (within- vs between-component similarity), a **permutation-null
z and p**, the **best lens**, and an entity-class **label** (cell-type / molecular-family / functional-module).
Plus the cross-lens **consilience matrix** and the **structure⊥expression** orthogonality.

## Status

v1.0.0 (engine + four lenses + config-driven CLI). Included: an offline caching layer, unit + property +
metamorphic tests under continuous integration, and a deposited literature-based-discovery benchmark. Built
from a 410-gene/49-component nervous-system map and a 132-gene/18-component immune replication (see the
companion preprint / `LENS_MAP`). Possible future work: more lenses (genetics, pathways, proteomics).

## Caveats (honest)

- STRING aggregates text-mining, so it is a near-universal detector but partly reflects co-citation.
- Component definitions are user-supplied; the engine uses them only as labels, never to build similarities.
- The expression lens is tissue-specific (a brain field is blind to peripheral systems; pick the right one).
- Separation z rises with group size, so compare raw separation across components, not z alone.
