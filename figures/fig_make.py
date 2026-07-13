#!/usr/bin/env python3
"""Render preprint figures F2-F5 from the saved JSON artifacts. (.venv + matplotlib)"""
import json, itertools, os
import os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":8,"axes.titlesize":10,"figure.dpi":150,"savefig.dpi":300,
                     "axes.spines.top":False,"axes.spines.right":False,"font.family":"DejaVu Sans"})
CDIR=os.environ.get("RESULTS_DIR","."); OUT=os.environ.get("FIG_OUT",".")
os.makedirs(OUT,exist_ok=True)
COL={"cell":"#2ca02c","family":"#1f77b4","module":"#ff7f0e","weak":"#999999"}

# ---------- F2: nervous-system lens map ----------
lm=json.load(open(f"{CDIR}/lens_map.json"))
def cls(s):
    ipr,snr,inter=s["InterPro"],s["snRNA"],s["STRING"]
    if snr>=0.18 and snr>=ipr: return "cell"
    if ipr>=0.18 and ipr>snr: return "family"
    if inter>=0.18: return "module"
    return "weak"
comps=list(lm);
order=sorted(comps,key=lambda c:({"cell":0,"family":1,"module":2,"weak":3}[cls(lm[c]["seps"])], -lm[c]["seps"]["STRING"]))
lenses=["InterPro","snRNA","STRING","GO-BP"]; lab=["Structure","Expression","Interaction","Process"]
M=np.array([[lm[c]["seps"][l] for l in lenses] for c in order])
fig=plt.figure(figsize=(9,11));
axh=fig.add_axes([0.30,0.06,0.30,0.88])
im=axh.imshow(M,aspect="auto",cmap="magma",vmin=0,vmax=0.9)
axh.set_xticks(range(4)); axh.set_xticklabels(lab,rotation=40,ha="right")
axh.set_yticks(range(len(order))); axh.set_yticklabels(order,fontsize=6)
for i,c in enumerate(order):
    axh.add_patch(plt.Rectangle((-0.5,i-0.5),0.18,1,color=COL[cls(lm[c]["seps"])],transform=axh.get_yaxis_transform(),clip_on=False))
axh.set_title("a  Separation by Lens (49 Components)")
cb=fig.colorbar(im,ax=axh,fraction=0.04,pad=0.02); cb.set_label("Separation")
# scatter panel b
axs=fig.add_axes([0.70,0.30,0.27,0.42])
for c in comps:
    s=lm[c]["seps"]; k=cls(s)
    axs.scatter(s["InterPro"],s["snRNA"],c=COL[k],s=22,edgecolor="white",linewidth=0.4,zorder=3)
axs.scatter(lm["Reward-DA"]["seps"]["InterPro"],lm["Reward-DA"]["seps"]["snRNA"],facecolor="none",edgecolor="red",s=90,linewidth=1.5,zorder=4)
axs.annotate("Dopamine\n(Dual)",(lm["Reward-DA"]["seps"]["InterPro"],lm["Reward-DA"]["seps"]["snRNA"]),xytext=(0.30,0.30),fontsize=7,color="red")
ipr=[lm[c]["seps"]["InterPro"] for c in comps]; snr=[lm[c]["seps"]["snRNA"] for c in comps]
r=np.corrcoef(ipr,snr)[0,1]
axs.set_xlabel("Structure Separation (InterPro)"); axs.set_ylabel("Expression Separation (snRNA)")
axs.set_title(f"b  Structure vs Expression\n(weak: r = {r:+.2f}, p = 0.04)"); axs.set_xlim(-0.05,1); axs.set_ylim(-0.05,1)
from matplotlib.lines import Line2D
axs.legend(handles=[Line2D([0],[0],marker='o',color='w',markerfacecolor=COL[k],label=l,markersize=7)
           for k,l in [("cell","Cell Type"),("family","Molecular Family"),("module","Functional Module")]],
           loc="upper right",fontsize=7,frameon=False)
fig.suptitle("Figure 2 — Nervous System: Each Component Class Has a Distinct Diagnostic Lens",x=0.5,y=0.99,fontsize=11,weight="bold")
fig.savefig(f"{OUT}/F2_nervous_lensmap.png",bbox_inches="tight"); plt.close(fig)

# ---------- F3: immune generalization ----------
im_=json.load(open(f"{CDIR}/immune_lens_map.json")); seps=im_["seps"]; kind=im_["kind"]
fig,ax=plt.subplots(1,2,figsize=(10,4.6))
# neuro
for c in comps:
    s=lm[c]["seps"]; ax[0].scatter(s["InterPro"],s["snRNA"],c=COL[cls(s)],s=20,edgecolor="white",linewidth=0.3)
ax[0].set_title(f"a  Nervous System  (r = {r:+.2f}, p = 0.04)"); ax[0].set_xlabel("Structure Sep"); ax[0].set_ylabel("Expression Sep")
ax[0].set_xlim(-0.05,1); ax[0].set_ylim(-0.05,1)
# immune
ix=[seps[g]["InterPro"] for g in seps]; ex=[seps[g]["blood-expr"] for g in seps]
ri=np.corrcoef(ix,ex)[0,1]
km={"cell":"cell","family":"family","module":"module"}
for g in seps:
    ax[1].scatter(seps[g]["InterPro"],seps[g]["blood-expr"],c=COL[km[kind[g]]],s=34,edgecolor="white",linewidth=0.4)
for g in ["Complement","JAK-STAT","TCR-signaling"]:
    ax[1].annotate(g,(seps[g]["InterPro"],seps[g]["blood-expr"]),fontsize=6,xytext=(3,3),textcoords="offset points")
ax[1].set_title(f"b  Immune System  (r = {ri:+.2f}, n.s.; ARI 0.55)"); ax[1].set_xlabel("Structure Sep"); ax[1].set_ylabel("Expression Sep")
ax[1].set_xlim(-0.05,1); ax[1].set_ylim(-0.05,1)
ax[1].legend(handles=[Line2D([0],[0],marker='o',color='w',markerfacecolor=COL[k],label=l,markersize=7)
           for k,l in [("cell","Cell Type"),("family","Molecular Family"),("module","Functional Module")]],loc="upper right",fontsize=7,frameon=False)
fig.suptitle("Figure 3 — The Principle Generalizes: Entity-Classes Recover From Lens Data in a Second Organ System",fontsize=11,weight="bold")
fig.tight_layout(rect=[0,0,1,0.95]); fig.savefig(f"{OUT}/F3_immune_generalization.png",bbox_inches="tight"); plt.close(fig)

# ---------- F4: consilience matrix ----------
cm=json.load(open(f"{CDIR}/consilience_matrix.json")); corr=cm["corr"]
order4=["literature","interpro","pharm","reactome","pathway","goBP","string","proteinclass","disease","genetics","coexpr","gtex","singlecell","scrna","proteomics"]
order4=[d for d in order4 if any(d in k.split("|") for k in corr)]
DISP={"literature":"Literature","string":"STRING","pharm":"Pharmacology","reactome":"Reactome","pathway":"KEGG","goBP":"GO-BP","interpro":"InterPro","proteinclass":"Protein-Class","disease":"Disease","genetics":"Genetics","coexpr":"Co-Expr","gtex":"GTEx","singlecell":"Single-Cell","scrna":"snRNA","proteomics":"Proteomics"}
n=len(order4); Mx=np.full((n,n),np.nan)
for i,a in enumerate(order4):
    for j,b in enumerate(order4):
        v=corr.get(f"{a}|{b}") or corr.get(f"{b}|{a}") or (1.0 if a==b else None)
        if v is not None: Mx[i,j]=v
fig,ax=plt.subplots(figsize=(7.5,6.5))
im=ax.imshow(Mx,cmap="RdBu_r",vmin=-0.3,vmax=0.7)
ax.set_xticks(range(n)); ax.set_xticklabels([DISP.get(d,d) for d in order4],rotation=55,ha="right",fontsize=7)
ax.set_yticks(range(n)); ax.set_yticklabels([DISP.get(d,d) for d in order4],fontsize=7)
for (b0,b1,name) in [(0,8,"function/structure"),(8,10,"disease/gen"),(10,15,"expression")]:
    ax.add_patch(plt.Rectangle((b0-0.5,b0-0.5),b1-b0,b1-b0,fill=False,edgecolor="k",lw=1.6))
fig.colorbar(im,fraction=0.046,pad=0.04).set_label("Spearman r (Gene-Pair Similarity)")
ax.set_title("Figure 4 — Cross-Modality Consilience Matrix → Three Axes",weight="bold")
fig.savefig(f"{OUT}/F4_consilience_matrix.png",bbox_inches="tight"); plt.close(fig)

# ---------- F5: connectome conservation ----------
md=json.load(open(f"{CDIR}/matched_density.json"))["mouse_sweep"]
ms=json.load(open(f"{CDIR}/multispecies_connectome.json"))
dens=sorted(float(k) for k in md); sig=[md[f"{d:.4f}"]["sigma"] for d in dens]; Q=[md[f"{d:.4f}"]["Q"] for d in dens]
# matched-density species
sp={}
for src in ("matched_0075","matched_0075_added"):
    for k,v in ms[src].items():
        if "Macaque" in k: continue
        sp[k.split(" (")[0]]= (v["sigma"],v["Q"])
sp["Drosophila hemibrain"]=(ms["hemibrain"]["sigma"],ms["hemibrain"]["Q"]); sp["Mouse 316reg"]=(ms["mouse_0075"]["sigma"],ms["mouse_0075"]["Q"])
fig,ax=plt.subplots(1,2,figsize=(11,4.4))
ax[0].plot(dens,sig,"o-",label="Small-World σ",color="#d62728")
ax2=ax[0].twinx(); ax2.plot(dens,Q,"s--",label="Modularity Q",color="#1f77b4"); ax2.set_ylabel("Modularity Q",color="#1f77b4")
ax[0].set_xlabel("Graph Density"); ax[0].set_ylabel("Small-World σ",color="#d62728"); ax[0].set_title("a  Mouse: σ and Q Are Density-Dependent")
names=sorted(sp,key=lambda x:sp[x][1]); x=np.arange(len(names)); w=0.38
ax[1].bar(x-w/2,[sp[n][0] for n in names],w,label="σ (Small-World)",color="#d62728")
ax3=ax[1].twinx(); ax3.bar(x+w/2,[sp[n][1] for n in names],w,label="Q (Modularity)",color="#1f77b4")
ax3.set_ylim(0,0.8); ax3.axhspan(0.49,0.65,color="#1f77b4",alpha=0.08); ax3.set_ylabel("Modularity Q",color="#1f77b4")
ax[1].set_xticks(x); ax[1].set_xticklabels(names,rotation=30,ha="right",fontsize=7); ax[1].set_ylabel("Small-World σ",color="#d62728")
ax[1].set_title("b  At Matched Density (0.0075): Q ≈ 0.49–0.65 Across Phyla")
fig.suptitle("Figure 5 — Connectome Organisation Is Comparable From Worm to Human at Matched Density",fontsize=11,weight="bold")
fig.tight_layout(rect=[0,0,1,0.94]); fig.savefig(f"{OUT}/F5_connectome.png",bbox_inches="tight"); plt.close(fig)
print("wrote:", os.listdir(OUT))
