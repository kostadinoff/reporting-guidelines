# Inventory

Status of every guideline in this repository, what is still missing, and what to watch for
version drift. Last full review: **2026-07-27**.

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
| TRIPOD | 2015 | 22 items | 22 ✔ | `guidelines/tripod-2015.md` | PDF table |
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

| Guideline | Covers | Why it matters | Source |
|---|---|---|---|
| **TRIPOD+AI** (2024) | Prediction models using regression or machine learning | Supersedes TRIPOD 2015 for most new prediction-model work. The 2015 version in this repo is out of date for anything involving ML | https://www.tripod-statement.org/ |
| **PRISMA-P** (2015) | Systematic review protocols | The protocol counterpart to PRISMA; pairs with SPIRIT for trials | https://www.prisma-statement.org/ |
| **SRQR** (2014) | Qualitative research, broadly | Broader than COREQ, which is interview/focus-group specific | https://www.equator-network.org/reporting-guidelines/srqr/ |
| **ARRIVE 2.0** (2020) | Animal pre-clinical studies | Required by an increasing number of journals | https://arriveguidelines.org/ |
| **RIGHT** (2017) | Clinical practice guidelines | Companion to AGREE; AGREE covers appraisal and reporting, RIGHT is reporting-specific | https://www.equator-network.org/reporting-guidelines/right-statement/ |
| **PRISMA 2020 for Abstracts** | Systematic review abstracts | PRISMA item 2 explicitly defers to it, so the main checklist is incomplete without it | https://www.prisma-statement.org/ |

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
| TRIPOD | TRIPOD+AI (2024) is the current version for ML-based models; the 2015 statement remains valid for conventional regression models |
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
