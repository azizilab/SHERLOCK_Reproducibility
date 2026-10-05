<p align="center">
  <img src="SHERLOCK_logo.png" alt="SHERLOCK logo" width="420">
</p>

# SHERLOCK: Reproducibility

Code that reproduces the figures and analyses of the SHERLOCK manuscript:

> Zhang M\*, Myers JD\*, Shi L\*, Giglio RM, Chatterjee S, McFaline-Figueroa JL§, Azizi E§.
> **SHERLOCK: Structured representation learning and causal inference of downstream perturbation effects.**
> *bioRxiv* (2026). [doi:10.64898/2026.09.25.754573](https://doi.org/10.64898/2026.09.25.754573)
> \* Equal contribution · § Senior and corresponding authors

This repository holds only notebooks and instructions. The SHERLOCK method itself is the
`sherlock-perturb` package from [azizilab/SHERLOCK](https://github.com/azizilab/SHERLOCK),
documented at [azizilabsherlock.readthedocs.io](https://azizilabsherlock.readthedocs.io).

## Structure

```
.
├── figures/            # ★ one notebook per main figure, plus the supplementary figures
│   ├── Figure1.ipynb … Figure5.ipynb
│   ├── Supplementary_Figures.ipynb
│   ├── build_figure_notebooks.py   # assembles the figure notebooks from scripts/
│   └── panels/                     # panels written by the notebooks (created on first run)
├── scripts/            # full analysis per dataset: preprocessing, training, analysis
│   ├── replogle/                   # genome-scale CRISPRi Perturb-seq      (Fig. 1, S1)
│   ├── raefish/                    # spatial CRISPR screen                 (Fig. 2a–d)
│   ├── egfr_drug_screen/           # EGFR inhibitor sci-Plex screen        (Fig. 2e–h, S2)
│   ├── kinome_crispri_crispra/     # kinome CRISPRi / CRISPRa screens      (Fig. 2i–j, S3)
│   ├── kinase_inhibitors_tcell/    # 11 kinase inhibitors ± T cells        (Fig. 3, S4–S6)
│   └── norman/                     # combinatorial CRISPRa Perturb-seq     (Fig. 4–5, S7–S15)
├── data/               # input datasets (placeholder, see data/README.md)
├── results/            # saved models and intermediate results (placeholder, see results/README.md)
├── paths.py            # DATA_DIR / RESULTS_DIR / FIGURES_DIR, overridable by environment variables
├── environment.yml
└── requirements.txt
```

**To reproduce a figure,** populate `data/` and `results/`, then open the matching notebook in
`figures/` and run it from top to bottom. Each figure notebook reruns the relevant parts of the
analysis notebooks in `scripts/` from the saved models and labels every panel with its figure
number. The notebooks in `scripts/` run the complete analysis, including model training, and keep
the outputs from the runs reported in the manuscript.

| Figure | Notebook | Analysis notebooks used |
|---|---|---|
| 1 | [`figures/Figure1.ipynb`](figures/Figure1.ipynb) | `scripts/replogle/` |
| 2 | [`figures/Figure2.ipynb`](figures/Figure2.ipynb) | `scripts/raefish/`, `scripts/egfr_drug_screen/`, `scripts/kinome_crispri_crispra/` |
| 3 | [`figures/Figure3.ipynb`](figures/Figure3.ipynb) | `scripts/kinase_inhibitors_tcell/` |
| 4 | [`figures/Figure4.ipynb`](figures/Figure4.ipynb) | `scripts/norman/` |
| 5 | [`figures/Figure5.ipynb`](figures/Figure5.ipynb) | `scripts/norman/` |
| S1–S15 | [`figures/Supplementary_Figures.ipynb`](figures/Supplementary_Figures.ipynb) | all of the above |

A panel-by-panel index is in [`figures/README.md`](figures/README.md).

## System requirements

- **Operating system:** Linux (tested on Debian 11, kernel 5.10). macOS and Windows should work
  for the CPU path but were not tested.
- **Hardware:** a CUDA GPU is recommended for training (tested on an NVIDIA L4, 24 GB, with
  32 CPU cores and 125 GB of RAM). Every notebook also runs on CPU, more slowly. The largest
  inputs (Norman, 11-drug screen) are 2–3 GB on disk and need several times that in memory.
- **Software:** Python ≥ 3.10, SHERLOCK 0.1.0 (`sherlock-perturb`), and the packages in
  [`requirements.txt`](requirements.txt). The analyses were run with:

| Package | Version | Package | Version |
|---|---|---|---|
| python | 3.10 / 3.12 | scikit-learn | 1.5–1.7 |
| torch | 2.7–2.12 | scipy | 1.13–1.15 |
| pyro-ppl | 1.9.1 | statsmodels | 0.14 |
| scanpy | 1.11 | seaborn | 0.13 |
| anndata | 0.11.4 | matplotlib | 3.9–3.10 |
| numpy | 1.26 / 2.2 | gseapy | 1.1.11 |
| pandas | 2.2–2.3 | scvi-tools (baselines) | 1.3.3 |
| networkx | 3.3–3.4 | cell-gears (baseline) | 0.1.2 |

The GBM, RAEFISH and EGFR notebooks were run with Python 3.12; the Replogle benchmark and the
Norman notebooks with Python 3.10.

## Installation

```bash
git clone https://github.com/azizilab/SHERLOCK_Reproducibility.git
cd SHERLOCK_Reproducibility

conda env create -f environment.yml
conda activate sherlock-repro
```

or, with pip into an existing Python ≥ 3.10 environment:

```bash
pip install -r requirements.txt
```

Both install SHERLOCK with the extras for the baselines (`scvi-tools`, `cell-gears`) and the
tutorials, plus the packages the notebooks use. Installation takes about 5–10 minutes on a
desktop computer, most of it downloading PyTorch. To use a specific CUDA build of PyTorch,
install it first by following [pytorch.org](https://pytorch.org/get-started/locally/).

## Data and saved models

1. **Inputs** go in `data/`. [`data/README.md`](data/README.md) lists every file, where it comes
   from and the expected layout. The processed Replogle and Norman datasets can be downloaded with
   SHERLOCK:
   ```bash
   export SHERLOCK_DATA_DIR=$PWD/data
   python -c "import sherlock as slk; slk.datasets.replogle(); slk.datasets.norman()"
   ```
   The other processed datasets are available from the first authors on request; the raw
   data are available from the original studies (see [Data sources](#data-sources)).
2. **Saved models and intermediate results** go in `results/`.
   [`results/README.md`](results/README.md) lists each file and the notebook that writes it. With
   these in place, no model has to be retrained to regenerate the figures.

`paths.py` resolves both folders, so they can live elsewhere:

| Variable | Default | Override |
|---|---|---|
| `DATA_DIR` | `./data` | `SHERLOCK_DATA_DIR` |
| `RESULTS_DIR` | `./results` | `SHERLOCK_RESULTS_DIR` |
| `FIGURES_DIR` | `./figures/panels` | `SHERLOCK_FIGURES_DIR` |

## Demo

The SHERLOCK documentation has three tutorials that run on the published datasets and show the
expected output of each step:

| Tutorial | Design | Data | Run time* |
|---|---|---|---|
| [Single perturbations](https://azizilabsherlock.readthedocs.io/en/latest/tutorials/single_perturbations.html) | one perturbation per cell | genome-scale CRISPRi Perturb-seq (Replogle et al.), downloaded by `slk.datasets.replogle()` | ~10 min with the saved model |
| [Single perturbations across conditions](https://azizilabsherlock.readthedocs.io/en/latest/tutorials/conditional_perturbations.html) | one perturbation per cell, with and without T cells | 11 kinase inhibitors, sci-Plex (Shi et al.), available from the first authors on request | ~25 min including training |
| [Combinatorial perturbations](https://azizilabsherlock.readthedocs.io/en/latest/tutorials/combinatorial_perturbations.html) | one or two perturbations per cell | combinatorial CRISPRa Perturb-seq (Norman et al.), downloaded by `slk.datasets.norman()` | ~35 min with the saved model |

\*Measured on a workstation with one NVIDIA L4 GPU.

## Reproducing the analyses from scratch

Run the notebooks in each `scripts/` folder in the order of their numeric prefix. Training cells
are present in every notebook; in the notebooks that load the manuscript's checkpoints, the
training call is commented out and can be re-enabled. Retrained models will not match the reported
numbers exactly because training is stochastic; the manuscript reports the spread over five
independently seeded runs where relevant.

| Folder | Notebooks, in order | Training settings |
|---|---|---|
| `replogle/` | `1_replogle_analysis` (data, model, Fig. 1d–f) → `2_benchmarking` (five runs of SHERLOCK and four baselines, Fig. 1g, S1) | analysis model: latent 16, L0 10 with a 200-epoch warm-up, ≤1,000 epochs, seed 1; benchmark runs: latent 16, L0 0.1 with a 300-epoch warm-up, classifier weight 20, ≤500 epochs, patience 20 |
| `raefish/` | `1_preprocess` (MATLAB cell list → AnnData) → `2_raefish_analysis` | latent 16, rank 6, L0 10, ≤1,000 epochs |
| `egfr_drug_screen/` | `1_preprocess` (DEG panel, 10 µM) → `2_egfr_analysis` | latent 16, L0 50, ≤1,000 epochs, patience 350 |
| `kinome_crispri_crispra/` | `1a`/`1b_preprocess` (metacells, guide selection) → `2a`/`2b_reproducibility` (five runs each) | latent 16, rank 6, L0 35, ≤2,500 epochs, patience 500 |
| `kinase_inhibitors_tcell/` | `1_preprocess` (run with `concentration = '1'` and `'10'`) → `2_analysis_1uM` → `3_analysis_10uM`; `4_reproducibility_10uM` (ten seeded runs at 10 µM: agreement of groups, correlations, conditional responses and downstream genes across runs) | latent 8, rank 3, L0 200, ≤1,000 epochs, patience 500, with conditions |
| `norman/` | `1_norman_analysis` (five runs, baselines, GEARS, Fig. 4, 5a, S7, S8) → `2_raw_expression_gi` (S9) → `3_module_interaction` (consensus modules) → `4_interaction_biology` (Fig. 5b, S10–S15) | combinatorial, latent 16, rank 16, interaction rank 6, L0 0.1, ≤500 epochs, patience 30 |

The full settings are in each notebook and in the manuscript's Methods. After editing a notebook in
`scripts/`, rebuild the figure notebooks with `python figures/build_figure_notebooks.py`.

## Data sources

| Dataset | Original study | Source |
|---|---|---|
| Genome-scale CRISPRi Perturb-seq (K562) | Replogle et al., *Cell* 2022 | https://gwps.wi.mit.edu |
| Perturb-RAEFISH spatial screen | Cheng et al., *Cell* 2025 | [Mendeley Data](https://data.mendeley.com/datasets/8kbv637pxh/1) |
| EGFR inhibitor sci-Plex screen (BT333) | Giglio et al., *bioRxiv* 2025 | GEO [GSE261618](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE261618) |
| GBM kinome CRISPRi/a and 11-drug sci-Plex screens (BT333) | Shi et al., *bioRxiv* 2026 | Not yet publicly available |
| Combinatorial CRISPRa Perturb-seq (K562) | Norman et al., *Science* 2019 | [Figshare](https://figshare.com/articles/dataset/Norman_et_al_2019_Science_labeled_Perturb-seq_data/24688110?file=43390776) |

The baselines are cVAE, sVAE+ (Lopez et al. 2023), contrastiveVI (Weinberger et al. 2023),
scGen (Lotfollahi et al. 2019) and GEARS (Roohani et al. 2024).

## Citation

If you use SHERLOCK or this code, please cite:

```bibtex
@article{zhang2026sherlock,
  title     = {SHERLOCK: Structured representation learning and causal inference of downstream perturbation effects},
  author    = {Zhang, Mingxuan and Myers, Joshua D. and Shi, Lingting and Giglio, Ross M. and
               Chatterjee, Sharanya and McFaline-Figueroa, Jos{\'e} L. and Azizi, Elham},
  journal   = {bioRxiv},
  year      = {2026},
  doi       = {10.64898/2026.09.25.754573},
  url       = {https://www.biorxiv.org/content/10.64898/2026.09.25.754573v1}
}
```

If you use the data, please also cite the studies that generated it:

```bibtex
@article{replogle2022mapping,
  title   = {Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq},
  author  = {Replogle, Joseph M. and others},
  journal = {Cell}, volume = {185}, number = {14}, pages = {2559--2575.e28}, year = {2022},
  doi     = {10.1016/j.cell.2022.05.013}
}

@article{cheng2025sequencing,
  title   = {Sequencing-free whole-genome spatial transcriptomics at single-molecule resolution},
  author  = {Cheng, Yubao and others},
  journal = {Cell}, year = {2025},
  doi     = {10.1016/j.cell.2025.09.006}
}

@article{giglio2025heterogeneous,
  title   = {A heterogeneous pharmaco-transcriptomic landscape induced by targeting a single oncogenic kinase},
  author  = {Giglio, Ross M. and others},
  journal = {bioRxiv}, year = {2025},
  doi     = {10.1101/2024.04.08.587960}
}

@article{shi2026mapping,
  title   = {Mapping kinase-dependent tumor immune adaptation with multiplexed single-cell CRISPR screens},
  author  = {Shi, Lingting and others},
  journal = {bioRxiv}, year = {2026},
  doi     = {10.64898/2026.01.08.698516}
}

@article{norman2019exploring,
  title   = {Exploring genetic interaction manifolds constructed from rich single-cell phenotypes},
  author  = {Norman, Thomas M. and others},
  journal = {Science}, volume = {365}, number = {6455}, pages = {786--793}, year = {2019},
  doi     = {10.1126/science.aax4438}
}
```

## License

[CC BY-NC-ND 4.0](LICENSE), the same license as the SHERLOCK package and the preprint.

## Contact

José L. McFaline-Figueroa (jm5200@columbia.edu) and Elham Azizi (elham@azizilab.com). Questions
about the code can also be raised as an issue in this repository.
