---
name: CHEERS-AI
full_name: Consolidated Health Economic Evaluation Reporting Standards for Interventions that use Artificial Intelligence
version: "2024"
extends: cheers-2022
applies_to: Health economic evaluations of interventions with an AI component
items: 10
elaborations: 8
citation_key: elvidge2024cheersai
doi: 10.1016/j.jval.2024.05.006
official_url: https://www.equator-network.org/reporting-guidelines/cheers/
licence: CC BY-NC-ND 4.0
licence_basis: "Crossref licence metadata for the version of record (Value in Health, Elsevier). Verified 2026-07-28."
source_format: Journal article, Tables 1-3
extracted: verbatim
retrieved: 2026-07-27
last_checked: 2026-07-28
---

# CHEERS-AI

Two kinds of addition to CHEERS 2022, and the distinction matters:

- **Elaborations** — AI-specific context attached to eight existing CHEERS items (1, 2, 7,
  11, 12, 14, 16, 26). The item itself is unchanged; the elaboration says what it means for
  an AI intervention.
- **Extensions** — ten genuinely new items, numbered **AI 1–AI 10**.

Base items are in `cheers-2022.md`. Where an AI component is a prediction model, its
development and validation should be reported against `tripod-ai-2024.md` and cited from
items AI 4 and AI 5 rather than restated.

The recurring theme is that an adaptive ("learning") AI breaks the standard assumption of a
fixed intervention effect — see AI 3 and AI 8.

Cite as `[@elvidge2024cheersai]`.

## Elaborations on existing CHEERS 2022 items

### Item 1 — Title (elaboration)

Indicate that the intervention involves an AI component that is under evaluation.

**Guidance.** AI refers to algorithmic techniques that analyze large amounts of data for correlations and patterns and use these patterns to simulate the problem-solving and decision-making capabilities of the human mind. This does not include more traditional statistical techniques. If an intervention under evaluation uses AI to perform its function (eg, through algorithms embedded in a digital health technology), then an appropriate term such as "artificial intelligence" should be included in the study title.

### Item 2 — Abstract (elaboration)

Specify the purpose of the intervention with an AI component, and the AI technique used.

**Guidance.** The purpose of the intervention (eg, to treat or diagnose, drive clinical management, inform clinical management) and the way the AI works (eg, deep neural networks for image processing and not traditional statistical techniques) should be reported in the abstract.

### Item 7 — Comparators (elaboration)

Describe key details of the AI component of the intervention (and comparators, if appropriate), including:

- (a) the classification by intended purpose and risk tier (for digital health technologies);
- (b) the AI technique used;
- (c) whether it is "locked" (static) or adaptive;
- (d) the version under evaluation;
- (e) the purpose of the intervention, including its potential impact on care;
- (f) the intended user(s), and how users interact with it;
- (g) additional requirements to use it;
- (h) how it is expected to provide benefit over the standard of care.

**Guidance.** (a) Classification and risk tier can relate to existing regulatory frameworks, such as the SaMD framework proposed by the IMDRF and the evidence standards framework for digital health technologies proposed by NICE. The SaMD framework classifies technologies by intended purpose (critical, serious or nonserious situations) and significance on the healthcare decision (treat or diagnose, drive clinical management, inform clinical management). The NICE framework defines tiers by potential risk (tier A, no direct patient/health/care outcomes; tier B, interventions to assist personal health and wellbeing; tier C, interventions for treating, diagnosing, or guiding care choices). (b) The way the AI works (eg, deep neural networks for image processing) should be reported. (c, d) A "locked" or static AI component does not change over time, whereas an adaptive AI may continue to learn from data and change over time, potentially affecting outcomes. (f) Intended users could include patients, clinicians, healthcare providers, or other agents. (g) Additional requirements could include specific consent processes or staff training. (h) Potential benefits could include clinical effects on health outcomes and economic effects on resource use or system efficiency.

### Item 11 — Selection of outcomes (elaboration)

Describe whether the measure(s) chosen to indicate the benefits and harms of the AI intervention (and comparators) relates to health outcomes, diagnostic outcomes, process outcomes, or other/multiple outcomes.

**Guidance.** An outcome measure is used to quantify the extent to which an intervention has an effect. A study may measure effectiveness in terms of changes in health outcomes, diagnostic outcomes (such as improved accuracy), process outcomes (eg, faster decision making), or several outcomes simultaneously.

### Item 12 — Measurement of outcomes (elaboration)

For model-based analysis, describe any assumptions used to inform the potential benefit(s) and harm(s) of the AI intervention in the model (and comparators, if appropriate). Describe the plausibility of analyst assumptions, citing any supportive evidence.

**Guidance.** Assumptions regarding the effect of the AI intervention, such as the use of arbitrary or exploratory input values, should be transparently reported. Their theoretical or scientific basis should be explained.

### Item 14 — Measurement and valuation of resources and costs (elaboration)

Describe the purchase cost of the AI intervention (and comparators, if appropriate) and what it is composed of. Describe any additional implementation and maintenance costs.

**Guidance.** The purchase cost may include a purchase price and other components, such as the developer implementing the AI into practice or maintaining it over time. There may be other relevant costs to the healthcare system relating to implementation.

### Item 16 — Rationale and description of model (elaboration)

Describe if the AI component of the intervention has influenced the choice of health economic model and explain why.

**Guidance.** Explain if a particular model structure or programming approach, such as individual patient simulation, has been chosen to characterize the AI intervention appropriately.

### Item 26 — Study findings, limitations, generalizability, and current knowledge (elaboration)

Comment on potential biases associated with the AI intervention (eg, algorithmic bias) and implications for the generalizability and interpretation of results (eg, reinforcing existing health inequalities).

**Guidance.** There may be ethical and equity issues associated with AI that are relevant for decision makers alongside the cost-effectiveness results. Biases may include, for example, the AI intervention being developed using a training data set that is not representative of the population of interest.

## New AI-specific extension items

### Item AI 1 — User autonomy (Methods)

Indicate whether the AI intervention (and comparators, if appropriate) is directive, or whether the user(s) retains autonomy to make the care decision.

**Guidance.** How directly the intervention affects clinical care may be defined against existing regulatory frameworks (eg, SaMD): "leads to direct care action" could include the intervention being used for definitive diagnosis, or itself being a treatment; "drives clinical management" means it aids treatment, diagnosis or decision making in a supportive way; "informs clinical management" means no direct care action, for example informing users of options or providing information.

### Item AI 2 — Measurement of AI effect (Methods)

Describe the data sources (assessment studies) for the AI intervention's impact on outcomes.

**Guidance.** This relates to the evidence informing the impact of the AI intervention. For interventions that directly affect care (eg, treatments), these may be clinical trials evaluating efficacy. For interventions that drive or inform care (eg, diagnostic algorithms), these may be diagnostic studies reporting predictive accuracy. In the absence of evidence, analyst assumptions may be required. **This is not the same as "training data"**, which an AI component might learn from during development.

### Item AI 3 — Measurement of AI learning over time (Methods)

If the AI intervention (and comparators, if appropriate) learns over time, explain how this affects its performance at the individual level and how this was measured.

**Guidance.** An intervention with a "learning" (adaptive) AI component may become more effective over time as it learns from data collected during its use. How this learning effect was measured should be reported or signposted using a suitable citation.

### Item AI 4 — Development of AI component (Methods)

Describe how the AI component of the intervention (and comparators, if appropriate) was developed, including the training data used and how errors and biases were identified, or cite a source that provides this information.

**Guidance.** May be signposted using a suitable citation — for example a completed TRIPOD+AI checklist for prediction model development.

### Item AI 5 — Validation of AI component (Methods)

Describe how the AI component of the intervention (and comparators, as appropriate) and its performance estimates were validated, or cite a source that provides this information.

**Guidance.** As with traditional statistical techniques, internal and external validity should be described or signposted — for example a completed TRIPOD+AI checklist for prediction model validation.

### Item AI 6 — Health benefit (Methods)

Describe how the AI intervention (and comparators, if appropriate) could directly or indirectly provide a health benefit.

**Guidance.** "Health benefit" refers to the way an intervention affects health outcomes, which can be quantified to estimate incremental cost-effectiveness. AI interventions may have different mechanisms for generating health benefits. For example, an AI-based digital health technology designed to inform clinical management (with no direct care action) may have an indirect effect on health outcomes.

### Item AI 7 — Population differences (Methods)

Describe important differences between the data sources (assessment studies) for the AI intervention's impact on outcomes and the data set that was used to develop the AI intervention (training data set).

**Guidance.** The data used to develop the AI component may be referred to as its "training" data set. This may differ from the study population used to examine the beneficial impact of the intervention compared with alternatives.

### Item AI 8 — Modeling of AI learning over time (Methods)

If the AI intervention (and comparators, if appropriate) learns over time at the individual level, describe any assumptions used to model how this learning affects its performance over time.

**Guidance.** Any modeling assumptions capturing an adaptive component's improvement over time should be transparently reported.

### Item AI 9 — Impact of AI uncertainty (Results)

Indicate the extent to which features of the AI intervention may contribute to increased uncertainty about its cost-effectiveness.

**Guidance.** Uncertainty is usually characterized as random error, parameter uncertainty or structural uncertainty. The AI nature of an intervention may contribute disproportionately to one or more of these. AI-specific uncertainties and their potential implications on study results should be reported.

### Item AI 10 — Implementation of AI (Discussion)

Comment on any requirements needed to integrate the AI intervention (and comparators, as appropriate) into practice, and other implementation considerations relating to the AI component of the intervention, including implications for the interpretation of cost-effectiveness results.

**Guidance.** Requirements may include necessary software distinct from standard clinical equipment, or a new data acquisition process. Barriers to implementing a new technology may be relevant for decision makers alongside the cost-effectiveness results.
