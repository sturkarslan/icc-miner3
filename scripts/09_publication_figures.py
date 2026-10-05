#!/usr/bin/env python
"""Step 09 (ICC): two publication figures (Nature double column, 183 mm), assembled from saved results only.

Figure 1  Data, network and biology
  a study design            b network by the numbers
  c programs x states (clustered) with published iCCA classes, drivers and risk
  d what the programs are: program activity vs published iCCA signatures
  e FGFR2-fusion causal flow (driver -> regulators -> programs)
  f replication of causal flows in an independent cohort with WES (OEP002768, step 08e)
Figure 2  Risk and validation
  a risk-model program weights         b risk score across published classes
  c states ordered by risk: class composition, risk score, observed GuanRank
  d Kaplan-Meier in test cohorts       e HR per SD, all test cohorts (+ pooled external)
  f C-index vs published classes and signatures in held-out cohorts (step 07g)
  g split-half stability (step 08b)

Programs: config/program_labels.tsv (curated). Classes, signatures and biology blocks: config/reference_panel.yaml
(ICC panel; classes are our NTP calls, checked against the published calls). Outputs: results/09_figures/.
"""

import argparse
import importlib.util
import json
import os

import numpy as np
import pandas as pd
from scipy import stats

from hcc_common import load_params, miner_id_backmap, p, setup_logging
from hcc_panel import Panel

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import gridspec  # noqa: E402
from matplotlib.patches import FancyBboxPatch, PathPatch  # noqa: E402
from matplotlib.path import Path  # noqa: E402

import qc_plots as Q  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
MM = 1 / 25.4
W = 183 * MM

# ---------------------------------------------------------------- style (Nature)
plt.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["Liberation Sans", "Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 6, "axes.titlesize": 6.5, "axes.labelsize": 6, "xtick.labelsize": 5.5, "ytick.labelsize": 5.5,
    "legend.fontsize": 5.5, "axes.linewidth": 0.5, "xtick.major.width": 0.5, "ytick.major.width": 0.5,
    "xtick.major.size": 2, "ytick.major.size": 2, "lines.linewidth": 0.9, "axes.titleweight": "normal",
    "axes.titlelocation": "left", "axes.titlepad": 3, "axes.labelpad": 2, "pdf.fonttype": 42, "ps.fonttype": 42,
    "savefig.dpi": 300, "axes.grid": False, "legend.frameon": False, "legend.handlelength": 1.2,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
})
ADV, PROT = Q.SLOTS[7], Q.SLOTS[0]          # adverse red / protective blue, everywhere
COH = Q.cohort_colors(["FU_iCCA", "TCGA", "GSE107943", "GSE179443"])
EXT_COL = {"GSE244807": Q.SLOTS[4], "OEP002768": Q.SLOTS[6]}
_AX = {"adverse": "adverse", "protective": "protective", "immune": "immune", "other": "other"}
PN = Panel()   # reference signature panel (config/reference_panel.yaml)
_BCOL = {"adverse": ADV, "protective": PROT, "immune": Q.SLOTS[2]}
BLOCK_COL = {b: _BCOL.get(spec.get("colour"), Q.MUTED) for b, spec in PN.blocks.items()}
AXIS_COL = {"adverse": ADV, "protective": PROT, "immune": Q.SLOTS[2], "other": Q.MUTED}
MODEL_COL = {"background": Q.BACKGROUND, "muted": Q.MUTED, "slot2": Q.SLOTS[2], "slot3": Q.SLOTS[3],
             "slot4": Q.SLOTS[4], "slot5": Q.SLOTS[5], "slot6": Q.SLOTS[6]}


# Red-blue is reserved for risk and regulon dysregulation; fractions use viridis and signed
# correlations a purple-green diverging scale.
FRAC_CMAP = "viridis"
COR_CMAP = "PRGn"  # signed correlations: purple negative, white zero, green positive


def class_tag(key, level):
    """Small grey tag next to a class label: the class code, or the source when the code is the label."""
    t = PN.class_title(key)
    return t.split(" (")[-1].rstrip(")") if " (" in t else t


def _module(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def letter(ax, s, x=-0.02, y=1.02):
    ax.text(x, y, s, transform=ax.transAxes, fontsize=8, fontweight="bold", va="bottom", ha="right")


def despine(ax):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)


def km(ax, dur_days, ev, color, label, lw=0.9):
    ts, ss, t, e = Q.kaplan_meier(dur_days / 30.44, ev)
    ax.step(np.append(ts, t.max()), np.append(ss, ss[-1]), where="post", color=color, lw=lw, label=label)


# ================================================================ data
def load_all(P, log):
    res = p(P["paths"]["results"])
    mx = P["miner"]["matrix"]
    D = {"res": res}
    mdir = os.path.join(res, "04_miner", mx)
    D["samples"] = pd.read_csv(os.path.join(res, "01_harmonized", "samples.tsv"), sep="\t", index_col="sample")
    D["genes"] = pd.read_csv(os.path.join(res, "01_harmonized", "genes.tsv"), sep="\t", index_col="ensembl")
    D["programs"] = {k: [str(r) for r in v] for k, v in json.load(open(os.path.join(mdir, "subtypes_filtered", "transcriptional_programs.json"))).items()}
    D["states"] = json.load(open(os.path.join(mdir, "subtypes_filtered", "transcriptional_states.json")))
    over = pd.read_csv(os.path.join(mdir, "subtypes_filtered", "overExpressedMembers.csv"), index_col=0)
    under = pd.read_csv(os.path.join(mdir, "subtypes_filtered", "underExpressedMembers.csv"), index_col=0)
    over.index, under.index = over.index.astype(str), under.index.astype(str)
    D["diff"] = over - under
    D["cor"] = pd.read_csv(os.path.join(res, "07_post", "subtype_mapping", "subtypes_filtered",
                                        "program_signature_correlation.tsv"), sep="\t", index_col=0).rename(index=str)
    D["ntp"] = PN.class_calls(os.path.join(res, "07_post", "subtype_mapping", "subtypes_filtered"), D["samples"])
    D["genomic"] = pd.read_csv(os.path.join(res, "03_genomics_clinical", "genomic_features.csv"), index_col=0)
    rdir = os.path.join(res, "06_risk", mx)
    D["model"] = P["validation"]["models"][0]
    D["weights"] = pd.read_csv(os.path.join(rdir, f"predictor_ridge_programs_{D['model']}", "weights.tsv"), sep="\t",
                               index_col=0)["weight"].rename(index=str)
    pred = pd.read_csv(os.path.join(rdir, f"predictor_ridge_programs_{D['model']}", "predictions.tsv"), sep="\t", index_col=0)
    D["pred"] = pred
    D["risk"] = pred.groupby("cohort")["risk_score"].transform(lambda v: (v - v.mean()) / v.std())
    D["prog_meta"] = pd.read_csv(os.path.join(rdir, "prognostic_programs_h36m_OS.tsv"), sep="\t", index_col=0).rename(index=str)
    D["surv"] = {(c, "OS"): pd.read_csv(os.path.join(res, "03_genomics_clinical", f"survival_{c}_OS_h36m_miner.csv"),
                                        index_col=0).set_axis(["duration", "observed"], axis=1)
                 for c in P["risk"]["survival_cohorts"]}
    D["P"] = P
    D["rdir"] = rdir
    lab = pd.read_csv(p("config/program_labels.tsv"), sep="\t", comment="#", dtype={"program": str}).set_index("program")
    D["plabel"] = lab["label"].to_dict()
    # biology block per program: anchor signature group with the highest mean activity r (>= 0.3), else other
    D["block"] = pd.Series({k: PN.block_of_program(D["cor"].loc[k]) for k in D["cor"].index})
    log.info("Program blocks: %s", D["block"].value_counts().to_dict())
    return D


def plab(D, k, short=False):
    return f"P{k} {D['plabel'][k]}" if k in D["plabel"] else f"P{k}"


# ================================================================ Figure 1
def f1a_design(ax, D, P):
    ax.set_xlim(0, 100)
    ax.set_ylim(1.5, 40.5)
    ax.axis("off")
    S = D["samples"]["cohort"].value_counts()

    def box(x, y, w, h, title, lines, ec, fc="white", tc=None):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=0.8", fc=fc, ec=ec, lw=0.7))
        ax.text(x + 0.8, y + h - 0.8, title, fontsize=5.4, fontweight="bold", va="top", color=tc or Q.INK)
        ax.text(x + 0.8, y + h - 3.1, "\n".join(lines), fontsize=4.4, va="top", color=Q.INK2, linespacing=1.15)

    def arrow(x0, y0, x1, y1):
        ax.annotate("", (x1, y1), (x0, y0), arrowprops=dict(arrowstyle="-|>", lw=0.6, color=Q.MUTED, shrinkA=0, shrinkB=0,
                                                              mutation_scale=6))
    ax.text(0, 39.5, f"Discovery ({len(D['samples'])} iCCA)", fontsize=5.8, fontweight="bold", va="top")
    coh = [("FU-iCCA", "FU_iCCA", [f"n = {S['FU_iCCA']} · RNA-seq", "WES · CNA · FGFR2 fusion", "OS · China (Dong 2022)"]),
           ("GSE179443", "GSE179443", [f"n = {S['GSE179443']} · RNA-seq", "expression only · Korea"]),
           ("TCGA-CHOL", "TCGA", [f"n = {S['TCGA']} intrahepatic", "WES · OS · US"]),
           ("GSE107943", "GSE107943", [f"n = {S['GSE107943']} · RNA-seq", "OS / RFS · Korea"])]
    hh = [10.4, 8.4, 8.4, 8.4]
    y = 37.8
    for (t, c, lines), h in zip(coh, hh):
        y -= h
        box(0, y, 20.3, h - 1.0, t, lines, COH[c])
    steps = [("Harmonize", [f"{int(D['genes']['kept'].sum()):,} genes", "log2 TPM", "ComBat by cohort"]),
             ("MINER network", ["regulons", "(technical excluded)", "→ programs", "→ states"]),
             ("Causal inference", [f"{D['genomic'].shape[0]} genomic", "features: driver", "→ regulator", "→ regulon"]),
             ("Risk model", ["ridge on", f"{len(D['programs'])} programs;", "FU-iCCA OS,", "36 months"])]
    for i, (t, lines) in enumerate(steps):
        x = 22.6 + i * 15.1
        box(x, 15.0, 14.1, 14.5, t, lines, Q.INK)
        arrow(x - 1.0 if i else 20.7, 22, x - 0.15, 22)
    ax.text(22.6, 12.6, "Annotation: STIM, Dong 2022, Lin 2026, Andersen, Song duct-type classes; published signatures",
            fontsize=4.7, color=Q.INK2, va="top")
    ax.text(84.5, 40.2, "Held-out validation", fontsize=5.8, fontweight="bold", va="top")
    ext = [("GSE244807", ["n = 246 · RNA-seq · OS", "109 resected,", "137 biopsies"], EXT_COL["GSE244807"]),
           ("OEP002768", ["n = 59 unique", "RNA-seq · WES · OS"], EXT_COL["OEP002768"]),
           ("GSE255058", ["n = 18 biopsies", "response to HAIC +", "lenvatinib + anti-PD-1"], Q.MUTED)]
    for i, (t, lines, col) in enumerate(ext):
        box(84.5, 27.6 - i * 10.8, 15.0, 9.6, t, lines, col)
    arrow(83.2, 22, 84.3, 22)
    ax.text(84.5, 4.4, "fixed weights, never refit", fontsize=4.4, color=Q.INK2)


def f1b_numbers(ax, D, P):
    res = D["res"]
    mdir = os.path.join(res, "04_miner", P["miner"]["matrix"])
    rdf = pd.read_csv(os.path.join(mdir, "mechinf", "regulonDf.csv"), index_col=0)
    keep = set(json.load(open(os.path.join(mdir, "mechinf", "regulons_filtered.json"))))
    rk = rdf[rdf["Regulon_ID"].astype(str).isin(keep)]
    hc = pd.read_csv(os.path.join(res, "05_causal", P["miner"]["matrix"], "highConfidenceCausalResults.csv"), index_col=0)
    fam = pd.read_csv(os.path.join(res, "05_causal", P["miner"]["matrix"], "regulon_families.tsv"), sep="\t")
    rows = [("genes", int(D["genes"]["kept"].sum())),
            ("co-expression modules", len(json.load(open(os.path.join(mdir, "coexpr", "coexpressionDictionary.json"))))),
            ("regulons", len(keep)), ("regulators", rk["Regulator"].nunique()), ("regulon genes", rk["Gene"].nunique()),
            ("regulon families", fam["family"].nunique()), ("programs", len(D["programs"])), ("states", len(D["states"])),
            ("genomic features", D["genomic"].shape[0]), ("causal drivers", hc["Mutation"].nunique()),
            ("causal flows", len(hc))]
    y = np.arange(len(rows))
    v = np.array([r[1] for r in rows], float)
    ax.barh(y, np.log10(v), color=[Q.MUTED] * 6 + [Q.INK] * 2 + [Q.MUTED] * 3, height=0.62)
    for yi, (lab, n) in zip(y, rows):
        ax.text(np.log10(n) + 0.06, yi, f"{n:,}", va="center", fontsize=5.2, color=Q.INK)
    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rows], fontsize=5.3)
    ax.invert_yaxis()
    ax.set_xlim(0, 5.9)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(["1", "10", "10²", "10³", "10⁴"])
    ax.set_xlabel("count (log scale)")
    despine(ax)
    ax.set_title("Network by the numbers")
    return pd.DataFrame(rows, columns=["item", "n"])


def cluster(X):
    from scipy.cluster.hierarchy import leaves_list, linkage
    from scipy.spatial.distance import pdist
    Z = linkage(np.nan_to_num(pdist(np.nan_to_num(np.asarray(X, float)), "correlation"), nan=1.0), "average")
    return Z, leaves_list(Z)


def frac_table(states, labels, levels):
    out = pd.DataFrame(index=levels, columns=list(states), dtype=float)
    for k, v in states.items():
        x = labels.reindex(v).dropna()
        x = x[x != "unassigned"]
        for lv in levels:
            out.loc[lv, k] = (x == lv).mean() if len(x) else np.nan
    return out


def f1c_map(fig, sub, D):
    progs0, states0 = list(D["programs"]), list(D["states"])
    diff = D["diff"]
    M0 = pd.DataFrame({s: [diff.loc[D["programs"][k], [x for x in D["states"][s] if x in diff.columns]].values.mean()
                           for k in progs0] for s in states0}, index=progs0)
    from scipy.cluster.hierarchy import dendrogram
    Zc, co = cluster(M0.values.T)
    s_order = [states0[i] for i in co]
    # programs grouped by biology block, clustered within block
    p_order = []
    for b in list(BLOCK_COL) + ["Other"]:
        ks = [k for k in progs0 if D["block"].get(k) == b]
        if len(ks) > 2:
            _, o = cluster(M0.loc[ks].values)
            ks = [ks[i] for i in o]
        p_order += ks
    M = M0.loc[p_order, s_order]
    rz = pd.Series({s: D["risk"].reindex(D["states"][s]).mean() for s in s_order})
    tracks = []
    for cl, lv in PN.figures["fig1c_tracks"]:
        if cl not in D["ntp"]:
            continue
        T = frac_table(D["states"], D["ntp"][cl], lv)[s_order]
        T.index = [f"{PN.class_label(cl, l)}|{class_tag(cl, l)}" for l in lv]
        tracks.append(T)
    G = D["genomic"]
    mut = pd.DataFrame({s: [G.loc[m, [x for x in D["states"][s] if x in G.columns]].mean()
                            for m in ("MUT_KRAS", "MUT_TP53", "PATH_IDH", "MUT_BAP1", "FUS_FGFR2")] for s in s_order},
                       index=["KRAS mut|", "TP53 mut|", "IDH1/2 mut|", "BAP1 mut|", "FGFR2 fusion|"])
    tracks.append(mut)
    nrow = [1.6, 2.2] + [len(t) * 1.6 for t in tracks] + [len(M) * 0.3]
    gs = gridspec.GridSpecFromSubplotSpec(len(nrow), 4, subplot_spec=sub, height_ratios=nrow,
                                          width_ratios=[0.36, 0.05, 1, 0.34], hspace=0.12, wspace=0.02)
    x = np.arange(len(s_order))
    axd = fig.add_subplot(gs[0, 2])
    dendrogram(Zc, ax=axd, no_labels=True, color_threshold=0, link_color_func=lambda k: Q.MUTED)
    for c in axd.collections:
        c.set_linewidth(0.4)
    axd.axis("off")
    letter(axd, "c", x=-0.42, y=0.5)
    axd.set_title("Programs × states (clustered): published-class biology, drivers and risk", fontsize=6.5, pad=1)
    axr = fig.add_subplot(gs[1, 2])
    axr.bar(x, rz.values, color=[ADV if v > 0 else PROT for v in rz.values], width=0.75)
    axr.axhline(0, color=Q.AXIS, lw=0.4)
    axr.set_xlim(-0.5, len(x) - 0.5)
    axr.set_xticks([])
    axr.set_yticks([])
    for sp in axr.spines.values():
        sp.set_visible(False)
    axr.text(-0.6, 0, "risk", ha="right", va="center", fontsize=5.2)
    for i, T in enumerate(tracks):
        ax = fig.add_subplot(gs[2 + i, 2])
        imt = ax.imshow(T.values.astype(float), aspect="auto", cmap=FRAC_CMAP, vmin=0, vmax=1, interpolation="none")
        ax.set_yticks(range(len(T)))
        ax.set_yticklabels([t.split("|")[0] for t in T.index], fontsize=4.8)
        ax.set_xticks([])
        for sp in ax.spines.values():
            sp.set_linewidth(0.3)
        axt = fig.add_subplot(gs[2 + i, 3])
        axt.set_ylim(len(T) - 0.5, -0.5)
        axt.axis("off")
        for j, t in enumerate(T.index):
            axt.text(0.03, j, t.split("|")[1], fontsize=4.4, color=Q.MUTED, va="center")
    ax = fig.add_subplot(gs[-1, 2])
    v = np.nanpercentile(np.abs(M.values), 98)
    im = ax.imshow(M.values, aspect="auto", cmap=Q.DIV, vmin=-v, vmax=v, interpolation="none")
    ax.set_yticks([])
    ax.set_xticks(x)
    ax.set_xticklabels([f"S{s}" for s in s_order], fontsize=4.2, rotation=90)
    ax.set_xlabel("MINER transcriptional state", fontsize=5.5, labelpad=1)
    for sp in ax.spines.values():
        sp.set_linewidth(0.3)
    # block strip + labels
    axb = fig.add_subplot(gs[-1, 1])
    blocks = [D["block"][k] for k in p_order]
    for i, b in enumerate(blocks):
        axb.add_patch(plt.Rectangle((0, i - 0.5), 1, 1, color=BLOCK_COL.get(b, Q.BACKGROUND), lw=0))
    axb.set_xlim(0, 1)
    axb.set_ylim(len(blocks) - 0.5, -0.5)
    axb.axis("off")
    axl = fig.add_subplot(gs[-1, 3])
    axl.set_ylim(len(blocks) - 0.5, -0.5)
    axl.axis("off")
    start = 0
    for b in list(BLOCK_COL) + ["Other"]:
        n = blocks.count(b)
        if n:
            axl.text(0.03, start + n / 2 - 0.5, f"{b}\n({n} programs)", fontsize=4.8, va="center",
                     color=BLOCK_COL.get(b, Q.MUTED), fontweight="bold" if b != "Other" else "normal")
            start += n
    cax = axl.inset_axes([0.05, -0.075, 0.85, 0.018])
    cb = fig.colorbar(im, cax=cax, orientation="horizontal")
    cb.set_label("regulon dysregulation", fontsize=4.6, labelpad=1)
    cb.ax.tick_params(labelsize=4.2, length=1.5, width=0.3)
    cb.outline.set_linewidth(0.3)
    cax = axl.inset_axes([0.05, -0.2, 0.85, 0.018])
    cb = fig.colorbar(imt, cax=cax, orientation="horizontal", ticks=[0, 0.5, 1])
    cb.set_label("fraction of tumours (tracks)", fontsize=4.6, labelpad=1)
    cb.ax.tick_params(labelsize=4.2, length=1.5, width=0.3)
    cb.outline.set_linewidth(0.3)
    return M, pd.DataFrame(tracks[0])


def f1d_signatures(ax, D):
    ks = [k for k in D["plabel"] if k in D["cor"].index]
    ks = sorted(ks, key=lambda k: (list(BLOCK_COL).index(D["block"][k]) if D["block"][k] in BLOCK_COL else 9,
                                   -D["weights"].get(k, 0)))
    panel = PN.signatures(available=set(D["cor"].columns))
    sigs = [x["set"] for x in panel]
    C = D["cor"].loc[ks, sigs]
    im = ax.imshow(C.values, aspect="auto", cmap=COR_CMAP, vmin=-1, vmax=1, interpolation="none")
    ax.set_yticks(range(len(ks)))
    ax.set_yticklabels([plab(D, k) for k in ks], fontsize=4.6)
    for t, k in zip(ax.get_yticklabels(), ks):
        t.set_color(ADV if D["weights"].get(k, 0) > 0 else PROT)
    info = {x["set"]: (x["label"], x["tag"], x["block"]) for x in panel}
    ax.set_xticks(range(len(sigs)))
    ax.set_xticklabels([f"{info[s][0]} ({info[s][1]})" for s in sigs], fontsize=4.1, rotation=60, ha="right",
                       rotation_mode="anchor")
    for t, s in zip(ax.get_xticklabels(), sigs):
        t.set_color(BLOCK_COL[info[s][2]])
    for sp in ax.spines.values():
        sp.set_linewidth(0.3)
    # group separators
    g = [info[s][2] for s in sigs]
    for j in range(1, len(g)):
        if g[j] != g[j - 1]:
            ax.axvline(j - 0.5, color="white", lw=1.2)
    bk = [D["block"][k] for k in ks]
    for i in range(1, len(bk)):
        if bk[i] != bk[i - 1]:
            ax.axhline(i - 0.5, color="white", lw=1.2)
    ax.set_title("What the programs are (activity r with reference signatures)", pad=13)
    cax = ax.inset_axes([0.78, 1.02, 0.22, 0.018])
    cb = plt.colorbar(im, cax=cax, orientation="horizontal", ticks=[-1, 0, 1])
    cb.ax.xaxis.set_ticks_position("top")
    cb.ax.tick_params(labelsize=4.2, length=1.5, width=0.3, pad=1)
    cb.outline.set_linewidth(0.3)
    ax.text(0.77, 1.029, "r", transform=ax.transAxes, fontsize=5, ha="right", va="center")
    ax.text(0.0, 1.035, "row colour: risk weight (red adverse, blue protective)", transform=ax.transAxes, fontsize=4.4,
            color=Q.INK2, va="bottom", ha="left")
    return C


def curve(ax, x0, y0, x1, y1, color, lw, ls="-"):
    xm = (x0 + x1) / 2
    path = Path([(x0, y0), (xm, y0), (xm, y1), (x1, y1)], [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])
    ax.add_patch(PathPatch(path, facecolor="none", edgecolor=color, lw=lw, ls=ls, alpha=0.85, zorder=1))


def f1e_ctnnb1(ax, D, P, n_top=12, force=(), driver="FUS_FGFR2", name="FGFR2\nfusion"):
    res = D["res"]
    hc = pd.read_csv(os.path.join(res, "05_causal", P["miner"]["matrix"], "highConfidenceCausalResults.csv"), index_col=0)
    hc["program"] = hc["program"].astype(int).astype(str)
    x = hc[hc["Mutation"] == driver].assign(ad=lambda d: d["cohen_d"].abs())
    x = x.sort_values("ad", ascending=False).drop_duplicates("family")
    sel = pd.concat([x.head(n_top), x[x["regulator_symbol"].isin(force)]]).drop_duplicates("family")
    sel = sel.drop_duplicates("regulator_symbol")
    sel = sel.sort_values(["MutationRegulatorEdge", "ad"], ascending=[False, False])
    pg = sel.groupby("program").agg(n=("family", "size"), d=("cohen_d", "mean")).reset_index()
    pg = pg.assign(w=pg["program"].map(D["weights"])).sort_values("w")
    ry = dict(zip(sel["regulator_symbol"], np.linspace(0.95, 0.05, len(sel))))
    py = dict(zip(pg["program"], np.linspace(0.92, 0.08, len(pg))))
    X0, X1, X2 = 0.07, 0.36, 0.55
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    for _, r in sel.iterrows():
        curve(ax, X0 + 0.055, 0.5, X1 - 0.05, ry[r["regulator_symbol"]], ADV if r["MutationRegulatorEdge"] > 0 else PROT,
              0.35 + 0.9 * min(r["ad"], 2) / 2)
        curve(ax, X1 + 0.05, ry[r["regulator_symbol"]], X2 - 0.005, py[r["program"]], ADV if r["cohen_d"] > 0 else PROT,
              0.35 + 1.2 * min(r["ad"], 2) / 2, ls="-" if r["RegulatorRegulon_Spearman_R"] > 0 else (0, (2.5, 1.5)))
    ax.add_patch(FancyBboxPatch((X0 - 0.055, 0.45), 0.11, 0.1, boxstyle="round,pad=0.01", fc=Q.INK, ec=Q.INK))
    ax.text(X0, 0.5, name, color="white", ha="center", va="center", fontsize=5.5, fontweight="bold")
    ax.text(X0, 0.42, f"n = {int(x['n_altered'].iloc[0])}", ha="center", va="top", fontsize=4.6, color=Q.INK2)
    for _, r in sel.iterrows():
        up = r["MutationRegulatorEdge"] > 0
        ax.text(X1, ry[r["regulator_symbol"]], f"{r['regulator_symbol']} {'↑' if up else '↓'}", ha="center", va="center",
                fontsize=5, fontweight="bold" if r["regulator_symbol"] in force else "normal",
                bbox=dict(boxstyle="round,pad=0.18", fc="white", ec=Q.MUTED, lw=0.4))
    for _, r in pg.iterrows():
        k = r["program"]
        adverse = D["weights"].get(k, 0) > 0
        ax.text(X2, py[k], f"{plab(D, k)} {'↑' if r['d'] > 0 else '↓'}", ha="left", va="center", fontsize=4.9,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=ADV if adverse else PROT, lw=0.8))
    ax.set_title(f"{name.replace(chr(10), ' ')} causal flow: driver → regulators → programs", fontsize=6.5)
    ax.text(0.0, -0.04, "edges: red up / blue down in mutant tumours; dashed = repressor; width ~ |d|; "
            "box border: red adverse / blue protective program", transform=ax.transAxes, fontsize=4.4, color=Q.INK2,
            va="top")
    return sel


def f1f_replication(ax, D, P):
    """Causal flows in an independent cohort with WES (OEP002768, step 08e): share of driver -> regulon effects with
    the predicted direction, against random regulons with the same predicted signs."""
    f = os.path.join(D["res"], "08_validation", "OEP002768", "causal_replication.tsv")
    R = pd.read_csv(f, sep="\t")
    names = {"MUT_TP53": "TP53", "MUT_BAP1": "BAP1", "FUS_FGFR2": "FGFR2 fusion", "PATH_IDH": "IDH1/2", "MUT_IDH1": "IDH1"}
    R = R[R["driver"].isin(names)].set_index("driver").reindex([k for k in names if k in set(R["driver"])])
    y = np.arange(len(R))
    ax.barh(y, 100 * R["sign_agreement"], color=Q.SLOTS[0], height=0.6, label="same direction")
    ax.barh(y, 100 * R["same_sign_p_lt_0_05"], color=Q.INK, height=0.6, label="same direction, P < 0.05")
    ax.scatter(100 * R["null_sign_agreement_mean"], y, marker="|", s=60, color=ADV, zorder=4, label="random regulons")
    for yi, (_, r) in zip(y, R.iterrows()):
        ax.text(100 * r["sign_agreement"] + 1.5, yi, f"{100 * r['sign_agreement']:.0f}%\n{int(r['flows_tested'])} flows, "
                f"n = {int(r['n_altered'])}", va="center", fontsize=4.3, linespacing=1.0)
    ax.set_yticks(y)
    ax.set_yticklabels([names[k] for k in R.index], fontsize=5.3)
    ax.invert_yaxis()
    ax.set_xlim(0, 128)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.axvline(50, color=Q.AXIS, lw=0.4, ls=":")
    ax.set_xlabel("% of high-confidence driver → regulon effects")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, -0.32), ncol=3, fontsize=4.3, handlelength=1, columnspacing=0.8)
    despine(ax)
    ax.set_title("Causal flows replicate (OEP002768, WES)")
    return R


def figure1(D, P, outdir, log):
    fig = plt.figure(figsize=(W, 238 * MM))
    gs = gridspec.GridSpec(3, 1, height_ratios=[40, 120, 62], hspace=0.36, left=0.03, right=0.985, top=0.985, bottom=0.03)
    top = gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=gs[0], width_ratios=[3.25, 1], wspace=0.28)
    ax = fig.add_subplot(top[0])
    f1a_design(ax, D, P)
    letter(ax, "a", x=0.0, y=0.99)
    ax = fig.add_subplot(top[1])
    tb = f1b_numbers(ax, D, P)
    letter(ax, "b", x=-0.33)
    mid = gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=gs[1], width_ratios=[1.25, 1], wspace=0.55)
    M, _ = f1c_map(fig, mid[0], D)
    dsub = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=mid[1], height_ratios=[1, 0.4], hspace=0.0)
    axd = fig.add_subplot(dsub[0])
    C = f1d_signatures(axd, D)
    letter(axd, "d", x=-0.42, y=1.07)
    bot = gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=gs[2], width_ratios=[1.38, 1], wspace=0.16)
    ax = fig.add_subplot(bot[0])
    e = f1e_ctnnb1(ax, D, P)
    letter(ax, "e", x=0.0, y=1.0)
    sub = gridspec.GridSpecFromSubplotSpec(3, 2, subplot_spec=bot[1], width_ratios=[0.3, 1], height_ratios=[0.25, 1, 0.5])
    ax = fig.add_subplot(sub[1, 1])
    f = f1f_replication(ax, D, P)
    letter(ax, "f", x=-0.2, y=1.05)
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(outdir, f"figure1.{ext}"))
    plt.close(fig)
    with pd.ExcelWriter(os.path.join(outdir, "figure1_source_data.xlsx")) as xw:
        tb.to_excel(xw, sheet_name="1b_numbers", index=False)
        M.to_excel(xw, sheet_name="1c_programs_x_states")
        C.to_excel(xw, sheet_name="1d_program_signature_r")
        e.to_excel(xw, sheet_name="1e_fgfr2_flows")
        f.to_excel(xw, sheet_name="1f_causal_replication")
    log.info("Figure 1 written")


# ================================================================ Figure 2
def f2a_weights(ax, D, n=8):
    w = D["weights"].sort_values()
    sel = pd.concat([w.head(n), w.tail(n)])
    y = np.r_[np.arange(n), np.arange(n) + n + 1]
    ax.barh(y, 1000 * sel.values, color=[ADV if v > 0 else PROT for v in sel], height=0.7)
    ax.axvline(0, color=Q.AXIS, lw=0.4)
    ax.set_yticks(y)
    ax.set_yticklabels([plab(D, k) for k in sel.index], fontsize=4.5)
    for t, v in zip(ax.get_yticklabels(), sel.values):
        t.set_color(ADV if v > 0 else PROT)
    ax.text(0, n, f"… {len(w) - 2 * n} programs with smaller weights …", ha="center", va="center", fontsize=4.5,
            color=Q.MUTED)
    ax.set_ylim(-0.7, 2 * n + 0.7)
    ax.set_xlabel("ridge weight ×10³ (FU-iCCA, OS)\n← protective   adverse →")
    despine(ax)
    ax.set_title(f"Largest of {len(w)} program weights", loc="right")
    return w


def f2b_classes(fig, sub, D):
    risk = D["risk"]
    panels = [(cl, D["ntp"][cl], lv, PN.class_title(cl)) for cl, lv in PN.figures["fig2b_panels"] if cl in D["ntp"]]
    gs = gridspec.GridSpecFromSubplotSpec(1, len(panels), subplot_spec=sub, wspace=0.12,
                                          width_ratios=[max(3, len(lv)) for _, _, lv, _ in panels])
    rng = np.random.default_rng(0)
    axes = []
    for j, (cl, lab, levels, name) in enumerate(panels):
        ax = fig.add_subplot(gs[j], sharey=axes[0] if axes else None)
        axes.append(ax)
        lab = lab.reindex(risk.index)
        groups = [risk[lab == lv].dropna() for lv in levels]
        for i, g in enumerate(groups):
            col = AXIS_COL.get(PN.class_axis(cl, levels[i]), Q.MUTED)
            ax.scatter(i + rng.uniform(-0.25, 0.25, len(g)), g, s=1.2, color=col, alpha=0.45, lw=0)
            if len(g):
                q1, md, q3 = np.percentile(g, [25, 50, 75])
                ax.plot([i, i], [q1, q3], color=Q.INK, lw=1.2)
                ax.plot([i - 0.28, i + 0.28], [md, md], color=Q.INK, lw=1.0)
        ok = [g for g in groups if len(g) >= 3]
        pk = stats.kruskal(*ok).pvalue if len(ok) >= 2 else np.nan
        ax.set_xticks(range(len(levels)))
        ax.set_xticklabels([PN.class_label(cl, lv) for lv in levels], fontsize=4.4, rotation=45, ha="right",
                           rotation_mode="anchor")
        ax.set_title(f"{name}\nP = {pk:.0e}".replace("e-0", "e-"), fontsize=4.8)
        ax.axhline(0, color=Q.AXIS, lw=0.4)
        despine(ax)
        if j:
            plt.setp(ax.get_yticklabels(), visible=False)
        else:
            ax.set_ylabel("risk score (z)")
    return axes[0]


def f2c_states(fig, sub, D, m07c, P):
    S = D["samples"]
    st = pd.Series({k: D["risk"].reindex(v).mean() for k, v in D["states"].items()})
    s_order = st.sort_values().index.tolist()
    guan = pd.concat([m07c.guan_rank(D["surv"][(c, "OS")]) for c in D["P"]["risk"]["survival_cohorts"]])
    rows, labs = [], []
    for cl, lv in PN.figures["fig2c_rows"]:
        if cl not in D["ntp"]:
            continue
        rows.append(frac_table(D["states"], D["ntp"][cl], [lv]).loc[lv, s_order].values.astype(float))
        labs.append(f"{PN.class_label(cl, lv)} ({class_tag(cl, lv)})")
    G = D["genomic"]
    for m, lab in (("MUT_KRAS", "KRAS mut"), ("FUS_FGFR2", "FGFR2 fusion")):
        rows.append([G.loc[m, [x for x in D["states"][s] if x in G.columns]].mean() for s in s_order])
        labs.append(lab)
    gs = gridspec.GridSpecFromSubplotSpec(3, 2, subplot_spec=sub, height_ratios=[len(rows), 5, 5], hspace=0.1,
                                          width_ratios=[0.2, 1], wspace=0.0)
    ax0 = fig.add_subplot(gs[0, 1])
    im0 = ax0.imshow(np.array(rows), aspect="auto", cmap=FRAC_CMAP, vmin=0, vmax=1, interpolation="none")
    cax = ax0.inset_axes([0.86, 1.04, 0.14, 0.06])
    cb = fig.colorbar(im0, cax=cax, orientation="horizontal", ticks=[0, 0.5, 1])
    cb.ax.xaxis.set_ticks_position("top")
    cb.ax.tick_params(labelsize=4.2, length=1.5, width=0.3, pad=1)
    cb.outline.set_linewidth(0.3)
    ax0.text(0.855, 1.07, "fraction of tumours", transform=ax0.transAxes, fontsize=4.4, ha="right", va="center", color=Q.INK2)
    ax0.set_yticks(range(len(labs)))
    ax0.set_yticklabels(labs, fontsize=4.5)
    ax0.set_xticks([])
    for sp in ax0.spines.values():
        sp.set_linewidth(0.3)
    ax0.set_title("States ordered by mean risk: class composition, predicted risk, observed outcome", loc="left", y=1.02)
    x = np.arange(len(s_order))
    for axi, vals, lab in ((1, D["risk"], "risk score (z)"), (2, guan, "GuanRank (OS)")):
        ax = fig.add_subplot(gs[axi, 1], sharex=ax0)
        data = [vals.reindex(D["states"][s]).dropna() for s in s_order]
        bp = ax.boxplot(data, positions=x, widths=0.55, showfliers=False, patch_artist=True,
                        medianprops=dict(color=Q.INK, lw=0.8), whiskerprops=dict(color=Q.MUTED, lw=0.4),
                        capprops=dict(color=Q.MUTED, lw=0.4), boxprops=dict(lw=0.4))
        med = np.array([np.median(d) if len(d) else np.nan for d in data])
        cmap = plt.get_cmap(Q.DIV)
        for patch, s in zip(bp["boxes"], s_order):
            patch.set_facecolor(cmap(0.5 + np.clip(st[s], -1.2, 1.2) / 2.4))
            patch.set_edgecolor(Q.MUTED)
        ax.set_ylabel(lab, fontsize=5)
        ax.set_xlim(-0.6, len(x) - 0.4)
        despine(ax)
        if axi == 1:
            ax.axhline(0, color=Q.AXIS, lw=0.4)
            plt.setp(ax.get_xticklabels(), visible=False)
        else:
            n = [len(d) for d in data]
            ok = [i for i, k in enumerate(n) if k >= 5]
            rho, pv = stats.spearmanr(st[[s_order[i] for i in ok]], med[ok])
            ax.text(0.01, 0.97, f"state risk vs median GuanRank: ρ = {rho:.2f}, P = {pv:.1e} ({len(ok)} states)",
                    transform=ax.transAxes, fontsize=4.8, va="top")
            ax.set_xticks(x)
            ax.set_xticklabels([f"S{s}" for s in s_order], fontsize=4.2, rotation=90)
    return ax0


def _ev(score, s):
    from lifelines import CoxPHFitter
    from lifelines.utils import concordance_index
    hi = (score >= score.quantile(0.8)).astype(int)
    c = CoxPHFitter().fit(s.assign(high=hi), "duration", "observed").summary.loc["high"]
    return {"c_index": concordance_index(s["duration"], -score, s["observed"]), "hr": c["exp(coef)"], "hr_p": c["p"]}, hi.astype(bool)


def f2d_e_km(fig, sub, D, P):
    res = D["res"]
    gs = gridspec.GridSpecFromSubplotSpec(1, 5, subplot_spec=sub, wspace=0.18)
    panels = []
    for c in ("TCGA", "GSE107943"):
        s = D["surv"][(c, "OS")]
        r = D["pred"].loc[s.index, "risk_score"]
        ev, hi = _ev(r, s)
        panels.append((f"{c.replace('TCGA', 'TCGA-CHOL')} OS", "in network, not in model", s, hi, ev, COH[c]))
    sc = pd.read_csv(os.path.join(res, "08_validation", "GSE244807", "scores.tsv"), sep="\t", index_col=0)
    so = pd.read_csv(os.path.join(res, "08_validation", "OEP002768", "scores.tsv"), sep="\t", index_col=0)
    for name, tab, sub_, keep, col in (("GSE244807", sc, "resected", sc["stratum"] == "Surgical specimen", EXT_COL["GSE244807"]),
                                       ("GSE244807", sc, "biopsies", sc["stratum"] == "Biopsy", EXT_COL["GSE244807"]),
                                       ("OEP002768", so, "unique patients", pd.Series(True, index=so.index), EXT_COL["OEP002768"])):
        s = tab.loc[keep, ["OS_time", "OS_event"]].dropna().set_axis(["duration", "observed"], axis=1)
        over = s["duration"] > 1096
        s.loc[over, "duration"], s.loc[over, "observed"] = 1096, 0
        s = s[s["duration"] > 0]
        r = tab.loc[s.index, f"risk_{D['model']}"]
        ev, hi = _ev(r, s)
        panels.append((f"{name} OS, {sub_}", "held out", s, hi, ev, col))
    axes = []
    for j, (title, sub_, s, high, ev, col) in enumerate(panels):
        ax = fig.add_subplot(gs[j], sharey=axes[0] if axes else None)
        axes.append(ax)
        km(ax, s.loc[high[high].index, "duration"], s.loc[high[high].index, "observed"], ADV, "top 20%")
        km(ax, s.loc[high[~high].index, "duration"], s.loc[high[~high].index, "observed"], PROT, "rest")
        ax.set_ylim(0, 1.03)
        ax.set_xlim(0, 36.5)
        ax.set_xticks([0, 12, 24, 36])
        ax.set_title(f"{title}\n{sub_} (n = {len(s)})", fontsize=5.0, color=col)
        ax.text(0.04, 0.05, f"C = {ev['c_index']:.2f}\nHR = {ev['hr']:.2f}, P = {ev['hr_p']:.0e}".replace("e-0", "e-"),
                transform=ax.transAxes, fontsize=4.6)
        ax.set_xlabel("months")
        despine(ax)
        if j:
            plt.setp(ax.get_yticklabels(), visible=False)
        else:
            ax.set_ylabel("overall survival")
            ax.legend(loc="upper right", fontsize=4.5)
    return axes[0], axes[2]


def f2f_forest(fig, sub, D):
    res = D["res"]
    rows = []
    rs = pd.read_csv(os.path.join(D["rdir"], "risk_summary.tsv"), sep="\t")
    rs = rs[rs["unit"].astype(str) == f"ridge_programs_{D['model']}"].set_index("cohort")
    for c in ("TCGA", "GSE107943"):
        e = rs.loc[c]
        rows.append((f"{c.replace('TCGA', 'TCGA-CHOL')} (in network)", "network", e["hr_per_sd"], e["hr_per_sd_lo"], e["hr_per_sd_hi"], COH[c]))
    V = pd.read_csv(os.path.join(res, "08_validation", "summary.tsv"), sep="\t")
    ext = []
    for _, r in V.iterrows():
        lab = {"all": "all", "Surgical specimen": "resected", "Biopsy": "biopsies"}[r["subset"]]
        rows.append((f"{r['cohort']} {lab}", "external", r["hr_per_sd"], r["hr_per_sd_lo"], r["hr_per_sd_hi"], EXT_COL[r["cohort"]]))
        if (r["cohort"] == "OEP002768") or (r["cohort"] == "GSE244807" and r["subset"] != "all"):
            ext.append((np.log(r["hr_per_sd"]), (np.log(r["hr_per_sd_hi"]) - np.log(r["hr_per_sd_lo"])) / 3.92))
    E = pd.DataFrame(ext, columns=["b", "se"])
    w = 1 / E["se"] ** 2
    q = (w * (E["b"] - (w * E["b"]).sum() / w.sum()) ** 2).sum()
    tau2 = max(0, (q - (len(E) - 1)) / (w.sum() - (w ** 2).sum() / w.sum()))
    wr = 1 / (E["se"] ** 2 + tau2)
    b, se = (wr * E["b"]).sum() / wr.sum(), np.sqrt(1 / wr.sum())
    rows.append(("pooled held-out (RE)", "pooled", np.exp(b), np.exp(b - 1.96 * se), np.exp(b + 1.96 * se), Q.INK))
    g3 = gridspec.GridSpecFromSubplotSpec(1, 3, subplot_spec=sub, width_ratios=[0.62, 1, 0.5], wspace=0.02)
    ax = fig.add_subplot(g3[1])
    axl = fig.add_subplot(g3[0], sharey=ax)
    axn = fig.add_subplot(g3[2], sharey=ax)
    for i, (lab, kind, hr, lo, hi, col) in enumerate(rows):
        ax.plot([lo, hi], [i, i], color=col, lw=0.8)
        ax.scatter(hr, i, marker="D" if kind == "pooled" else "s", s=10 if kind == "pooled" else 6, color=col, zorder=3)
        axn.text(0.05, i, f"{hr:.2f} ({lo:.2f}–{hi:.2f})", fontsize=4.4, va="center")
        axl.text(0.98, i, lab, fontsize=4.7, va="center", ha="right", color=Q.INK)
    ax.axvline(1, color=Q.AXIS, lw=0.4)
    ax.set_xscale("log")
    ax.set_xlim(0.6, 4.6)
    ax.set_xticks([1, 2, 3, 4])
    ax.set_xticklabels(["1", "2", "3", "4"])
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_yticks([])
    ax.set_ylim(len(rows) - 0.5, -0.5)
    for a_ in (axl, axn):
        a_.axis("off")
    for i in range(1, len(rows)):
        if rows[i][1] != rows[i - 1][1]:
            ax.axhline(i - 0.5, color=Q.GRID, lw=0.5)
    ax.set_xlabel("HR per s.d. of risk score")
    despine(ax)
    ax.set_title("HR per s.d., all test cohorts")
    ax.spines["left"].set_visible(False)
    return ax, pd.DataFrame(rows, columns=["cohort", "kind", "hr", "lo", "hi", "color"]).drop(columns="color")


def f2g_benchmark(ax, D):
    """C-index in the held-out cohorts: MINER risk vs published classes (fitted in the test cohort) and signatures
    (oriented in FU-iCCA); step 07g. GSE244807 models are stratified by specimen."""
    H = pd.read_csv(os.path.join(D["res"], "07_post", "published", "head_to_head.tsv"), sep="\t")
    show = {"MINER risk": ("MINER programs", ADV, "D"), "SIA2013_SURVIVAL_POOR": ("Sia 2013 survival", Q.SLOTS[3], "^"),
            "SIA2013_RECURRENCE_POOR": ("Sia 2013 recurrence", Q.SLOTS[3], "v"),
            "DONG2022_PROGNOSTIC_BIOMARKERS": ("Dong 2022 prognostic", Q.SLOTS[5], "P"),
            "FAN2024_CORE37": ("Fan 2024 CORE-37", Q.SLOTS[4], "X"),
            "stim classes (fitted here)": ("STIM classes (fitted)", Q.SLOTS[2], "s"),
            "lin2026 classes (fitted here)": ("Lin 2026 classes (fitted)", Q.SLOTS[2], "s")}
    small = [m for m in H["model"].unique() if m.startswith("ICC_PROGNOSTIC")]
    sets = ["GSE244807", "OEP002768"]
    y = {c: i for i, c in enumerate(sets)}
    for m in small:
        d = H[H["model"] == m]
        ax.scatter(d["c_index"], d["cohort"].map(y) + 0.18, s=6, color=Q.BACKGROUND, marker="o", zorder=2,
                   label="7 small iCCA signatures" if m == small[0] else None)
    for m, (lab, col, mk) in show.items():
        d = H[H["model"] == m]
        if len(d):
            ax.scatter(d["c_index"], d["cohort"].map(y), s=14 if m == "MINER risk" else 10, color=col, marker=mk, label=lab,
                       zorder=3, edgecolor=Q.INK if m == "MINER risk" else "none", linewidth=0.3)
    for i in y.values():
        ax.axhline(i, color=Q.GRID, lw=0.3, zorder=0)
    ax.axvline(0.5, color=Q.AXIS, lw=0.4)
    ax.set_yticks(list(y.values()))
    ax.set_yticklabels([f"{c}\n(n = {int(H[(H['cohort'] == c) & (H['model'] == 'MINER risk')]['n'].iloc[0])})" for c in sets], fontsize=5)
    ax.set_ylim(len(sets) - 0.5, -0.6)
    ax.set_xlim(0.35, 0.78)
    ax.set_xlabel("C-index (overall survival, 36 months)")
    ax.legend(loc="lower left", ncol=2, fontsize=4.0, handletextpad=0.2, borderaxespad=0.2, columnspacing=0.6,
              bbox_to_anchor=(-0.02, 1.01))
    despine(ax)
    add = H[H["model"].isin(["SIA2013_SURVIVAL_POOR", "DONG2022_PROGNOSTIC_BIOMARKERS", "stim classes (fitted here)"])]
    ax.set_title("vs published classes / signatures", pad=36)
    ax.text(0.99, 0.02, f"MINER added to Sia / Dong / STIM: P ≥ {add['p_add_miner'].min():.2f}", transform=ax.transAxes,
            fontsize=4.3, ha="right", va="bottom", color=Q.INK2)
    return H


def f2h_loco(ax, D):
    """Split-half stability (step 08b, ICC): networks built on one half, compared with the full network."""
    f = os.path.join(D["res"], "08_validation", "split", "loco_summary.tsv")
    if not os.path.exists(f):
        ax.axis("off")
        ax.text(0.5, 0.5, "Split-half stability\n(pending)", ha="center", va="center", fontsize=5.5, color=Q.MUTED)
        return None
    S = pd.read_csv(f, sep="\t").set_index("held_out")
    mets = [("regulators_recovered", "regulators recovered"), ("program_median_activity_r", "program activity r"),
            ("risk_programs_median_activity_r", "risk-program activity r"), ("causal_edges_recovered_filtered", "causal edges")]
    x = np.arange(len(mets))
    for j, h in enumerate([h for h in ("A", "B") if h in S.index]):
        ax.bar(x + (j - 0.5) * 0.36, [S.loc[h, m] for m, _ in mets], width=0.34, color=[Q.SLOTS[0], Q.SLOTS[1]][j],
               label=f"half {h} held out")
    ax.set_xticks(x)
    ax.set_xticklabels([l for _, l in mets], fontsize=4.4, rotation=40, ha="right", rotation_mode="anchor")
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("recovered / median r", fontsize=5)
    despine(ax)
    ax.legend(loc="upper left", fontsize=4.3, handlelength=0.8, bbox_to_anchor=(0.0, -0.5), ncol=1)
    txt = [f"half {h}: C {S.loc[h, 'risk_OS_train_FU_iCCA_c_index']:.2f}, HR/SD {S.loc[h, 'risk_OS_train_FU_iCCA_hr_per_sd']:.2f}"
           for h in S.index if "risk_OS_train_FU_iCCA_c_index" in S.columns]
    ax.text(0.0, -0.85, "risk in unseen FU-iCCA half\n(network + model without it):\n" + "\n".join(txt), transform=ax.transAxes,
            fontsize=4.4, va="top", color=Q.INK)
    ax.set_title("Split-half stability", fontsize=6.2)
    return S


def figure2(D, P, outdir, log, m07c):
    fig = plt.figure(figsize=(W, 240 * MM))
    gs = gridspec.GridSpec(4, 1, height_ratios=[50, 62, 42, 62], hspace=0.5, left=0.035, right=0.985, top=0.975,
                           bottom=0.035)
    r1 = gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=gs[0], width_ratios=[1, 1.45], wspace=0.12)
    r1a = gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=r1[0], width_ratios=[0.8, 1], wspace=0.0)
    ax = fig.add_subplot(r1a[1])
    w = f2a_weights(ax, D)
    fig.text(0.005, 0.978, "a", fontsize=8, fontweight="bold", va="bottom")
    r1b = gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=r1[1], width_ratios=[0.08, 1], wspace=0.0)
    axb = f2b_classes(fig, r1b[1], D)
    letter(axb, "b", x=-0.35)
    axc = f2c_states(fig, gs[1], D, m07c, P)
    letter(axc, "c", x=-0.1)
    r3 = gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=gs[2], width_ratios=[0.045, 1], wspace=0.0)
    axd, axe = f2d_e_km(fig, r3[1], D, P)
    letter(axd, "d", x=-0.3)
    r4 = gridspec.GridSpecFromSubplotSpec(1, 3, subplot_spec=gs[3], width_ratios=[1.45, 1.12, 0.78], wspace=0.3)
    axf, fo = f2f_forest(fig, r4[0], D)
    letter(axf, "e", x=-0.6)
    r4g = gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=r4[1], width_ratios=[0.5, 1], wspace=0.0)
    ax = fig.add_subplot(r4g[1])
    H = f2g_benchmark(ax, D)
    letter(ax, "f", x=-0.55)
    r4h = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=r4[2], height_ratios=[1, 0.9], hspace=0.0)
    ax = fig.add_subplot(r4h[0])
    loco = f2h_loco(ax, D)
    letter(ax, "g", x=-0.08, y=1.02)
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(outdir, f"figure2.{ext}"))
    plt.close(fig)
    with pd.ExcelWriter(os.path.join(outdir, "figure2_source_data.xlsx")) as xw:
        w.to_frame("weight").to_excel(xw, sheet_name="2a_weights")
        fo.to_excel(xw, sheet_name="2e_forest", index=False)
        H.to_excel(xw, sheet_name="2f_head_to_head", index=False)
        if loco is not None:
            loco.to_excel(xw, sheet_name="2g_split_half")
    log.info("Figure 2 written")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--params", default=None)
    ap.add_argument("--only", default="1,2")
    args = ap.parse_args()
    P = load_params(args.params)
    outdir = p(os.path.join(P["paths"]["results"], "09_figures"))
    log = setup_logging(outdir, "09_publication_figures")
    D = load_all(P, log)
    m07c = _module("m07c", "07c_figures.py")
    if "1" in args.only:
        figure1(D, P, outdir, log)
    if "2" in args.only:
        figure2(D, P, outdir, log, m07c)


if __name__ == "__main__":
    main()
