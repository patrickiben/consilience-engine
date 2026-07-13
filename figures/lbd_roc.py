#!/usr/bin/env python3
"""F6: ROC curve for the time-sliced LBD benchmark (reuses cached PubMed data; no re-pull)."""
import json, math, itertools, collections, os
import os
import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":9,"figure.dpi":150,"savefig.dpi":300,"axes.spines.top":False,"axes.spines.right":False})
CDIR=os.environ.get("RESULTS_DIR","."); OUT=os.environ.get("FIG_OUT",".")
CUTOFF,POST_HI,MIN_PRE,MIN_POST=2015,2023,5,3
STOP=set(["Humans","Animals","Male","Female","Adult","Middle Aged","Aged","Aged, 80 and over","Young Adult","Adolescent",
 "Child","Child, Preschool","Infant","Mice","Rats","Rats, Sprague-Dawley","Rats, Wistar","Mice, Inbred C57BL","Mice, Knockout",
 "Mice, Transgenic","Mice, Inbred Strains","Disease Models, Animal","Cells, Cultured","Molecular Sequence Data","Amino Acid Sequence",
 "Base Sequence","Time Factors","Dose-Response Relationship, Drug","Reproducibility of Results","Rats, Long-Evans","Treatment Outcome",
 "Retrospective Studies","Prospective Studies","Cohort Studies","Case-Control Studies","Rabbits","Guinea Pigs","Cricetinae",
 "Chick Embryo","Xenopus laevis","Xenopus","Sensitivity and Specificity","Cell Line","HEK293 Cells","Models, Biological",
 "Models, Molecular","Models, Neurological","Aging","Pregnancy","Species Specificity","Neurons","Brain"])
recs=json.load(open(f"{CDIR}/lbd_pubmed_mglur.json"))
pre=[r for r in recs if r["y"]<=CUTOFF]; post=[r for r in recs if CUTOFF<r["y"]<=POST_HI]
def clean(ms): return sorted(set(t for t in ms if t and t not in STOP))
def counter(LL):
    c=collections.Counter()
    for L in LL: c.update(set(L))
    return c
def pairs(LL):
    c=collections.Counter()
    for L in LL:
        for a,b in itertools.combinations(sorted(set(L)),2): c[(a,b)]+=1
    return c
pre_tp=counter(clean(r["m"]) for r in pre); pre_co=pairs(clean(r["m"]) for r in pre); post_co=pairs(clean(r["m"]) for r in post)
est=set(t for t,c in pre_tp.items() if c>=MIN_PRE)
adj={t:set() for t in est}
for (a,b),c in pre_co.items():
    if a in est and b in est: adj[a].add(b); adj[b].add(a)
deg={t:len(adj[t]) for t in est}
cand=set()
for a in est:
    two=set()
    for c in adj[a]: two|=adj[c]
    for b in two:
        if b!=a and b in est and b not in adj[a]: cand.add((a,b) if a<b else (b,a))
def pc(a,b): return post_co.get((a,b) if a<b else (b,a),0)
rows=[]
for (a,b) in cand:
    cn=adj[a]&adj[b]
    if not cn: continue
    AA=sum(1/math.log(deg[c]+1e-9) for c in cn if deg[c]>1)
    RA=sum(1/deg[c] for c in cn if deg[c]>0)
    JA=len(cn)/len(adj[a]|adj[b]); CN=len(cn)
    rows.append((AA,RA,JA,CN,1 if pc(a,b)>=MIN_POST else 0))
labs=np.array([r[4] for r in rows]); base=labs.mean()
preds={"Adamic-Adar":0,"Resource Allocation":1,"Jaccard":2,"Common Neighbours":3}
fig,ax=plt.subplots(figsize=(5.2,5))
roc={}
for name,ix in preds.items():
    sc=np.array([r[ix] for r in rows],float); auc=roc_auc_score(labs,sc); fpr,tpr,_=roc_curve(labs,sc)
    ax.plot(fpr,tpr,lw=1.8,label=f"{name} (AUC {auc:.2f})")
    roc[name]={"auc":float(auc)}
ax.plot([0,1],[0,1],"k--",lw=1,alpha=0.5,label="Chance")
ax.set_xlabel("False Positive Rate"); ax.set_ylabel("True Positive Rate")
ax.set_title(f"Figure 6 — Pre-2015 Topology Predicts Post-2015\nLiterature Links (n={len(rows)} Candidate Pairs, Base Rate {base:.3f})",fontsize=10,weight="bold")
ax.legend(loc="lower right",fontsize=8,frameon=False)
fig.tight_layout(); fig.savefig(f"{OUT}/F6_lbd_roc.png",bbox_inches="tight")
json.dump({"n_candidates":len(rows),"positives":int(labs.sum()),"base_rate":float(base),"auc":roc},open(f"{CDIR}/lbd_roc.json","w"),indent=1)
print(f"F6: n={len(rows)} pos={int(labs.sum())} base={base:.3f}  AUCs={ {k:round(v['auc'],3) for k,v in roc.items()} }")
print("wrote F6_lbd_roc.png")
