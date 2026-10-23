# Manuscript figure inputs

Install the optional plotting dependency with `pip install -e ".[figures]"` (Python >=3.12).
The [OSF code/data deposit](https://doi.org/10.17605/OSF.IO/ZKTRJ) contains the companion derived
data; the [Zenodo archive](https://doi.org/10.5281/zenodo.21399794) is the citable software release.
Download and extract the deposit yourself; set `RESULTS_DIR` to its `results/` directory.

| Script | Output | Required inputs under `RESULTS_DIR` |
|---|---|---|
| `fig1_schematic.py` | F1 | None; self-contained schematic |
| `fig_make.py` | F2–F5 | `lens_map.json`, `immune_lens_map.json`, `consilience_matrix.json`, `matched_density.json`, `multispecies_connectome.json` |
| `lbd_roc.py` | F6 | `lbd_pubmed_mglur.json` (cached PubMed records) |

For example, from the repository root:

```bash
RESULTS_DIR=/path/to/extracted-deposit/results FIG_OUT=/path/to/output python figures/fig_make.py
RESULTS_DIR=/path/to/extracted-deposit/results FIG_OUT=/path/to/output python figures/lbd_roc.py
```

The two lens-map JSON files also ship under `robustness/data/`, but the remaining figure inputs
do not ship in this code repository. F7/F8 are produced by the deposit's analysis scripts
`robustness_orthogonality.py` and `null_calibration.py`. The top-level `run` command verifies the
engine, cached example reports and class-recovery multiverse; it does not rebuild this full figure set.
