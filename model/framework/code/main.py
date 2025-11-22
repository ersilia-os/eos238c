import os
import csv
import sys
from lazyqsar.qsar import LazyBinaryQSAR

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

MODELPATH = os.path.join(root, "..", "..", "checkpoints")

models = ['antiinfective','antiinflammatory','antineoplastic','cardio',
              'cns','dermatologic','gastrointestinal','hematologic',
              'lipidregulating','reproductivecontrol','respiratorysystem','urological']

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
y_preds = {}
for m in models:
    model_folder = os.path.join(MODELPATH, f"{m}")
    model = LazyBinaryQSAR.load(model_folder)
    y_pred = model.predict_proba(smiles_list=smiles_list)[:, 1]
    y_preds[m]=y_pred

header = list(y_preds.keys())

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(models) 
    for o1, o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 in zip(*(y_preds[m].tolist() for m in header)):
        writer.writerow([o1, o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12])