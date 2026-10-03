# Gap-Open Research Record

This directory is a committed research record despite its `scratch/` location. It contains analysis code, frozen test specifications, reports, audits, and compact result artifacts for the gap-open research programme. It is not disposable temporary output.

## Start here

- [`FINDINGS_SUMMARY.md`](FINDINGS_SUMMARY.md) — consolidated findings and limitations
- [`GAP_FILL_SIGNAL_MODULE_SPEC.md`](GAP_FILL_SIGNAL_MODULE_SPEC.md) — proposed module boundary
- `GATE_A_*` — gap-fill put, censoring, stop/target, and walk-forward checks
- `GATE_B_*` — continuation, structure, exits, volume/open-interest, and robustness
- `FOLKLORE_BATTERY_*`, `NGE_*`, `RANGE_FORECAST_*`, `TAIL_CLIP_*`, and `VRP_*` — other registered research families

## File conventions

| Pattern | Role |
|---|---|
| `*.py` | Analysis or verification code |
| `*_SPEC.md` | Question/protocol frozen before the corresponding test |
| `*_TEST.md` and reports | Human-readable results and interpretation |
| `*_results.json` and audit files | Compact reproducibility artifacts |

[`gate_b_structure_search.py.orig`](gate_b_structure_search.py.orig) is intentionally retained as the documented pre-patch baseline; it is not an editor backup. `FOLKLORE_BATTERY_RESULTS.md` is an intentional report alias emitted by the corresponding analysis.

Source market data, model environments, caches, and large generated outputs are external to this tree.

## Interpretation

These files preserve the design and sample actually tested. They are research evidence, not a production signal catalogue or a trading-performance claim. Later work should amend or supersede a frozen question explicitly rather than silently rewriting its historical record.
