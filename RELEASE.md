# Release notes

The `consilience-engine` package is public on GitHub with release v1.0.0. The source code is archived with a citable DOI on Zenodo (10.5281/zenodo.21399794), and the code plus derived data are archived on OSF (DOI 10.17605/OSF.IO/ZKTRJ).

## Cutting a new release
1. Update the version in `pyproject.toml`, `__init__.py`, and `CITATION.cff`.
2. Commit, then create a GitHub Release with the new tag (e.g. `v1.1.0`).
3. The repository is enabled on Zenodo (Settings -> GitHub), so each GitHub release is auto-archived and issued a DOI (`.zenodo.json` supplies the metadata); the current release DOI is 10.5281/zenodo.21399794.

## Reproducing
See `README.md` (one-command offline reproduction) and `CODE_OCEAN.md` (Docker / Code Ocean capsule).
The example-domain reports and class-recovery multiverse reproduce offline from shipped caches.
Full manuscript figure inputs and the literature-discovery benchmark are in the OSF companion deposit;
see `figures/README.md`. Live API results can differ from the deposited snapshots.
