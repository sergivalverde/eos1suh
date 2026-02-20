import os
import csv
import sys

from biosynfoni import Biosynfoni
from biosynfoni.subkeys import fpVersions
from rdkit import Chem

# Parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Get column names from the default version
column_names = fpVersions["full_1103"]

# Read input
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# Run model
outputs = []
for smi in smiles_list:
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        outputs.append([0] * len(column_names))
    else:
        fp = Biosynfoni(mol).fingerprint
        outputs.append(fp)

# Verify
assert len(smiles_list) == len(outputs)

# Write output
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(column_names)
    for o in outputs:
        writer.writerow(o)
