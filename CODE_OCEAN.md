# Reproducing on Code Ocean (or plain Docker)

GigaScience encourages a Code Ocean compute capsule alongside the source. This repository is
capsule-ready: it ships a `Dockerfile` (the environment) and a single `run` entrypoint that
reproduces every headline offline, with no network access, from the shipped caches
(`examples/.consilience_cache/`) and the shipped robustness inputs (`robustness/data/`).

## What `run` does (identical to the CI matrix)
1. absolute-path guard (portability)
2. engine unit test
3. property-based and metamorphic tests
4. teeth check (the test suite is non-vacuous)
5. independent symbolic re-derivation of the separation metric
6. offline reproduction of the example domains from shipped caches
7. numeric gate: reproduced numbers match the committed values within tolerance
8. method-invariance multiverse (the false-floor robustness check for the unsupervised
   class-recovery claim), which asserts the recovery holds across four clustering algorithms

## Plain Docker
    docker build -t consilience .
    docker run --rm consilience

## Import into Code Ocean
1. In Code Ocean, choose Create Capsule, then Import from a Git repository.
2. Point it at `https://github.com/patrickiben/consilience-engine`.
3. Code Ocean detects the `Dockerfile` as the environment. Set the run command to `bash run`
   (or accept the `Dockerfile` CMD, which is already `bash run`).
4. Run the capsule. All steps above execute with no network.
5. On publish, Code Ocean mints a capsule DOI; add it to the manuscript's
   "Availability of supporting source code and requirements" section next to the GitHub and OSF
   identifiers. Publishing and the DOI are account-side steps for the author.

Nothing here requires network access at run time, so the capsule is fully self-contained.
