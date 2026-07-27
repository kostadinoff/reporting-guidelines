---
name: CLAIM
full_name: Checklist for Artificial Intelligence in Medical Imaging
version: "2024 update"
supersedes: CLAIM (2020)
applies_to: Studies of AI methodology applied to medical imaging
items: 44
citation_key: tejani2024claim
doi: 10.1148/ryai.240300
official_url: https://pubs.rsna.org/journal/ai
licence: no open licence — all rights reserved
licence_basis: "Copyright statement on the article: '© 2024 by the Radiological Society of North America, Inc.' (PMC11304031). Free to read, but no Creative Commons licence — redistribution requires RSNA permission. Verified 2026-07-28."
source_format: PDF checklist
extracted: verbatim
retrieved: 2026-07-27
last_checked: 2026-07-28
---

# CLAIM

44 items for **AI studies in medical imaging**. The 2024 update expands the 2020 original,
adding explainability, robustness/sensitivity analysis, and ensembling.

**Where it sits among the AI guidelines.** CLAIM is imaging-specific and
methodology-focused. `tripod-ai-2024.md` governs clinical prediction models generally;
`consort-ai-2020.md` and `spirit-ai-2020.md` govern trials of AI interventions;
`cheers-ai-2024.md` governs their economic evaluation. For an imaging model evaluated in a
trial, CLAIM and CONSORT-AI are complementary.

Items with no counterpart in the other AI checklists: **19–20** (how data were assigned to
partitions, and the level at which partitions are disjoint — the item that catches patient-
level leakage between train and test), **24** (initialization of model parameters), **27**
(ensembling), and **39** (failure analysis of incorrectly classified cases).

Report the subheading where each item is addressed.

Cite as `[@tejani2024claim]`.

## Title/abstract

### Item 1

Identification as a study of AI methodology, specifying the category of technology used (eg, deep learning).

### Item 2

Summary of study design, methods, results, and conclusions.

## Introduction

### Item 3

Scientific and/or clinical background, including the intended use and role of the AI approach.

### Item 4

Study aims, objectives, and hypotheses.

## Methods: study design

### Item 5

Prospective or retrospective study.

### Item 6

Study goal.

## Methods: data

### Item 7

Data sources.

### Item 8

Inclusion and exclusion criteria.

### Item 9

Data preprocessing.

### Item 10

Selection of data subsets.

### Item 11

De-identification methods.

### Item 12

How missing data were handled.

### Item 13

Image acquisition protocol.

## Methods: reference standard

### Item 14

Definition of method(s) used to obtain reference standard.

### Item 15

Rationale for choosing the reference standard.

### Item 16

Source of reference standard annotations.

### Item 17

Annotation of test set.

### Item 18

Measures of inter- and intrarater variability of features described by the annotators.

## Methods: data partitions

### Item 19

How data were assigned to partitions.

### Item 20

Level at which partitions are disjoint.

## Methods: testing data

### Item 21

Intended sample size.

## Methods: model

### Item 22

Detailed description of model.

### Item 23

Software libraries, frameworks, and packages.

### Item 24

Initialization of model parameters.

## Methods: training

### Item 25

Details of training approach.

### Item 26

Method of selecting the final model.

### Item 27

Ensembling techniques.

## Methods: evaluation

### Item 28

Metrics of model performance.

### Item 29

Statistical measures of significance and uncertainty.

### Item 30

Robustness or sensitivity analysis.

### Item 31

Methods for explainability or interpretability.

### Item 32

Evaluation on internal data.

### Item 33

Testing on external data.

### Item 34

Clinical trial registration.

## Results: data

### Item 35

Numbers of patients or examinations included and excluded.

### Item 36

Demographic and clinical characteristics of cases in each partition.

## Results: model performance

### Item 37

Performance metrics and measures of statistical uncertainty.

### Item 38

Estimates of diagnostic performance and their precision.

### Item 39

Failure analysis of incorrectly classified cases.

## Discussion

### Item 40

Study limitations.

### Item 41

Implications for practice, including intended use and/or clinical role.

## Other information

### Item 42

Provide a reference to the full study protocol or to additional technical details.

### Item 43

Statement about the availability of software, trained model, and/or data.

### Item 44

Sources of funding and other support; role of funders.
