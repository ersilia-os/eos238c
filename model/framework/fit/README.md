# Fit folder: mesh-therapeutic-use (eos238c)

This folder holds the data, code and results needed to rebuild the model. It is stored with
[eosvc](https://github.com/ersilia-os/eosvc) in the **public** bucket; only this README is
tracked in git.

## Data processing

`notebooks/00_data_processing.ipynb` turns the per-class PubChem files (`data/*_smiles_rmsaltol.csv`) into the twelve binary training sets in `data/ml_datasets/`.

## Model building

`src/01_fit_oof.py` builds one LazyQSAR 3.9.3 classifier per task, in slow mode. For each task
it runs five-fold stratified out-of-fold (OOF) cross-validation (seed 42), so every compound
gets one prediction from a model that never saw it. It writes the OOF predictions and metrics to
`results/`, then trains the final model on all compounds into `model/checkpoints/<task>/`.
`src/02_performance.py` plots the OOF ROC curve and the OOF rank of actives and inactives per
task, and collects all metrics in `results/oof_metrics.json`.

```bash
cd src
OMP_NUM_THREADS=1 python 01_fit_oof.py        # or one task: python 01_fit_oof.py antiinfective
python 02_performance.py
```

| Task | Output column | Training file | Compounds | Actives | OOF AUROC | Descriptors in final model |
|---|---|---|---|---|---|---|
| `antiinfective` | `antiinfective_rank` | `data/ml_datasets/antiinfective.csv` | 6,948 | 2,398 | 0.984 | chemeleon, clamp |
| `antiinflammatory` | `antiinflammatory_rank` | `data/ml_datasets/antiinflammatory.csv` | 6,948 | 373 | 0.977 | chemeleon, clamp, morgan |
| `antineoplastic` | `antineoplastic_rank` | `data/ml_datasets/antineoplastic.csv` | 6,948 | 1,177 | 0.980 | chemeleon, clamp, morgan |
| `cardio` | `cardio_rank` | `data/ml_datasets/cardio.csv` | 6,948 | 788 | 0.971 | chemeleon, clamp, morgan |
| `cns` | `cns_rank` | `data/ml_datasets/cns.csv` | 6,948 | 1,139 | 0.980 | chemeleon, clamp, morgan |
| `dermatologic` | `dermatologic_rank` | `data/ml_datasets/dermatologic.csv` | 6,948 | 116 | 0.938 | chemeleon, morgan, clamp |
| `gastrointestinal` | `gastrointestinal_rank` | `data/ml_datasets/gastrointestinal.csv` | 6,948 | 258 | 0.961 | chemeleon, clamp, morgan |
| `hematologic` | `hematologic_rank` | `data/ml_datasets/hematologic.csv` | 6,948 | 267 | 0.947 | chemeleon, clamp, morgan |
| `lipidregulating` | `lipidregulating_rank` | `data/ml_datasets/lipidregulating.csv` | 6,948 | 164 | 0.961 | chemeleon, morgan, clamp |
| `reproductivecontrol` | `reproductivecontrol_rank` | `data/ml_datasets/reproductivecontrol.csv` | 6,948 | 148 | 0.981 | chemeleon, clamp, morgan |
| `respiratorysystem` | `respiratorysystem_rank` | `data/ml_datasets/respiratorysystem.csv` | 6,948 | 101 | 0.933 | chemeleon, clamp, morgan |
| `urological` | `urological_rank` | `data/ml_datasets/urological.csv` | 6,948 | 26 | 0.868 | chemeleon, morgan, clamp |
