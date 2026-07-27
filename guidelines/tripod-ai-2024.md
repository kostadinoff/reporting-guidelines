---
name: TRIPOD+AI
full_name: Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis — updated guidance for models using regression or machine learning
version: "2024"
supersedes: TRIPOD 2015
applies_to: Studies developing or evaluating a clinical prediction model, whether built with regression or machine learning
items: 27
item_blocks: 52
citation_key: collins2024tripodai
doi: 10.1136/bmj-2023-078378
official_url: https://www.tripod-statement.org/
licence: not verified — confirm at official source before redistribution
source_format: Journal article, Table 2
extracted: verbatim
retrieved: 2026-07-27
last_checked: 2026-07-27
---

# TRIPOD+AI

27 items. **Supersedes the TRIPOD 2015 checklist**, which should no longer be used for new
prediction-model studies — see `tripod-2015.md`, retained for reference and for appraising
older papers.

The "+AI" indicates consolidated recommendations covering models developed by regression
*or* machine learning (deep learning, random forests). What is genuinely new relative to
2015: **fairness** (item 14), **class imbalance** (item 13), **health inequalities** (item
3c), an **open science** section (items 18a–18f, including code sharing), **patient and
public involvement** (item 19), and **usability in the context of current care** (27a–27c).

Applicability markers:

- **D** — relevant only to model *development*
- **E** — relevant only to model *evaluation*
- **D;E** — applies to both

A companion **TRIPOD+AI for Abstracts** checklist (13 items) exists and is not yet in this
repository.

Cite as `[@collins2024tripodai]`.

## Title

### Item 1 (D;E) — Title

Identify the study as developing or evaluating the performance of a multivariable prediction model, the target population, and the outcome to be predicted.

## Abstract

### Item 2 (D;E) — Abstract

See TRIPOD+AI for Abstracts checklist.

## Introduction

### Item 3a (D;E) — Background

Explain the healthcare context (including whether diagnostic or prognostic) and rationale for developing or evaluating the prediction model, including references to existing models.

### Item 3b (D;E) — Background

Describe the target population and the intended purpose of the prediction model in the context of the care pathway, including its intended users (eg, healthcare professionals, patients, public).

### Item 3c (D;E) — Background

Describe any known health inequalities between sociodemographic groups.

### Item 4 (D;E) — Objectives

Specify the study objectives, including whether the study describes the development or validation of a prediction model (or both).

## Methods

### Item 5a (D;E) — Data

Describe the sources of data separately for the development and evaluation datasets (eg, randomised trial, cohort, routine care or registry data), the rationale for using these data, and representativeness of the data.

### Item 5b (D;E) — Data

Specify the dates of the collected participant data, including start and end of participant accrual; and, if applicable, end of follow-up.

### Item 6a (D;E) — Participants

Specify key elements of the study setting (eg, primary care, secondary care, general population) including the number and location of centres.

### Item 6b (D;E) — Participants

Describe the eligibility criteria for study participants.

### Item 6c (D;E) — Participants

Give details of any treatments received, and how they were handled during model development or evaluation, if relevant.

### Item 7 (D;E) — Data preparation

Describe any data pre-processing and quality checking, including whether this was similar across relevant sociodemographic groups.

### Item 8a (D;E) — Outcome

Clearly define the outcome that is being predicted and the time horizon, including how and when assessed, the rationale for choosing this outcome, and whether the method of outcome assessment is consistent across sociodemographic groups.

### Item 8b (D;E) — Outcome

If outcome assessment requires subjective interpretation, describe the qualifications and demographic characteristics of the outcome assessors.

### Item 8c (D;E) — Outcome

Report any actions to blind assessment of the outcome to be predicted.

### Item 9a (D) — Predictors

Describe the choice of initial predictors (eg, literature, previous models, all available predictors) and any pre-selection of predictors before model building.

### Item 9b (D;E) — Predictors

Clearly define all predictors, including how and when they were measured (and any actions to blind assessment of predictors for the outcome and other predictors).

### Item 9c (D;E) — Predictors

If predictor measurement requires subjective interpretation, describe the qualifications and demographic characteristics of the predictor assessors.

### Item 10 (D;E) — Sample size

Explain how the study size was arrived at (separately for development and evaluation), and justify that the study size was sufficient to answer the research question. Include details of any sample size calculation.

### Item 11 (D;E) — Missing data

Describe how missing data were handled. Provide reasons for omitting any data.

### Item 12a (D) — Analytical methods

Describe how the data were used (eg, for development and evaluation of model performance) in the analysis, including whether the data were partitioned, considering any sample size requirements.

### Item 12b (D) — Analytical methods

Depending on the type of model, describe how predictors were handled in the analyses (functional form, rescaling, transformation, or any standardisation).

### Item 12c (D) — Analytical methods

Specify the type of model, rationale†, all model building steps, including any hyperparameter tuning, and method for internal validation.

### Item 12d (D;E) — Analytical methods

Describe if and how any heterogeneity in estimates of model parameter values and model performance was handled and quantified across clusters (eg, hospitals, countries). See TRIPOD-Cluster for additional considerations‡.

### Item 12e (D;E) — Analytical methods

Specify all measures and plots used (and their rationale) to evaluate model performance (eg, discrimination, calibration, clinical utility) and, if relevant, to compare multiple models.

### Item 12f (E) — Analytical methods

Describe any model updating (eg, recalibration) arising from the model evaluation, either overall or for particular sociodemographic groups or settings.

### Item 12g (E) — Analytical methods

For model evaluation, describe how the model predictions were calculated (eg, formula, code, object, application programming interface).

### Item 13 (D;E) — Class imbalance

If class imbalance methods were used, state why and how this was done, and any subsequent methods to recalibrate the model or the model predictions.

### Item 14 (D;E) — Fairness

Describe any approaches that were used to address model fairness and their rationale.

### Item 15 (D) — Model output

Specify the output of the prediction model (eg, probabilities, classification). Provide details and rationale for any classification and how the thresholds were identified.

### Item 16 (D;E) — Training versus evaluation

Identify any differences between the development and evaluation data in healthcare setting, eligibility criteria, outcome, and predictors.

### Item 17 (D;E) — Ethical approval

Name the institutional research board or ethics committee that approved the study and describe the participant informed consent or the ethics committee waiver of informed consent.

## Open science

### Item 18a (D;E) — Funding

Give the source of funding and the role of the funders for the present study.

### Item 18b (D;E) — Conflicts of interest

Declare any conflicts of interest and financial disclosures for all authors.

### Item 18c (D;E) — Protocol

Indicate where the study protocol can be accessed or state that a protocol was not prepared.

### Item 18d (D;E) — Registration

Provide registration information for the study, including register name and registration number, or state that the study was not registered.

### Item 18e (D;E) — Data sharing

Provide details of the availability of the study data.

### Item 18f (D;E) — Code sharing

Provide details of the availability of the analytical code§.

## Patient and public involvement

### Item 19 (D;E) — Patient and public involvement

Provide details of any patient and public involvement during the design, conduct, reporting, interpretation, or dissemination of the study or state no involvement.

## Results

### Item 20a (D;E) — Participants

Describe the flow of participants through the study, including the number of participants with and without the outcome and, if applicable, a summary of the follow-up time. A diagram may be helpful.

### Item 20b (D;E) — Participants

Report the characteristics overall and, where applicable, for each data source or setting, including the key dates, key predictors (including demographics), treatments received, sample size, number of outcome events, follow-up time, and amount of missing data. A table may be helpful. Report any differences across key demographic groups.

### Item 20c (E) — Participants

For model evaluation, show a comparison with the development data of the distribution of important predictors (demographics, predictors, and outcome).

### Item 21 (D;E) — Model development

Specify the number of participants and outcome events in each analysis (eg, for model development, hyperparameter tuning, model evaluation).

### Item 22 (D) — Model specification

Provide details of the full prediction model (eg, formula, code, object, application programming interface) to allow predictions in new individuals and to enable third party evaluation and implementation, including any restrictions to access or reuse (eg, freely available, proprietary)¶.

### Item 23a (D;E) — Model performance

Report model performance estimates with confidence intervals, including for any key subgroups (eg, sociodemographic). Consider plots to aid presentation.

### Item 23b (D;E) — Model performance

If examined, report results of any heterogeneity in model performance across clusters. See TRIPOD-Cluster for additional details‡.

### Item 24 (E) — Model updating

Report the results from any model updating, including the updated model and subsequent performance.

## Discussion

### Item 25 (D;E) — Interpretation

Give an overall interpretation of the main results, including issues of fairness in the context of the objectives and previous studies.

### Item 26 (D;E) — Limitations

Discuss any limitations of the study (such as a non-representative sample, sample size, overfitting, missing data) and their effects on any biases, statistical uncertainty, and generalisability.

### Item 27a (D) — Usability of the model in the context of current care

Describe how poor quality or unavailable input data (eg, predictor values) should be assessed and handled when implementing the prediction model.

### Item 27b (D) — Usability of the model in the context of current care

Specify whether users will be required to interact in the handling of the input data or use of the model, and what level of expertise is required of users.

### Item 27c (D;E) — Usability of the model in the context of current care

Discuss any next steps for future research, with a specific view to applicability and generalisability of the model.

## Footnotes

- **\*** D = items relevant only to the development of a prediction model; E = items relating solely to the evaluation of a prediction model; D;E = items applicable to both.
- **†** Separately for all model building approaches.
- **‡** TRIPOD-Cluster is a checklist of reporting recommendations for studies developing or validating models that explicitly account for clustering or explore heterogeneity in model performance (eg, at different hospitals or centres).
- **§** Relates to the analysis code — for example, any data cleaning, feature engineering, model building, and evaluation.
- **¶** Relates to the code to implement the model to get estimates of risk for a new individual.
