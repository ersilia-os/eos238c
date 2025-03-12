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
model_dir = os.path.abspath(os.path.join(root, "..","..","checkpoints"))

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

activities = ['antiinfective_use','antiinflammatory_use','antineoplastic_use','cardiovascular_use',
              'central_nervous_system_use','dermatologic_use','gastrointestinal_use','hematologic_use',
              'lipid_regulating_use','reproductive_control_use','respiratory_system_use','urological_use']
              
df_results = pd.read_csv(input_file, sep=" ",skiprows=1, header=None, names=['Smiles'])
input_smiles = df_results['Smiles'].tolist()

for activity in activities:
    model_path = os.path.join(model_dir, activity+'.joblib')
    model = joblib.load(model_path)
    y_hat = model.predict_proba(input_smiles)
    df_results[activity] = y_hat[:,1]
    
df_results.to_csv(output_file,index=False)
