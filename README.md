<p align="center">
  <img src="SHERLOCK_logo.png" alt="SHERLOCK logo" width="420">
</p>

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

## Contents

| Folder | Dataset | Technology | Paper figures |
|---|---|---|---|
| [`genetic_screen_genome_wide_crispri/`](genetic_screen_genome_wide_crispri/) | Replogle et al. genome-scale CRISPRi Perturb-seq (K562) | 10x Chromium | Fig. 1d–f |
| [`genetic_screen_spatial_reafish/`](genetic_screen_spatial_reafish/) | Perturb-RAEFISH spatial CRISPR screen | Imaging (RAEFISH) | Fig. 2a–d |
| [`drug_screen_with EGFR_inhibitors/`](<drug_screen_with EGFR_inhibitors/>) | EGFR / kinase-pathway inhibitor screen in BT333 glioblastoma cells (Giglio et al.) | sci-Plex | Fig. 2e–h, Fig. S2 |
| [`genetic_screen_kinome-wide_crispria/`](genetic_screen_kinome-wide_crispria/) | Kinome CRISPRi and CRISPRa screens in BT333 cells under T-cell co-culture (Shi et al.) | sci-Plex | Fig. 2i–j, Fig. S3 |
| [`drug_screen_with_11_kinases_inhibitors/`](drug_screen_with_11_kinases_inhibitors/) | 11 kinase inhibitors in BT333 cells ± T cells, at 1 µM and 10 µM (Shi et al.) | sci-Plex | Fig. 3, Figs. S4–S6 |
| [`genetic_screen_combinatorial_crispra/`](genetic_screen_combinatorial_crispra/) | Norman et al. 2019 combinatorial CRISPRa Perturb-seq | 10x Chromium | Fig. 4, Figs. S7–S15 (*notebooks coming soon*) |

## Data sources

The original data are public. If you use any of these datasets, please also cite the original study (full references are in [Citation](#citation)):

| Dataset | Original study | Source |
|---|---|---|
| Genome-scale CRISPRi Perturb-seq | Replogle et al., *Cell* 2022 ([doi:10.1016/j.cell.2022.05.013](https://doi.org/10.1016/j.cell.2022.05.013)) | https://gwps.wi.mit.edu |
| Spatial perturbation dataset (Perturb-RAEFISH) | Cheng et al., *Cell* 2025 ([doi:10.1016/j.cell.2025.09.006](https://doi.org/10.1016/j.cell.2025.09.006)) | [Mendeley Data](https://data.mendeley.com/datasets/8kbv637pxh/1) |
| EGFR inhibitor sci-Plex screen | Giglio et al., *bioRxiv* 2025 ([doi:10.1101/2024.04.08.587960](https://doi.org/10.1101/2024.04.08.587960)) | GEO [GSE261618](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE261618) |
| GBM kinome CRISPRi/a and 11-drug screens | Shi et al., *bioRxiv* 2026 ([doi:10.64898/2026.01.08.698516](https://doi.org/10.64898/2026.01.08.698516)) | Not yet publicly available |
| Combinatorial CRISPRa Perturb-seq | Norman et al., *Science* 2019 ([doi:10.1126/science.aax4438](https://doi.org/10.1126/science.aax4438)) | [Figshare](https://figshare.com/articles/dataset/Norman_et_al_2019_Science_labeled_Perturb-seq_data/24688110?file=43390776) |

## Quick start

1. **Clone both repositories:**
   ```bash
   git clone https://github.com/azizilab/SHERLOCK.git
   git clone https://github.com/azizilab/SHERLOCK_Reproducibility.git
   ```
2. **Install dependencies** (see [Environment](#environment)), and make `sherlock` importable. You can either install it into your environment or edit the `sys.path.append(...)` line at the top of each notebook.
3. **Run the notebooks in each dataset folder in the order given below.** The training cells are commented out, and the notebooks load saved checkpoints instead. To train the models yourself, uncomment those cells.

## Environment

The notebooks were run with Python 3.12 and these package versions:

| Package | Version | Package | Version |
|---|---|---|---|
| torch | 2.7.1 | scipy | 1.13.1 |
| scanpy | 1.11.2 | scikit-learn | 1.5.1 |
| anndata | 0.11.4 | statsmodels | 0.14.4 |
| numpy | 1.26.4 | seaborn | 0.13.2 |
| pandas | 2.2.2 | matplotlib | 3.9.2 |
| networkx | 3.3 | gseapy | 1.1.11 |
| kneed | 0.8.5 | pyreadr | 0.5.3 |
| squidpy | (RAEFISH preprocessing only) | | |

The `gseapy` enrichment cells (Replogle and RAEFISH) query the Enrichr web service, so they need internet access. A GPU is used if one is available but is not required.

---

## 1. Genome-wide CRISPRi Perturb-seq: Replogle et al. (`genetic_screen_genome_wide_crispri/`)

**Data:** K562 genome-scale CRISPRi Perturb-seq. The working subset has 118,641 cells, 1,185 genes and 682 perturbation labels (681 targeted genes plus a non-targeting control). The ground truth for grouping is the 8 complexes and pathways annotated by Replogle et al., covering 335 genes. These are stored in `data.uns['pathways']`.

**Source:** Replogle et al., *Cell* 2022 ([doi:10.1016/j.cell.2022.05.013](https://doi.org/10.1016/j.cell.2022.05.013)).

| Notebook | What it does |
|---|---|
| [`demo_ls_interpretation.ipynb`](genetic_screen_genome_wide_crispri/demo_ls_interpretation.ipynb) | Loads the data with `slk.datasets.replogle()`, then runs SHERLOCK or loads `replogle_model_1.pth` (seed 1). It then shows the latent UMAP, the perturbation correlation matrix and hierarchical clustering (`t = 1.5`, Ward linkage), and maps clusters to pathways (accuracy, ARI, AMI). It also runs MSigDB enrichment of the inferred downstream targets with gseapy. |

**Training settings** (`slk.tl.run`):

```python
model="vae", latent_dim=16, batch_size=4096, num_epochs=1000, validate_every=50, patience=20,
l0_lambda=10, n_epochs_l0_warmup=200, seed=1
```

**Outputs:** files in `../results/`:

| Output | Paper |
|---|---|
| `umap_pathway_comparison*` and `umap_true_pathway*` (expression UMAPs vs SHERLOCK latent UMAP) | Fig. 1d |
| `benchmark_correlation_color*` (correlation matrix with reference and mapped pathways) | Fig. 1e |
| `hallmark_enrichment_dotplot*` | Fig. 1f |
| `cluster_rho_dendrogram*` | Clustering used for the panels above |

## 2. Spatial perturbation screen: RAEFISH (`genetic_screen_spatial_reafish/`)

**Data:** Perturb-RAEFISH imaging-based spatial CRISPR screen, from [Mendeley Data](https://data.mendeley.com/datasets/8kbv637pxh/1). It has 17,931 segmented cells and a 492-gene MERFISH panel.

**Source:** Cheng et al., *Cell* 2025 ([doi:10.1016/j.cell.2025.09.006](https://doi.org/10.1016/j.cell.2025.09.006)).

| # | Notebook | What it does |
|---|---|---|
| 1 | [`raefish.ipynb`](genetic_screen_spatial_reafish/raefish.ipynb) | Reads the MATLAB cell list and codebooks, builds an AnnData object with spatial coordinates, keeps `Single` cells with a top-barcode ratio above 0.75, and writes `raefish.h5ad` |
| 2 | [`raefish_run_ls_interpretation.ipynb`](genetic_screen_spatial_reafish/raefish_run_ls_interpretation.ipynb) | Restricts the data to the largest experiment (`241203_kraken`), perturbations with at least 20 cells, and cells with log(total counts + 1) > 3. This leaves 3,436 cells and 76 perturbations plus NTC. It then loads `raefish_model_20260603_112214_3.pth` (seed 3), makes the latent UMAP and hierarchical clustering (`t = 1.5`), and runs GO enrichment for each group (gseapy Enrichr) |

**Outputs:**

| Output | Paper |
|---|---|
| `raefish_sherlock_zspace*` | Fig. 2a |
| `raefish__dendrogram*` | Fig. 2b |
| `raefish_sherlock_zspace_conditions_group*` | Fig. 2c |
| `go_enrichment_per_group*`, `go_top_term_per_group*` | Fig. 2d |
| `raefish_correlation_color*` | Perturbation correlation matrix |

## 3. EGFR inhibitor screen: Giglio et al. (`drug_screen_with EGFR_inhibitors/`)

**Data:** BT333 glioblastoma cells treated with EGFR and kinase-pathway inhibitors or DMSO, profiled with sci-Plex (GEO GSE261618). Only the 10 µM dose (`concentration = 10000` nM) is analyzed.

**Source:** Giglio et al., *bioRxiv* 2025 ([doi:10.1101/2024.04.08.587960](https://doi.org/10.1101/2024.04.08.587960)).

| # | Notebook | What it does |
|---|---|---|
| 1 | [`gbm_preprocess_EGFR.ipynb`](<drug_screen_with EGFR_inhibitors/gbm_preprocess_EGFR.ipynb>) | Builds an AnnData object from the count matrix (`.mtx`) and the row and column metadata. It keeps cells with hash UMIs > 10, a top-to-second-best ratio > 5 and more than 100 UMIs, and drugs with more than 100 cells. It keeps the genes that are differentially expressed between any drug and DMSO (Wilcoxon test, FDR < 0.05), then writes `bt333_egfr_degs_10000.h5ad`. The paper reports 11,420 cells and 1,157 genes. |
| 2 | [`gbm_run_conditions_bt333_egfr_sparse_executed.ipynb`](<drug_screen_with EGFR_inhibitors/gbm_run_conditions_bt333_egfr_sparse_executed.ipynb>) | Loads `drug_egfr_model_20260529_163520_1.pth` (seed 1) and makes the latent UMAP, the drug grouping, the correlation matrix and the dendrogram. It also annotates drugs by chemical class and reversibility (`EGFRi_annotations_final_RG.csv`) and tests class enrichment within each group (Fisher's exact test with BH correction). |

**Training settings** (`slk.tl.run`):

```python
model="vae", latent_dim=16, batch_size=4096, num_epochs=1000, validate_every=50, patience=350,
l0_lambda=50, n_epochs_l0_warmup=100, seed=1
```

**Outputs:**

| Output | Paper |
|---|---|
| `drug_egfr_10000_sherlock_zspace*` | Fig. 2e–f |
| `drug_egfr_correlation_color*` | Fig. 2g |
| `drug_egfr_10000uM_dendrogram*` | Fig. 2h |
| `umap_pert_class_broad*`, `umap_pert_reversible*`, the enrichment heatmap, `*_presherlock*` | Fig. S2 |

## 4. Kinome CRISPRi / CRISPRa screens: Shi et al. (`genetic_screen_kinome-wide_crispria/`)

**Data:** sci-Plex CRISPRi and CRISPRa screens of about 140 kinase-targeting guides plus NTCs in BT333 cells. The cells were profiled at three T-cell co-culture dose ratios (1:1, 1:0.5 and 1:0.25) and untreated. Because the screens have few cells per guide, we aggregated cells into **bootstrap metacells**: 4 cells per metacell for CRISPRi and 6 for CRISPRa, with 30 draws per guide-by-treatment group.

**Source:** Shi et al., *bioRxiv* 2026 ([doi:10.64898/2026.01.08.698516](https://doi.org/10.64898/2026.01.08.698516)).

| # | Notebook | What it does |
|---|---|---|
| 1a | [`12. Preparing_h5ad_files_final_immun_guides_boostrap_ncells.ipynb`](<genetic_screen_kinome-wide_crispria/12. Preparing_h5ad_files_final_immun_guides_boostrap_ncells.ipynb>) | **CRISPRi** (`ncells = 4`). Keeps cells with more than 3 sgRNA reads, a top-guide proportion above 0.3 and a confident hash assignment, and guides with at least 50 cells. It builds the metacells and selects guides with more than 50 DEGs vs NTC. The gene panel is the union of the top DEGs and the kinase target genes. Writes `filtered_gbm_crispri_crop_top_bootstrap_4.h5ad`. |
| 1b | [`12. Preparing_h5ad_files_final_immun_guides_boostrap_v1_CRISPRa_6cell_thisone.ipynb`](<genetic_screen_kinome-wide_crispria/12. Preparing_h5ad_files_final_immun_guides_boostrap_v1_CRISPRa_6cell_thisone.ipynb>) | **CRISPRa** (`ncells = 6`). The same steps, using the guide list in `guides_over_50_DEGs.csv`. Writes `filtered_gbm_crispra_crop_top_bootstrap_6.h5ad`. |
| 2a | [`reproducibility_metacell_boostrap_v1_nonconditions_v2_treated.ipynb`](genetic_screen_kinome-wide_crispria/reproducibility_metacell_boostrap_v1_nonconditions_v2_treated.ipynb) | **CRISPRi:** trains 5 seeded runs on the T-cell-treated metacells (`N_RUNS = 5`). It saves each run's matrices and the model with the best ATE, then measures reproducibility across runs for `W`, `rho` and the clusters (`N_CLUSTERS = 6`). |
| 2b | [`reproducibility_metacell_boostrap_v1_nonconditions_v2_treated_crispra.ipynb`](genetic_screen_kinome-wide_crispria/reproducibility_metacell_boostrap_v1_nonconditions_v2_treated_crispra.ipynb) | **CRISPRa:** the same analysis. |

**Training settings** (`slk.tl.run_single`, for both screens):

```python
batch_size=4096, num_epochs=2500, use_conditions=False, validate_every=20, l0_lambda=35,
patience=500, latent_dim=16, rank=6, ce_lambda=1, n_epochs_kl_warmup=20, n_epochs_l0_warmup=500
```

With `use_conditions=False`, metacells from all three T-cell dose ratios are modeled together. The result is a single set of perturbation effects under T-cell co-culture.

**Skipping training:** Notebooks 2a and 2b set `use_rerun = True`. Training is skipped for every run whose `RESULTS_DIR/matrices/run_{i}.npz` file already exists. If all five runs are already saved, you can start the notebook from *Part 2 — Load saved matrices*.

**Outputs:** files in `RESULTS_DIR/figures/`:

| Output | Paper |
|---|---|
| Perturbation correlation matrix and clustering | Fig. 2i–j (CRISPRi), Fig. S3a–b (CRISPRa) |
| `crisri_clustering_confidence_heatmap_k6*`, `crisra_clustering_confidence_heatmap_k6*` | Fig. S3c |
| `clustering_reproducibility_k6.png` | Reproducibility summary |

## 5. 11-drug kinase inhibitor screen ± T cells: Shi et al. (`drug_screen_with_11_kinases_inhibitors/`)

**Data:** Patient-derived BT333 glioblastoma cells were profiled with sci-Plex. The cells were treated with 11 candidate immune-modulating kinase inhibitors or with DMSO, at 1 µM and at 10 µM. Each drug was washed out before the cells were co-cultured with tumor antigen-specific cytotoxic T cells (`0.5T`) or cultured without T cells (`NoT`).

**Drugs:** ALWII4127 (EPHA2 inhibitor), CP673451 (PDGFRA inhibitor), Abemaciclib mesylate, BAY1217389, Laduviglusib, PF06260933, SGCAAK11, STK16IN1, Taletrectinib, Tyrphostin9 and Zabedosertib.

**Source:** Shi et al., *bioRxiv* 2026 ([doi:10.64898/2026.01.08.698516](https://doi.org/10.64898/2026.01.08.698516)).

| # | Notebook | What it does |
|---|---|---|
| 1 | [`gbm_preprocess_11drugs_degs_tcellgenes.ipynb`](drug_screen_with_11_kinases_inhibitors/gbm_preprocess_11drugs_degs_tcellgenes.ipynb) | Run once with `concentration = '1'` and once with `concentration = '10'`. Keeps cells with hash UMIs > 1, a top-to-second-best ratio > 2 and more than 500 UMIs. The gene panel is the union of each drug's DEGs vs DMSO in `NoT` cells (FDR < 0.05) and the top 1,000 genes changed by T cells in DMSO cells. Writes `bt333_degs_tcell_{1,10}_1000.h5ad`, which have 38,755 cells × 1,320 genes (1 µM) and 35,511 cells × 2,894 genes (10 µM). Also makes the PCA UMAP for Fig. 3a. |
| 2 | [`gbm_run_conditions_bt333_with_T_cell_conditions_figures_1um_LS.ipynb`](drug_screen_with_11_kinases_inhibitors/gbm_run_conditions_bt333_with_T_cell_conditions_figures_1um_LS.ipynb) | SHERLOCK analysis at **1 µM**, using `drug_model_20260525_185605_0.pth` (seed 0) |
| 3 | [`gbm_run_conditions_bt333_with_T_cell_conditions_figures_10um_LS_this_one.ipynb`](drug_screen_with_11_kinases_inhibitors/gbm_run_conditions_bt333_with_T_cell_conditions_figures_10um_LS_this_one.ipynb) | SHERLOCK analysis at **10 µM**, using `drug_model_20260519_192528_2.pth` (seed 2). Also compares the two concentrations, so **run notebook 2 first**. |

**Training settings** (`slk.tl.run_single`, at both concentrations):

```python
batch_size=4096, num_epochs=1000, use_conditions=True, validate_every=20, l0_lambda=200,
patience=500, latent_dim=8, rank=3, n_epochs_l0_warmup=200
```

The notebooks configure SHERLOCK with `pert_key='drug'`, `ntc_label='DMSO'`, `treatment_key='tcell_treatment'` and `untreated_label='NoT'`. Each perturbation shift is applied to a control background from the matching T-cell condition.

**Outputs:**

| Output | Paper |
|---|---|
| `{conc}_umaps_with_legends*` (PCA UMAP) | Fig. 3a |
| `{conc}_sherlock_zspace[_with_legends]*` | Fig. 3b |
| `drug_{conc}_correlation_color*`, `drug_{conc}uM_dendrogram*` | Fig. 3c, Fig. S4a |
| `{conc}_condition_effect_on_perturbation*`, `{conc}um_pert_sensitivity.csv` | Fig. 3d, Fig. S4b |
| `{conc}_cf_bipartite_CP673451_ALWII4127_{NoT,0.5T}*` | Fig. 3e |
| `figure_ev_sig_*`, `filtered_significant_drug_*.csv` | Fig. S5 |
| `10_cf_bipartite_blue_genes_violin_0.5T*` (10 µM only) | Fig. S6 |
| `CP673451_ALWII4127_sensitivity_comparison*` | Comparison of 1 µM and 10 µM |

**Main result:** CP673451 (a PDGFRA inhibitor) and ALWII4127 (an EPHA2 inhibitor) have among the lowest conditional perturbation response scores. Their inferred downstream effects become more similar at 10 µM in the presence of T cells. The genes they share (OLIG1, OLIG2, PHGDH, SLC26A2 and GBP1) cover both glioma cell-state programs and interferon-responsive programs.

## 6. Combinatorial CRISPRa Perturb-seq: Norman et al. 2019 (`genetic_screen_combinatorial_crispra/`)

**Source:** Norman et al., *Science* 2019 ([doi:10.1126/science.aax4438](https://doi.org/10.1126/science.aax4438)).

Notebooks for this dataset are coming soon. They will cover prediction of held-out combinations and genetic-interaction classification (Fig. 4, Figs. S7–S15).

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

### Datasets

If you use the data, please also cite the studies that generated it:

1. **Replogle et al. (genome-scale CRISPRi Perturb-seq):** Joseph M. Replogle et al. "Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq." *Cell* 185(14):2559–2575.e28 (2022). doi:[10.1016/j.cell.2022.05.013](https://doi.org/10.1016/j.cell.2022.05.013)
2. **Cheng et al. (Perturb-RAEFISH spatial screen):** Yubao Cheng et al. "Sequencing-free whole-genome spatial transcriptomics at single-molecule resolution." *Cell* (2025). doi:[10.1016/j.cell.2025.09.006](https://doi.org/10.1016/j.cell.2025.09.006)
3. **Giglio et al. (EGFR inhibitor sci-Plex screen):** Ross M. Giglio et al. "A heterogeneous pharmaco-transcriptomic landscape induced by targeting a single oncogenic kinase." *bioRxiv* (2025). doi:[10.1101/2024.04.08.587960](https://doi.org/10.1101/2024.04.08.587960)
4. **Shi et al. (GBM kinome CRISPRi/a and 11-drug screens):** Lingting Shi et al. "Mapping kinase-dependent tumor immune adaptation with multiplexed single-cell CRISPR screens." *bioRxiv* (2026). doi:[10.64898/2026.01.08.698516](https://doi.org/10.64898/2026.01.08.698516)
5. **Norman et al. (combinatorial CRISPRa Perturb-seq):** Thomas M. Norman et al. "Exploring genetic interaction manifolds constructed from rich single-cell phenotypes." *Science* 365(6455):786–793 (2019). doi:[10.1126/science.aax4438](https://doi.org/10.1126/science.aax4438)

```bibtex
@article{replogle2022mapping,
  title   = {Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq},
  author  = {Replogle, Joseph M. and others},
  journal = {Cell},
  volume  = {185},
  number  = {14},
  pages   = {2559--2575.e28},
  year    = {2022},
  doi     = {10.1016/j.cell.2022.05.013}
}

@article{cheng2025sequencing,
  title   = {Sequencing-free whole-genome spatial transcriptomics at single-molecule resolution},
  author  = {Cheng, Yubao and others},
  journal = {Cell},
  year    = {2025},
  doi     = {10.1016/j.cell.2025.09.006}
}

@article{giglio2025heterogeneous,
  title   = {A heterogeneous pharmaco-transcriptomic landscape induced by targeting a single oncogenic kinase},
  author  = {Giglio, Ross M. and others},
  journal = {bioRxiv},
  year    = {2025},
  doi     = {10.1101/2024.04.08.587960}
}

@article{shi2026mapping,
  title   = {Mapping kinase-dependent tumor immune adaptation with multiplexed single-cell CRISPR screens},
  author  = {Shi, Lingting and others},
  journal = {bioRxiv},
  year    = {2026},
  doi     = {10.64898/2026.01.08.698516}
}

@article{norman2019exploring,
  title   = {Exploring genetic interaction manifolds constructed from rich single-cell phenotypes},
  author  = {Norman, Thomas M. and others},
  journal = {Science},
  volume  = {365},
  number  = {6455},
  pages   = {786--793},
  year    = {2019},
  doi     = {10.1126/science.aax4438}
}
```

## Contact

Please contact the lead contacts with questions:

- José L. McFaline-Figueroa: jm5200@columbia.edu
- Elham Azizi: elham@azizilab.com

You can also open an issue in this repository.
