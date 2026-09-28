# Shaurya Research

Shaurya Research is the independently installable analysis component of Shaurya. It contains market-microstructure features, volatility-surface tooling, predictive experiments, walk-forward evaluation, research dashboards, daily pipelines, and persistent research evidence.

**Distribution:** `shaurya-research`  
**Python:** 3.11+  
**Market-data dependency:** the public catalogue/access interface supplied by `shaurya-data`

Shaurya Research has no broker connectivity, order-placement authority, or live execution engine.

## Install and test

From a source checkout:

```bash
cd research
uv sync --extra dev
uv run ruff check .
uv run mypy
uv run pytest
```

The source workspace resolves the sibling Data project through Research's declared development source. Official release artifacts declare `shaurya-data` as a normal package dependency.

Build the package with:

```bash
uv build
```

## Daily research pipeline

Run the quality-aware post-close pipeline against a completed Data catalogue handle:

```bash
shaurya-daily-research \
  --catalog /path/to/datasets \
  --date 2026-08-26 \
  --output-root /path/to/research-output
```

Or pin an exact dataset:

```bash
shaurya-daily-research \
  --catalog /path/to/datasets \
  --dataset-id ds-example \
  --output-root /path/to/research-output
```

The pipeline validates lifecycle, schema, hashes, ordered replay, and domain coverage through `DataAccess` before producing `FINAL_MEMO.md` and machine-readable result artifacts.

## Installed commands

| Command | Purpose |
|---|---|
| `shaurya-research` | Hypothesis, evidence, and walk-forward research tooling |
| `shaurya-daily-research` | Daily post-close research pipeline |
| `shaurya-ofi-dashboard` | Order-flow-imbalance research dashboard |
| `shaurya-surface-dashboard` | Implied-volatility surface dashboard |
| `shaurya-live-ofi-studies` | Focused live/read-only OFI studies |
| `shaurya-rolling-c8` | Rolling C8 study runner |
| `shaurya-feature-selection-experiment` | Feature-selection experiment runner |

Use `--help` on each command for the current contract.

Additional bounded research scripts live under `scripts/`; they are not installed console commands.

## Data boundary

Current research pipelines consume logical rows and dataset identities through Shaurya Data. Research should not discover raw capture directories, open broker connections, or treat a local file path as a substitute for a verified dataset lifecycle.

Historical experiments that deliberately pin older evidence remain reproducible through documented compatibility paths. Their existence does not relax the boundary for new work.

## Research integrity

Shaurya separates:

- software correctness from empirical evidence;
- exploratory results from confirmatory or identification-grade claims;
- implementation status from economic support; and
- current protocols from immutable historical registrations and dated amendments.

A passing test demonstrates software behavior, not profitability or external validity. Pre-registered protocols and their amendments live under [docs/sig-claims/](docs/sig-claims/). The broader hypothesis/feature catalogue lives under [hypothesis_feature_research/](hypothesis_feature_research/).

## Generated output

Large or local generated outputs belong outside Git. Only deliberately curated, reviewable evidence and compact reproducibility artifacts should be committed.

The repository `.gitignore` excludes normal runtime output, caches, and generated research lanes.

## Documentation

- [docs/README.md](docs/README.md) — research documentation index
- [docs/sig-claims/README.md](docs/sig-claims/README.md) — pre-registration ledger
- [hypothesis_feature_research/README.md](hypothesis_feature_research/README.md) — hypothesis/feature catalogue
- [docs/DAILY-AUTOMATION.md](docs/DAILY-AUTOMATION.md) — daily evidence-orchestration contract

## Release and security

The package is built and tested as part of the repository release gate described in [../RELEASING.md](../RELEASING.md). It contains research code and metadata only; credentials, captured market data, runtime state, and private deployment details are not release artifacts.

See [../SECURITY.md](../SECURITY.md).
