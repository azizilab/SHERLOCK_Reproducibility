"""Assemble the figure notebooks in figures/ from the analysis notebooks in scripts/.

Each figure notebook runs, in order, the cells of the analysis notebooks that a figure
needs: data loading, loading the saved models, and the cells that draw each panel, with a
heading above every panel. Training cells are not included; the models are read from
``RESULTS_DIR`` (see ../paths.py and ../results/README.md).

Re-run this script after editing a notebook in scripts/:

    python figures/build_figure_notebooks.py
"""

import os

import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(HERE, "..", "scripts")

SETUP = (
    "import os\nimport sys\n\n"
    "# Repository root, so that paths.py (DATA_DIR / RESULTS_DIR / FIGURES_DIR) can be imported.\n"
    "sys.path.insert(0, os.path.abspath('..'))\n"
    "import paths\n\n"
    "for d in (paths.DATA_DIR, paths.RESULTS_DIR, paths.FIGURES_DIR):\n"
    "    print(d, '(found)' if os.path.isdir(d) else '(missing)')"
)


def md(text):
    return nbf.v4.new_markdown_cell(text.strip("\n"))


def section(script, cells, panels, title, note=None):
    """Cells ``cells`` (indices) of scripts/<script>, with a heading before each panel."""
    src = nbf.read(os.path.join(SCRIPTS, script), as_version=4).cells
    out = [md(f"## {title}\n\nFrom [`scripts/{script}`](../scripts/{script})."
              + (f"\n\n{note}" if note else ""))]
    for i in cells:
        if i in panels:
            out.append(md(f"### {panels[i]}"))
        c = src[i]
        if c.cell_type == "code":
            out.append(nbf.v4.new_code_cell(c.source))
        else:
            out.append(nbf.v4.new_markdown_cell(c.source))
    missing = sorted(set(panels) - set(cells))
    assert not missing, (script, missing)
    return out


def write(name, title, intro, body):
    nb = nbf.v4.new_notebook()
    nb.cells = [md(f"# {title}\n\n{intro.strip()}"), nbf.v4.new_code_cell(SETUP)] + body
    nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    nb.metadata["language_info"] = {"name": "python"}
    nbf.write(nb, os.path.join(HERE, name))
    print(f"wrote {name}: {len(nb.cells)} cells")


def upto(n, skip=()):
    """Cells 1..n of a script notebook (cell 0 is that notebook's own path setup)."""
    return [i for i in range(1, n + 1) if i not in skip]


INTRO = """
Run this notebook from the `figures/` folder after populating `data/` and `results/`
(see the repository README). Each section below reruns the relevant part of an analysis
notebook from the saved models; panels are written to `figures/panels/`
(`paths.FIGURES_DIR`).
"""

# ── Figure 1: Replogle ───────────────────────────────────────────────────────
write("Figure1.ipynb", "Figure 1: genome-scale Perturb-seq (Replogle et al.)", INTRO + """
Panels a–c are schematics.
""", [
    *section("replogle/1_replogle_analysis.ipynb", upto(67),
             {55: "Fig. 1d: UMAPs of the expression space and the SHERLOCK latent space, by pathway",
              60: "Fig. 1d: Leiden clusters of the expression space",
              67: "Fig. 1e: learned perturbation correlation with reference and inferred pathways",
              51: "Fig. 1f: Hallmark enrichment of downstream targets per inferred group"},
             "Replogle: perturbation groups, pathway recovery and enrichment",
             "The enrichment cell queries Enrichr through `gseapy` and needs internet access."),
    *section("replogle/2_benchmarking.ipynb", upto(14),
             {14: "Fig. 1g: benchmark of SHERLOCK, cVAE, sVAE+, contrastiveVI and scGen"},
             "Replogle: benchmarking",
             "Loads the five saved runs of each method from `results/benchmarking/models/`; "
             "missing runs are trained. Needs the `benchmarks` extra of SHERLOCK."),
])

# ── Figure 2: RAEFISH, EGFR drug screen, CRISPRi ─────────────────────────────
write("Figure2.ipynb", "Figure 2: perturbation programs across sequencing- and imaging-based screens",
      INTRO, [
    *section("raefish/2_raefish_analysis.ipynb", upto(52),
             {30: "Fig. 2a: SHERLOCK latent space, by perturbation",
              44: "Fig. 2b: hierarchical clustering of perturbations",
              45: "Fig. 2c: SHERLOCK latent space, by perturbation group",
              52: "Fig. 2d: top GO term per perturbation group"},
             "Spatial screen (Perturb-RAEFISH)",
             "The GO enrichment cells query Enrichr through `gseapy` and need internet access."),
    *section("egfr_drug_screen/2_egfr_analysis.ipynb", upto(51),
             {49: "Fig. 2e–f: SHERLOCK latent space, by drug and by perturbation group",
              51: "Fig. 2g: learned perturbation correlation",
              45: "Fig. 2h: hierarchical clustering of drugs"},
             "EGFR inhibitor screen (Giglio et al.)"),
    md("## Fig. 2i–j: CRISPRi kinome screen\n\n"
       "The correlation matrix and dendrogram are drawn from the best of the five CRISPRi runs "
       "saved by [`scripts/kinome_crispri_crispra/2a_reproducibility_crispri.ipynb`]"
       "(../scripts/kinome_crispri_crispra/2a_reproducibility_crispri.ipynb) "
       "(`matrices/best_model.pth`), with `slk.pl.plot_corr` and `slk.tl.cluster_rho`. "
       "The plotting cells for these two panels are not yet part of that notebook."),
])

# ── Figure 3: 11 kinase inhibitors ± T cells ─────────────────────────────────
DRUG_NOTE = ("Run the 1 µM section before the 10 µM section: panel d compares the two doses using "
             "the per-dose scores written by each section.")
write("Figure3.ipynb", "Figure 3: context-dependent drug responses (11 kinase inhibitors ± T cells)",
      INTRO + "\n" + DRUG_NOTE, [
    *section("kinase_inhibitors_tcell/1_preprocess.ipynb", [1, 2] + list(range(28, 38)),
             {35: "Fig. 3a: UMAP of the expression space (10 µM), by T-cell condition and drug"},
             "Expression-space UMAP",
             "Shown for 10 µM; set `concentration = '1'` in the first cell of this section for 1 µM."),
    *section("kinase_inhibitors_tcell/2_analysis_1uM.ipynb", upto(78),
             {64: "Fig. 3b (1 µM): SHERLOCK latent space, by T-cell condition and drug",
              62: "Fig. 3c (1 µM): learned correlation between drugs, with groups",
              75: "Fig. 3e (1 µM): downstream genes of CP673451 and ALWII4127 per condition",
              78: "Fig. 3e: group legend"},
             "1 µM"),
    *section("kinase_inhibitors_tcell/3_analysis_10uM.ipynb", upto(84),
             {64: "Fig. 3b (10 µM): SHERLOCK latent space, by T-cell condition and drug",
              62: "Fig. 3c (10 µM): learned correlation between drugs, with groups",
              75: "Fig. 3e (10 µM): downstream genes of CP673451 and ALWII4127 per condition",
              84: "Fig. 3d: condition dependence of CP673451 and ALWII4127 at 1 and 10 µM"},
             "10 µM"),
])

# ── Figures 4 and 5: Norman ──────────────────────────────────────────────────
NORMAN_NOTE = ("Loads the five SHERLOCK runs, the baseline runs and the GEARS runs from "
               "`results/norman_figure/`; any run that is missing is trained.")
write("Figure4.ipynb", "Figure 4: combinatorial perturbations and genetic-interaction classes (Norman et al.)",
      INTRO, [
    *section("norman/1_norman_analysis.ipynb", upto(39),
             {26: "Fig. 4a: SHERLOCK latent space, by Norman et al. perturbation module",
              31: "Fig. 4b: genetic-interaction metric embedding, Norman labels vs SHERLOCK",
              23: "Fig. 4c: counterfactual ATE for all perturbations, singles, seen and held-out pairs",
              39: "Fig. 4d: genetic-interaction classification (observed mode)"},
             "Norman CRISPRa screen", NORMAN_NOTE),
])
write("Figure5.ipynb", "Figure 5: interaction classes and erythroid-associated modules (Norman et al.)",
      INTRO + """
Panel b shows the redundant, suppression and synergy arcs of the arc plot drawn below,
which shows all interaction classes (Fig. S13a).
""", [
    *section("norman/1_norman_analysis.ipynb", upto(42, skip=(41,)),
             {42: "Fig. 5a: genetic-interaction classes in reconstructed gene space"},
             "Norman CRISPRa screen", NORMAN_NOTE),
    *section("norman/4_interaction_biology.ipynb", upto(19),
             {19: "Fig. 5b: labelled pairs as arcs between consensus modules on the erythroid axis"},
             "Consensus modules and the erythroid axis",
             "Needs `results/module_interaction/consensus_modules.csv`, written by "
             "[`scripts/norman/3_module_interaction.ipynb`](../scripts/norman/3_module_interaction.ipynb)."),
])

# ── Supplementary figures ────────────────────────────────────────────────────
write("Supplementary_Figures.ipynb", "Supplementary Figures S1–S15", INTRO + "\n" + DRUG_NOTE, [
    *section("replogle/2_benchmarking.ipynb", upto(12) + [16],
             {16: "Fig. S1: reproducibility across five runs (Replogle)"},
             "Replogle: reproducibility"),
    *section("egfr_drug_screen/2_egfr_analysis.ipynb", upto(66),
             {65: "Fig. S2a: UMAP of the expression space, by drug",
              66: "Fig. S2a: UMAP of the expression space, by perturbation group",
              54: "Fig. S2b: SHERLOCK latent space, by chemical class",
              55: "Fig. S2b: SHERLOCK latent space, by reversibility",
              62: "Fig. S2c: enrichment of drug classes in SHERLOCK groups"},
             "EGFR inhibitor screen"),
    md("## Fig. S3a–b: CRISPRa kinome screen\n\n"
       "Drawn from the best CRISPRa run saved by "
       "[`scripts/kinome_crispri_crispra/2b_reproducibility_crispra.ipynb`]"
       "(../scripts/kinome_crispri_crispra/2b_reproducibility_crispra.ipynb), as for Fig. 2i–j; "
       "the plotting cells are not yet part of that notebook."),
    *section("kinome_crispri_crispra/2a_reproducibility_crispri.ipynb", upto(24),
             {24: "Fig. S3c (CRISPRi): group confidence across five runs"},
             "CRISPRi kinome screen: reproducibility",
             "Reloads the five saved runs from `results/reproducibility_meta_bootstrap_only_v1_noconditions_v2/`; "
             "missing runs are trained."),
    *section("kinome_crispri_crispra/2b_reproducibility_crispra.ipynb", upto(24),
             {24: "Fig. S3c (CRISPRa): group confidence across five runs"},
             "CRISPRa kinome screen: reproducibility"),
    *section("kinase_inhibitors_tcell/2_analysis_1uM.ipynb", upto(77),
             {41: "Fig. S5a: significance of downstream effects per condition (1 µM)",
              59: "Fig. S4a (1 µM): hierarchical clustering of drugs",
              71: "Fig. S4b (1 µM): condition dependence of each drug",
              77: "Fig. S4c (1 µM): downstream genes of CP673451 and STK16IN1 per condition"},
             "11 kinase inhibitors, 1 µM"),
    *section("kinase_inhibitors_tcell/3_analysis_10uM.ipynb", upto(86),
             {41: "Fig. S5b: significance of downstream effects per condition (10 µM)",
              59: "Fig. S4a (10 µM): hierarchical clustering of drugs",
              71: "Fig. S4b (10 µM): condition dependence of each drug",
              79: "Fig. S4c (10 µM): downstream genes of CP673451 and STK16IN1 per condition",
              86: "Fig. S6: expression of the shared CP673451 / ALWII4127 targets under T-cell co-culture"},
             "11 kinase inhibitors, 10 µM"),
    *section("norman/1_norman_analysis.ipynb", upto(35),
             {24: "Fig. S7: reproducibility across five runs (Norman)",
              35: "Fig. S8: genetic-interaction classification on the 22 held-out pairs"},
             "Norman: reproducibility and held-out pairs", NORMAN_NOTE),
    *section("norman/2_raw_expression_gi.ipynb", upto(14),
             {14: "Fig. S9: genetic-interaction classification from measured expression, SHERLOCK and GEARS"},
             "Norman: classification from measured expression",
             "Reads the per-run scores cached by `scripts/norman/1_norman_analysis.ipynb`."),
    *section("norman/3_module_interaction.ipynb", upto(9),
             {}, "Norman: consensus modules",
             "Builds `results/module_interaction/consensus_modules.csv`, used by Figs. S10–S15."),
    *section("norman/4_interaction_biology.ipynb", upto(31),
             {29: "Fig. S10: worked examples of five labelled pairs",
              6: "Fig. S11a: rule-classifier confusion matrix and per-parameter AUROC",
              31: "Fig. S11b: descriptor fingerprint per class",
              25: "Fig. S11c: the neomorphic rule",
              27: "Fig. S11d: class-average schematics",
              21: "Fig. S12a–c: consensus modules vs Norman clusters, measured programs and latent factors",
              19: "Fig. S13a–b: labelled interactions on the erythroid axis",
              10: "Fig. S14: latent factors matched across runs",
              23: "Fig. S15: perturbations driving F13, F5 and F12"},
             "Norman: interaction rules, modules and the erythroid axis"),
])
