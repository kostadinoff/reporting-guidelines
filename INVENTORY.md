# Inventory

Status of every guideline in this repository, what is still missing, and what to watch for
version drift. Last full review: **2026-07-27** (second pass, same day).

Status values:

- **full** — every checklist item transcribed verbatim, item numbers verified against the
  published count
- **metadata** — source identified, citation and DOI recorded in `references.bib`, item
  text not yet transcribed
- **missing** — not in the repository at all

## Present, complete

| Guideline | Version | Items | Verified count | File | Source format |
|---|---|---|---|---|---|
| CONSORT | 2025 | 42 rows | matches published | `guidelines/consort-2025.md` | DOCX |
| SPIRIT | 2025 | 53 rows | matches published | `guidelines/spirit-2025.md` | DOCX |
| STROBE | 2007 | 22 items | 22 ✔ | `guidelines/strobe-2007.md` | DOCX |
| PRISMA | 2020 | 42 rows (27 items + sub-items) | ✔ | `guidelines/prisma-2020.md` | DOCX |
| STARD | 2015 | 34 rows (30 items + sub-items) | ✔ | `guidelines/stard-2015.md` | DOCX |
| **TRIPOD+AI** | **2024** | **27 items / 52 blocks** | **1-27 all present ✔** | `guidelines/tripod-ai-2024.md` | Article Table 2 |
| TRIPOD | 2015 | 22 items | 22 ✔ | `guidelines/tripod-2015.md` | PDF table — **superseded by TRIPOD+AI** |
| PRISMA for Abstracts | 2020 | 12 items | 12 ✔ | `guidelines/prisma-abstracts-2020.md` | PDF checklist (CC BY 4.0) |
| PRISMA-P | 2015 | 17 items / 26 blocks | ✔ | `guidelines/prisma-p-2015.md` | DOCX |
| ARRIVE | 2.0 (2020) | 21 items | 21 ✔ | `guidelines/arrive-2.0.md` | PDF checklist |
| **CODE-EHR** | **2022** | **8 items** | **8 ✔** | `guidelines/code-ehr-2022.md` | DOCX |
| AGREE Reporting Checklist | 2016 | 23 items | 23 ✔ | `guidelines/agree-2016.md` | DOCX |
| CARE | 2013 | 13 items | 13 ✔ | `guidelines/care-2013.md` | PDF checklist |
| COREQ | 2007 | 32 items | 32 ✔ | `guidelines/coreq-2007.md` | PDF table |
| SQUIRE | 2.0 (2015) | 18 items | 18 ✔ | `guidelines/squire-2.0.md` | PDF checklist |
| CHEERS | 2022 | 28 items | 28 ✔ | `guidelines/cheers-2022.md` | PDF checklist |

## Present, metadata only — item text still to transcribe

| Guideline | Version | File | Note |
|---|---|---|---|
| MOOSE | 2000 | `guidelines/moose-2000.md` | Observational meta-analysis; largely superseded in practice by PRISMA 2020 |
| TIDieR | 2014 | `guidelines/tidier-2014.md` | 12 items; extends CONSORT item 5 / SPIRIT item 11, not standalone |
| GREET | 2016 | `guidelines/greet-2016.md` | Evidence-based-practice education; niche |
| Simulation extensions | 2016 | `guidelines/simulation-2016.md` | Extension to CONSORT and STROBE |
| Braun & Clarke | 2025 | `guidelines/qualitative-values-2025.md` | Not a checklist — a critique of checklist reporting in qualitative research |

## Missing — to add

Ordered by how likely they are to be needed.

| Guideline | Covers | Why it matters | Blocker |
|---|---|---|---|
| **RECORD** (2015) | Observational studies using routinely-collected health data | Highest-value addition for NHIF/NCPHA administrative-data work | Have the paper; its side-by-side STROBE\|RECORD table does not extract reliably. Need the official checklist file |
| **RECORD-PE** (2018) | Pharmacoepidemiology using routine data | Extends RECORD | Have the paper; four-column STROBE\|RECORD\|RECORD-PE table. Need the official checklist |
| **RIGHT** (2017) | Clinical practice guidelines | Companion to AGREE | Have the paper; extractable, not yet transcribed |
| **RIGHT-PVG** (2021) | Public versions of guidelines | Extends RIGHT | Have the paper; layout defeats extraction. Need official checklist |
| **SRQR** (2014) | Qualitative research, broadly | Broader than COREQ's interview/focus-group scope | Have the paper; extractable, not yet transcribed |
| **TRIPOD+AI for Abstracts** | Abstracts of prediction-model studies | TRIPOD+AI item 2 defers to it | Not downloaded |

### Extensions not yet included

None of the extension checklists are here. The ones most likely to come up:

- **STROBE**: RECORD (routinely collected health data), RECORD-PE (pharmacoepidemiology), STROBE-MR (Mendelian randomisation)
- **PRISMA**: PRISMA-ScR (scoping reviews), PRISMA-DTA (diagnostic test accuracy), PRISMA-S (search strategies), PRISMA-LSR (living reviews), PRISMA-Equity
- **CONSORT/SPIRIT**: -AI, -Outcomes 2022, -Equity, -ROUTINE, children and adolescents
- **CHEERS**: extensions for specific evaluation types

RECORD is the highest-value addition for administrative-data work (NHIF, NCPHA).

## Version watch-list

Guidelines that changed recently, or are expected to:

| Guideline | Watch because |
|---|---|
| CONSORT / SPIRIT | Both updated April 2025 after fifteen years. Anything citing CONSORT 2010 is now out of date. Published simultaneously in BMJ, JAMA, Lancet, Nature Medicine, PLOS Medicine — cite whichever the target journal expects |
| TRIPOD | TRIPOD+AI (2024) **supersedes** the 2015 checklist outright — the paper states it "should no longer be used". It covers regression *and* machine learning, so this is not an ML-only replacement. TRIPOD 2015 is retained here only for appraising papers written against it |
| STROBE | Unchanged since 2007 and showing its age, particularly around data sharing and pre-registration. A revision has been discussed |
| CHEERS | Updated 2022; the 2013 version is still widely cited in error |

## Known issues

- **Licences unverified.** Only CHEERS 2022 has been confirmed (CC BY 4.0). Every other
  file carries `licence: not verified`. This matters because the repository is public —
  confirm terms before relying on redistribution, especially for AGREE, which requires
  registration with the AGREE Research Trust.
- **STROBE design-specific variants not included.** The combined checklist covering cohort,
  case-control, and cross-sectional designs is here; the three separate per-design files are
  not. The combined file marks design-specific items with an asterisk, which covers most
  practical use.
- **Flow diagrams not transcribed.** CONSORT 2025, STARD 2015, and PRISMA 2020 each have a
  flow diagram. These are images and cannot be represented as item text; use the official
  templates.
- **One downloaded file was not a reporting guideline.** `1748-5908-7-70.pdf` was Scott et
  al., *Systematic review of knowledge translation strategies in the allied health
  professions* (Implementation Science 2012;7:70) — a systematic review, not a guideline.
  Excluded, and not recorded in `references.bib`.
