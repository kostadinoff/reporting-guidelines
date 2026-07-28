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

All item text verbatim, counts checked against the published guideline. 39 files.

**Core designs** — CONSORT 2025, SPIRIT 2025, STROBE, PRISMA 2020, PRISMA-P, PRISMA for
Abstracts, STARD 2015, TRIPOD+AI 2024, TRIPOD 2015 (superseded), AGREE, CARE, COREQ, SRQR,
SQUIRE 2.0, CHEERS 2022, ARRIVE 2.0, RIGHT, RIGHT-PVG, MOOSE.

**Routine / administrative data** — RECORD, RECORD-PE, CODE-EHR. Layer these on STROBE;
the closest fit for NHIF and NCPHA work.

**Extensions** — TIDieR (interventions), GREET (EBP education, built on TIDieR),
PRISMA-ScR (scoping reviews), PRISMA-DTA (diagnostic accuracy reviews), PRISMA-S (literature
searches), PRISMA-E (health equity), PRISMA-LSR (living reviews), STROBE-MR (Mendelian
randomization), CONSORT-ROUTINE (trials run in cohorts or routine data), TRIPOD-Cluster
(clustered data), TRIPOD+AI for Abstracts.

**AI-specific** — TRIPOD+AI (prediction models), CONSORT-AI and SPIRIT-AI (trials and
protocols), CHEERS-AI (economic evaluation), STARD-AI (diagnostic accuracy), CLAIM (medical
imaging), DECIDE-AI (early live clinical evaluation of decision-support systems).

**Qualitative** — COREQ (interviews/focus groups), SRQR (any design), Braun & Clarke
15-point checklist (quality of a thematic analysis, not reporting structure).

See the table in [README.md](README.md) for versions and item counts.

## Present, metadata only — item text still to transcribe

| Guideline | Version | File | Note |
|---|---|---|---|
| Simulation extensions | 2016 | `guidelines/simulation-2016.md` | Extension to CONSORT and STROBE |

## Missing — to add

Nothing from the original scope is missing. Remaining candidates are further extensions:

| Guideline | Covers |
|---|---|
| CONSORT-Outcomes 2022, CONSORT-Equity | CONSORT extensions |

### Extension checklists

Present: RECORD, RECORD-PE, CODE-EHR and STROBE-MR (STROBE); PRISMA-P, PRISMA for Abstracts,
PRISMA-ScR, PRISMA-DTA, PRISMA-S, PRISMA-E and PRISMA-LSR (PRISMA); CONSORT-AI, SPIRIT-AI,
CONSORT-ROUTINE, CONSORT-Outcomes 2022 and the simulation extensions (CONSORT/SPIRIT);
TRIPOD+AI, TRIPOD+AI for Abstracts and TRIPOD-Cluster (TRIPOD); CHEERS-AI (CHEERS);
RIGHT-PVG (RIGHT); TIDieR and GREET (intervention description).

RECORD, RECORD-PE and CODE-EHR are the administrative-data checklists most relevant to NHIF
and NCPHA work. Layer them on STROBE, not instead of it. CONSORT-ROUTINE is the trials
counterpart for studies run inside routine data.

Still absent: CONSORT-Equity, CONSORT for children and adolescents, SPIRIT-Outcomes 2022
(the protocol counterpart of CONSORT-Outcomes, JAMA 2022, doi:10.1001/jama.2022.21243),
SPIRIT-Surrogate, CARE extensions, and PRISMA-DTA for Abstracts.


## Version watch-list

Guidelines that changed recently, or are expected to:

| Guideline | Watch because |
|---|---|
| CONSORT / SPIRIT | Both updated April 2025 after fifteen years. Anything citing CONSORT 2010 is now out of date. Published simultaneously in BMJ, JAMA, Lancet, Nature Medicine, PLOS Medicine — cite whichever the target journal expects |
| TRIPOD | TRIPOD+AI (2024) **supersedes** the 2015 checklist outright — the paper states it "should no longer be used". It covers regression *and* machine learning, so this is not an ML-only replacement. TRIPOD 2015 is retained here only for appraising papers written against it |
| STROBE | Unchanged since 2007 and showing its age, particularly around data sharing and pre-registration. A revision has been discussed |
| CHEERS | Updated 2022; the 2013 version is still widely cited in error |

## Known issues

- **Licence position, all 43 recorded — none unexamined.** 32 reproduced under an
  established licence; the PRISMA, CONSORT and TRIPOD groups each distribute their
  checklists *and extensions* under CC BY, which settled ten files at once. 8 carry no open
  licence at source and rest on attribution plus the EQUATOR Network's terms. 3 are
  metadata-only because their licence forbids reproducing the items in this format — CLAIM
  (all rights reserved), CHEERS-AI and TRIPOD 2015 (both CC BY-NC-ND, where **ND** is the
  binding term). Several established licences are non-commercial. See `NOTICE`.
- **Version of record vs accepted manuscript.** Two files turn on this. STARD-AI's Nature
  Medicine version of record is bronze OA with no licence, but the peer-reviewed *accepted*
  version in institutional repositories is CC BY — that is the basis on which it is
  reproduced. CLAIM has a CC BY *submitted* version (a preprint), which does **not** rescue
  it: a preprint may differ from the published checklist, so CLAIM stays metadata-only.
- **Weakest position: DECIDE-AI.** Version of record paywalled, only a green accepted
  manuscript openly available with no CC licence, and not covered by EQUATOR terms.
- **Outstanding compliance task.** The EQUATOR terms require copies to retain all copyright
  notices carried on the source material. Files record author, DOI, official URL and licence
  basis, but not the literal copyright line printed on each checklist PDF. Capturing those
  would move the nine from arguably compliant to demonstrably compliant.

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
