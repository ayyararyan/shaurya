# Hypothesis and Feature Research Catalogue

This catalogue maps research questions to features, experiments, source tests, and evidence. It complements the executable Research package and the registered `SIG` ledger; it does not replace raw evidence, frozen specifications, or source tests.

The core rule is simple: **software correctness and empirical support are separate claims.**

## Structure

| Path | Purpose |
|---|---|
| [`HYPOTHESES.md`](HYPOTHESES.md) | Human-readable master catalogue |
| `hypotheses.csv` | Stable hypothesis registry |
| `features.csv` | Feature definitions and provenance |
| `test_traceability.csv` | Mapping from source tests to hypotheses/features |
| [`methodology/`](methodology/) | Research-family methodology |
| [`data_sources.md`](data_sources.md) | Source lineage, timing, and completeness boundaries |
| [`feature_data/`](feature_data/) | Provenance records for small derived feature artifacts |
| `schemas/` | Machine-readable catalogue contracts |
| [`tools/`](tools/) | Deterministic inventory and validation tools |

Stable IDs form a many-to-many graph: an `HF-*` family contains `H-*` hypotheses; hypotheses use `F-*` features and are exercised by `T-*` tests. IDs are registered explicitly and are not renumbered merely because files move.

## Status semantics

Implementation status describes code availability only. Evidence status describes what a located design/sample supports.

A passing unit or integration test cannot, by itself, upgrade empirical evidence. Likewise, a supported empirical result does not excuse a broken or unreproducible implementation.

Statements should identify whether they are verified from code, verified from documentation/evidence, inferred, or awaiting researcher input.

## Maintenance

Before adding or changing catalogue content:

1. use an existing research family or register a stable family;
2. allocate the next explicit hypothesis/feature/test ID;
3. state the null/alternative, direction, timing, and evidence basis only where supported;
4. preserve causal timing and leakage constraints;
5. keep generated values separate from their source datasets; and
6. run the deterministic catalogue validator.

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 research/hypothesis_feature_research/tools/catalogue.py --check
```

When the recursive test inventory changes:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 research/hypothesis_feature_research/tools/catalogue.py --update-inventory
PYTHONDONTWRITEBYTECODE=1 python3 research/hypothesis_feature_research/tools/catalogue.py --check
```

The high-frequency registry rows are synchronized from the frozen runtime registries with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 research/hypothesis_feature_research/tools/sync_high_frequency_catalogue.py
```

Review the resulting diff before committing.

## Feature-data policy

Only small, derived values with explicit lineage belong under `feature_data/`. Raw market tapes do not.

Each artifact record must identify its dataset, grain, feature version, code revision, timestamps, quality status, size, and checksum. Incomplete or cancelled captures are not silently treated as complete sources.

## Researcher decisions

Economic rationale, family boundaries, hypothesis direction, interpretation of mixed evidence, confirmatory eligibility, materiality, and changes to pre-registered designs require explicit researcher judgment. The tooling may validate structure and provenance; it must not manufacture those decisions.
