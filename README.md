# MeSH therapeutic use based on chemical structure

Assigns a molecule to twelve broad therapeutic categories taken from the MeSH therapeutic use vocabulary, inferring likely clinical purpose straight from structure. Meyer and colleagues gathered 6955 PubChem compounds each falling in exactly one of the twelve classes, reaching 83 to 88 percent accuracy with convolutional networks on molecule images and random forests on Morgan fingerprints. Ersilia replicates the task with twelve independent binary classifiers, so several categories can score highly for one compound even though the training labels were exclusive.

This model was incorporated on 2022-10-12.
Last packaged on 2026-10-28.

## Information
### Identifiers
- **Ersilia Identifier:** `eos238c`
- **Slug:** `mesh-therapeutic-use`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Therapeutic indication`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `12`
- **Output Consistency:** `Fixed`
- **Interpretation:** Rank scores for twelve MeSH therapeutic use classes from twelve independent classifiers, calibrated against the Ersilia reference library of 50K compounds, where 0.65 beats 99% of it.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| antiinfective_rank | float | high | Rank score of how likely the compound is to belong to the anti-infective therapeutic use class as defined by MeSH. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| antiinflammatory_rank | float | high | Rank score of how likely the compound is to belong to the anti-inflammatory therapeutic use class as defined by MeSH. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| antineoplastic_rank | float | high | Rank score of how likely the compound is to belong to the antineoplastic therapeutic use class as defined by MeSH. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| cardio_rank | float | high | Rank score of how likely the compound is to belong to the cardiovascular therapeutic use class as defined by MeSH. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| cns_rank | float | high | Rank score of how likely the compound is to belong to the central nervous system therapeutic use class as defined by MeSH. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| dermatologic_rank | float | high | Rank score of how likely the compound is to belong to the dermatologic therapeutic use class as defined by MeSH. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| gastrointestinal_rank | float | high | Rank score of how likely the compound is to belong to the gastrointestinal therapeutic use class as defined by MeSH. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| hematologic_rank | float | high | Rank score of how likely the compound is to belong to the hematologic therapeutic use class as defined by MeSH. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| lipidregulating_rank | float | high | Rank score of how likely the compound is to belong to the lipid regulating therapeutic use class as defined by MeSH. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| reproductivecontrol_rank | float | high | Rank score of how likely the compound is to belong to the reproductive control therapeutic use class as defined by MeSH. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |

_10 of 12 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Replicated`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos238c](https://hub.docker.com/r/ersiliaos/eos238c)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos238c.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos238c.zip)

### Resource Consumption
- **Model Size (Mb):** `106`
- **Environment Size (Mb):** `7552`
- **Image Size (Mb):** `7584`

**Computational Performance (seconds):**
- 10 inputs: `70.76`
- 100 inputs: `70.21`
- 10000 inputs: `1602.39`

### References
- **Source Code**: [https://github.com/jgmeyerucsd/drug-class](https://github.com/jgmeyerucsd/drug-class)
- **Publication**: [https://doi.org/10.1021/acs.jcim.9b00236](https://doi.org/10.1021/acs.jcim.9b00236)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2019`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos238c
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos238c
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
