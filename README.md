# consilience-engine

A keyless, **domain-agnostic** multi-lens consilience engine for any gene set. Give it a set of named
components (gene groups); it pulls several public data modalities — **structure** (InterPro domains),
**expression** (Human Protein Atlas cell-type RNA), **interaction** (STRING), **process** (GO-BP) — builds a
gene–gene similarity graph per modality, and quantifies *which data modality is required to recognise each
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
detector. No single lens sees everything — which is why integrating them (consilience) is necessary.

## Install

```bash
pip install -e .          # from this directory
```

Requires Python ≥3.9; deps: numpy, scipy, scikit-learn, networkx. All data sources are keyless/public.

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

## Use (CLI)

```bash
python -m consilience run examples/immune_groups.json \
    --expression-field "RNA blood cell specific nTPM" --out immune_report.json
```

Pick the HPA expression field for your tissue:
`RNA single nuclei brain specific nCPM` (brain) · `RNA blood cell specific nTPM` (immune) ·
`RNA single cell type specific nTPM` (pan-tissue).

## What you get back

For every component: per-lens **separation** (within- vs between-component similarity), a **permutation-null
z and p**, the **best lens**, and an entity-class **label** (cell-type / molecular-family / functional-module).
Plus the cross-lens **consilience matrix** and the **structure⊥expression** orthogonality.

## Status

v0.1 scaffold (engine + four lenses + CLI). Built from a 410-gene/49-component nervous-system map and a
132-gene/18-component immune replication (see the companion preprint / `LENS_MAP`). Roadmap: caching layer,
more lenses (genetics, pathways, proteomics), tests, and a Zenodo-deposited benchmark.

## Caveats (honest)

- STRING aggregates text-mining, so it is a near-universal detector but partly reflects co-citation.
- Component definitions are user-supplied; the engine uses them only as labels, never to build similarities.
- The expression lens is tissue-specific (a brain field is blind to peripheral systems; pick the right one).
- Separation z rises with group size — compare raw separation across components, not z alone.
