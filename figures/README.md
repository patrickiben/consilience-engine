# Figure-generation scripts

Scripts that produce the manuscript figures from the deposited results.
- `fig1_schematic.py` -> F1 (self-contained schematic).
- `fig_make.py` -> F2-F5 (reads the result JSONs; set `RESULTS_DIR` to the deposit `results/`).
- `lbd_roc.py` -> F6 (reads the cached LBD data `lbd_pubmed_mglur.json`).

Usage: `RESULTS_DIR=<results dir> FIG_OUT=<output dir> python <script>.py`. F7/F8 are produced by the analysis scripts in `results/` (robustness_orthogonality.py, null_calibration.py).
