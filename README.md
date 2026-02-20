# BioSynFoni: Biosynthesis-Informed Molecular Fingerprint

**Ersilia Model ID:** `eos1suh`

| | |
|---|---|
| **Task** | Representation / Featurization |
| **Input** | Single SMILES |
| **Output** | 39-dimensional integer count vector |
| **Framework** | [biosynfoni](https://github.com/lucinamay/biosynfoni) v1.0.0 |
| **License** | MIT |

## Description

BioSynFoni is a biosynthesis-informed count-based molecular fingerprint designed for natural product research. It decomposes molecules into 39 biosynthetic building block substructures derived from Dewick's classification of natural product biosynthetic pathways, including coenzymes, amino acids, sugars, shikimate, acetate, and terpenoid pathway building blocks, as well as halogens, functional groups, and carbon ring systems.

The fingerprint is computed via SMARTS substructure matching using RDKit and returns an integer count vector. It was shown to outperform MACCS, Morgan, and Daylight-like fingerprints for biosynthetic distance estimation and performs comparably for natural product classification while being more compact and interpretable.

## Interpretation

Each of the 39 integers counts occurrences of a biosynthetic building block substructure in the molecule. Higher counts mean more of that motif. Useful for natural product classification and biosynthetic distance estimation.

## Source

- **Publication:** [Schomaker et al., J Cheminform 2025](https://doi.org/10.1186/s13321-025-01081-6)
- **Source Code:** https://github.com/lucinamay/biosynfoni

## Deep Validation

| Check | Status | Details |
|-------|--------|---------|
| Distribution (50 molecules) | PASS | 100% valid, 27/39 columns vary (69%), runtime 0.02s |
| Sanity (fingerprint similarity) | PASS | Similar pair 0.98 > dissimilar 0.88 |
| Paper reproduction (biosynthetic classes) | PASS | Within-class 0.94 > between-class 0.68 (1.38x separation) |

**Overall: PASS (3/3)**

### Highlights

- **Distribution analysis:** 50 diverse molecules processed in 0.02s. 27 of 39 fingerprint dimensions show variation. Constant dimensions (12) correspond to rare building blocks (CoA, NADH, NADPH, bromide, iodide, epoxides, etc.) absent in common drug-like molecules.

- **Sanity check:** Aspirin and salicylic acid (structurally related) have cosine similarity 0.98, while eicosane and adenine (unrelated) have 0.88 — correct directional separation.

- **Paper reproduction:** 23 natural products across 6 biosynthetic classes (alkaloid, isoprenoid, phenylpropanoid, carbohydrate, fatty acid, polyketide). Within-class cosine similarity (0.94) is significantly higher than between-class (0.68), confirming the paper's claim that BioSynFoni captures biosynthetic origin. Fatty acids show near-perfect within-class similarity (0.9999).

See [`deep_validation.ipynb`](deep_validation.ipynb) for full analysis with visualizations.

## Usage

```python
# Input CSV format
# smiles
# CC(=O)Oc1ccccc1C(=O)O
# c1ccccc1

python model/framework/code/main.py input.csv output.csv
```

## Dependencies

```yaml
python: "3.10"
commands:
    - ["pip", "biosynfoni", "1.0.0"]
```
