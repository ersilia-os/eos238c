# MeSH therapeutic use based on chemical structure

Drug function, defined as Medical Subject Headings (MeSH) “therapeutic use” is predicted based on the chemical structure. 6955 non-redundant molecules, pertaining to one of the twelve therapeutic use classes selected, were downloaded from PubChem and used to train a binary classifier. The model provides the probability that a molecule has one of the following therapeutic uses: antineoplastic, cardiovascular, central nervous system (CNS), anti-infective, gastrointestinal, anti-inflammatory, dermatological, hematologic, lipid regulating, reproductive control, respiratory system, urological.

This model was incorporated on 2022-10-12.


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
- **Interpretation:** Probability that the molecule belongs to each therapeutic use specified.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| antiinfective | float | high | Probability that the molecule has an effect on the antiinfective therapeutic area as defined by MeSH |
| antiinflammatory | float | high | Probability that the molecule has an effect on the antiinflamatory therapeutic area as defined by MeSH |
| antineoplastic | float | high | Probability that the molecule has an effect on the antneoplastic therapeutic area as defined by MeSH |
| cardio | float | high | Probability that the molecule has an effect on the cardiovascular therapeutic area as defined by MeSH |
| cns | float | high | Probability that the molecule has an effect on the central nervous system therapeutic area as defined by MeSH |
| dermatologic | float | high | Probability that the molecule has an effect on the dermatologic therapeutic area as defined by MeSH |
| gastrointestinal | float | high | Probability that the molecule has an effect on the gastrointestinal therapeutic area as defined by MeSH |
| hematologic | float | high | Probability that the molecule has an effect on the hematologic therapeutic area as defined by MeSH |
| lipidregulating | float | high | Probability that the molecule has an effect on the lipid regulating therapeutic area as defined by MeSH |
| reproductivecontrol | float | high | Probability that the molecule has an effect on the reproductive control therapeutic area as defined by MeSH |

_10 of 12 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos238c](https://hub.docker.com/r/ersiliaos/eos238c)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos238c.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos238c.zip)

### Resource Consumption
- **Model Size (Mb):** `28`
- **Environment Size (Mb):** `1421`


### References
- **Source Code**: [https://github.com/jgmeyerucsd/drug-class](https://github.com/jgmeyerucsd/drug-class)
- **Publication**: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6819987/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6819987/)
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
