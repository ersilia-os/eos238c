# Therapeutic use prediction based on MeSH medical subheadings
## Model identifiers
- Slug: mesh-therapeutic-use
- Ersilia ID: eos238c
- Tags: Therapeutic use, MESH

# Model description
Therapeutic uses expressed as twelve medical subheadings (MeSH) are predicted in a binary classification.
- Input: SMILES
- Output: Therapeutic use (Therapeutic use data according to MESH hierarchies in the PubChem database)
- Model type: Classification
- Training set: 7005 (https://github.com/jgmeyerucsd/drug-class)
- Mode of training: In-house Training
- Validation Summary: 

|Activity  |           CV-1 |  CV-2 |  CV-3  | CV-4 |  CV-5 |  Mean AUROC |
| -------- | -------------- | ------|  ------|------|-------|-------------|
|reproductivecontrol  |0.97   |0.93   |0.99   |0.9    |0.98   |0.96      |
|gastrointestinal     |0.98   |0.92   |0.94   |0.95   |0.93   |0.94      |
|hematologic          |0.94   |0.87   |0.88   |0.98   |0.97   |0.93      |
|antineoplastic       |0.98   |0.96   |0.95   |0.97   |0.96   |0.96      |
|dermatologic         |0.95   |0.84   |0.95   |0.87   |0.88   |0.9       |
|lipidregulating      |0.93   |0.96   |0.92   |0.84   |0.95   |0.92      |
|urological           |0.76   |0.74   |0.64   |0.83   |0.8    |0.75      |
|cns                  |0.97   |0.98   |0.96   |0.97   |0.97   |0.97      |
|cardio               |0.95   |0.96   |0.95   |0.94   |0.96   |0.95      |
|antiinfective        |0.98   |0.99   |0.99   |0.95   |0.97   |0.97      |
|respiratorysystem    |0.88   |0.84   |0.88   |0.93   |0.9    |0.89      |
|antiinflammatory     |0.91   |0.98   |0.92   |0.98   |0.97   |0.95      |

# Source code
Source Publication: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6819987/
- Code: https://github.com/jgmeyerucsd/drug-class
- Checkpoints: N/A

# License
The GPL-v3 license applies to all parts of the repository.

# History 
- Data Preparation:
  - Remove all smiles that overlap among the classes
  - Remove salts from molecules using `rdkit.Chem.SaltRemover`
  - Apply stratified train-test split with 20 percent test data. 
- Training Models:
  - Morgan Binary Classifier from [lazy-qsar](https://github.com/ersilia-os/lazy-qsar) library is used to train models
  - 5-folds Cross-validation is used to validate models
  - Trained models are kept in [models](https://github.com/ersilia-os/eos238c/tree/main/model/framework/models) folder
- Model was incorporated in Ersilia on 10/17/2022

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
