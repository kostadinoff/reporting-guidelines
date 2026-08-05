# reporting-guidelines

Health-research reporting guidelines (EQUATOR Network) as structured Markdown, built to be
read by AI coding agents and by people.

Each guideline is one file under `guidelines/`, with YAML frontmatter carrying its version,
DOI, and provenance, and one `### Item N` block per checklist item. No PDFs, no DOCX — just
headings and prose, so items can be grepped, cited by number, and diffed line-by-line when a
guideline is revised. One file departs from that: `target-2025.md` carries its checklist as a
table, because a NoDerivatives licence permits reproducing it but not restructuring it.

> **Guideline developers:** if your checklist appears here and you would rather it did not,
> open an issue and it will be removed or reduced to metadata and a link, promptly and
> without argument. Every entry carries attribution, a DOI, and a record of its licence
> position in [NOTICE](NOTICE).

## Why not just link to EQUATOR?

Because an agent asked to "check this manuscript against STROBE" will otherwise invent the
checklist from memory. Item numbers drift between versions, and the most common failure is
producing a confident CONSORT 2010 checklist for a paper that must follow CONSORT 2025.
This repository exists so the item text comes from a file, not from a language model's
recollection.

## Layout

```
guidelines/          one .md per guideline, per-item blocks (target-2025.md: one table)
references.bib       BibTeX for every guideline, each with an abstract or curated findings
INVENTORY.md         status, versions, update watch-list, what is still missing
```

## Using it

Point an agent at `guidelines/` and ask it to check a manuscript section against a named
file. Each file states in its frontmatter what study design it applies to, so a routing
question ("which guideline applies to a prospective cohort?") is answerable from frontmatter
alone without reading every file.

Grep for an item directly:

```bash
grep -A3 '^### Item 12' guidelines/strobe-2007.md
```

Cite a guideline in a manuscript with the key from `references.bib`, e.g. `[@page2021prisma]`.

## Status at a glance

| Guideline | Version | Items | Status |
|---|---|---|---|
| [AGREE Reporting Checklist](guidelines/agree-2016.md) | 2016 | 23 | full item text |
| [ARRIVE 2.0](guidelines/arrive-2.0.md) | 2.0 (2020) | 21 | full item text — supersedes ARRIVE (2010) |
| [BQQRG](guidelines/bqqrg-2025.md) | 2025 | 24 | full item text |
| [Braun & Clarke 15-point checklist](guidelines/braun-clarke-ta-2013.md) | 2013 | 15 | full item text |
| [CARE](guidelines/care-2013.md) | 2013 | 13 | full item text |
| [CHEERS 2022](guidelines/cheers-2022.md) | 2022 | 28 | full item text — supersedes CHEERS 2013 |
| [CHEERS-AI](guidelines/cheers-ai-2024.md) | 2024 | 10 | **metadata only — licence forbids reproducing items here** |
| [CLAIM](guidelines/claim-2024.md) | 2024 update | 44 | **metadata only — licence forbids reproducing items here** |
| [CODE-EHR](guidelines/code-ehr-2022.md) | 2022 | 8 | full item text |
| [CONSORT 2025](guidelines/consort-2025.md) | 2025 | 30 | full item text — supersedes CONSORT 2010 |
| [CONSORT-AI](guidelines/consort-ai-2020.md) | 2020 | 14 | full item text — extends [consort-2025](guidelines/consort-2025.md) |
| [CONSORT-Outcomes 2022](guidelines/consort-outcomes-2022.md) | 2022 | 17 | full item text — extends [consort-2025](guidelines/consort-2025.md) |
| [CONSORT-ROUTINE](guidelines/consort-routine-2021.md) | 2021 | 13 | full item text — extends [consort-2025](guidelines/consort-2025.md) |
| [COREQ](guidelines/coreq-2007.md) | 2007 | 32 | full item text |
| [DECIDE-AI](guidelines/decide-ai-2022.md) | 2022 | 27 | full item text |
| [GREET](guidelines/greet-2016.md) | 2015 checklist (published 2016) | 17 | full item text — extends [tidier-2014](guidelines/tidier-2014.md) |
| [MOOSE](guidelines/moose-2000.md) | 2000 | 34 | full item text |
| [PRISMA 2020](guidelines/prisma-2020.md) | 2020 | 27 | full item text — supersedes PRISMA 2009 |
| [PRISMA 2020 for Abstracts](guidelines/prisma-abstracts-2020.md) | 2020 | 12 | full item text — supersedes PRISMA for Abstracts (2013) |
| [PRISMA-DTA](guidelines/prisma-dta-2018.md) | 2018 | 27 | full item text — extends [prisma-2020](guidelines/prisma-2020.md) |
| [PRISMA-E 2012](guidelines/prisma-e-2012.md) | 2012 | 16 | full item text — extends [prisma-2020](guidelines/prisma-2020.md) |
| [PRISMA-LSR](guidelines/prisma-lsr-2024.md) | 2024 | 4 | full item text — extends [prisma-2020](guidelines/prisma-2020.md) |
| [PRISMA-P](guidelines/prisma-p-2015.md) | 2015 | 17 | full item text |
| [PRISMA-S](guidelines/prisma-s-2021.md) | 2021 | 16 | full item text — extends [prisma-2020](guidelines/prisma-2020.md) |
| [PRISMA-ScR](guidelines/prisma-scr-2018.md) | 2018 | 22 | full item text — extends [prisma-2020](guidelines/prisma-2020.md) |
| [RECORD](guidelines/record-2015.md) | 2015 | 13 | full item text — extends [strobe-2007](guidelines/strobe-2007.md) |
| [RECORD-PE](guidelines/record-pe-2018.md) | 2018 | 15 | full item text — extends [strobe-2007](guidelines/strobe-2007.md), [record-2015](guidelines/record-2015.md) |
| [RIGHT](guidelines/right-2017.md) | 2017 | 22 | full item text |
| [RIGHT for PVG](guidelines/right-pvg-2021.md) | 2021 | 17 | full item text — extends [right-2017](guidelines/right-2017.md) |
| [Simulation-based research extensions](guidelines/simulation-2016.md) | 2016 | 21 | full item text — extends [consort-2025](guidelines/consort-2025.md), [strobe-2007](guidelines/strobe-2007.md) |
| [SPIRIT 2025](guidelines/spirit-2025.md) | 2025 | 34 | full item text — supersedes SPIRIT 2013 |
| [SPIRIT-AI](guidelines/spirit-ai-2020.md) | 2020 | 13 | full item text — extends [spirit-2025](guidelines/spirit-2025.md) |
| [SQUIRE 2.0](guidelines/squire-2.0.md) | 2.0 (2015) | 18 | full item text — supersedes SQUIRE 1.0 |
| [SRQR](guidelines/srqr-2014.md) | 2014 | 21 | full item text |
| [STARD 2015](guidelines/stard-2015.md) | 2015 | 30 | full item text — supersedes STARD 2003 |
| [STARD-AI](guidelines/stard-ai-2025.md) | 2025 | 44 | full item text — extends [stard-2015](guidelines/stard-2015.md) |
| [STROBE](guidelines/strobe-2007.md) | 2007 | 22 | full item text |
| [STROBE-MR](guidelines/strobe-mr-2021.md) | 2021 | 20 | full item text — extends [strobe-2007](guidelines/strobe-2007.md) |
| [TARGET](guidelines/target-2025.md) | 2025 | 21 | full item text as a **verbatim table** (CC BY-ND) — layers on [strobe-2007](guidelines/strobe-2007.md) |
| [TIDieR](guidelines/tidier-2014.md) | 2014 | 12 | full item text — extends [consort-2025](guidelines/consort-2025.md), [spirit-2025](guidelines/spirit-2025.md) |
| [TRIPOD](guidelines/tripod-2015.md) | 2015 | 22 | **metadata only — licence forbids reproducing items here** |
| [TRIPOD+AI](guidelines/tripod-ai-2024.md) | 2024 | 27 | full item text — supersedes TRIPOD 2015 |
| [TRIPOD+AI for Abstracts](guidelines/tripod-ai-abstracts-2024.md) | 2024 | 13 | full item text — extends [tripod-ai-2024](guidelines/tripod-ai-2024.md) |
| [TRIPOD-Cluster](guidelines/tripod-cluster-2023.md) | 2023 | 19 | full item text — extends [tripod-ai-2024](guidelines/tripod-ai-2024.md) |

Every guideline in the original scope is now present with full item text. Remaining gaps
are the extension checklists still to be added and the three metadata-only files listed in
[INVENTORY.md](INVENTORY.md). See [INVENTORY.md](INVENTORY.md).

## Provenance and licensing

Item text was transcribed from the official checklists (DOCX and PDF) published by each
guideline group, or from the checklist table in the source article. Source files are not
redistributed here — every guideline's DOI is in `references.bib`, so the original is
retrievable.

Licences differ per guideline and every position is recorded. 33 are reproduced under an
established licence — chiefly CC BY 4.0, since the PRISMA, CONSORT and TRIPOD groups each
distribute their checklists and extensions under it. 8 carry no open licence at source and
rest on attribution plus the EQUATOR Network's terms, which permit copying provided notices
are retained. 3 are metadata-only because their licence forbids reproducing the items here.

One file, `target-2025.md`, sits between those categories. TARGET is CC BY-**ND**, so the
per-item block structure is not available, but ND permits reproduction in any format — so the
checklist is carried unchanged and in whole as its published table, with the copyright notice,
under `extracted: verbatim-table`. Grep it by item number in the table, not by `### Item N`.

Each file records `licence` and `licence_basis` — what the position is and how it was
determined — so the record is auditable rather than assumed. See [NOTICE](NOTICE) for the
per-guideline detail and for what the EQUATOR terms do and do not grant.

Note that "established" does not mean "unrestricted": several are CC BY-NC or
CC BY-NC-ND, which exclude commercial reuse and, for ND, derivatives. `NOTICE` lists
these under known restrictions.

After changing any guideline file, regenerate the derived documents:

```bash
python3 tools/mknotice.py     # NOTICE — attribution and licence position
python3 tools/mkinventory.py  # INVENTORY status section
```

`LICENSE` separates this repository's own contribution (structure, routing, cross-references,
version warnings, commentary — CC BY 4.0) from the checklist item text, which belongs to the
guideline developers and is reproduced with attribution and a citable DOI in every case.

This repository is a working aid, not an authoritative copy. Where a checklist matters —
a submission, a peer review, a compliance statement — go to the official source. If you
find a transcription error, that is a bug worth reporting.

## Maintenance

`last_checked` in each file's frontmatter records when its version was last verified
against the official source. Guidelines are revised without much fanfare; CONSORT went
fifteen years between updates and then changed substantially.
