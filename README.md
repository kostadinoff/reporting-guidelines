# reporting-guidelines

Health-research reporting guidelines (EQUATOR Network) as structured Markdown, built to be
read by AI coding agents and by people.

Each guideline is one file under `guidelines/`, with YAML frontmatter carrying its version,
DOI, and provenance, and one `### Item N` block per checklist item. No tables, no PDFs, no
DOCX — just headings and prose, so items can be grepped, cited by number, and diffed
line-by-line when a guideline is revised.

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
guidelines/          one .md per guideline, per-item blocks
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
| AGREE Reporting Checklist | 2016 | 23 | full item text |
| ARRIVE 2.0 | 2.0 (2020) | 21 | full item text — supersedes ARRIVE (2010) |
| BQQRG | 2025 | 24 | full item text |
| Braun & Clarke 15-point checklist | 2013 | 15 | full item text |
| CARE | 2013 | 13 | full item text |
| CHEERS 2022 | 2022 | 28 | full item text — supersedes CHEERS 2013 |
| CHEERS-AI | 2024 | 10 | **metadata only — licence forbids reproducing items here** |
| CLAIM | 2024 update | 44 | **metadata only — licence forbids reproducing items here** |
| CODE-EHR | 2022 | 8 | full item text |
| CONSORT 2025 | 2025 | 30 | full item text — supersedes CONSORT 2010 |
| CONSORT-AI | 2020 | 14 | full item text — extends consort-2025 |
| CONSORT-Outcomes 2022 | 2022 | 17 | full item text — extends consort-2025 |
| CONSORT-ROUTINE | 2021 | 13 | full item text — extends consort-2025 |
| COREQ | 2007 | 32 | full item text |
| DECIDE-AI | 2022 | 27 | full item text |
| GREET | 2015 checklist (published 2016) | 17 | full item text — extends tidier-2014 |
| MOOSE | 2000 | 34 | full item text |
| PRISMA 2020 | 2020 | 27 | full item text — supersedes PRISMA 2009 |
| PRISMA 2020 for Abstracts | 2020 | 12 | full item text — supersedes PRISMA for Abstracts (2013) |
| PRISMA-DTA | 2018 | 27 | full item text — extends prisma-2020 |
| PRISMA-E 2012 | 2012 | 16 | full item text — extends prisma-2020 |
| PRISMA-LSR | 2024 | 4 | full item text — extends prisma-2020 |
| PRISMA-P | 2015 | 17 | full item text |
| PRISMA-S | 2021 | 16 | full item text — extends prisma-2020 |
| PRISMA-ScR | 2018 | 22 | full item text — extends prisma-2020 |
| RECORD | 2015 | 13 | full item text — extends strobe-2007 |
| RECORD-PE | 2018 | 15 | full item text — extends strobe-2007, record-2015 |
| RIGHT | 2017 | 22 | full item text |
| RIGHT for PVG | 2021 | 17 | full item text — extends right-2017 |
| Simulation-based research extensions | 2016 | 21 | full item text — extends consort-2025, strobe-2007 |
| SPIRIT 2025 | 2025 | 34 | full item text — supersedes SPIRIT 2013 |
| SPIRIT-AI | 2020 | 13 | full item text — extends spirit-2025 |
| SQUIRE 2.0 | 2.0 (2015) | 18 | full item text — supersedes SQUIRE 1.0 |
| SRQR | 2014 | 21 | full item text |
| STARD 2015 | 2015 | 30 | full item text — supersedes STARD 2003 |
| STARD-AI | 2025 | 44 | full item text — extends stard-2015 |
| STROBE | 2007 | 22 | full item text |
| STROBE-MR | 2021 | 20 | full item text — extends strobe-2007 |
| TIDieR | 2014 | 12 | full item text — extends consort-2025, spirit-2025 |
| TRIPOD | 2015 | 22 | **metadata only — licence forbids reproducing items here** |
| TRIPOD+AI | 2024 | 27 | full item text — supersedes TRIPOD 2015 |
| TRIPOD+AI for Abstracts | 2024 | 13 | full item text — extends tripod-ai-2024 |
| TRIPOD-Cluster | 2023 | 19 | full item text — extends tripod-ai-2024 |

Every guideline in the original scope is now present with full item text. Remaining gaps
are extension checklists (PRISMA-ScR, PRISMA-DTA, STROBE-MR, CONSORT-AI, ...) and the five
metadata-only files listed in [INVENTORY.md](INVENTORY.md). See [INVENTORY.md](INVENTORY.md).

## Provenance and licensing

Item text was transcribed from the official checklists (DOCX and PDF) published by each
guideline group, or from the checklist table in the source article. Source files are not
redistributed here — every guideline's DOI is in `references.bib`, so the original is
retrievable.

Licences differ per guideline and every position is recorded. 32 are reproduced under an
established licence — chiefly CC BY 4.0, since the PRISMA, CONSORT and TRIPOD groups each
distribute their checklists and extensions under it. 8 carry no open licence at source and
rest on attribution plus the EQUATOR Network's terms, which permit copying provided notices
are retained. 3 are metadata-only because their licence forbids reproducing the items here.

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
