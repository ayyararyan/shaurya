# Shaurya Data

Shaurya Data is the independently installable market-data component of Shaurya. It owns market-data acquisition, immutable storage, integrity validation, dataset cataloguing, discovery, and deterministic replay. It contains no order-placement or live-trading authority.

**Distribution:** `shaurya-data`  
**Python:** 3.11+  
**Primary storage:** segmented Parquet with append-only lifecycle/catalogue metadata

## Install and test

From a source checkout:

```bash
cd data
uv sync --extra dev
uv run ruff check .
uv run mypy
uv run pytest
```

Build distributable artifacts with:

```bash
uv build
```

Official Shaurya releases build the wheel and source distribution in CI from an attested Git commit.

## Public dataset interface

Consumers locate data through the catalogue contract rather than by scanning capture directories:

```python
from datetime import date
from pathlib import Path

from shaurya.data import DataAccess, DataCatalog

catalog = DataCatalog(Path("/path/to/archive/2026-08-26/metadata/datasets"))
handle = catalog.get_dataset(trading_date=date(2026, 8, 26))

access = DataAccess(catalog)
access.validate(handle)
rows = access.rows(handle)
```

The equivalent CLI surface includes:

```bash
shaurya-data catalog list --catalog /path/to/datasets
shaurya-data catalog get  --catalog /path/to/datasets --date 2026-08-26
shaurya-data validate     --catalog /path/to/datasets --date 2026-08-26
shaurya-data preview      --catalog /path/to/datasets --date 2026-08-26 --limit 100
shaurya-data export       --catalog /path/to/datasets --dataset-id ds-example --output /tmp/preview.csv
```

`inspect` and `preview` are human-oriented. Validation checks lifecycle state, ordered segment metadata, hashes, schema, sequence, coverage, and logical replay. Machine export is explicit; production capture remains Parquet/catalogue based.

## Live capture

Credential and security-master files are external inputs:

```bash
shaurya-dhan-capture \
  --credentials /path/to/private/dhan.env \
  --security-master /path/to/dhan_instrument_master.csv \
  --security-id <id> \
  --expected-symbol <symbol>
```

For option-chain capture:

```bash
shaurya-chain-capture --help
```

For the daily combined-chain launcher:

```bash
shaurya-daily-chain-launch --help
```

Deployments should configure archive locations explicitly with `SHAURYA_NSE_ARCHIVE_ROOT` or supported CLI options. Package documentation intentionally avoids workstation-specific paths.

## Storage model

A completed v2 dataset is a logical stream over immutable Parquet segments plus append-only metadata:

```text
YYYY-MM-DD/
├── raw/
│   └── ... immutable Parquet segments ...
├── metadata/
│   └── datasets/
├── indexes/
└── derived/
```

Writers close and validate a temporary segment, atomically publish it, hash it, and only then publish catalogue metadata. File presence alone does not imply a completed dataset; completion is a lifecycle state.

Recovery inventory distinguishes partial files from final-but-unpublished orphans. Neither is promoted silently.

## Active consumers

Capture can expose accepted canonical rows through an authenticated localhost stream for bounded low-latency consumers. This fan-out is operational convenience, not a second source of record. Immutable storage and catalogue metadata remain authoritative for replay and recovery.

Use:

- `DataAccess.live(handle)` for bounded low-latency observation;
- `DataAccess.follow(handle)` for immutable-segment publication boundaries; and
- `DataAccess.rows(handle)` for deterministic completed-dataset replay.

## Legacy data

Legacy JSONL tapes and their sidecars remain available through compatibility paths so earlier experiments can be reproduced. Conversion is explicit and preserves the source representation; it does not silently replace historical evidence.

## Security

Secrets, runtime state, and captured data must remain outside Git and outside release artifacts. See [SECURITY.md](SECURITY.md) and the repository [security policy](../SECURITY.md).

## Documentation

- [DAT.md](DAT.md) — canonical Data specification and architecture
- [SECURITY.md](SECURITY.md) — credential and storage security
- [ADR-0001-SEGMENTED-PARQUET-STORAGE.md](ADR-0001-SEGMENTED-PARQUET-STORAGE.md) — storage-v2 decision record
- [STORAGE_V2_IMPLEMENTATION_PLAN.md](STORAGE_V2_IMPLEMENTATION_PLAN.md) — migration and acceptance criteria
- [DAT_01_RECONCILIATION.md](DAT_01_RECONCILIATION.md) — original client-reconciliation record
