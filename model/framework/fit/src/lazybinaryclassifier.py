import os
import sys
import pandas as pd
import numpy as np
import json
from lazyqsar.qsar import LazyClassifierQSAR
from lazyqsar.utils.logging import logger
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
import collections
import shutil

root = os.path.dirname(os.path.abspath(__file__))

# One binary task per MeSH therapeutic use class (Meyer et al. 2019).
TASKS = {a: (f"{a}.csv", "bin") for a in [
    "antiinfective", "antiinflammatory", "antineoplastic", "cardio",
    "cns", "dermatologic", "gastrointestinal", "hematologic",
    "lipidregulating", "reproductivecontrol", "respiratorysystem", "urological",
]}

task = sys.argv[1]
data_file, label = TASKS[task]

train_file = os.path.join(root, "..", "data", "ml_datasets", data_file)
model_folder = os.path.join(root, "..", "..", "..", "checkpoints", task)

if not os.path.exists(model_folder):
    os.makedirs(model_folder)

train = pd.read_csv(train_file)
x = train["smiles"].astype(str)
y = train[label].astype(int)


def fit_and_evaluate(x_train, x_test, y_train, y_test, output_dir, mode, clean=True):
    logger.info("Binary classification task")
    logger.info("Using featurizer")
    model = LazyClassifierQSAR(mode=mode)
    model.fit(smiles_list=x_train, y=y_train)
    model.save(output_dir)
    model = LazyClassifierQSAR.load(output_dir)
    y_pred = model.predict_proba(smiles_list=x_test)[:, 1]
    logger.info("ROC-AUC: {0}".format(roc_auc_score(y_test, y_pred)))
    if clean:
        logger.info("Removing temporary files from {0}".format(output_dir))
        shutil.rmtree(output_dir)
    return roc_auc_score(y_test, y_pred), y_pred


print(f"Crossvalidation [{task}] n={len(x)} actives={int(y.sum())}", flush=True)
folds = 5
roc_aucs = []
report = collections.defaultdict(dict)
skf = StratifiedKFold(n_splits=folds, shuffle=True, random_state=42)
for fold, (train_idx, test_idx) in enumerate(skf.split(x, y)):
    output_dir = os.path.join(model_folder, f"fold_{fold}")
    X_train, X_test = x[train_idx].tolist(), x[test_idx].tolist()
    y_train, y_test = y[train_idx].tolist(), y[test_idx].tolist()
    roc_auc, y_hat = fit_and_evaluate(x_train=X_train, x_test=X_test, y_train=y_train, y_test=y_test, output_dir=output_dir, mode="slow")
    print(f"Fold {fold}", "AUROC", roc_auc, flush=True)
    report[fold]["y_true"] = list(y_test)
    report[fold]["y_hat"] = [float(v) for v in y_hat]
    report[fold]["roc_auc"] = roc_auc
    roc_aucs += [roc_auc]

mean_roc = np.mean(roc_aucs)
st_dev = np.std(roc_aucs)
print("MEAN AUC: ", mean_roc, st_dev, flush=True)

with open(os.path.join(model_folder, "report_crossval.json"), "w") as f:
    json.dump(report, f, indent=2)

print("training final model", flush=True)
model = LazyClassifierQSAR(mode="slow")
model.fit(smiles_list=x.tolist(), y=y.tolist())
model.save(model_folder)
