"""Command-line interface: fully config-driven, path-independent, with a local cache.

    python -m consilience run examples/cardiac.json [--cache-dir DIR] [--lenses ...] [--out FILE]

The config JSON bundles the whole domain:
    {"name": "...", "expression_field": "RNA single cell type specific nCPM",
     "species": 9606, "components": {"GroupName": ["GENE1", ...], ...}}
A bare {"GroupName": [...]} dict is also accepted (uses --expression-field / defaults).

Lens similarities are cached to <cache-dir>/<name>__<lens>.json (string keys "A|B"), so a second
run is offline and reproducible, and the headline numbers regenerate from a clean checkout.
"""
from __future__ import annotations
import argparse, json, os, sys
from . import lenses, engine

DEFAULT_FIELD = "RNA single nuclei brain specific nCPM"


def _save_sim(path, sim):
    json.dump({f"{a}|{b}": v for (a, b), v in sim.items()}, open(path, "w"))


def _load_sim(path):
    return {tuple(k.split("|")): v for k, v in json.load(open(path)).items()}


def _lens_cached(lens, genes, field, cache_dir, name):
    fp = os.path.join(cache_dir, f"{name}__{lens}.json")
    if os.path.exists(fp):
        print(f"[lens] {lens}: cache hit", file=sys.stderr)
        return _load_sim(fp)
    print(f"[lens] {lens}: fetching ...", file=sys.stderr)
    if lens == "expression":
        ids = lenses.resolve_ids(genes)   # resolve gene ids only on a cache miss, so a fully cached run stays offline
        sim, _ = lenses.expression_sim(genes, ids, hpa_field=field)
    else:
        sim = lenses.LENSES[lens](genes)
    _save_sim(fp, sim)
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
    r.add_argument("--null-draws", type=int, default=1000)
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
    sims = {L: _lens_cached(L, genes, field, cache_dir, name) for L in want}

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
