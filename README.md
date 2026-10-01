# SHERLOCK Reproducibility

Notebooks that reproduce the analyses and figures in:

> **SHERLOCK: Structured representation learning and causal inference of downstream perturbation effects**
> Mingxuan Zhang\*, Joshua D. Myers\*, Lingting Shi\*, Ross M. Giglio, Sharanya Chatterjee, José L. McFaline-Figueroa§, Elham Azizi§
> \* Equal contribution · § Senior and corresponding authors

- **Paper (PDF):** [Zhang Myers Shi et al SHERLOCK ….pdf](<Zhang Myers Shi et al SHERLOCK Structured representation learning and causal inference of downstream perturbation effects.pdf>) (included in this repository; we will add the preprint link once it is public)
- **SHERLOCK package:** https://github.com/azizilab/SHERLOCK
- **This repository:** https://github.com/azizilab/SHERLOCK_Reproducibility

## About SHERLOCK

SHERLOCK (Structured representation learning and causal inference of downstream perturbation effects) is a deep generative framework for single-cell perturbation data. It is built on a variational autoencoder. SHERLOCK models each perturbation as a structured intervention on a latent baseline cell state. With this design, SHERLOCK can:

- **learn interpretable perturbation representations.** Perturbation effects are correlated and sparse, so genetic and chemical perturbations are grouped by the transcriptional responses they share.
- **estimate downstream effects causally.** The model applies a perturbation to an inferred baseline state and decodes the resulting counterfactual outcome. This relies on explicit identifiability assumptions within a structural causal model.
- **measure how responses depend on condition.** For example, it compares drug responses in tumor cells with and without T-cell co-culture.
- **model combinations of perturbations.** It predicts held-out combinations and classifies genetic interactions.

## Repository layout

Each dataset has its own folder of notebooks.

| Folder | Dataset | Paper section / figures |
|---|---|---|
| [`drug_screen_with_11_kinases_drugs/`](drug_screen_with_11_kinases_drugs/) | sci-Plex drug screen of 11 kinase inhibitors in BT333 glioblastoma cells, ± T-cell co-culture, at 1 µM and 10 µM (Shi et al.) | *SHERLOCK reveals context-dependent drug responses and their downstream gene programs*: Fig. 3, Figs. S4–S6 |

The paper also analyzes the datasets below. Each table entry gives the public data source from the paper's Data Availability section.

| Dataset | Source |
|---|---|
| Replogle et al. genome-scale Perturb-seq | https://gwps.wi.mit.edu |
| Norman et al. 2019 combinatorial Perturb-seq | [Figshare](https://figshare.com/articles/dataset/Norman_et_al_2019_Science_labeled_Perturb-seq_data/24688110?file=43390776) |
| Spatial perturbation dataset | [Mendeley Data](https://data.mendeley.com/datasets/8kbv637pxh/1) |
| EGFR inhibitor sci-Plex screen (Giglio et al.) | GEO [GSE261618](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE261618) |
| GBM kinase CRISPRi/a and drug screens (Shi et al.) | GEO GSE319938, GSE319348 |

**Intermediate files** such as processed `.h5ad` files and trained model checkpoints will be available on [Google Drive](https://drive.google.com/drive/folders/1Ru4_jC25V0c9LDfVup4o2P8kgKTBKBaD?usp=sharing).

## Setup

The notebooks were run with Python 3.12 and these package versions:

| Package | Version |
|---|---|
| scanpy | 1.11.2 |
| anndata | 0.11.4 |
| torch | 2.7.1 |
| numpy | 1.26.4 |
| pandas | 2.2.2 |
| scipy | 1.13.1 |
| scikit-learn | 1.5.1 |
| seaborn | 0.13.2 |
| matplotlib | 3.9.2 |
| networkx | 3.3 |

To install SHERLOCK:

```bash
git clone https://github.com/azizilab/SHERLOCK.git
```

The notebooks import it with `sys.path.append('../../..')` followed by `import sherlock as slk`. Change that path to wherever you cloned SHERLOCK, or install the package into your environment.

A GPU is used if one is available but is not required. The notebooks load pretrained checkpoints by default, so you do not need to retrain the models.

> **Paths:** The notebooks contain absolute paths from the authors' machines, such as `/home/user/Documents/...`. Before you run them, update the input `.h5ad` paths, the model checkpoint paths (`../data/drug_model_*.pth`) and `figure_dir` to point to your own copies.

---

## Dataset: GBM 11-drug screen ± T cells (`drug_screen_with_11_kinases_drugs/`)

### Data

Patient-derived BT333 glioblastoma cells were profiled with sci-Plex. The cells were treated with 11 candidate immune-modulating kinase inhibitors or with DMSO, at 1 µM and at 10 µM. Each drug was washed out before the cells were co-cultured with tumor antigen-specific cytotoxic T cells (`0.5T`) or cultured without T cells (`NoT`).

**Drugs:** ALWII4127 (EPHA2 inhibitor), CP673451 (PDGFRA inhibitor), Abemaciclib mesylate, BAY1217389, Laduviglusib, PF06260933, SGCAAK11, STK16IN1, Taletrectinib, Tyrphostin9 and Zabedosertib.

Raw data: GEO GSE319348 / GSE319938 (Shi et al., *Mapping kinase-dependent tumor immune adaptation with multiplexed single-cell CRISPR screens*, bioRxiv 2026, doi:10.64898/2026.01.08.698516).

### Notebooks and run order

| # | Notebook | What it does | Main outputs |
|---|---|---|---|
| 1 | [`gbm_preprocess_11drugs_degs_tcellgenes.ipynb`](drug_screen_with_11_kinases_drugs/gbm_preprocess_11drugs_degs_tcellgenes.ipynb) | Quality filtering, gene panel selection, and a PCA-based UMAP for comparison | `bt333_degs_tcell_{1,10}_1000.h5ad`, `{conc}_umaps_with_legends.{svg,png,pdf}` (Fig. 3a) |
| 2 | [`gbm_run_conditions_bt333_with_T_cell_conditions_figures_1um_LS.ipynb`](drug_screen_with_11_kinases_drugs/gbm_run_conditions_bt333_with_T_cell_conditions_figures_1um_LS.ipynb) | SHERLOCK model and analysis at **1 µM** | Latent UMAPs, perturbation correlation and clustering, counterfactual effects, `1um_pert_sensitivity.csv` |
| 3 | [`gbm_run_conditions_bt333_with_T_cell_conditions_figures_10um_LS_this_one.ipynb`](drug_screen_with_11_kinases_drugs/gbm_run_conditions_bt333_with_T_cell_conditions_figures_10um_LS_this_one.ipynb) | SHERLOCK model and analysis at **10 µM**, plus a comparison across concentrations | The same outputs at 10 µM, the 1 vs 10 µM comparison, and the expression of the shared CP/AL targets (Fig. S6) |

Run the notebooks in the order shown above. The comparison cell near the end of notebook 3 reads both `1um_pert_sensitivity.csv` and `10um_pert_sensitivity.csv`, so notebook 2 must finish first.

#### 1. Preprocessing

The notebook takes `CDS_BT333_Tcells_0_cutoff.h5ad` as input. Set `concentration = '1'` and run the first half, then set `concentration = '10'` and run it again. Each run does the following:

1. Keeps cells with a confident hash assignment (hash UMIs > 1 and a top-to-second-best ratio > 2) and more than 500 UMIs.
2. Splits `treatment` into `experiment`, `drug`, `concentration` and `tcell_treatment`.
3. Selects the gene panel as the union of:
   - DEGs for each drug vs DMSO in `NoT` cells (Wilcoxon test, FDR < 0.05)
   - the top 1,000 genes most changed by T-cell co-culture in DMSO cells (`tcdg = 1000`, ranked by |score|)
4. Writes `datasets/gbm/bt333_degs_tcell_{concentration}_1000.h5ad`.

| Concentration | Cells | Genes |
|---|---|---|
| 1 µM | 38,755 | 1,320 |
| 10 µM | 35,511 | 2,894 |

The second half of the notebook makes the PCA-based UMAP that Fig. 3a compares against SHERLOCK.

#### 2–3. SHERLOCK analysis (1 µM and 10 µM)

The two notebooks contain the same steps and differ only in `concentration`:

1. **Configure** SHERLOCK with `pert_key='drug'`, `ntc_label='DMSO'`, `treatment_key='tcell_treatment'` and `untreated_label='NoT'`. Then run `slk.pp.slk_prepare_data` and `slk.pp.treat_effect`.
2. **Train or load the model.** The training call (`slk.tl.run_single`) is commented out, and the notebooks load these pretrained checkpoints instead:
   - 1 µM: `drug_model_20260525_185605_0.pth` (seed 0)
   - 10 µM: `drug_model_20260519_192528_2.pth` (seed 2)

   To retrain, uncomment the `SHERLOCK_KWARGS` dict and the `run_single` and `save_results` cells. The hyperparameters for both concentrations were:
   ```python
   SHERLOCK_KWARGS = dict(
       batch_size=4096, num_epochs=1000, use_conditions=True, validate_every=20,
       l0_lambda=200, patience=500, latent_dim=8, rank=3, n_epochs_l0_warmup=200,
   )
   ```
   These settings give an 8-dimensional latent space, a rank-3 shared covariance and an L0 (hard-concrete) sparse gate. With `use_conditions=True`, each perturbation shift is applied to a control latent background from the matching T-cell condition.
3. **Evaluate** with `slk.tl.eval_single`, which returns the reconstruction R², the latent `z`, the perturbation correlation `rho_corr`, the gate matrix `W`, the counterfactual effect sizes and the condition–perturbation interaction.
4. **Make the figures:**

| Analysis | Output file(s) | Paper |
|---|---|---|
| UMAP of the SHERLOCK latent space, colored by drug and by T-cell condition | `{conc}_sherlock_zspace[_with_legends]` | Fig. 3b |
| Perturbation correlation heatmap and hierarchical clustering (`CLUSTER_T = 0.7`) | `drug_{conc}_correlation_color`, `drug_{conc}uM_dendrogram` | Fig. 3c, S4a |
| Conditional perturbation response: how much each drug's response separates by T-cell condition | `{conc}_condition_effect_on_perturbation`, `{conc}um_pert_sensitivity.csv` | Fig. 3d, S4b |
| Counterfactual downstream genes (top 15) for CP673451 and ALWII4127, `NoT` vs `0.5T` | `{conc}_cf_bipartite_CP673451_ALWII4127_{cond}` | Fig. 3e |
| Significant downstream effects for each drug (q < 0.05) | `figure_ev_sig_*`, `filtered_significant_drug_*.csv` | Fig. S5 |
| Genes shared by AL and CP and genes exclusive to them | `shared_AL_CP_*.csv`, `exclusive_AL_CP_*.csv` | Fig. 3e |
| Expression of the shared CP/AL targets in `0.5T` cells (10 µM only) | `10_cf_bipartite_blue_genes_violin_0.5T` | Fig. S6 |
| CP673451 and ALWII4127 compared across 1 µM and 10 µM (10 µM notebook) | `CP673451_ALWII4127_sensitivity_comparison` | Fig. S4 |
| Diagnostic plots: gate `W` histogram and heatmap, R² and correlation plots | `{conc}_W_histogram`, `{conc}_W_heatmap`, `{conc}_correlation` | n/a |

Each figure is saved to `figure_dir` as `.svg`, `.png` and `.pdf`.

**Main result:** CP673451 (a PDGFRA inhibitor) and ALWII4127 (an EPHA2 inhibitor) have among the lowest conditional perturbation response scores. Their inferred downstream effects become more similar at 10 µM in the presence of T cells. The genes they share (OLIG1, OLIG2, PHGDH, SLC26A2 and GBP1) cover both glioma cell-state programs and interferon-responsive programs.

---

## Citation

If you use SHERLOCK or these notebooks, please cite:

```bibtex
@article{zhang_myers_shi_sherlock,
  title   = {SHERLOCK: Structured representation learning and causal inference of downstream perturbation effects},
  author  = {Zhang, Mingxuan and Myers, Joshua D. and Shi, Lingting and Giglio, Ross M. and
             Chatterjee, Sharanya and McFaline-Figueroa, Jos{\'e} L. and Azizi, Elham},
  year    = {2026}
}
```

## Contact

Please contact the lead contacts with questions:

- José L. McFaline-Figueroa: jm5200@columbia.edu
- Elham Azizi: elham@azizilab.com

You can also open an issue in this repository.
