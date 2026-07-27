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

All item text verbatim, counts checked against the published guideline. 29 files.

**Core designs** — CONSORT 2025, SPIRIT 2025, STROBE, PRISMA 2020, PRISMA-P, PRISMA for
Abstracts, STARD 2015, TRIPOD+AI 2024, TRIPOD 2015 (superseded), AGREE, CARE, COREQ, SRQR,
SQUIRE 2.0, CHEERS 2022, ARRIVE 2.0, RIGHT, RIGHT-PVG, MOOSE.

**Routine / administrative data** — RECORD, RECORD-PE, CODE-EHR. Layer these on STROBE;
the closest fit for NHIF and NCPHA work.

**Extensions** — TIDieR (interventions), PRISMA-ScR (scoping reviews), STROBE-MR (Mendelian
randomization), CONSORT-AI, SPIRIT-AI, CHEERS-AI, TRIPOD+AI for Abstracts.

See the table in [README.md](README.md) for versions and item counts.

## Present, metadata only — item text still to transcribe

| Guideline | Version | File | Note |
|---|---|---|---|
| GREET | 2016 | `guidelines/greet-2016.md` | Evidence-based-practice education; niche |
| Simulation extensions | 2016 | `guidelines/simulation-2016.md` | Extension to CONSORT and STROBE |
| Braun & Clarke | 2025 | `guidelines/qualitative-values-2025.md` | Not a checklist — a critique of checklist reporting in qualitative research |

## Missing — to add

Nothing from the original scope is missing. Remaining candidates are further extensions:

| Guideline | Covers |
|---|---|
| PRISMA-DTA | Diagnostic test accuracy reviews |
| PRISMA-S | Search-strategy reporting |
| PRISMA-LSR / PRISMA-Equity | Living reviews; equity-focused reviews |
| CONSORT-Outcomes 2022, CONSORT-Equity, CONSORT-ROUTINE | CONSORT extensions |
| STARD-AI, DECIDE-AI, CLAIM | AI diagnostic accuracy, early clinical evaluation, medical imaging |
| TRIPOD-Cluster | Prediction models accounting for clustering (referenced by TRIPOD+AI items 12d, 23b) |

### Extensions not yet included

None of the extension checklists are here. The ones most likely to come up:

- **STROBE**: RECORD (routinely collected health data), RECORD-PE (pharmacoepidemiology), STROBE-MR (Mendelian randomisation)
- **PRISMA**: PRISMA-ScR (scoping reviews), PRISMA-DTA (diagnostic test accuracy), PRISMA-S (search strategies), PRISMA-LSR (living reviews), PRISMA-Equity
- **CONSORT/SPIRIT**: -AI, -Outcomes 2022, -Equity, -ROUTINE, children and adolescents
- **CHEERS**: extensions for specific evaluation types

RECORD, RECORD-PE and CODE-EHR are now included — these are the administrative-data
checklists most relevant to NHIF and NCPHA work. Use them layered on STROBE, not instead of it.

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
- **One footnote missing.** TRIPOD+AI for Abstracts items 7 and 10 carry a `†` marker whose
  footnote text was not captured; flagged in the file itself.
- **Worked examples omitted from RIGHT-PVG.** Its published Table 1 pairs each item with
  several pages of example text from real patient booklets. Those are illustrative, not
  normative; only item text is reproduced. Consult the paper for examples.
- **Flow diagrams not transcribed.** CONSORT 2025, STARD 2015, and PRISMA 2020 each have a
  flow diagram. These are images and cannot be represented as item text; use the official
  templates.
- **One downloaded file was not a reporting guideline.** `1748-5908-7-70.pdf` was Scott et
  al., *Systematic review of knowledge translation strategies in the allied health
  professions* (Implementation Science 2012;7:70) — a systematic review, not a guideline.
  Excluded, and not recorded in `references.bib`.
