---
name: RECORD
full_name: REporting of studies Conducted using Observational Routinely-collected health Data
version: "2015"
extends: strobe-2007
applies_to: Observational studies using routinely-collected health data — administrative claims, EHR, registries
items: 13
citation_key: benchimol2015record
doi: 10.1371/journal.pmed.1001885
official_url: https://www.record-statement.org/
licence: CC BY 4.0
licence_basis: PLOS (all articles CC BY 4.0 by publisher policy)
source_format: Journal article, checklist table
extracted: verbatim
retrieved: 2026-07-27
last_checked: 2026-07-27
---

# RECORD

13 items **extending STROBE**, not replacing it. Item numbers map onto the STROBE item they
extend: RECORD 6.1–6.3 elaborate STROBE item 6 (participants), 7.1 elaborates STROBE item 7
(variables), and so on.

**Use both files.** Complete `strobe-2007.md` first, then add these. An article reporting a
routinely-collected-data study against STROBE alone is incomplete.

The most consequential items for administrative data are **6.1** (the codes or algorithms
used to identify participants), **7.1** (the complete code list for exposures, outcomes and
confounders), and **12.3** (linkage methods and linkage-quality evaluation) — these are what
make a claims-based study reproducible.

Cite as `[@benchimol2015record]`. See also `record-pe-2018.md` for pharmacoepidemiology and
`code-ehr-2022.md` for structured EHR reporting.

## Title and abstract — extends STROBE item 1

### Item 1.1

The type of data used should be specified in the title or abstract. When possible, the name of the databases used should be included.

### Item 1.2

If applicable, the geographical region and timeframe within which the study took place should be reported in the title or abstract.

### Item 1.3

If linkage between databases was conducted for the study, this should be clearly stated in the title or abstract.

## Methods: participants — extends STROBE item 6

### Item 6.1

The methods of study population selection (such as codes or algorithms used to identify participants) should be listed in detail. If this is not possible, an explanation should be provided.

### Item 6.2

Any validation studies of the codes or algorithms used to select the population should be referenced. If validation was conducted for this study and not published elsewhere, detailed methods and results should be provided.

### Item 6.3

If the study involved linkage of databases, consider use of a flow diagram or other graphical display to demonstrate the data linkage process, including the number of individuals with linked data at each stage.

## Methods: variables — extends STROBE item 7

### Item 7.1

A complete list of codes and algorithms used to classify exposures, outcomes, confounders, and effect modifiers should be provided. If these cannot be reported, an explanation should be provided.

## Methods: statistical methods — extends STROBE item 12

### Item 12.1

Authors should describe the extent to which the investigators had access to the database population used to create the study population.

### Item 12.2

Authors should provide information on the data cleaning methods used in the study.

### Item 12.3

State whether the study included person level, institutional level, or other data linkage across two or more databases. The methods of linkage and methods of linkage quality evaluation should be provided.

## Results: participants — extends STROBE item 13

### Item 13.1

Describe in detail the selection of the individuals included in the study (that is, study population selection) including filtering based on data quality, data availability, and linkage. The selection of included individuals can be described in the text or by means of the study flow diagram.

## Discussion: limitations — extends STROBE item 19

### Item 19.1

Discuss the implications of using data that were not created or collected to answer the specific research question(s). Include discussion of misclassification bias, unmeasured confounding, missing data, and changing eligibility over time, as they pertain to the study being reported.

## Other information — extends STROBE item 22

### Item 22.1

Authors should provide information on how to access any supplemental information such as the study protocol, raw data, or programming code.
