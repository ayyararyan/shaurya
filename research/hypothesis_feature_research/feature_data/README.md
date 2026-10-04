# Feature Data

This directory is reserved for small derived feature artifacts whose lineage, grain, and quality state are explicit. It never stores raw market tapes.

The catalogue may reference existing immutable derived tables in `manifest.csv` without copying them here. A reference records integrity metadata so the artifact can be identified without turning this directory into a data lake.

## Minimum long-form fields

```text
as_of_date
session_date
event_timestamp
instrument
venue
feature_id
feature_value
feature_version
source_dataset
source_test_or_pipeline
generated_at
code_revision
quality_status
```

Rules:

- `event_timestamp` is the market observation/anchor time; `generated_at` is provenance time.
- `feature_id` must resolve in [`../features.csv`](../features.csv).
- `source_dataset` must identify an immutable dataset or a documented synthetic fixture.
- Incomplete or cancelled captures are not eligible as completed sources.
- `quality_status` must state exclusions, partial support, or unvalidated status explicitly.
- Wide tables are allowed only when their keys, common grain, feature columns, and provenance fields are documented in `manifest.csv`.
- Regeneration must be bounded and read-only with respect to source data, with no broker, credential, order, or live-routing side effects.

See [`../schemas/feature_data.schema.md`](../schemas/feature_data.schema.md) for the complete contract.
