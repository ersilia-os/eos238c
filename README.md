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

# Source code
Cite the source publication.
- Code: include link to the source code
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
  - Trained models' parameters are kept in [models](https://github.com/ersilia-os/eos238c/tree/main/model/framework/models)
Model was incorporated in Ersilia on 10/17/2022

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
