# `data/`: input datasets (placeholder)

This folder is a placeholder; its contents are not tracked by git. Put the input files here in the
layout below, or point `SHERLOCK_DATA_DIR` at another location:

```bash
export SHERLOCK_DATA_DIR=/path/to/sherlock_data   # overrides the default ./data
```

All notebooks resolve their inputs from `DATA_DIR` (see `../paths.py`). Files marked *written*
are produced by the preprocessing notebooks from the raw inputs above them.

## Expected layout

```
data/
├── raefish/                                   # Cheng et al. 2025 (Mendeley Data)
│   ├── CellList_PerturbRaeFISH.mat
│   ├── Codebook_MERFISH.mat
│   ├── Codebook_RaeFISH.mat
│   └── raefish.h5ad                           # written by scripts/raefish/1_preprocess
│
├── gbm/
│   ├── egfr/                                  # Giglio et al. 2025 (GEO GSE261618)
│   │   ├── BT333_EGFRi_cds_count_matrix_transposed.mtx
│   │   ├── BT333_EGFRi_cds_rowData.csv
│   │   └── BT333_EGFRi_cds_colData.csv
│   ├── bt333_egfr_degs_10000.h5ad             # written by scripts/egfr_drug_screen/1_preprocess
│   ├── EGFRi_annotations_final_RG.csv         # drug chemical class and reversibility (Fig. S2)
│   │
│   ├── CDS_BT333_Tcells_0_cutoff.h5ad         # 11 kinase inhibitors ± T cells (Shi et al. 2026)
│   ├── bt333_degs_tcell_1_1000.h5ad           # written by scripts/kinase_inhibitors_tcell/1_preprocess
│   ├── bt333_degs_tcell_10_1000.h5ad          #   (run once per concentration)
│   │
│   ├── crispri_final/                         # kinome CRISPRi screen (Shi et al. 2026)
│   │   ├── preprocessed_cds_without_Tcells.h5ad
│   │   └── deg_ntc_kinases.csv
│   ├── crispra_final/                         # kinome CRISPRa screen (Shi et al. 2026)
│   │   └── preprocessed_cds_without_Tcells.h5ad
│   ├── NTC_crispri/T_cell_dose_gene.csv       # T-cell dose-responsive genes in NTC cells
│   ├── NTC_crispra/T_cell_dose_gene.csv
│   ├── KinMap_kinase_protein_to_gene_map.rds  # kinase protein -> gene symbol map
│   ├── guides_over_50_DEGs.csv                # guides with > 50 DEGs vs NTC, used for both screens
│   ├── filtered_gbm_crispri_crop_top_bootstrap_4.h5ad   # written by scripts/kinome_crispri_crispra/1a
│   └── filtered_gbm_crispra_crop_top_bootstrap_6.h5ad   # written by scripts/kinome_crispri_crispra/1b
│
└── norman/                                    # Norman et al. 2019
    ├── Norman_2019.h5ad                       # Figshare (labelled Perturb-seq data)
    ├── genetic_interactions.csv               # the 88 pairs with genetic-interaction labels from Norman et al.
    └── aax4438_tables6.xlsx                   # Norman et al. Table S6 (perturbation-map clusters)
```

The Replogle dataset is loaded with `sherlock.datasets.replogle()`, which downloads it on first use
to `~/.cache/sherlock` (or `$SHERLOCK_DATA_DIR` if set).

## Sources

| Folder | Study | Source |
|---|---|---|
| (downloaded) | Replogle et al., *Cell* 2022 | https://gwps.wi.mit.edu |
| `raefish/` | Cheng et al., *Cell* 2025 | [Mendeley Data](https://data.mendeley.com/datasets/8kbv637pxh/1) |
| `gbm/egfr/` | Giglio et al., *bioRxiv* 2025 | GEO [GSE261618](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE261618) |
| `gbm/` (kinome screens, 11 drugs) | Shi et al., *bioRxiv* 2026 | to be deposited in GEO (see the manuscript's Data Availability) |
| `norman/` | Norman et al., *Science* 2019 | [Figshare](https://figshare.com/articles/dataset/Norman_et_al_2019_Science_labeled_Perturb-seq_data/24688110?file=43390776); supplementary tables of the paper |
