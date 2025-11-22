import os
import sys
import pandas as pd
import numpy as np
import json
from lazyqsar.qsar import LazyBinaryQSAR
from lazyqsar.utils.logging import logger
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
import collections
import shutil

root = os.path.dirname(os.path.abspath(__file__))

def fit_and_evaluate(x_train, x_test, y_train, y_test, output_dir, mode, clean=True, onnx=True):
    logger.info("Binary classification task")
    logger.info("Using featurizer")
    model = LazyBinaryQSAR(mode=mode)
    model.fit(smiles_list=x_train, y=y_train)
    model.save(output_dir, onnx=onnx)
    model = LazyBinaryQSAR.load(output_dir)
    y_pred = model.predict_proba(smiles_list=x_test)[:, 1]
    logger.info("ROC-AUC: {0}".format(roc_auc_score(y_test, y_pred)))
    if clean:
        logger.info("Removing temporary files from {0}".format(output_dir))
        shutil.rmtree(output_dir)
    return roc_auc_score(y_test, y_pred), y_pred

activities = ['antiinfective','antiinflammatory','antineoplastic','cardio',
              'cns','dermatologic','gastrointestinal','hematologic',
              'lipidregulating','reproductivecontrol','respiratorysystem','urological']
for a in activities:
    train_file = os.path.join(root, "..","data", "ml_datasets", f"{a}.csv")
    model_folder = os.path.join(root, "..", "..", "..", "checkpoints", f"{a}")

    if not os.path.exists(model_folder):
        os.makedirs(model_folder)

    train = pd.read_csv(train_file)
    x = train["smiles"].astype(str)
    y = train["bin"].astype(int)

    print("Crossvalidation")
    folds = 5
    roc_aucs = []
    report = collections.defaultdict(dict)
    skf = StratifiedKFold(n_splits=folds, shuffle=True, random_state=42)
    for fold, (train_idx, test_idx) in enumerate(skf.split(x, y)):
        output_dir = os.path.join(model_folder, f"fold_{fold}")
        X_train, X_test = x[train_idx].tolist(), x[test_idx].tolist()
        y_train, y_test = y[train_idx].tolist(), y[test_idx].tolist()
        roc_auc, y_hat = fit_and_evaluate(x_train=X_train, x_test=X_test, y_train=y_train, y_test=y_test, output_dir=output_dir, mode="default")
        print(f"Fold {fold}","AUROC", roc_auc)
        report[fold]["y_true"] = list(y_test)
        report[fold]["y_hat"] = list(y_hat)
        report[fold]["roc_auc"] = roc_auc
        roc_aucs += [roc_auc]

    mean_roc = np.mean(roc_aucs)
    st_dev = np.std(roc_aucs)
    print("MEAN AUC: ", mean_roc, st_dev)

    print("training final model")
    model = LazyBinaryQSAR(mode="default")
    model.fit(smiles_list=x, y=y)
    model.save(model_folder, onnx=True)

    with open(os.path.join(model_folder,f"report_crossval.json"), "w") as f:
        json.dump(report, f, indent=2)