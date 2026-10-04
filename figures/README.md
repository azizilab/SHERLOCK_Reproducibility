# `figures/`

One notebook per main figure, plus one for the supplementary figures. Each notebook reruns the
relevant cells of the analysis notebooks in [`../scripts/`](../scripts) from the saved models in
`results/` and writes the panels to `figures/panels/` (`paths.FIGURES_DIR`). Every panel has a
heading with its figure number.

The notebooks are assembled by [`build_figure_notebooks.py`](build_figure_notebooks.py); rerun it
after changing a notebook in `scripts/`.

## Panel index

| Panel | Notebook section | Source notebook |
|---|---|---|
| 1a–c | schematics | none |
| 1d | expression-space UMAPs (pathway, Leiden) and SHERLOCK latent UMAP | `replogle/1_replogle_analysis` |
| 1e | perturbation correlation with reference and inferred pathways | `replogle/1_replogle_analysis` |
| 1f | Hallmark enrichment of downstream targets | `replogle/1_replogle_analysis` |
| 1g | benchmark against cVAE, sVAE+, contrastiveVI, scGen | `replogle/2_benchmarking` |
| 2a–c | RAEFISH latent space, clustering, groups | `raefish/2_raefish_analysis` |
| 2d | GO enrichment per group | `raefish/2_raefish_analysis` |
| 2e–h | EGFR screen latent space, groups, correlation, clustering | `egfr_drug_screen/2_egfr_analysis` |
| 2i–j | CRISPRi correlation and clustering | `kinome_crispri_crispra/2a_reproducibility_crispri` (best run) |
| 3a | expression-space UMAP | `kinase_inhibitors_tcell/1_preprocess` |
| 3b, 3c, 3e | latent space, correlation, downstream genes (1 µM and 10 µM) | `kinase_inhibitors_tcell/2_analysis_1uM`, `3_analysis_10uM` |
| 3d | condition dependence of CP673451 and ALWII4127 | `kinase_inhibitors_tcell/3_analysis_10uM` |
| 4a–d | latent space, GI-metric embedding, ATE, GI classification | `norman/1_norman_analysis` |
| 5a | GI classes in reconstructed gene space | `norman/1_norman_analysis` |
| 5b | interaction arcs on the erythroid axis | `norman/4_interaction_biology` |
| S1 | Replogle reproducibility | `replogle/2_benchmarking` |
| S2 | EGFR screen: expression UMAP, chemical annotations, enrichment | `egfr_drug_screen/2_egfr_analysis` |
| S3a–b | CRISPRa correlation and clustering | `kinome_crispri_crispra/2b_reproducibility_crispra` (best run) |
| S3c | group confidence across runs (CRISPRi, CRISPRa) | `kinome_crispri_crispra/2a`, `2b` |
| S4a–c, S5 | drug clustering, condition dependence, CP673451 vs STK16IN1, significance of downstream effects | `kinase_inhibitors_tcell/2_analysis_1uM`, `3_analysis_10uM` |
| S6 | expression of the shared CP673451 / ALWII4127 targets | `kinase_inhibitors_tcell/3_analysis_10uM` |
| S7, S8 | Norman reproducibility; held-out pairs | `norman/1_norman_analysis` |
| S9 | GI classification from measured expression | `norman/2_raw_expression_gi` |
| S10–S15 | interaction rules, modules, erythroid axis, latent factors | `norman/4_interaction_biology` |

Fig. 5b shows the redundant, suppression and synergy arcs of the arc plot that Fig. S13a shows in
full.
