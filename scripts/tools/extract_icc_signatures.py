#!/usr/bin/env python
"""Extract the iCCA classifier gene sets and published per-sample class labels from the supplements fetched by
scripts/tools/fetch_signature_sources.py (data/papers/<key>/supp/).

    python scripts/tools/extract_icc_signatures.py [--papers data/papers]

Writes
  config/subtype_signatures_custom.tsv   rows of the sets below are replaced, other sets are kept
  config/icc_published_labels.tsv        cohort, sample, gsm, classifier, class, source

Gene sets (all thresholds are the authors' unless marked "ours"):
  SIA2013_PROLIFERATION / _INFLAMMATION   Sia, Gastroenterology 2013, Suppl Table 2 (class signature; the ICC class
                                          column decides the set)
  SIA2013_SURVIVAL_POOR (+ _DN = good)    Suppl Table 13 (survival signature)
  SIA2013_RECURRENCE_POOR (+ _DN = good)  Suppl Table 14 (recurrence signature)
  MARTINSERRANO2023_<class>               STIM classifier, top 100 genes per class (Gut 2023, online Table S5). The
                                          Gut supplement is not reachable; the 500 genes are taken from Lin 2026 Table
                                          S2A, which lists them in five blocks of 100 in the order immune classical,
                                          inflammatory stroma, hepatic stem-like, tumour classical, desert-like. The
                                          order is checked here against FU-iCCA expression and Lin's FU-iCCA STIM calls.
  JOB2020_<signature>                     Job, Hepatology 2020, Table S1: 8 MCP-counter populations, 3 Boers hepatic
                                          stellate cell states and the functional signatures (sets with >= 3 genes)
  DONG2022_S1..S4                         ours: mRNA templates of the proteomic subgroups (Dong, Cancer Cell 2022),
                                          top 100 genes up in each subgroup vs the rest (Welch t, BH q < 0.05) in the
                                          published FU-iCCA mRNA (Table S1C) of the 214 tumours with a subgroup
                                          (Table S5E). The paper publishes no subgroup gene list.
  DONG2022_PROGNOSTIC_BIOMARKERS (+ _DN)  Table S6A: 34 prognostic proteins (HR > 1 up, HR < 1 dn)
  CHAISAINGMONGKOL2017_C1_DRIVERS         Cancer Cell 2017, Table S9: driver genes higher in ICC-C1 (ratio > 1, FDR < 0.05)
  FAN2024_C1_MESENCHYMAL / _C2_METABOLIC  Nat Commun 2024, Suppl Table 6: the 30-gene NTP classifier
  FAN2024_CORE37 (+ _DN)                  Suppl Table 8: genes of the CORE-37 score (C1 = up, C2 = dn)
  FAN2024_LIVER_SPECIFIC / _PANCREAS_SPECIFIC  Suppl Table 4 (normal-tissue contamination markers)
  SONG2022_LARGE_DUCT / _SMALL_DUCT       Nat Commun 2022, Suppl Data 5: S100P+SPP1- (large duct) vs S100P-SPP1+
                                          (small duct) tumour cells; ours: BH q < 0.01, top 100 per side by logFC
  LIN2026_<subgroup>                      Cell Rep Med 2026, Table S5C: NTP template of the five subgroups
  ICC_PROGNOSTIC_<author>                 Lin 2026 Table S2D: seven published iCCA prognostic signatures (unsigned)

Labels: FU-iCCA Dong proteomic subgroups (Table S5E); FU-iCCA calls of nine classifications by Lin 2026 (Table S4D);
STIM classes of GSE244807 and TCGA-CHOL by Beaufrere 2025 (authors' repository csv_labels/); Lin 2026 subgroups of
GSE89749 and OEP002768 (Table S4A); Song 2022 S100P / SPP1 groups of GSE89749 (Suppl Data 4).
"""

import argparse
import os
import re
import sys
import urllib.request

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hcc_common import p  # noqa: E402

PREFIXES = ("SIA2013_", "MARTINSERRANO2023_", "JOB2020_", "DONG2022_", "CHAISAINGMONGKOL2017_", "FAN2024_",
            "SONG2022_", "LIN2026_", "ICC_PROGNOSTIC_")
STIM_ORDER = ["IMMUNE_CLASSICAL", "INFLAMMATORY_STROMA", "HEPATIC_STEM_LIKE", "TUMOUR_CLASSICAL", "DESERT_LIKE"]
STIM_LIN = {"Immune Classical": "IMMUNE_CLASSICAL", "Inflammatory Stroma": "INFLAMMATORY_STROMA",
            "Hepati Stem-like": "HEPATIC_STEM_LIKE", "Tumor Classical": "TUMOUR_CLASSICAL",
            "Desert-like": "DESERT_LIKE"}
STIM_BEAUFRERE = {"Immune_classical": "IMMUNE_CLASSICAL", "Inflammatory_stroma": "INFLAMMATORY_STROMA",
                  "HepaticStem_like": "HEPATIC_STEM_LIKE", "Tumor_classical": "TUMOUR_CLASSICAL",
                  "Desert_like": "DESERT_LIKE"}


def clean_symbol(s):
    s = str(s).strip()
    m = re.match(r"^(sep|mar|dec)-0?(\d+)$", s, re.I)  # Excel date corruption (sep-02 = SEPT2, now SEPTIN2;
    if m:                                               # 07a maps these previous symbols through HGNC)
        return {"sep": "SEPT", "mar": "MARCH", "dec": "DEC"}[m.group(1).lower()] + m.group(2)
    return re.sub(r"^C(\d+)ORF(\d+)$", r"C\1orf\2", s)


def rows(name, ref, up, dn=()):
    up, dn = [clean_symbol(g) for g in up], [clean_symbol(g) for g in dn]
    both = set(up) & set(dn)
    out = [(name, ref, "up", g) for g in dict.fromkeys(up) if g not in both]
    return out + [(name, ref, "dn", g) for g in dict.fromkeys(dn) if g not in both]


def bh(pv):
    pv = np.asarray(pv, float)
    n, o = len(pv), np.argsort(pv)
    q = np.empty(n)
    q[o] = np.minimum.accumulate((pv[o] * n / np.arange(1, n + 1))[::-1])[::-1]
    return np.minimum(q, 1)


# ---------------------------------------------------------------- per paper
def sia2013(d):
    import pdfplumber
    ref = "Sia 2013 Gastroenterology 144:829 Suppl"
    rx = re.compile(r"^(\S+)\s+(.*?)\s*(Proliferation|Inflammation|Poor|Good)\s+(-?[\d.]+)(?:\s+([\d.]+|#N/A))?$")
    found = {"T2": [], "T13": [], "T14": []}
    with pdfplumber.open(os.path.join(d, "sia2013/supp/mmc1.pdf")) as pdf:
        tab = None
        for page in pdf.pages:
            for line in (page.extract_text() or "").splitlines():
                line = line.strip()
                m = re.match(r"^Supplementary [Tt]able (\d+)", line)
                if m:
                    tab = {"2": "T2", "13": "T13", "14": "T14"}.get(m.group(1))
                    continue
                m = rx.match(line)
                if tab and m:
                    sym, title = m.group(1), m.group(2)
                    t = re.match(r"^([A-Za-z0-9.\-]+):", title)  # symbol cut by the column width: take it from the title
                    if t and t.group(1).upper().startswith(sym.upper()):
                        sym = t.group(1)
                    found[tab].append((sym, m.group(3)))
    c = {k: pd.DataFrame(v, columns=["g", "c"]) for k, v in found.items()}
    for k, v in c.items():
        print(f"  Sia {k}: {v.c.value_counts().to_dict()}")
    assert len(c["T2"]) > 1500 and len(c["T13"]) > 500 and len(c["T14"]) > 300, "Sia tables not parsed"
    t2 = c["T2"]
    out = rows("SIA2013_PROLIFERATION", f"{ref} Table 2 (class signature)", t2.g[t2.c == "Proliferation"])
    out += rows("SIA2013_INFLAMMATION", f"{ref} Table 2 (class signature)", t2.g[t2.c == "Inflammation"])
    for k, name in (("T13", "SIA2013_SURVIVAL_POOR"), ("T14", "SIA2013_RECURRENCE_POOR")):
        t = c[k]
        out += rows(name, f"{ref} Table {k[1:]} (Poor = up, Good = dn)", t.g[t.c == "Poor"], t.g[t.c == "Good"])
    return out


def job2020(d):
    import docx
    ref = "Job 2020 Hepatology 72:965 Table S1"
    doc = docx.Document(os.path.join(d, "job2020/supp/HEP-72-965-s003.docx"))
    rec = []
    for t in doc.tables[:12]:                      # Table S1 is split over 12 Word tables
        for r in t.rows:
            c = [x.text.strip() for x in r.cells]
            if c[0] != "Signature type" and len(c) >= 3:
                rec += [(c[0], c[1], g.strip()) for g in c[2].split(";") if g.strip()]
    t = pd.DataFrame(rec, columns=["type", "sig", "g"])
    core = {"Lymphoid", "NK_or_T", "T_adaptative", "Cytotoxic", "B_derived", "Myeloid", "Monocyte_derived",
            "Fibroblast", "HSCquiescent", "HSCactivated", "Myofibroblast", "proinflammation", "checkpoint", "Complement"}
    assert core <= set(t.sig), f"Job: missing {core - set(t.sig)}"
    out = []
    for sig, g in t.groupby("sig", sort=False):
        if len(g) < 3:
            continue
        name = "JOB2020_" + re.sub(r"[^A-Z0-9]+", "_", sig.upper()).strip("_")
        tag = "14 TME classification signatures" if sig in core else "functional signature"
        out += rows(name, f"{ref} ({g.type.iloc[0]}; {tag})", g.g)
    print(f"  Job: {t.sig.nunique()} signatures, {len(t)} rows; core 14 present")
    return out


def fu_mrna(d):
    m = pd.read_excel(os.path.join(d, "dong2022/supp/mmc2.xlsx"), "S1C. mRNA expression", header=None)
    ids = [str(int(float(x))) for x in m.iloc[1, 1:]]
    e = m.iloc[2:].set_index(0)
    e.columns = ids
    e = e.astype(float)
    return e[~e.index.duplicated()]


def dong2022(d, expr):
    ref = "Dong 2022 Cancer Cell 40:70"
    s = pd.read_excel(os.path.join(d, "dong2022/supp/mmc6.xlsx"), "S5E.ssGSEA results", header=None)
    start = s.index[s[0].astype(str).str.startswith("Proteome ssGSEA")][0] + 2
    end = s.index[(s.index > start) & s[0].isna()].min()       # block ends at the blank row before the phospho block
    lab = s.iloc[start:end, :2].dropna()
    lab = lab[lab[1].astype(str).str.match(r"^S\d$")]
    lab = pd.Series(lab[1].values, index=[str(int(float(x))) for x in lab[0]])
    counts = lab.value_counts().sort_index().to_dict()
    print(f"  Dong proteomic subgroups (Table S5E): {counts}")
    assert counts == {"S1": 41, "S2": 60, "S3": 46, "S4": 67}, "Dong subgroup counts differ from the paper"
    x = expr[[c for c in lab.index if c in expr.columns]]
    x = x[(x > 1).mean(axis=1) >= 0.2]             # ours: expressed (log2 TPM+1 > 1) in >= 20% of tumours
    full, lab = lab, lab[x.columns]
    names = {"S1": "INFLAMMATION", "S2": "INTERSTITIAL", "S3": "METABOLISM", "S4": "DIFFERENTIATION"}
    out = []
    for k in sorted(names):
        a, b = x.loc[:, lab == k], x.loc[:, lab != k]
        t, pv = stats.ttest_ind(a, b, axis=1, equal_var=False)
        r = pd.DataFrame({"t": t, "q": bh(pv)}, index=x.index)
        top = r[(r.q < 0.05) & (r.t > 0)].sort_values("t", ascending=False).head(100).index
        out += rows(f"DONG2022_{k}_{names[k]}", f"{ref}: ours, top 100 up vs other subgroups in FU-iCCA mRNA "
                    f"(Table S1C) by proteomic subgroup (Table S5E; n = {(lab == k).sum()})", top)
    b = pd.read_excel(os.path.join(d, "dong2022/supp/mmc7.xlsx"), "S6A. Biomarker analysis", header=1)
    hr = b["Hazard ratio (HR)"].astype(float)
    out += rows("DONG2022_PROGNOSTIC_BIOMARKERS", f"{ref} Table S6A (protein HR > 1 up, < 1 dn)",
                b.Gene[hr > 1], b.Gene[hr < 1])
    return out, full


def martin_serrano2023(d, expr):
    s = pd.read_excel(os.path.join(d, "lin2026/supp/mmc3.xlsx"), "Table S2A", header=None)
    col = [c for c in s.columns if str(s.iloc[0, c]).startswith("Martin-Serrano")][0]
    genes = s[col].iloc[5:].dropna().astype(str).str.strip().tolist()
    assert len(genes) == 500, f"STIM: expected 500 genes, found {len(genes)}"
    # check the block order: each block's genes should peak in that class in Lin's FU-iCCA STIM calls
    lab = pd.read_excel(os.path.join(d, "lin2026/supp/mmc5.xlsx"), "Table S4D")
    lab = lab.set_index(lab.Patient_ID.astype(str))["Martin-Serrano et al."].map(STIM_LIN).dropna()
    x = expr[[c for c in lab.index if c in expr.columns]]
    x = x.sub(x.mean(axis=1), axis=0)
    means = pd.DataFrame({k: x.loc[:, lab[x.columns] == k].mean(axis=1) for k in STIM_ORDER})
    out = []
    for i, cls in enumerate(STIM_ORDER):
        block = [g for g in genes[i * 100:(i + 1) * 100]]
        peak = means.reindex(block).dropna().idxmax(axis=1)
        frac = (peak == cls).mean()
        print(f"  STIM block {i + 1} ({cls}): {len(peak)} genes in FU-iCCA, {frac:.0%} peak in that class")
        assert frac >= 0.5, f"STIM block {i + 1} does not match {cls}"
        out += rows(f"MARTINSERRANO2023_{cls}", "Martin-Serrano 2023 Gut 72:736 STIM classifier (top 100 per class; "
                    f"gene list from Lin 2026 Table S2A, block {i + 1}; {frac:.0%} of FU-iCCA genes peak in this class)",
                    block)
    return out


def chaisaingmongkol2017(d):
    t = pd.read_excel(os.path.join(d, "chaisaingmongkol2017/supp/mmc10.xlsx"), "Gene list", header=None, skiprows=3)
    t = t[t[0].notna()]
    up = t[(t[5].astype(float) > 1) & (t[6].astype(float) < 0.05)][0]
    print(f"  Chaisaingmongkol C1 drivers: {len(up)} of {len(t)}")
    return rows("CHAISAINGMONGKOL2017_C1_DRIVERS", "Chaisaingmongkol 2017 Cancer Cell 32:57 Table S9 "
                "(ICC C1/C2 ratio > 1, FDR < 0.05)", up)


def fan2024(d):
    f = os.path.join(d, "fan2024/supp/41467_2024_44748_MOESM5_ESM.xlsx")
    ref = "Fan 2024 Nat Commun 15 (s41467-024-44748-8)"
    t6 = pd.read_excel(f, "Supplementary Table 6", header=1)
    c1 = t6[t6.Classifier.str.contains("C1")]["Probe ID"]
    c2 = t6[t6.Classifier.str.contains("C2")]["Probe ID"]
    t8 = pd.read_excel(f, "Supplementary Table 8", header=1)
    t4 = pd.read_excel(f, "Supplementary Table 4", header=1)
    print(f"  Fan classifier C1 {len(c1)} / C2 {len(c2)}; CORE-37 {len(t8)}; liver {t4.iloc[:, 0].notna().sum()}")
    assert len(c1) + len(c2) == 30 and len(t8) == 37
    out = rows("FAN2024_C1_MESENCHYMAL", f"{ref} Suppl Table 6 (30-gene classifier, Mesenchymal & "
               "Immunosuppressive C1)", c1)
    out += rows("FAN2024_C2_METABOLIC", f"{ref} Suppl Table 6 (30-gene classifier, Metabolic & Proliferative C2)", c2)
    out += rows("FAN2024_CORE37", f"{ref} Suppl Table 8 (CORE-37 genes; C1 = up, C2 = dn)",
                t8[t8.iloc[:, 0].str.contains("C1")].iloc[:, 1], t8[t8.iloc[:, 0].str.contains("C2")].iloc[:, 1])
    out += rows("FAN2024_LIVER_SPECIFIC", f"{ref} Suppl Table 4", t4.iloc[:, 0].dropna())
    out += rows("FAN2024_PANCREAS_SPECIFIC", f"{ref} Suppl Table 4", t4.iloc[:, 1].dropna())
    return out


def song2022(d):
    t = pd.read_excel(os.path.join(d, "song2022/supp/41467_2022_29164_MOESM8_ESM.xlsx"), header=1)
    t["q"] = bh(t["P-value"])
    t = t[t.q < 0.01]
    large = t[t.logFC > 0].sort_values("logFC", ascending=False).head(100).Gene
    small = t[t.logFC < 0].sort_values("logFC").head(100).Gene
    ref = "Song 2022 Nat Commun 13:1642 Suppl Data 5 (tumour cells; ours: BH q < 0.01, top 100 by logFC)"
    assert "S100P" in set(large) and "SPP1" in set(small)
    return (rows("SONG2022_LARGE_DUCT", f"{ref}; S100P+SPP1- perihilar large duct", large)
            + rows("SONG2022_SMALL_DUCT", f"{ref}; S100P-SPP1+ peripheral small duct", small))


def lin2026(d):
    f = os.path.join(d, "lin2026/supp/mmc6.xlsx")
    t = pd.read_excel(f, "Table S5C")
    out = []
    for k, g in t.groupby("Subgourp"):
        out += rows("LIN2026_" + k.replace("-", "_"), "Lin 2026 Cell Rep Med Table S5C (NTP template)", g.Symbol)
    print(f"  Lin subgroups: {t.Subgourp.value_counts().to_dict()}")
    s = pd.read_excel(os.path.join(d, "lin2026/supp/mmc3.xlsx"), "Table S2D", header=None)
    for c in range(0, s.shape[1], 2):
        author = re.sub(r"[^A-Z]+", "_", str(s.iloc[0, c]).upper().replace(" ET AL.", "")).strip("_")
        doi = str(s.iloc[2, c]).strip()
        genes = s[c].iloc[4:].dropna().astype(str)
        out += rows(f"ICC_PROGNOSTIC_{author}", f"iCCA prognostic signature {doi} via Lin 2026 Table S2D (unsigned)",
                    genes)
    return out


# ---------------------------------------------------------------- labels
def geo_titles(acc):
    url = f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={acc}&targ=gsm&form=text&view=brief"
    try:
        txt = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "icc-miner3"}),
                                     timeout=120).read().decode()
    except Exception as e:  # noqa: BLE001
        print(f"  GEO {acc}: {e}; GSM column left empty")
        return {}
    gsm = re.findall(r"^\^SAMPLE = (\S+)", txt, re.M)
    title = re.findall(r"^!Sample_title = (.+)$", txt, re.M)
    return dict(zip([t.strip() for t in title], gsm))


def labels(d, dong_lab):
    rec = [("FU_iCCA", s, "", "dong2022_proteomic", c, "Dong 2022 Table S5E") for s, c in dong_lab.items()]
    lin = pd.read_excel(os.path.join(d, "lin2026/supp/mmc5.xlsx"), "Table S4D")
    names = {"Heterogeneity subgroups": "lin2026", "Andersen et al.": "andersen2012", "Oishi et al.": "oishi2012",
             "Sia et al.": "sia2013", "Dong et al.": "dong2022_rna", "Nakamura et al.": "nakamura2015",
             "Protein": "dong2022_proteomic_lin", "Lin J et al.": "linj2022_immune", "Job et al.": "job2020",
             "Martin-Serrano et al.": "stim"}
    for col, cl in names.items():
        v = lin[col].map(STIM_LIN).fillna(lin[col]) if cl == "stim" else lin[col]
        rec += [("FU_iCCA", str(s), "", cl, c, "Lin 2026 Table S4D (Lin's calls)")
                for s, c in zip(lin.Patient_ID, v) if pd.notna(c)]
    repo = os.path.join(d, "beaufrere2025/supp")
    ck = pd.read_csv(os.path.join(repo, "heptastem_testsplit.csv"))
    ck["pat"] = ck.ID.str.extract(r"^(CK\d+)")[0]
    ck["cls"] = ck[list(STIM_BEAUFRERE)].idxmax(axis=1).map(STIM_BEAUFRERE)
    assert ck.groupby("pat").cls.nunique().max() == 1, "Beaufrere: slides of one patient disagree"
    ck = ck.drop_duplicates("pat")
    gsm = geo_titles("GSE244807")
    rec += [("GSE244807", r.pat, gsm.get(r.pat, ""), "stim", r.cls, "Beaufrere 2025 (trislaz/ICCA_prediction labels)")
            for r in ck.itertuples()]
    print(f"  Beaufrere GSE244807 STIM: {ck.cls.value_counts().to_dict()}")
    tc = pd.read_csv(os.path.join(repo, "TCGA_chol_final_transcripto_hemstem.csv"))
    tc["cls"] = tc[list(STIM_BEAUFRERE)].idxmax(axis=1).map(STIM_BEAUFRERE)
    rec += [("TCGA_CHOL", i[:15], "", "stim", c, "Beaufrere 2025 (trislaz/ICCA_prediction labels)")
            for i, c in zip(tc.ID, tc.cls)]
    a = pd.read_excel(os.path.join(d, "lin2026/supp/mmc5.xlsx"), "Table S4A", header=None)
    for name, sc, cc in (("GSE89749", 8, 9), ("OEP002768", 5, 7)):
        v = a.iloc[2:, [sc, cc]].dropna()
        rec += [(name, str(s), str(s) if name == "GSE89749" else "", "lin2026", c, "Lin 2026 Table S4A")
                for s, c in v.values]
    song = pd.read_excel(os.path.join(d, "song2022/supp/41467_2022_29164_MOESM7_ESM.xlsx"),
                         "1.Jusakul et al.’s dataset")
    gsm = geo_titles("GSE89749")
    rec += [("GSE89749", r.Sample, gsm.get(r.Sample, ""), "song2022_duct", r.Group,
             f"Song 2022 Suppl Data 4 (site: {r.Subtype})") for r in song.itertuples()]
    out = pd.DataFrame(rec, columns=["cohort", "sample", "gsm", "classifier", "class", "source"])
    # Lin's proteomic calls vs Dong's own
    lp = out[out.classifier == "dong2022_proteomic_lin"].set_index("sample")["class"]
    dp = dong_lab.reindex(lp.index).dropna()
    print("  Dong proteomic subgroup vs Lin's 'Protein' call (FU-iCCA):")
    print("   " + pd.crosstab(dp, lp[dp.index]).to_string().replace("\n", "\n   "))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--papers", default="data/papers")
    ap.add_argument("--custom", default="config/subtype_signatures_custom.tsv")
    ap.add_argument("--labels", default="config/icc_published_labels.tsv")
    a = ap.parse_args()
    d = p(a.papers)
    expr = fu_mrna(d)
    print(f"FU-iCCA mRNA (Dong Table S1C): {expr.shape}")
    new = sia2013(d) + job2020(d) + martin_serrano2023(d, expr) + chaisaingmongkol2017(d) + fan2024(d) \
        + song2022(d) + lin2026(d)
    dong_rows, dong_lab = dong2022(d, expr)
    new += dong_rows
    new = pd.DataFrame(new, columns=["set", "reference", "direction", "gene_symbol"])
    print(new.groupby(["set", "direction"]).size().to_string())

    path = p(a.custom)
    comments = [line for line in open(path).read().splitlines() if line.startswith("#")]
    body = pd.read_csv(path, sep="\t", comment="#", dtype=str)
    body = body[~body["set"].fillna("").str.startswith(PREFIXES)]
    body = pd.concat([body, new])
    with open(path, "w") as fh:
        fh.write("\n".join(comments) + "\n")
        body.to_csv(fh, sep="\t", index=False)
    print(f"wrote {len(new)} iCCA rows ({new.set.nunique()} sets) to {a.custom} ({len(body)} rows total)")

    lab = labels(d, dong_lab)
    lab.to_csv(p(a.labels), sep="\t", index=False)
    print(f"wrote {len(lab)} labels to {a.labels}:")
    print(lab.groupby(["cohort", "classifier"]).size().to_string())


if __name__ == "__main__":
    main()
