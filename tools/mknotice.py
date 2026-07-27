#!/usr/bin/env python3
"""Generate NOTICE from the guideline files, so attribution cannot drift from frontmatter."""
import datetime
import pathlib
import re

D = pathlib.Path(__file__).resolve().parent.parent
bib = (D / "references.bib").read_text(encoding="utf-8")

def bib_field(key, field):
    m = re.search(r"@\w+\{" + re.escape(key) + r",(.*?)\n\}", bib, re.S)
    if not m:
        return ""
    f = re.search(field + r"=\{(.*?)\}", m.group(1), re.S)
    return re.sub(r"\s+", " ", f.group(1)).strip() if f else ""

rows = []
for f in sorted((D / "guidelines").glob("*.md")):
    t = f.read_text(encoding="utf-8")
    fm = t.split("---")[1]

    def g(k, default=""):
        m = re.search(rf"^{k}:\s*(.+)$", fm, re.M)
        return m.group(1).strip().strip('"') if m else default

    key = g("citation_key")
    rows.append(dict(
        name=g("name"), file=f.name, doi=g("doi"),
        lic=g("licence"), basis=g("licence_basis"),
        authors=bib_field(key, "author"), journal=bib_field(key, "journal"),
        year=bib_field(key, "year"),
    ))

def first_author(a):
    if not a:
        return ""
    first = a.split(" and ")[0]
    return (first.split(",")[0] if "," in first else first.split()[-1]) + " et al."

verified = [r for r in rows if r["lic"].startswith("CC")]
unverified = [r for r in rows if not r["lic"].startswith("CC")]

out = ["# NOTICE", "",
       "Attribution and licence position for every reporting guideline reproduced in this",
       "repository. Generated from the guideline files themselves — see `LICENSE` for the",
       "split between this repository's own contribution and the guideline developers' work.",
       "", f"Last generated: {datetime.date.today().isoformat()}. {len(rows)} guidelines.", "",
       "## Established licences", "",
       "Reproduced under the stated licence, with attribution as required.", "",
       "| Guideline | Source | Licence | Basis |", "|---|---|---|---|"]
for r in sorted(verified, key=lambda x: x["name"].lower()):
    src = f"{first_author(r['authors'])} {r['journal']} {r['year']}".strip()
    out.append(f"| {r['name']} | {src} | {r['lic']} | {r['basis'] or '—'} |")

out += ["", "## Licence not yet verified", "",
        "Reproduced with full attribution and DOI, but the terms have **not** been confirmed.",
        "Treat as all-rights-reserved until checked at the official source. Guideline",
        "developers who object should open an issue; the entry will be removed or reduced to",
        "metadata and a link.", "",
        "| Guideline | Source | DOI |", "|---|---|---|"]
for r in sorted(unverified, key=lambda x: x["name"].lower()):
    src = f"{first_author(r['authors'])} {r['journal']} {r['year']}".strip()
    out.append(f"| {r['name']} | {src} | {r['doi']} |")

out += ["", "## Known restrictions", "",
        "- **AGREE** — the AGREE Research Trust requires registration for access to AGREE II",
        "  materials. The AGREE Reporting Checklist reproduced here was published open access",
        "  in the BMJ, but confirm terms before further redistribution.",
        "- **Braun & Clarke 15-point checklist** — from a SAGE book, not an open-access",
        "  article. No open licence; reproduced as short factual criteria with full citation.",
        ""]

(D / "NOTICE").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"NOTICE written — {len(verified)} with established licence, {len(unverified)} unverified")
