# `results/`: saved models and intermediate results (placeholder)

This folder is a placeholder; its contents are not tracked by git. The figure notebooks read the
saved models and cached results from here, so the figures can be regenerated without retraining.
The saved models from the manuscript will be released with the published version of the
paper; until then, regenerate them with the notebooks in `scripts/`. To keep them elsewhere:

```bash
export SHERLOCK_RESULTS_DIR=/path/to/results
```

All paths resolve from `RESULTS_DIR` (see `../paths.py`).

## Saved SHERLOCK models (`results/models/`)

| File | Dataset | Written by |
|---|---|---|
| `replogle_model_1.pth` | Replogle (Fig. 1d–f) | `scripts/replogle/1_replogle_analysis` |
| `raefish_model_20260603_112214_3.pth` | RAEFISH | `scripts/raefish/2_raefish_analysis` |
| `drug_egfr_model_20260529_163520_1.pth` | EGFR screen | `scripts/egfr_drug_screen/2_egfr_analysis` |
| `drug_model_20260525_185605_0.pth` | 11 drugs, 1 µM | `scripts/kinase_inhibitors_tcell/2_analysis_1uM` |
| `drug_model_20260519_192528_2.pth` | 11 drugs, 10 µM | `scripts/kinase_inhibitors_tcell/3_analysis_10uM` |

The file names carry the training time stamp and seed. The notebooks load these exact files; a
newly trained model is saved under a new time stamp, so update the load cell to use it.

## Multi-run analyses

| Folder | Contents | Written by |
|---|---|---|
| `benchmarking/` | `models/<method>/run_{0..4}.pth` and `best.pth` for SHERLOCK, cVAE, sVAE, contrastiveVI and scGen; cached robustness matrices | `scripts/replogle/2_benchmarking` |
| `reproducibility_meta_bootstrap_only_v1_noconditions_v2/` | CRISPRi: per-run matrices (`matrices/run_{i}*`), `matrices/best_model.pth`, figures | `scripts/kinome_crispri_crispra/2a_reproducibility_crispri` |
| `reproducibility_meta_bootstrap_only_v1_noconditions_v2_treated_crispra/` | CRISPRa: the same | `scripts/kinome_crispri_crispra/2b_reproducibility_crispra` |
| `reproducibility_drug/` | 11 drugs, 10 µM: per-run matrices (`matrices/run_{i}.npz`), `matrices/best_model.pth`, figures | `scripts/kinase_inhibitors_tcell/4_reproducibility_10uM` |
| `norman_figure/` | `models/run_{1..5}.pth`, `benchmark_models/`, `gears_models/`, `gears_runs/`, per-run metrics and genetic-interaction scores, `run_matrices.npz` | `scripts/norman/1_norman_analysis` |
| `gears_data/` | GEARS's preprocessed copy of the Norman data and its gene-ontology graph | `scripts/norman/1_norman_analysis` (GEARS) |
| `module_interaction/` | `consensus_modules.csv`, `model_features/run_{1..5}.npz`, `factor_signatures.npz` | `scripts/norman/3_module_interaction` |

Every multi-run notebook checks for a run's saved files before training it, so a populated
`results/` folder skips all training.
