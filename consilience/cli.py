"""Command-line interface: fully config-driven, path-independent, with a local cache.

    python -m consilience run examples/cardiac.json [--cache-dir DIR] [--lenses ...] [--out FILE]

The config JSON bundles the whole domain:
    {"name": "...", "expression_field": "RNA single cell type specific nCPM",
     "species": 9606, "components": {"GroupName": ["GENE1", ...], ...}}
A bare {"GroupName": [...]} dict is also accepted (uses --expression-field / defaults).

Lens caches include input fingerprints. Deposited <name>__<lens>.json snapshots remain immutable;
custom/refresh runs use <name>__<lens>__<fingerprint>.json with source-contract metadata.
"""
from __future__ import annotations
import argparse, hashlib, json, os, sys
from datetime import datetime, timezone
from . import lenses, engine

DEFAULT_FIELD = "RNA single nuclei brain specific nCPM"
CACHE_SCHEMA = 1
# API/implementation contracts, not claims about the release date of live source data.
PROVIDERS = {
    "interaction": "STRING network API; human 9606; combined score",
    "structure": "UniProt REST reviewed human gene_exact; InterPro Jaccard",
    "process": "mygene v3 human symbol; GO-BP Jaccard",
    "expression": "Human Protein Atlas gene JSON; log1p cosine; mygene v3 IDs",
}


def _cache_inputs(lens, genes, field, species=9606):
    if species != 9606:
        raise ValueError("The implemented providers support human genes only (species=9606).")
    if lens not in PROVIDERS:
        raise ValueError(f"Unknown lens: {lens!r}")
    return {"schema_version": CACHE_SCHEMA, "lens": lens, "genes": sorted(set(genes)),
            "expression_field": field if lens == "expression" else None,
            "species": species, "provider_contract": PROVIDERS[lens],
            "implementation_version": 1}


def _fingerprint(inputs):
    return hashlib.sha256(json.dumps(inputs, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _save_sim(path, sim, inputs, provenance=None):
    payload = {"inputs": inputs, "fingerprint": _fingerprint(inputs),
               "similarities": {f"{a}|{b}": v for (a, b), v in sim.items()},
               "provenance": provenance or {"kind": "live-fetch", "provider_data_version": None,
                                             "fetched_at": datetime.now(timezone.utc).isoformat()}}
    with open(path, "w") as stream:
        json.dump(payload, stream, separators=(",", ":"))


def _load_sim(path, inputs):
    with open(path) as stream:
        payload = json.load(stream)
    # Old unlabelled caches are unsafe: we cannot infer their genes or tissue.
    if payload.get("inputs") != inputs or payload.get("fingerprint") != _fingerprint(inputs):
        return None
    return {tuple(k.split("|")): v for k, v in payload["similarities"].items()}


def _lens_cached(lens, genes, field, cache_dir, name, refresh=False, species=9606):
    inputs = _cache_inputs(lens, genes, field, species)
    # Shipped example snapshots are immutable. Overrides/new fetches get a fingerprinted
    # filename and can never overwrite those historical reproduction inputs.
    name = os.path.basename(name)
    snapshot = os.path.join(cache_dir, f"{name}__{lens}.json")
    fp = os.path.join(cache_dir, f"{name}__{lens}__{_fingerprint(inputs)}.json")
    if not refresh:
        for candidate in (snapshot, fp):
            if os.path.exists(candidate):
                sim = _load_sim(candidate, inputs)
                if sim is not None:
                    print(f"[lens] {lens}: cache hit", file=sys.stderr)
                    return sim
    print(f"[lens] {lens}: fetching ...", file=sys.stderr)
    if lens == "expression":
        ids = lenses.resolve_ids(genes)   # resolve gene ids only on a cache miss, so a fully cached run stays offline
        sim, _ = lenses.expression_sim(genes, ids, hpa_field=field)
    else:
        sim = lenses.LENSES[lens](genes)
    _save_sim(fp, sim, inputs)
    return sim


def main(argv=None):
    ap = argparse.ArgumentParser(prog="consilience")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="run the engine on a domain config (or components JSON)")
    r.add_argument("config", help="path to a domain config or {name:[genes]} JSON")
    r.add_argument("--lenses", default="interaction,structure,process,expression")
    r.add_argument("--expression-field", default=None,
                   help="HPA field for the expression lens (overrides config)")
    r.add_argument("--cache-dir", default=".consilience_cache")
    r.add_argument("--refresh", action="store_true", help="fetch current data into a new cache; preserve shipped snapshots")
    r.add_argument("--null-draws", type=int, default=2000)
    r.add_argument("--out", default=None)
    a = ap.parse_args(argv)

    # A non-absolute --cache-dir is resolved relative to the config file's directory,
    # so reproduction is path-independent (running from any cwd still finds the cache).
    cache_dir = a.cache_dir
    if not os.path.isabs(cache_dir):
        cache_dir = os.path.join(os.path.dirname(os.path.abspath(a.config)), cache_dir)

    cfg = json.load(open(a.config))
    if "components" in cfg:                       # full config object
        components = cfg["components"]
        name = cfg.get("name", os.path.splitext(os.path.basename(a.config))[0])
        field = a.expression_field or cfg.get("expression_field", DEFAULT_FIELD)
    else:                                         # bare components dict
        components = cfg
        name = os.path.splitext(os.path.basename(a.config))[0]
        field = a.expression_field or DEFAULT_FIELD

    os.makedirs(cache_dir, exist_ok=True)
    genes = sorted({g for v in components.values() for g in v})
    want = [x.strip() for x in a.lenses.split(",") if x.strip()]
    sims = {L: _lens_cached(L, genes, field, cache_dir, name, refresh=a.refresh,
                           species=cfg.get("species", 9606) if "components" in cfg else 9606) for L in want}

    report = engine.run(components, sims, null_draws=a.null_draws)
    report["structure_expression_orthogonality"] = engine.structure_expression_orthogonality(report)
    out = a.out or f"{name}_report.json"
    json.dump(report, open(out, "w"), indent=1)

    print(f"\n=== {name}: {report['n_components']} components, {report['n_genes']} genes ===")
    r_se = report["structure_expression_orthogonality"]
    print(f"structure-vs-expression r = {r_se:+.3f}  (weak/negative => the two specialized lenses rarely co-fire)")
    print(f"{'component':24}{'class':30}{'best lens':12}")
    for c, d in report["components"].items():
        print(f"{c:24}{d['class']:30}{str(d['best']):12}")
    print(f"\nwrote {out}  (cache: {cache_dir}/)")


if __name__ == "__main__":
    main()
