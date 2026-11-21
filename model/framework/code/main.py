import os
import sys

import numpy as np
from ersilia_pack_utils.core import read_smiles, write_out
from lazyqsar.qsar import LazyClassifierQSAR

root = os.path.dirname(os.path.abspath(__file__))
checkpoints = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

# output column -> checkpoint folder, in the order of run_columns.csv
MODELS = {
    "antiinfective_rank": "antiinfective",
    "antiinflammatory_rank": "antiinflammatory",
    "antineoplastic_rank": "antineoplastic",
    "cardio_rank": "cardio",
    "cns_rank": "cns",
    "dermatologic_rank": "dermatologic",
    "gastrointestinal_rank": "gastrointestinal",
    "hematologic_rank": "hematologic",
    "lipidregulating_rank": "lipidregulating",
    "reproductivecontrol_rank": "reproductivecontrol",
    "respiratorysystem_rank": "respiratorysystem",
    "urological_rank": "urological",
}


# Load every checkpoint once. When served, Ersilia calls this a single time and keeps
# the loaded models (descriptors and ONNX graphs) in memory between batches.
def load_tool():
    return {
        column: LazyClassifierQSAR.load(os.path.join(checkpoints, folder))
        for column, folder in MODELS.items()
    }


# Predict one batch. Nothing is loaded here and nothing is kept between batches.
def run_tool(models, input_file, output_file):
    _, smiles_list = read_smiles(input_file)
    columns = []
    for model in models.values():
        columns.append(model.predict_rank(smiles_list=smiles_list)[:, 1])
        # The loaded model caches every result it computes; clear it so a long-lived
        # served process does not grow with each batch.
        model._ensemble_cache.clear()
    outputs = np.column_stack(columns)
    assert outputs.shape[0] == len(smiles_list)
    if output_file.endswith(".csv"):
        # Unparseable SMILES come back as NaN; in a CSV Ersilia reports them as empty
        # cells. The binary format takes the array as is.
        outputs = [["" if v != v else v for v in row] for row in outputs.tolist()]
    write_out(outputs, list(models.keys()), output_file, np.float32)


if __name__ == "__main__":
    run_tool(load_tool(), sys.argv[1], sys.argv[2])
