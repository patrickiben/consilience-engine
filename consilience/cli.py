"""Command-line interface:  python -m consilience run components.json [options]

components.json is {"ComponentName": ["GENE1","GENE2", ...], ...}
"""
from __future__ import annotations
import argparse, json, sys
from . import lenses, engine


def main(argv=None):
    ap = argparse.ArgumentParser(prog="consilience")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="run the engine on a components JSON")
    r.add_argument("components", help="path to {name: [genes]} JSON")
    r.add_argument("--lenses", default="interaction,structure,process,expression",
                   help="comma list from: interaction,structure,process,expression")
    r.add_argument("--expression-field", default="RNA single nuclei brain specific nCPM",
                   help="HPA field for the expression lens (e.g. 'RNA blood cell specific nTPM')")
    r.add_argument("--null-draws", type=int, default=1000)
    r.add_argument("--out", default="consilience_report.json")
    a = ap.parse_args(argv)

    components = json.load(open(a.components))
    genes = sorted({g for v in components.values() for g in v})
    want = [x.strip() for x in a.lenses.split(",") if x.strip()]
    sims = {}
    ids = lenses.resolve_ids(genes) if "expression" in want else {}
    for L in want:
        print(f"[lens] {L} ...", file=sys.stderr)
        if L == "expression":
            sims[L], _ = lenses.expression_sim(genes, ids, hpa_field=a.expression_field)
        elif L in lenses.LENSES:
            sims[L] = lenses.LENSES[L](genes)
        else:
            print(f"  unknown lens '{L}', skipping", file=sys.stderr)

    report = engine.run(components, sims, null_draws=a.null_draws)
    report["structure_expression_orthogonality"] = engine.structure_expression_orthogonality(report)
    json.dump(report, open(a.out, "w"), indent=1)

    print(f"\n{report['n_components']} components, {report['n_genes']} genes")
    print(f"structure-expression orthogonality r = {report['structure_expression_orthogonality']:+.3f}")
    print(f"{'component':22}{'class':30}{'best':12}")
    for c, d in report["components"].items():
        print(f"{c:22}{d['class']:30}{str(d['best']):12}")
    print(f"\nwrote {a.out}")


if __name__ == "__main__":
    main()
