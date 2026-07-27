# reporting-guidelines

Health-research reporting guidelines (EQUATOR Network) as structured Markdown, built to be
read by AI coding agents and by people.

Each guideline is one file under `guidelines/`, with YAML frontmatter carrying its version,
DOI, and provenance, and one `### Item N` block per checklist item. No tables, no PDFs, no
DOCX — just headings and prose, so items can be grepped, cited by number, and diffed
line-by-line when a guideline is revised.

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
| CONSORT | 2025 | 42 | full item text |
| SPIRIT | 2025 | 53 | full item text |
| STROBE | 2007 | 22 | full item text |
| PRISMA | 2020 | 42 | full item text |
| PRISMA for Abstracts | 2020 | 12 | full item text |
| PRISMA-P | 2015 | 26 | full item text |
| STARD | 2015 | 34 | full item text |
| **TRIPOD+AI** | **2024** | **52** | **full item text — supersedes TRIPOD 2015** |
| TRIPOD | 2015 | 37 | full item text — superseded, kept for appraising older papers |
| AGREE Reporting Checklist | 2016 | 23 | full item text |
| CARE | 2013 | 30 | full item text |
| COREQ | 2007 | 32 | full item text |
| SQUIRE | 2.0 (2015) | 18 | full item text |
| CHEERS | 2022 | 28 | full item text |
| ARRIVE | 2.0 (2020) | 21 | full item text |
| CODE-EHR | 2022 | 8 | full item text |
| RECORD | 2015 | 13 | full item text — extends STROBE |
| RECORD-PE | 2018 | 15 | full item text — extends STROBE + RECORD |
| RIGHT | 2017 | 35 | full item text |
| SRQR | 2014 | 21 | full item text |
| RIGHT-PVG | 2021 | 17 | full item text — extends RIGHT |
| TRIPOD+AI for Abstracts | 2024 | 13 | full item text |
| MOOSE | 2000 | — | metadata only |
| TIDieR | 2014 | — | metadata only |
| GREET | 2016 | — | metadata only |
| Simulation extensions | 2016 | — | metadata only |
| Braun & Clarke (critique) | 2025 | n/a | metadata only |

Every guideline in the original scope is now present with full item text. Remaining gaps
are extension checklists (PRISMA-ScR, PRISMA-DTA, STROBE-MR, CONSORT-AI, ...) and the five
metadata-only files listed in [INVENTORY.md](INVENTORY.md). See [INVENTORY.md](INVENTORY.md).

## Provenance and licensing

Item text was transcribed from the official checklists (DOCX and PDF) published by each
guideline group, or from the checklist table in the source article. Source files are not
redistributed here — every guideline's DOI is in `references.bib`, so the original is
retrievable.

Licences differ per guideline and **most have not been verified**. CHEERS 2022 is
explicitly CC BY 4.0. AGREE materials require registration with the AGREE Research Trust.
Frontmatter records the licence status per file. Verify before reusing any item text
commercially or redistributing it further.

This repository is a working aid, not an authoritative copy. Where a checklist matters —
a submission, a peer review, a compliance statement — go to the official source. If you
find a transcription error, that is a bug worth reporting.

## Maintenance

`last_checked` in each file's frontmatter records when its version was last verified
against the official source. Guidelines are revised without much fanfare; CONSORT went
fifteen years between updates and then changed substantially.
