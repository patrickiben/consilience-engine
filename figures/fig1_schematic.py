#!/usr/bin/env python3
"""F1: engine schematic (Title Case; readable lens captions under the class boxes)."""
import matplotlib; matplotlib.use("Agg")
import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
plt.rcParams.update({"font.size":9,"savefig.dpi":300,"font.family":"DejaVu Sans"})
OUT=os.environ.get("FIG_OUT",".")
GREEN,BLUE,ORANGE="#2e8b3d","#1f6fc4","#e07b1a"
fig,ax=plt.subplots(figsize=(11.6,5.4)); ax.set_xlim(0,11.6); ax.set_ylim(0,5.4); ax.axis("off")
def box(x,y,w,h,txt,fc,ec="#333",fs=8.5,bold=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.04,rounding_size=0.08",
        fc=fc,ec=ec,lw=1.2)); ax.text(x+w/2,y+h/2,txt,ha="center",va="center",fontsize=fs,
        weight="bold" if bold else "normal")
def arrow(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=14,lw=1.3,color="#555"))
# stage 1
box(0.2,1.85,1.8,1.5,"Gene Set\n(Named Components)\n\ne.g. T-Cell, TLR-Family,\nInflammasome","#eef2f7",fs=8)
# stage 2: four lenses
lens=[("Structure\n(InterPro)","#cfe0f3"),("Expression\n(HPA Cell-Type)","#d6f0d6"),
      ("Interaction\n(STRING)","#ffe6cc"),("Process\n(GO-BP)","#eee0f0")]
for i,(t,c) in enumerate(lens):
    box(2.6,0.45+i*1.18,2.1,1.0,t,c,fs=8.5)
    arrow(2.05,2.6,2.55,0.95+i*1.18)
# stage 3
box(5.3,1.4,2.0,2.4,"Per-Lens\nGene–Gene\nSimilarity Graph","#f4f4f4",fs=9)
for i in range(4): arrow(4.75,0.95+i*1.18,5.25,2.6)
# stage 4
box(7.6,1.9,2.1,1.5,"Separation\n(Within − Between)\n+ Permutation\nNull (z, p)","#fff7d6",fs=8.5)
arrow(7.35,2.6,7.6,2.6)
# stage 5: classes (Title Case) + readable colored captions BELOW each box
cls=[("Cell Type",3.55,GREEN,"via Expression"),("Molecular Family",2.25,BLUE,"via Structure"),
     ("Functional Module",0.95,ORANGE,"via Interaction")]
bx,bw,bh=9.95,1.55,0.78
for name,y,col,cap in cls:
    box(bx,y,bw,bh,name,["#d6f0d6","#cfe0f3","#ffe6cc"][[ "Cell Type","Molecular Family","Functional Module"].index(name)],fs=8,bold=True)
    ax.text(bx+bw/2,y-0.20,cap,ha="center",va="center",fontsize=8.5,color=col,style="italic",weight="bold")
    arrow(9.7,2.6,bx-0.02,y+bh/2)
ax.text(bx+bw/2,4.75,"Diagnostic Class",ha="center",fontsize=8.5,style="italic",color="#555")
ax.text(5.6,5.15,"Figure 1 — The Consilience Engine: Each Entity-Class Is Diagnosed by the Lens That Separates It",
        ha="center",fontsize=11,weight="bold")
fig.savefig(f"{OUT}/F1_engine.png",bbox_inches="tight"); print("wrote F1_engine.png")
