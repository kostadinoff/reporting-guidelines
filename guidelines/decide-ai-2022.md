---
name: DECIDE-AI
full_name: Developmental and Exploratory Clinical Investigation of DEcision support systems driven by Artificial Intelligence
version: "2022"
applies_to: Early-stage live clinical evaluation of AI-based decision support systems
items: 27
numbering: "17 AI-specific items in Arabic numerals; 10 generic items in Roman numerals (I-X)"
citation_key: vasey2022decideai
doi: 10.1038/s41591-022-01772-9
official_url: https://www.decide-ai.org/
licence: "no open licence stated at source — weakest position in this repository"
licence_basis: "Nature Medicine version of record is paywalled; only a green accepted manuscript is openly available and it carries no CC licence. Not covered by EQUATOR terms. Checked 2026-07-28."
source_format: Journal article, Table 2
extracted: verbatim
retrieved: 2026-07-27
last_checked: 2026-07-28
---

# DECIDE-AI

27 items for the **early clinical evaluation** stage — after offline model validation, before
a full randomised trial. It fills the gap between `tripod-ai-2024.md` (model development and
evaluation) and `consort-ai-2020.md` (definitive trial).

Dual numbering, preserved here: **Arabic numerals (1–17)** are AI-specific items; **Roman
numerals (I–X)** are generic items that any early-stage clinical study would report.

What makes it distinctive is that the unit of evaluation is the **human–AI system**, not the
algorithm. Hence item 12 (human–computer agreement, and why users overrode the system),
item 14 (usability and user learning curves), item 3c (how users were familiarised with the
system), and item 11 (modifications made to the system *during* the study — normal at this
stage, and fatal to interpretation if unreported).

Cite as `[@vasey2022decideai]`.

## Title and abstract

### Item 1 — Title

Identify the study as early clinical evaluation of a decision support system based on AI or machine learning, specifying the problem addressed.

### Item I — Abstract

Provide a structured summary of the study. Consider including: intended use of the AI system, type of underlying algorithm, study setting, number of patients and users included, primary and secondary outcomes, key safety endpoints, human factors evaluated, main results, conclusions.

## Introduction

### Item 2 — Intended use

- (a) Describe the targeted medical condition(s) and problem(s), including the current standard practice, and the intended patient population(s).
- (b) Describe the intended users of the AI system, its planned integration in the care pathway, and the potential impact, including patient outcomes, it is intended to have.

### Item II — Objectives

State the study objectives.

## Methods

### Item III — Research governance

Provide a reference to any study protocol, study registration number, and ethics approval.

### Item 3 — Participants

- (a) Describe how patients were recruited, stating the inclusion and exclusion criteria at both patient and data level, and how the number of recruited patients was decided.
- (b) Describe how users were recruited, stating the inclusion and exclusion criteria, and how the intended number of recruited users was decided.
- (c) Describe steps taken to familiarise the users with the AI system, including any training received prior to the study.

### Item 4 — AI system

- (a) Briefly describe the AI system, specifying its version and type of underlying algorithm used. Describe, or provide a direct reference to, the characteristics of the patient population on which the algorithm was trained and its performance in preclinical development/validation studies.
- (b) Identify the data used as inputs. Describe how the data were acquired, the process needed to enter the input data, the pre-processing applied, and how missing/low-quality data were handled.
- (c) Describe the AI system outputs and how they were presented to the users (an image may be useful).

### Item 5 — Implementation

- (a) Describe the settings in which the AI system was evaluated.
- (b) Describe the clinical workflow/care pathway in which the AI system was evaluated, the timing of its use, and how the final supported decision was reached and by whom.

### Item IV — Outcomes

Specify the primary and secondary outcomes measured.

### Item 6 — Safety and errors

- (a) Provide a description of how significant errors/malfunctions were defined and identified.
- (b) Describe how any risks to patient safety or instances of harm were identified, analysed, and minimised.

### Item 7 — Human factors

Describe the human factors tools, methods or frameworks used, the use cases considered, and the users involved.

### Item V — Analysis

Describe the statistical methods by which the primary and secondary outcomes were analysed, as well as any prespecified additional analyses, including subgroup analyses and their rationale.

### Item 8 — Ethics

Describe whether specific methodologies were utilised to fulfil an ethics-related goal (such as algorithmic fairness) and their rationale.

### Item VI — Patient involvement

State how patients were involved in any aspect of: the development of the research question, the study design, and the conduct of the study.

## Results

### Item 9 — Participants

- (a) Describe the baseline characteristics of the patients included in the study, and report on input data missingness.
- (b) Describe the baseline characteristics of the users included in the study.

### Item 10 — Implementation

- (a) Report on the user exposure to the AI system, on the number of instances the AI system was used, and on the users' adherence to the intended implementation.
- (b) Report any significant changes to the clinical workflow or care pathway caused by the AI system.

### Item VII — Main results

Report on the prespecified outcomes, including outcomes for any comparison group if applicable.

### Item VIII — Subgroups analysis

Report on the differences in the main outcomes according to the prespecified subgroups.

### Item 11 — Modifications

Report any changes made to the AI system or its hardware platform during the study. Report the timing of these modifications, the rationale for each, and any changes in outcomes observed after each of them.

### Item 12 — Human-computer agreement

Report on the user agreement with the AI system. Describe any instances of and reasons for user variation from the AI system's recommendations and, if applicable, users changing their mind based on the AI system's recommendations.

### Item 13 — Safety and errors

- (a) List any significant errors/malfunctions related to: AI system recommendations, supporting software/hardware, or users. Include details of: (i) rate of occurrence, (ii) apparent causes, (iii) whether they could be corrected, and (iv) any significant potential impacts on patient care.
- (b) Report on any risks to patient safety or observed instances of harm (including indirect harm) identified during the study.

### Item 14 — Human factors

- (a) Report on the usability evaluation, according to recognised standards or frameworks.
- (b) Report on the user learning curves evaluation.

## Discussion

### Item 15 — Support for intended use

Discuss whether the results obtained support the intended use of the AI system in clinical settings.

### Item 16 — Safety and errors

Discuss what the results indicate about the safety profile of the AI system. Discuss any observed errors/malfunctions and instances of harm, their implications for patient care, and whether/how they can be mitigated.

### Item IX — Strengths and limitations

Discuss the strengths and limitations of the study.

## Statements

### Item 17 — Data availability

Disclose if and how data and relevant code are available.

### Item X — Conflicts of interest

Disclose any relevant conflicts of interest, including the source of funding for the study, the role of funders, any other roles played by commercial companies, and personal conflicts of interest for each author.
