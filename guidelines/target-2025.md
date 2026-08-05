---
name: TARGET
full_name: TrAnsparent ReportinG of studies Emulating a Target trial
version: "2025"
applies_to: Observational studies of interventions that explicitly emulate a parallel group, individually randomized target trial, with adjustment for baseline confounders
items: 21
sections: 6
citation_key: cashin2025target
doi: 10.1001/jama.2025.13350
official_url: https://target-guideline.org/
licence: CC BY-ND 4.0
licence_basis: "The TARGET group licenses the checklist itself, independently of the journal: 'The TARGET Checklist is licensed by the TARGET group under the Creative Commons Attribution-NoDerivs (CC BY-ND) 4.0 International license' — stated on the JAMA version of record and repeated on the PMC deposit (PMC13084563). The statement was co-published in JAMA and The BMJ (doi:10.1136/bmj-2025-087179); the checklist licence is the developers' and does not vary by journal. Verified 2026-08-05."
source_format: Journal article checklist table
extracted: verbatim-table
extracted_note: "ND. Reproduced unchanged and in whole as the published table, not restructured into per-item blocks. CC BY-ND 4.0 grants reproduction and sharing of the licensed material in any medium or format; it withholds only the sharing of adapted material, and the per-item block structure used elsewhere in this repository would be an adaptation. Grep by item number in the table rather than by '### Item N'."
retrieved: 2026-08-05
last_checked: 2026-08-05
---

# TARGET

21 items in 6 sections, for observational studies of interventions that explicitly emulate a
target trial. The statement was published simultaneously in JAMA
(doi:10.1001/jama.2025.13350) and The BMJ (doi:10.1136/bmj-2025-087179) in September 2025,
with a companion piece in PLOS Medicine (doi:10.1371/journal.pmed.1004787); PLOS Medicine now
requires adherence for new target trial emulation submissions.

**No explanation and elaboration document yet.** The official site lists one as coming soon.
Until it appears, the guideline's own development papers are the closest thing to elaboration:
the protocol (doi:10.1136/bmjopen-2023-074626) and the systematic review of reporting practices
that identified the candidate items (doi:10.1001/jamanetworkopen.2023.36023).

Cite as `[@cashin2025target]`.

## Scope, and what it does not cover

TARGET applies where the target trial being emulated is a **parallel group, individually
randomized** trial and confounding is handled by **adjustment for baseline confounders**.
That is the common case and the one the checklist was piloted on. It is not written for
cluster-randomized or crossover target trials, and it does not cover the reporting of
time-varying confounding adjustment (inverse probability weighting over follow-up, the
g-formula, g-estimation) beyond what items 6h/7h ask for generically.

## Relation to other checklists in this repository

TARGET does **not** replace STROBE. A target trial emulation is still an observational
study, and journals that mandate STROBE will continue to mandate it; TARGET adds the causal
specification that STROBE has no items for. Layer them:

- `strobe-2007.md` — the observational base checklist.
- `record-2015.md`, `record-pe-2018.md`, `code-ehr-2022.md` — if the emulation runs on
  routinely collected health data, claims, or linked registries, which is the usual case.
- `target-2025.md` — the emulation itself: the target trial protocol, how each component was
  mapped onto the data, and the identifying assumptions.

The overlap is real but not redundant. STROBE item 12 asks what statistical methods were
used; TARGET items 6h and 7h ask for the analysis plan **per causal estimand**, and 7h.ii
asks separately what was done to test the sensitivity of the results to the
operationalization choices — which is where emulations most often fail.

## Format note

**This file reproduces the checklist as published, in one table, unchanged and in whole.**
Every other full-text guideline here is split into `### Item N` blocks. TARGET is not,
because the checklist carries a NoDerivatives licence and that restructuring would be an
adaptation. To pull a single item:

```bash
grep -P '^\| ?7 ?\|' guidelines/target-2025.md      # or search the item's wording
```

Items 6 and 7 are paired: item 6 specifies a component of the target trial protocol, item 7
describes how that same component was emulated with the observational data. They share the
sub-item letters a–h and are reported together, which is why the source lays them out in
parallel columns rather than sequentially.

---

## The TARGET checklist

| Item no. | | Checklist item |
|---|---|---|
| **Abstract** | | |
| 1 | a | Identify that the study attempts to emulate a target trial using observational data. State the study objectives and briefly summarize the specified target trial. |
| | b | Report the data sources used for emulation. |
| | c | Summarize key assumptions, statistical methods, findings and conclusions. |
| **Introduction** | | |
| 2 | Background | Describe the scientific background of the study and the gap in knowledge. |
| 3 | Causal question | Summarize the causal question. |
| 4 | Rationale | Describe the rationale for emulating a target trial with the available data. Cite randomized trials informing the design of the target trial if applicable. |
| **Methods** | | |
| 5 | Data sources | Cite the data sources contributing to the analyses and for each one describe the following: original purpose, type, the geographic locations, setting and time-period. If relevant, describe how the data were linked or pooled. |
| 6 | Target trial specification | Specify the components of the target trial protocol that would answer the causal question. |
| 7 | Target trial emulation | Describe how the components of the target trial protocol were emulated with the observational data, including how all variables were measured or ascertained. |

Items 6 and 7 expand into the paired sub-items below. The left column is the specification of
the target trial (item 6); the right column is its emulation with the observational data
(item 7). Both are reported, and the source checklist provides a separate "Location reported"
column for each.

| | Item 6 — target trial specification | | Item 7 — target trial emulation |
|---|---|---|---|
| **Eligibility criteria** | | **Eligibility criteria** | |
| a | Describe the eligibility criteria. | a | Describe how the eligibility criteria were operationalized with the data. |
| **Treatment strategies** | | **Treatment strategies** | |
| b | Describe the treatment strategies that would be compared. | b | Describe how the treatment strategies were operationalized with the data. |
| **Assignment procedures** | | **Assignment procedures** | |
| c | Report that eligible individuals would be randomly assigned to treatment strategies and may be aware of their treatment allocation. | c | Describe how assignment to treatment strategies was operationalized with the data. |
| **Follow-up** | | **Follow-up** | |
| d | Clarify that follow-up would start at time of assignment to the treatment strategies. Specify when follow-up would end. | d | Clarify that follow-up starts at the time individuals were assigned to the treatment strategies. Describe how the end of follow-up was operationalized with the data. |
| **Outcomes** | | **Outcomes** | |
| e | Describe the outcomes. | e | Describe how the outcomes were operationalized with the data. |
| **Causal contrasts** | | **Causal contrasts** | |
| f | Describe the causal contrasts of interest, including effect measures. | f | Describe how the causal contrasts were operationalized with the data, including effect measures. |
| **Identifying assumptions** | | **Identifying assumptions** | |
| g | Describe assumptions that would be made to identify each causal estimand. Describe the variables, if any, related to these assumptions. | g.i | For each causal estimand, describe assumptions made to identify it, including assumptions regarding baseline confounding due to lack of randomization. |
| | | g.ii | Describe how the variables related to these assumptions were operationalized with the data. |
| **Data analysis plan** | | **Data analysis plan** | |
| h | For each causal estimand, describe the data analysis procedures and any associated statistical modelling assumptions, including approaches for handling missing data. | h.i | For each causal estimand, describe the data analysis procedures and any associated statistical modelling assumptions, including approaches for handling missing data. |
| | | h.ii | For each causal estimand, describe any additional analyses conducted to assess the sensitivity of the results to the choice of operationalizations, assumptions and analysis. |

| Item no. | | Checklist item |
|---|---|---|
| **Results** | | |
| 8 | Participant selection | Report numbers of individuals assessed for eligibility, eligible, and assigned to each treatment strategy. A flow diagram is strongly recommended. |
| 9 | Baseline data | Describe the distribution of characteristics of individuals at baseline, by treatment strategy. |
| 10 | Follow-up | Summarize length of follow-up and describe reasons for end of follow-up for each treatment strategy and causal contrast. |
| 11 | Missing data | Describe the frequency of missing data in all variables, by treatment strategy when applicable. |
| 12 | Outcomes | Describe the frequency or distribution of each outcome, by treatment strategy. |
| 13 | Effect estimates | Report the effect estimates for each causal contrast with corresponding measures of precision, including both absolute and relative measures of effect, when applicable. |
| 14 | Additional analyses | Report results of all analyses to assess the sensitivity of the estimates to choices in operationalizations, assumptions and analysis. |
| **Discussion** | | |
| 15 | Interpretation | Provide an interpretation of the key findings. |
| 16 | Limitations | Discuss the limitations of the study considering differences between the target trial and its emulation and the plausibility of assumptions, including assumptions regarding baseline confounding due to lack of randomization. |
| **Other information** | | |
| 17 | Ethics | Provide the institutional research board or ethics committee that approved the study and approval numbers, if relevant. |
| 18 | Registration | State whether, when and where the study protocol was registered. |
| 19 | Sharing of study materials | Provide information on whether data, analytic code and/or other materials are accessible, and where and how they can be accessed. |
| 20 | Funding sources | Provide the sources of funding and detail the role of the funders in the design, conduct and reporting of the study. |
| 21 | Conflicts of interest | State any conflicts of interest and financial disclosures for all authors. |

**Citation:** Cashin AG, Hansford HJ, Hernán MA, Swanson SA, Lee H, Jones MD, et al.
Transparent Reporting of Observational Studies Emulating a Target Trial: The TARGET
Statement. JAMA. 2025; DOI: 10.1001/jama.2025.13350

© 2025 Cashin et al. This is an Open Access article distributed under the terms of the
Creative Commons Attribution-NoDerivatives License (CC BY-ND 4.0), which permits
redistribution, commercial and non-commercial, provided the work is passed along unchanged
and in whole, with credit to the original author(s).

---

## Completing it

The checklist ships with a **"Location reported"** column — three of them, in fact: one for
the main table, and one each for the item 6 and item 7 halves of the target trial protocol.
Fill these with a subheading path, never a page number. See the `reporting-guidelines` skill
for the convention.

The two-column layout of items 6 and 7 is the point of the checklist and the thing most
emulations report badly. A completed TARGET supplement should read as a table where every
protocol component appears twice — once as what the trial would have done, once as what the
data actually allowed — so that the gap between them is visible rather than argued away.
Item 16 then asks you to discuss exactly that gap.

Common failures, all of which the checklist is built to expose:

- **Time zero not aligned.** Item 6d/7d. Eligibility, assignment and the start of follow-up
  must coincide. When they do not, follow-up before assignment is immortal time.
- **Prevalent users.** Item 6a/7a. Starting follow-up at a calendar date rather than at
  treatment initiation selects for people who already tolerated the drug.
- **Assignment using future information.** Item 7c. Classification into a strategy must use
  only data available at the eligible interval.
- **Estimand left implicit.** Item 6f/7f. Intention-to-treat and per protocol effects are
  different estimands with different identifying assumptions; say which, and say it per
  contrast.
- **Sensitivity analyses reported only for the model.** Item 7h.ii asks for sensitivity to
  the *operationalization* choices — grace period length, lookback window, outcome
  definition — not only to the statistical model.
