# qcalc — Automating FHI-aims workflows

qcalc is a lightweight command-line interface that helps you set up, run, analyze, and visualize **FHI-aims** electronic-structure calculations. It covers routine tasks such as generating `control.in`, `geometry.in`, and XYZ files, preparing queue/job scripts, post-processing outputs, and plotting results.

> Built with plain Python (no heavy frameworks). Optional plotting uses Matplotlib.

## Features

**Command-line interface** (`qcalc`) for end-to-end workflows:
  - `run` — run calculations (wrapper around your execution environment)
  - `move` — collect and move outputs to a destination folder
  - `convert` — XYZ ⇄ `geometry.in`
  - `controlin` — generate `control.in` with the bundled “light” basis presets
  - `job` — create job/queue scripts (supports `longq`, `workq`, `shortq`)
  - `analysis` — extract properties from outputs (energies, ΔE, HOMO/LUMO, magnetization, relaxation info, etc.)
  - `plot` — quick plots of analysis tables

Always validate basis settings for production runs.

## Installation

You can install `qcalc` directly from the GitHub repository using pip:

```bash
pip install git+https://github.com/gallpinheiro/qcalc.git
```

For details on any command, use the help flag:

```bash
qcalc <command> -h
```
