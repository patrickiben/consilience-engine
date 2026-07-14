# Release notes

The `consilience-engine` package is public on GitHub with release v1.0.0 and is archived (code + derived data) on OSF at DOI 10.17605/OSF.IO/ZKTRJ.

## Cutting a new release
1. Update the version in `pyproject.toml`, `__init__.py`, and `CITATION.cff`.
2. Commit, then create a GitHub Release with the new tag (e.g. `v1.1.0`).
3. If a software DOI is wanted, enable the repository on Zenodo (Settings -> GitHub) so the release is auto-archived; `.zenodo.json` supplies the metadata. Add the DOI badge to `README.md`.

## Reproducing
See `README.md` (one-command offline reproduction) and `CODE_OCEAN.md` (Docker / Code Ocean capsule). All headline numbers reproduce offline from the shipped caches with no network access.
