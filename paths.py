"""Central path configuration for the SHERLOCK reproducibility repository.

Every notebook under ``scripts/`` and ``figures/`` reads its inputs and writes its
outputs relative to the three roots below instead of hard-coding paths. Each root
defaults to a folder in this repository and can be moved with an environment
variable, for example::

    export SHERLOCK_DATA_DIR=/mnt/big_disk/sherlock_data

``data/`` and ``results/`` are placeholders; see their READMEs for how to populate
them. ``figures/`` holds the figure notebooks, and the panels they draw are written
to ``FIGURES_DIR`` (``figures/panels`` by default).
"""

import os

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.environ.get("SHERLOCK_DATA_DIR", os.path.join(REPO_ROOT, "data"))
RESULTS_DIR = os.environ.get("SHERLOCK_RESULTS_DIR", os.path.join(REPO_ROOT, "results"))
FIGURES_DIR = os.environ.get(
    "SHERLOCK_FIGURES_DIR", os.path.join(REPO_ROOT, "figures", "panels")
)

__all__ = ["REPO_ROOT", "DATA_DIR", "RESULTS_DIR", "FIGURES_DIR"]
