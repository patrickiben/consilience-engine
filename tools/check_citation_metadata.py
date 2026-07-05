#!/usr/bin/env python3
"""Deterministic citation METADATA gate (complements check_citations.py). Title-containment can pass a
reference with a wrong year/volume/first-page (the 'vetter2000' failure mode). This resolves each DOI
against CrossRef/DataCite and DIFFS the cited year / volume / first-page against the record. It also
checks completeness: every reference is cited in-text and every in-text [n] has a reference.
Usage: python3 tools/check_citation_metadata.py path/to/manuscript.md   (stdlib only)"""
import json, re, sys, time, urllib.parse, urllib.request
CROSSREF="https://api.crossref.org/works"; DATACITE="https://api.datacite.org/dois"
MAILTO="patrickiben@gmail.com"

def _get(url):
    req=urllib.request.Request(url, headers={"User-Agent":f"cite-meta/1.0 (mailto:{MAILTO})","Accept":"application/json"})
    for _ in range(3):
        try:
            with urllib.request.urlopen(req, timeout=25) as r: return r.read().decode("utf-8","replace")
        except urllib.error.HTTPError as e:
            if e.code==404: return None
            time.sleep(1.2)
        except Exception: time.sleep(1.2)
    return None

def crossref_meta(doi):
    b=_get(f"{CROSSREF}/{urllib.parse.quote(doi)}?mailto={MAILTO}")
    if not b: return None
    try:
        m=json.loads(b)["message"]
        y=None
        for k in ("published-print","published-online","issued"):
            dp=(m.get(k) or {}).get("date-parts")
            if dp and dp[0] and dp[0][0]: y=str(dp[0][0]); break
        page=(m.get("page") or "").split("-")[0]
        return {"year":y,"volume":str(m.get("volume") or ""),"first_page":page,"src":"CrossRef"}
    except Exception: return None

def datacite_meta(doi):
    b=_get(f"{DATACITE}/{urllib.parse.quote(doi)}")
    if not b: return None
    try:
        a=json.loads(b)["data"]["attributes"]
        return {"year":str(a.get("publicationYear") or ""),"volume":"","first_page":"","src":"DataCite"}
    except Exception: return None

if len(sys.argv)<2:
    raise SystemExit("usage: check_citation_metadata.py <manuscript.md>")
md=open(sys.argv[1],encoding="utf-8").read()
refblock=md.split("## References",1)[1] if "## References" in md else md
refs=re.findall(r"^(\d+)\.\s+(.*)$", refblock, re.M)

print(f"METADATA DIFF over {len(refs)} references\n"+"="*78)
issues=0
for num,txt in refs:
    dm=re.search(r"doi:(10\.\S+)", txt)
    if not dm:
        print(f"[  no-doi ] {num:>2}  (no DOI to diff)"); continue
    doi=dm.group(1).rstrip(".,;")
    # cited metadata: 'Journal YEAR;VOL(issue):FIRSTPAGE-...'
    cy=re.search(r"\b(19|20)\d{2}\b(?=;)", txt) or re.search(r";\s*(?:.*?)?\b((?:19|20)\d{2})\b", txt)
    cited_year=re.search(r"\b((?:19|20)\d{2})\b;", txt)
    cited_year=cited_year.group(1) if cited_year else ""
    vp=re.search(r";\s*(\d+)\s*\([^)]*\)\s*:\s*([A-Za-z]?\d+)", txt) or re.search(r";\s*(\d+)\s*:\s*([A-Za-z]?\d+)", txt)
    cited_vol=vp.group(1) if vp else ""; cited_fp=vp.group(2) if vp else ""
    rec=crossref_meta(doi) or datacite_meta(doi)
    if not rec:
        print(f"[ >FLAG< ] {num:>2}  DOI resolves nowhere: {doi}"); issues+=1; time.sleep(0.4); continue
    probs=[]
    if cited_year and rec["year"] and cited_year!=rec["year"]: probs.append(f"year {cited_year}!={rec['year']}")
    if cited_vol and rec["volume"] and cited_vol!=rec["volume"]: probs.append(f"vol {cited_vol}!={rec['volume']}")
    norm=lambda x: re.sub(r"^([A-Za-z]*)0*", r"\1", x)
    if cited_fp and rec["first_page"] and norm(cited_fp)!=norm(rec["first_page"]): probs.append(f"first-page {cited_fp}!={rec['first_page']}")
    if probs: print(f"[ >DIFF< ] {num:>2}  {', '.join(probs)}  ({rec['src']})"); issues+=1
    else: print(f"[   ok   ] {num:>2}  year={rec['year']} vol={rec['volume']} p={rec['first_page']} ({rec['src']})")
    time.sleep(0.4)

# completeness: every ref cited in-text, every in-text [n] has a ref
body=md.split("## References",1)[0]
cited=set(int(x) for x in re.findall(r"\[(\d{1,2}(?:,\s*\d{1,2})*)\]", body) for x in re.split(r",\s*", x))
refnums=set(int(n) for n,_ in refs)
print("="*78)
print(f"COMPLETENESS: {len(refnums)} references, {len(cited)} distinct in-text citation numbers")
orphan=sorted(refnums-cited); dangling=sorted(cited-refnums)
if orphan: print(f"  >WARN< references never cited in text: {orphan}"); issues+=1
if dangling: print(f"  >FLAG< in-text [n] with NO reference: {dangling}"); issues+=1
if not orphan and not dangling: print("  ok  every reference is cited and every citation resolves")
print("="*78); print(f"SUMMARY: {issues} issue(s)")
sys.exit(1 if issues else 0)
