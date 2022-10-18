# imports
import os
import sys
import pandas as pd
import joblib

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# model directory
model_dir = os.path.abspath(os.path.join(root, "..", "models"))

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

activities = ['antiinfective','antiinflammatory','antineoplastic','cardio',
              'cns','dermatologic','gastrointestinal','hematologic',
              'lipidregulating','reproductivecontrol','respiratorysystem','urological']
              
df_results = pd.read_csv(input_file, sep=" ",skiprows=1, header=None, names=['Smiles'])
input_smiles = df_results['Smiles'].tolist()

for activity in activities:
    model_path = os.path.join(model_dir, activity+'.joblib')
    model = joblib.load(model_path)
    y_hat = model.predict_proba(input_smiles)
    df_results[activity] = y_hat[:,1]
    
df_results.to_csv(output_file,index=False)
