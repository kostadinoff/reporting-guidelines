---
name: STARD-AI
full_name: The STARD-AI reporting guideline for diagnostic accuracy studies using artificial intelligence
version: "2025"
extends: stard-2015
applies_to: Diagnostic test accuracy studies where the index test is AI-centred
items: 44
citation_key: sounderajah2025stardai
doi: 10.1038/s41591-025-03953-8
official_url: https://www.equator-network.org/reporting-guidelines/stard-ai/
licence: not verified — not yet checked at source
source_format: Journal article, Supplementary Table 2
extracted: verbatim
retrieved: 2026-07-28
last_checked: 2026-07-28
---

# STARD-AI

Diagnostic accuracy reporting where the index test is an AI system. Extends STARD 2015 with
18 new or modified items; the full checklist is reproduced here.

**Where it sits among the AI guidelines.** `claim-2024.md` covers AI methodology in medical
*imaging*; STARD-AI covers AI-centred *diagnostic accuracy* in any modality;
`tripod-ai-2024.md` covers prediction models; `decide-ai-2022.md` covers early live clinical
evaluation. For an imaging AI evaluated for diagnostic accuracy, STARD-AI and CLAIM overlap
and are complementary.

What STARD 2015 does not ask for and this does: **11–14** (data provenance, who annotated it
and with what expertise, capture devices, acquisition and pre-processing protocols),
**15b** (train/validate/test/external evaluation with sample sizes), **15d** (the specified
end user and required expertise), **23** (performance error analysis, algorithmic bias and
fairness), **28–29** (whether the dataset represents the intended-use population, and how an
external dataset differs from the training data), and **40a–40b** (availability of datasets
and code, and whether outputs are auditable).

Cite as `[@sounderajah2025stardai]`.

## Title or abstract

### Item 1

Identification as a study reporting AI-centred diagnostic accuracy and reporting at least one measure of accuracy within title or abstract.

### Item 2 — Abstract

Structured summary of study design, methods, results and conclusions (for specific guidance, please see STARD for Abstracts).

## Introduction

### Item 3

Scientific and clinical background, including the intended use of the index test, whether it is novel or an established index test, and its integration into an existing or new workflow, if applicable.

### Item 4

Study objectives and hypotheses.

## Methods: study design

### Item 5

Whether data collection was planned before the index test and reference standard were performed (prospective study) or after (retrospective study).

## Methods: ethics

### Item 6

Formal approval from an ethics committee. If not required, justify why.

## Methods: participants

### Item 7

Eligibility criteria: listing separate inclusion and exclusion criteria in the order that they are applied at both participant level and data level.

### Item 8

On what basis potentially eligible participants were identified (such as symptoms, results from previous tests, inclusion in registry).

### Item 9

Where and when potentially eligible participants were identified (setting, location, and dates).

### Item 10

Whether participants formed a consecutive, random, or convenience series.

## Methods: dataset

### Item 11

Source of the data and whether it has been routinely collected, specifically collected for the purpose of the study or acquired from an open-source repository.

### Item 12

Who undertook the annotations for the dataset (including experience levels and background) and how (within the same clinical context or in a post-hoc fashion), if applicable.

### Item 13

Devices (manufacturer, model) that were used to capture data; software (with version number) used to engineer the index test, highlighting the intended use.

### Item 14

Data acquisition protocols (e.g. contrast protocol or reconstruction method for medical images) and details of data pre-processing in sufficient detail to allow replication.

## Methods: test methods

### Item 15a

Index test, in sufficient detail to allow replication.

### Item 15b

How the index test was developed, including any training, validation, testing and external evaluation, detailing sample sizes, when applicable.

### Item 15c

Definition of and rationale for test positivity cut-offs or result categories of the index test, distinguishing pre-specified from exploratory.

### Item 15d

The specified end user of the index test and the level of expertise required of users.

### Item 16a

Reference standard, in sufficient detail to allow replication.

### Item 16b

Rationale for choosing the reference standard (if alternatives exist).

### Item 16c

Definition of and rationale for test positivity cut-offs or result categories of the reference standard, distinguishing pre-specified from exploratory.

### Item 17a

Whether clinical information and reference standard results were available to the performers or readers of the index test.

### Item 17b

Whether clinical information and index test results were available to the assessors of the reference standard.

## Methods: analysis

### Item 18

Methods for estimating or comparing measures of diagnostic accuracy.

### Item 19

How indeterminate index test or reference standard results were handled.

### Item 20

How missing data on the index test and reference standard were handled.

### Item 21

Any analyses of variability in diagnostic accuracy, distinguishing pre-specified from exploratory.

### Item 22

Intended sample size and how it was determined.

### Item 23

Details of any performance error analysis, and algorithmic bias and fairness assessments if undertaken.

## Results: participants and dataset

### Item 24

Flow of participants, using a diagram.

### Item 25

Baseline demographic, clinical and technical characteristics of training, validation and test set, if applicable.

### Item 26a

Distribution of severity of disease in those with the target condition.

### Item 26b

Distribution of alternative diagnoses in those without the target condition.

### Item 27

Time interval and any clinical interventions between index test and reference standard.

### Item 28

Whether the datasets represent the distribution of the target condition that one would expect from the intended use population.

### Item 29

For external evaluation on an independent dataset, an assessment of how this differs from the training, validation and test sets.

## Results: test results

### Item 30

Cross tabulation of the index test results (or their distribution) by the results of the reference standard.

### Item 31

Estimates of diagnostic accuracy and their precision (such as 95% confidence intervals).

### Item 32

Any adverse events from performing the index test or the reference standard.

## Discussion

### Item 33

Study limitations, including sources of potential bias, statistical uncertainty, and generalisability.

### Item 34

Implications for practice, including the intended use and clinical role of the index test.

### Item 35

Ethical considerations and adherence to ethical standards associated with the use of the index test and issues of fairness.

## Other information

### Item 36

Registration number and name of registry.

### Item 37

Where the full study protocol can be accessed.

### Item 38

Sources of funding and other support; role of funders.

### Item 39

Commercial interests, if applicable.

### Item 40a

Availability of datasets and code; detailing any restrictions on their reuse and repurposing.

### Item 40b

Whether outputs are stored, auditable and available for evaluation, if necessary.
