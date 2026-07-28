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
    if not f:
        return ""
    return re.sub(r"\s+", " ", f.group(1)).replace(r"\&", "&").strip()

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
        stub=bool(g("item_text")),
        year=bib_field(key, "year"),
    ))

def first_author(a):
    if not a:
        return ""
    first = a.split(" and ")[0]
    return (first.split(",")[0] if "," in first else first.split()[-1]) + " et al."

CLOSED = "no open licence"  # licence checked and settled: no open terms at all
# Stubs: the licence forbids reproducing the item text here, so only metadata is carried.
stubbed = [r for r in rows if r["stub"]]
rest = [r for r in rows if not r["stub"]]
verified = [r for r in rest if r["lic"].startswith("CC")]
closed = [r for r in rest if r["lic"].startswith(CLOSED)]
unverified = [r for r in rest if not r["lic"].startswith(("CC", CLOSED))]

out = ["# NOTICE", "",
       "Attribution and licence position for every reporting guideline reproduced in this",
       "repository. Generated from the guideline files themselves — see `LICENSE` for the",
       "split between this repository's own contribution and the guideline developers' work.",
       "", f"Last generated: {datetime.date.today().isoformat()}. {len(rows)} guidelines.", "",
       "## Item text NOT reproduced here", "",
       "For these the licence forbids reproducing the checklist in this format — chiefly the",
       "**ND (NoDerivatives)** term, which the per-item block structure would breach, or no open",
       "licence at all. Only factual metadata is kept, so routing and cross-references still work.",
       "Get the items from the official source.", "",
       "| Guideline | Source | Licence | Why |", "|---|---|---|---|"] + [
    f"| {r['name']} | {first_author(r['authors'])} {r['journal']} {r['year']}".strip()
    + f" | {r['lic']} | {r['basis'] or chr(8212)} |"
    for r in sorted(stubbed, key=lambda x: x["name"].lower())
] + ["",
       "## Established licences — item text reproduced", "",
       "Reproduced under the stated licence, with attribution as required.", "",
       "| Guideline | Source | Licence | Basis |", "|---|---|---|---|"]
for r in sorted(verified, key=lambda x: x["name"].lower()):
    src = f"{first_author(r['authors'])} {r['journal']} {r['year']}".strip()
    out.append(f"| {r['name']} | {src} | {r['lic']} | {r['basis'] or '—'} |")

out += ["", "## Verified — no open licence", "",
        "The licence position **has** been checked and is settled: these are reproduced under",
        "no open licence at all. Free to read at the source does not mean free to redistribute —",
        "reuse beyond quotation needs the rightsholder's permission.", "",
        "| Guideline | Source | Position |", "|---|---|---|"]
for r in sorted(closed, key=lambda x: x["name"].lower()):
    src = f"{first_author(r['authors'])} {r['journal']} {r['year']}".strip()
    out.append(f"| {r['name']} | {src} | {r['basis'] or r['lic']} |")

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
        "  in the BMJ under CC BY-NC 4.0, so commercial reuse is excluded.",
        "- **Braun & Clarke 15-point checklist** — from a SAGE book, not an open-access",
        "  article. No open licence; reproduced as short factual criteria with full citation.",
        "- **CLAIM 2024** — © Radiological Society of North America. Free to read at PMC, but",
        "  no Creative Commons licence; redistribution needs RSNA permission.",
        "- **STROBE** — the licence comes from the PLoS Medicine co-publication",
        "  (10.1371/journal.pmed.0040296), not from the Lancet DOI recorded in the guideline",
        "  file, which is paywalled. The checklist text is the same in both.",
        "- **TRIPOD** — CC BY-NC-ND, but the metadata does not state whether it is 3.0 or 4.0.",
        "  Both exclude commercial use and derivatives.",
        "- **CHEERS-AI** and **SQUIRE 2.0** — CC BY-NC-ND 4.0 and CC BY-NC 4.0 respectively;",
        "  neither permits commercial redistribution.",
        "- **DECIDE-AI** — the Nature Medicine version of record is paywalled; only a green",
        "  accepted manuscript is openly available, and it carries no CC licence.",
        "- **CARE** — the checklist is free to download from care-statement.org, but neither",
        "  the site nor the J Clin Epidemiol article states an open licence.",
        "- **PRISMA-ScR** and **RIGHT** — free to read at Annals of Internal Medicine with no",
        "  CC licence stated; free access is not a redistribution licence.",
        "- **TIDieR** — bronze OA at the BMJ: readable without payment, but no licence is",
        "  declared, so the terms could not be confirmed from an official source.",
        ""]

(D / "NOTICE").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"NOTICE written — {len(verified)} with established licence, "
      f"{len(closed)} verified with no open licence, {len(unverified)} unverified")
