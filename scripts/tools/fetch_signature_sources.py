#!/usr/bin/env python
"""Download the supplementary files of the classifier papers in config/signature_sources.yaml and inventory them.

    python scripts/tools/fetch_signature_sources.py                  # all papers
    python scripts/tools/fetch_signature_sources.py --only sia2013 job2020
    python scripts/tools/fetch_signature_sources.py --inventory-only # re-inventory files already on disk

Per paper:
  1. identifiers: NCBI ID converter (DOI / PMID -> PMCID, PMID, DOI); title, journal and year from Europe PMC are
     logged so a wrong identifier is visible.
  2. supplements, first route that gives files:
       a. Europe PMC supplementaryFiles (zip of every supplementary file of a PMC article)
       b. links to /bin/ files on the PMC article page
       c. Elsevier (DOI 10.1016/...): PII from Crossref, then ars.els-cdn.com ...-mmc<N>.<ext>
     Files land in data/papers/<key>/supp/. Anything placed by hand in data/papers/<key>/manual/ is inventoried too,
     as are the folders listed under also_inventory (e.g. the FU-iCCA tables already on the server).
  3. inventory: every spreadsheet sheet (size, first rows, columns that look like gene symbols), text tables,
     Word tables and PDF pages that mention tables -> docs/signature_sources_inventory.md (small, committed: it
     describes published supplements, not project data) and data/papers/fetch.log.

Needs internet access (login node). pdfplumber is optional (PDF inventory); openpyxl / xlrd for spreadsheets.
"""

import argparse
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

import pandas as pd
import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hcc_common import p, setup_logging  # noqa: E402

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) icc-miner3-fetch/1.0"}
IDCONV = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
ELS_EXT = ("xlsx", "xls", "pdf", "docx", "doc", "zip", "csv", "txt")
GENE_RE = re.compile(r"^[A-Z][A-Z0-9]{1,7}(-[A-Z0-9]{1,4})?$|^C\d{1,2}orf\d{1,3}$")

log = None


# ---------------------------------------------------------------- http
def fetch_bytes(url, retries=3, accept_404=True):
    err = None
    for i in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180) as r:
                return r.read(), r.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            if e.code in (403, 404, 410) and accept_404:
                return None, str(e.code)
            err = e
        except Exception as e:  # noqa: BLE001
            err = e
        time.sleep(2 ** (i + 1))
    log.warning("failed %s: %s", url, err)
    return None, str(err)


def fetch_json(url):
    b, _ = fetch_bytes(url)
    try:
        return json.loads(b) if b else None
    except ValueError:
        return None


def save(dest, data):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as fh:
        fh.write(data)
    log.info("  saved %s (%.1f kB)", os.path.relpath(dest, p(".")), len(data) / 1e3)


# ---------------------------------------------------------------- identifiers
def resolve(spec):
    ids = {k: str(spec[k]) for k in ("doi", "pmid", "pmcid") if spec.get(k)}
    for q in [ids.get("pmcid"), ids.get("pmid"), ids.get("doi")]:
        if not q:
            continue
        j = fetch_json(f"{IDCONV}?{urllib.parse.urlencode({'ids': q, 'format': 'json', 'tool': 'icc-miner3'})}")
        rec = (j or {}).get("records", [{}])[0]
        if rec and "errmsg" not in rec:
            for k in ("doi", "pmid", "pmcid"):
                if rec.get(k) and k not in ids:
                    ids[k] = str(rec[k])
            break
    q = f"EXT_ID:{ids['pmid']}" if ids.get("pmid") else f"DOI:\"{ids.get('doi', '')}\""
    j = fetch_json(f"{EPMC}/search?{urllib.parse.urlencode({'query': q, 'format': 'json', 'resultType': 'lite'})}")
    hits = (j or {}).get("resultList", {}).get("result", [])
    if hits:
        h = hits[0]
        ids.setdefault("pmcid", h.get("pmcid"))
        ids.setdefault("doi", h.get("doi"))
        ids["title"] = f"{h.get('title')} {h.get('journalTitle')} {h.get('pubYear')}"
    return {k: v for k, v in ids.items() if v}


# ---------------------------------------------------------------- supplementary routes
def route_epmc_zip(ids, out):
    if not ids.get("pmcid"):
        return 0
    b, ctype = fetch_bytes(f"{EPMC}/{ids['pmcid']}/supplementaryFiles")
    if not b or not b.startswith(b"PK"):
        log.info("  Europe PMC supplementaryFiles: none (%s)", ctype)
        return 0
    n = 0
    with zipfile.ZipFile(io.BytesIO(b)) as z:
        for name in z.namelist():
            if name.endswith("/"):
                continue
            save(os.path.join(out, os.path.basename(name)), z.read(name))
            n += 1
    return n


def route_pmc_page(ids, out):
    if not ids.get("pmcid"):
        return 0
    n = 0
    for base in (f"https://pmc.ncbi.nlm.nih.gov/articles/{ids['pmcid']}/",
                 f"https://www.ncbi.nlm.nih.gov/pmc/articles/{ids['pmcid']}/"):
        b, _ = fetch_bytes(base)
        if not b:
            continue
        hrefs = set(re.findall(r'href="([^"]+/bin/[^"]+)"', b.decode("utf-8", "replace")))
        for h in sorted(hrefs):
            url = urllib.parse.urljoin(base, h)
            d, _ = fetch_bytes(url)
            if d:
                save(os.path.join(out, os.path.basename(urllib.parse.urlparse(url).path)), d)
                n += 1
        if n:
            break
    return n


def route_elsevier(ids, out, max_mmc):
    doi = ids.get("doi", "")
    if not doi.startswith("10.1016/"):
        return 0
    j = fetch_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
    alt = ((j or {}).get("message") or {}).get("alternative-id", [])
    pii = next((re.sub(r"[^A-Z0-9]", "", a.upper()) for a in alt if re.match(r"^S?\d{4}-?\d{3}[\dX]", a, re.I)), None)
    if not pii:
        log.info("  Elsevier: no PII from Crossref (%s)", alt)
        return 0
    log.info("  Elsevier PII %s", pii)
    n = 0
    for k in range(1, max_mmc + 1):
        for ext in ELS_EXT:
            url = f"https://ars.els-cdn.com/content/image/1-s2.0-{pii}-mmc{k}.{ext}"
            d, _ = fetch_bytes(url, retries=1)
            if d and not d[:200].lstrip().lower().startswith(b"<!doctype html"):
                save(os.path.join(out, f"mmc{k}.{ext}"), d)
                n += 1
                break
    return n


# ---------------------------------------------------------------- inventory
def gene_like_columns(df):
    out = []
    for c in df.columns:
        v = df[c].dropna().astype(str).str.strip()
        if len(v) >= 5:
            frac = v.map(lambda s: bool(GENE_RE.match(s))).mean()
            if frac >= 0.6:
                out.append(f"col {c} ({frac:.0%} of {len(v)})")
    return out


def show_rows(df, nrows, ncols=14, width=28):
    lines = []
    for _, r in df.head(nrows).iterrows():
        cells = ["" if pd.isna(x) else str(x).replace("\n", " ")[:width] for x in list(r.values)[:ncols]]
        lines.append("| " + " | ".join(cells) + (" | ..." if df.shape[1] > ncols else ""))
    return lines


def inv_spreadsheet(path, nrows):
    lines = []
    x = pd.ExcelFile(path)
    for s in x.sheet_names:
        df = x.parse(s, header=None, dtype=object)
        df = df.dropna(how="all").dropna(axis=1, how="all")
        lines.append(f"- sheet `{s}`: {df.shape[0]} rows x {df.shape[1]} cols")
        g = gene_like_columns(df)
        if g:
            lines.append(f"  - gene-symbol-like: {', '.join(g)}")
        lines += ["  " + l for l in show_rows(df, nrows)]
    return lines


def inv_text(path, nrows):
    sep = "," if path.lower().endswith(".csv") else "\t"
    df = pd.read_csv(path, sep=sep, header=None, dtype=object, on_bad_lines="skip", engine="python")
    lines = [f"- {df.shape[0]} rows x {df.shape[1]} cols"]
    g = gene_like_columns(df)
    if g:
        lines.append(f"  - gene-symbol-like: {', '.join(g)}")
    return lines + ["  " + l for l in show_rows(df, nrows)]


def inv_docx(path, nrows):
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8", "replace")
    lines = []
    tables = re.findall(r"<w:tbl>.*?</w:tbl>", xml, flags=re.S)
    paras = [re.sub(r"<[^>]+>", "", t) for t in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S)]
    heads = [t for t in paras if re.search(r"\b(Supplementa\w*|Table)\s*S?\d", t)][:40]
    lines.append(f"- {len(tables)} tables; captions: " + " / ".join(h[:90] for h in heads))
    for i, t in enumerate(tables):
        rows = re.findall(r"<w:tr[ >].*?</w:tr>", t, flags=re.S)
        lines.append(f"  - table {i + 1}: {len(rows)} rows")
        for r in rows[:nrows]:
            cells = [re.sub(r"<[^>]+>", "", c)[:28] for c in re.findall(r"<w:tc>.*?</w:tc>", r, flags=re.S)]
            lines.append("    | " + " | ".join(cells[:14]))
    return lines


def inv_pdf(path, nrows):
    try:
        import pdfplumber
    except ImportError:
        return ["- PDF (install pdfplumber to inventory)"]
    lines = []
    with pdfplumber.open(path) as pdf:
        lines.append(f"- {len(pdf.pages)} pages")
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            caps = [l for l in text.splitlines() if re.search(r"(Supplementa\w*\s+)?Table\s*S?\d", l)]
            genes = sum(1 for w in re.findall(r"\b[A-Z][A-Z0-9-]{1,10}\b", text) if GENE_RE.match(w))
            if caps or genes >= 40:
                lines.append(f"  - p{i + 1}: {genes} gene-like tokens; " + " / ".join(c[:100] for c in caps[:4]))
                if genes >= 40:
                    lines += ["    " + l[:140] for l in text.splitlines()[:nrows]]
    return lines


def inventory(key, spec, ids, folder, nrows):
    lines = [f"## {key}", "", f"{spec.get('citation', '')}", "",
             f"- identifiers: {json.dumps({k: v for k, v in ids.items() if k != 'title'})}",
             f"- resolved title: {ids.get('title', 'NOT RESOLVED')}",
             f"- want: {' '.join(str(spec.get('want', '')).split())}", ""]
    files = []
    dirs = [os.path.join(folder, "supp"), os.path.join(folder, "manual")]
    dirs += [p(x) for x in spec.get("also_inventory", [])]
    for d in dirs:
        if os.path.isdir(d):
            files += [os.path.join(d, f) for f in sorted(os.listdir(d)) if not f.startswith(".")]
    if not files:
        lines += ["**No files.** Download the supplement by hand into "
                  f"`data/papers/{key}/manual/` and re-run with --inventory-only.", ""]
    for f in files:
        low = f.lower()
        lines.append(f"### {os.path.relpath(f, p('.'))} ({os.path.getsize(f) / 1e3:.0f} kB)")
        try:
            if low.endswith((".xlsx", ".xls", ".xlsm")):
                lines += inv_spreadsheet(f, nrows)
            elif low.endswith((".csv", ".tsv", ".txt")):
                lines += inv_text(f, nrows)
            elif low.endswith(".docx"):
                lines += inv_docx(f, nrows)
            elif low.endswith(".pdf"):
                lines += inv_pdf(f, nrows)
            else:
                lines.append("- not inventoried (type)")
        except Exception as e:  # noqa: BLE001
            lines.append(f"- unreadable: {e}")
        lines.append("")
    return lines


def main():
    global log
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default="config/signature_sources.yaml")
    ap.add_argument("--only", nargs="+")
    ap.add_argument("--inventory-only", action="store_true")
    ap.add_argument("--rows", type=int, default=8, help="rows shown per sheet / table")
    ap.add_argument("--max-mmc", type=int, default=12, help="Elsevier mmc files to try")
    ap.add_argument("--out", default="docs/signature_sources_inventory.md")
    a = ap.parse_args()

    root = p("data/papers")
    log = setup_logging(root, "fetch")
    cfg = yaml.safe_load(open(p(a.config)))["papers"]
    keys = a.only or list(cfg)
    doc = ["# Supplementary files of the iCCA classifier papers", "",
           "Written by `scripts/tools/fetch_signature_sources.py` from `config/signature_sources.yaml`. "
           "Describes the published supplements (sheet names, sizes, first rows) so that extraction scripts can be "
           "written; files themselves stay in `data/papers/`.", ""]
    head, summary = len(doc), []
    for key in keys:
        spec, folder = cfg[key], os.path.join(root, key)
        log.info("== %s", key)
        ids = resolve(spec)
        log.info("  ids %s", ids)
        n, how = 0, "inventory-only"
        if not a.inventory_only:
            supp = os.path.join(folder, "supp")
            for how, fn in (("europepmc_zip", lambda: route_epmc_zip(ids, supp)),
                            ("pmc_page", lambda: route_pmc_page(ids, supp)),
                            ("elsevier_mmc", lambda: route_elsevier(ids, supp, a.max_mmc))):
                n = fn()
                if n:
                    break
            else:
                how = "none"
            log.info("  %d files via %s", n, how)
        summary.append(f"| {key} | {spec.get('priority', '')} | {ids.get('pmcid', '')} | {n} | {how} |")
        doc += inventory(key, spec, ids, folder, a.rows)
    doc[head:head] = ["| paper | priority | PMCID | files fetched | route |", "|---|---|---|---|---|"] + summary + [""]
    os.makedirs(os.path.dirname(p(a.out)), exist_ok=True)
    with open(p(a.out), "w") as fh:
        fh.write("\n".join(doc) + "\n")
    log.info("wrote %s", a.out)


if __name__ == "__main__":
    main()
