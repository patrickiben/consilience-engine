"""Keyless data lenses for the consilience engine.

Each lens turns a gene set into a gene-gene similarity dict {("GENEA","GENEB"): value}, keyed by
sorted symbol pairs. All sources are public and require no API key.

Lenses:
  - structure   : InterPro protein-domain architecture (Jaccard)        [UniProt]
  - process     : GO biological-process terms (Jaccard)                 [mygene]
  - interaction : STRING combined association score (0-1)               [STRING]
  - expression  : cell-type expression cosine over a chosen HPA field   [Human Protein Atlas]
"""
from __future__ import annotations
import json, time, itertools, urllib.request, urllib.parse

UA = {"User-Agent": "consilience/0.1"}


def _get(url, headers=None, timeout=45, retries=3):
    for a in range(retries):
        try:
            return json.loads(urllib.request.urlopen(
                urllib.request.Request(url, headers=headers or UA), timeout=timeout).read())
        except Exception:
            time.sleep(0.6 * (a + 1))
    return None


def _key(a, b):
    return tuple(sorted((a, b)))


def _jaccard(setd: dict) -> dict:
    sim = {}
    for a, b in itertools.combinations(sorted(setd), 2):
        A, B = setd[a], setd[b]
        u = len(A | B)
        if u:
            sim[_key(a, b)] = len(A & B) / u
    return sim


def resolve_ids(symbols: list[str]) -> dict:
    """symbol -> {'entrez','ensembl'} via mygene (batched, alias-aware)."""
    ids = {}
    for i in range(0, len(symbols), 100):
        chunk = symbols[i:i + 100]
        req = urllib.request.Request(
            "https://mygene.info/v3/query",
            data=urllib.parse.urlencode({
                "q": ",".join(chunk), "scopes": "symbol,alias",
                "fields": "entrezgene,ensembl.gene", "species": "human"}).encode(),
            headers={**UA, "Content-Type": "application/x-www-form-urlencoded"})
        for h in json.loads(urllib.request.urlopen(req, timeout=60).read()):
            q = h.get("query")
            if h.get("notfound") or q in ids or not h.get("entrezgene"):
                continue
            ens = h.get("ensembl", {})
            ens = ens.get("gene") if isinstance(ens, dict) else (
                ens[0]["gene"] if isinstance(ens, list) and ens else None)
            ids[q] = {"entrez": str(h["entrezgene"]), "ensembl": ens}
        time.sleep(0.2)
    return ids


def interaction_sim(symbols: list[str]) -> dict:
    """STRING combined association score (already 0-1) for all pairs in the set; one call."""
    url = ("https://string-db.org/api/tsv/network?identifiers="
           + "%0d".join(symbols) + "&species=9606")
    txt = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=200).read().decode()
    S = set(symbols)
    sim = {}
    for line in txt.strip().split("\n")[1:]:
        c = line.split("\t")
        if len(c) >= 6 and c[2] in S and c[3] in S and c[2] != c[3]:
            sim[_key(c[2], c[3])] = float(c[5])
    return sim


def process_sim(symbols: list[str]) -> dict:
    """GO biological-process Jaccard via mygene (batched)."""
    go = {}
    for i in range(0, len(symbols), 80):
        req = urllib.request.Request(
            "https://mygene.info/v3/query",
            data=urllib.parse.urlencode({
                "q": ",".join(symbols[i:i + 80]), "scopes": "symbol",
                "fields": "go.BP.id", "species": "human"}).encode(),
            headers={**UA, "Content-Type": "application/x-www-form-urlencoded"})
        for h in json.loads(urllib.request.urlopen(req, timeout=60).read()):
            q = h.get("query")
            bp = h.get("go", {}).get("BP") if isinstance(h.get("go"), dict) else None
            if q and bp:
                terms = {x["id"] for x in (bp if isinstance(bp, list) else [bp])
                         if isinstance(x, dict) and x.get("id")}
                if terms:
                    go[q] = go.get(q, set()) | terms
        time.sleep(0.3)
    return _jaccard(go)


def structure_sim(symbols: list[str]) -> dict:
    """InterPro domain Jaccard via UniProt (per gene; the structural 'family' lens)."""
    ipr = {}
    for g in symbols:
        r = _get("https://rest.uniprot.org/uniprotkb/search?query=gene_exact:%s+AND+"
                 "organism_id:9606+AND+reviewed:true&fields=xref_interpro&format=json&size=1" % g)
        res = (r or {}).get("results", [])
        if res:
            xr = {x["id"] for x in res[0].get("uniProtKBCrossReferences", [])
                  if x.get("database") == "InterPro"}
            if xr:
                ipr[g] = xr
        time.sleep(0.05)
    return _jaccard(ipr)


def expression_sim(symbols, ids=None, hpa_field="RNA single nuclei brain specific nCPM"):
    """Cell-type expression cosine over a chosen Human Protein Atlas field.

    Pick the field that matches your tissue, e.g.:
      - 'RNA single nuclei brain specific nCPM'  (brain cell types)
      - 'RNA blood cell specific nTPM'           (immune cell types)
      - 'RNA single cell type specific nCPM'     (pan-tissue)
    """
    import numpy as np
    ids = ids or resolve_ids(symbols)
    raw = {}
    for g in symbols:
        ens = ids.get(g, {}).get("ensembl")
        if not ens:
            continue
        j = _get("https://www.proteinatlas.org/%s.json" % ens)
        d = (j or {}).get(hpa_field) or {}
        if d:
            raw[g] = {ct: float(v) for ct, v in d.items()}
        time.sleep(0.12)
    cts = sorted({c for d in raw.values() for c in d})
    vec = {g: np.array([np.log1p(d.get(c, 0.0)) for c in cts]) for g, d in raw.items()}
    sim = {}
    for a, b in itertools.combinations(sorted(vec), 2):
        x, y = vec[a], vec[b]
        if x.sum() > 0 and y.sum() > 0:
            dn = np.linalg.norm(x) * np.linalg.norm(y)
            if dn:
                sim[_key(a, b)] = float(x @ y / dn)
    return sim, raw  # raw returned so callers can report coverage


LENSES = {
    "interaction": interaction_sim,
    "process": process_sim,
    "structure": structure_sim,
    # 'expression' is handled specially (needs ids + field); see engine.run
}
