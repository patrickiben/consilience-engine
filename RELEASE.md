# Release & deposit checklist

The package is a committed local git repo. The steps below require **your** GitHub and Zenodo accounts, so
they're listed as commands to run rather than done for you.

## 1. Push to GitHub

```bash
cd ~/Documents/consilience
gh repo create consilience-engine --public --source=. --remote=origin \
   --description "Domain-agnostic multi-lens consilience engine for gene sets"
git push -u origin main          # branch may be 'master'; rename with: git branch -M main
```
Then edit `pyproject.toml`, `README.md`, `CITATION.cff` to replace `USER` with your GitHub handle.

## 2. Mint a software DOI (Zenodo ↔ GitHub)

1. Log in to https://zenodo.org with GitHub, enable the `consilience-engine` repo under **Settings → GitHub**.
2. On GitHub, **create a Release** (tag `v0.1.0`). Zenodo auto-archives it and mints a DOI.
3. `.zenodo.json` (already in the repo) supplies the metadata. Add the DOI badge to `README.md`.

## 3. Deposit the data resource (separate DOI)

Bundle the atlases + per-lens similarities + figures as a citable dataset:

```bash
mkdir -p ~/Documents/consilience_data && cd ~/Documents/_neuro_atlas_build
cp expanded_atlas4.json lens_map.json immune_lens_map.json consilience_matrix.json \
   matched_density.json multispecies_connectome.json lbd_roc.json \
   domain_exp4_*.json immune_ids.json expand*_ids.json ~/Documents/consilience_data/
cp ~/Documents/Neuro_Atlas/figures/*.png ~/Documents/consilience_data/
```
Upload that folder to Zenodo as an **dataset** with a short data descriptor (the `LENS_MAP.md` + `DATA_DOMAINS.md`
content). You'll get a second DOI for the data.

## 4. Drop the DOIs into the preprint

In `~/Documents/Neuro_Atlas/PREPRINT.md`, replace the `[Zenodo DOI]` and `[GitHub URL]` placeholders in the
**Data and code availability** section, and fill `[affiliation]` + correspondence.

## 5. Post the preprint

Convert `PREPRINT.md` → PDF (pandoc) with the six figures, then submit to bioRxiv.
```bash
pandoc ~/Documents/Neuro_Atlas/PREPRINT.md -o preprint.pdf --pdf-engine=xelatex
```
