# Reproducible environment for the consilience-engine (Code Ocean capsule / plain Docker).
#   docker build -t consilience .
#   docker run --rm consilience          # runs the full offline reproduction + robustness
# The default command needs no network: the engine reproduces from shipped caches
# (examples/.consilience_cache/) and the method-invariance check from shipped inputs
# (robustness/data/).
FROM python:3.11-slim

WORKDIR /consilience

# Pinned scientific stack first, so this layer caches independently of source changes.
COPY requirements.txt pyproject.toml README.md ./
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# Full package + test/reproducibility extras.
COPY . .
RUN pip install -e ".[test]"

CMD ["bash", "run"]
