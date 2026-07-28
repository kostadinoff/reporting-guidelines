---
name: CONSORT-ROUTINE
full_name: CONSORT extension for trials conducted using cohorts or routinely collected data
version: "2021"
extends: consort-2025
extends_note: "Published against CONSORT 2010; item numbers below refer to that version."
applies_to: Randomised trials conducted using an existing cohort or routinely collected data (EHR, registry, claims)
items: 13
structure: "5 new ROUTINE items + 8 modified CONSORT items; the remaining CONSORT items are unchanged"
citation_key: kwakkenbos2021consortroutine
doi: 10.1136/bmj.n857
official_url: https://www.equator-network.org/reporting-guidelines/consort-routine/
licence: CC BY 4.0
licence_basis: "CONSORT checklists are distributed under CC BY per the CONSORT site: 'The CONSORT checklist is distributed under the terms of the Creative Commons Attribution License CC-BY.' Extensions are hosted on the same site. Full text of this extension is freely available at bmj.com/content/373/bmj.n857. Verified 2026-07-28."
source_format: Journal article, Tables 1 and 2
extracted: verbatim (new and modified items only)
retrieved: 2026-07-28
last_checked: 2026-07-28
---

# CONSORT-ROUTINE

For trials **run inside** an existing cohort or routine data source — registry-based trials,
EHR-embedded trials, cohort multiple RCTs. Five new items (**ROUTINE-1** to **ROUTINE-5**)
plus eight modified CONSORT items. Everything not listed here is unchanged; see
`consort-2025.md`.

**Version caveat.** Written against CONSORT 2010, so the item numbers below refer to that
version. Map by topic onto CONSORT 2025.

**Where this sits.** RECORD governs *observational* studies in routine data; CONSORT-ROUTINE
governs *trials* conducted in it. The shared concern is the same one: codes, algorithms,
linkage, and the accuracy and completeness of data collected for another purpose. For NHIF
or registry-embedded trials this is the checklist, not RECORD.

Note **ROUTINE-4** — consent. Trials embedded in routine data raise consent questions that a
conventional trial does not, and the item exists because they are routinely left unstated.

Cite as `[@kwakkenbos2021consortroutine]`.

## Title and abstract

### Item 1b — Abstract (modified)

Structured summary of trial design, methods, results, and conclusions (for specific guidance see CONSORT for abstracts). **Specify that a cohort or routinely collected data were used to conduct the trial and, if applicable, provide the name of the cohort or routinely collected database(s).**

## Methods: trial design

### Item 3a — Trial design (modified)

Description of trial design (such as parallel, factorial) including allocation ratio, **that a cohort or routinely collected database(s) was used to conduct the trial (such as electronic health record, registry) and how the data were used within the trial (such as identification of eligible trial participants, trial outcomes).**

## Methods: cohort or routinely collected database (new section)

### Item ROUTINE-1 (new)

Name, if applicable, and description of the cohort or routinely collected database(s) used to conduct the trial, including information on the setting (such as primary care), locations, and dates (such as periods of recruitment, follow-up, and data collection).

### Item ROUTINE-2 (new)

Eligibility criteria for participants in the cohort or routinely collected database(s).

### Item ROUTINE-3 (new)

State whether the study included person-level, institutional-level, or other data linkage across two or more databases and, if so, linkage techniques and methods used to evaluate completeness and accuracy of linkage.

## Methods: trial participants

### Item 4a — Eligibility criteria (modified)

Eligibility criteria for trial participants, **including information on how to access the list of codes and algorithms used to identify eligible participants, information on accuracy and completeness of data used to ascertain eligibility, and methods used to validate accuracy and completeness (eg, monitoring, adjudication), if applicable.**

### Item ROUTINE-4 (new)

Describe whether and how consent was obtained.

## Methods: outcomes

### Item 6a — Outcomes (modified)

Completely defined pre-specified primary and secondary outcome measures, including how and when they were **ascertained and the cohort or routinely collected database(s) used to ascertain each outcome.**

### Item ROUTINE-5 (new)

Information on how to access the list of codes and algorithms used to define or derive the outcomes from the cohort or routinely collected database(s) used to conduct the trial, information on accuracy and completeness of outcome variables, and methods used to validate accuracy and completeness (eg, monitoring, adjudication), if applicable.

## Methods: allocation concealment

### Item 9 — Allocation concealment mechanism (modified)

Mechanism used to implement the random allocation sequence (**such as embedding an automated randomiser within the cohort or routinely collected database(s)**), describing any steps taken to conceal the sequence until interventions were assigned.

## Results: participant flow

### Item 13a — Participant flow (modified)

For each group, **the number of participants in the cohort or routinely collected database(s) used to conduct the trial and** the numbers screened for eligibility, randomly assigned, **offered and accepted interventions (eg, cohort multiple RCTs)**, received intended treatment, and analysed for the primary outcome.

## Discussion: interpretation

### Item 22 — Interpretation (modified)

Interpretation consistent with results, balancing benefits and harms, and considering other relevant evidence, **including the implications of using data that were not collected to answer the trial research questions.**

## Other information: funding

### Item 25 — Funding (modified)

Sources of funding and other support **for both the trial and the cohort or routinely collected database(s)**, role of funders.
