# Research Documentation

This directory is the durable documentation and evidence index for Shaurya Research. It separates standing specifications, registered hypotheses, empirical results, operational evidence, background research, and superseded material so that current interfaces are easy to find without erasing provenance.

## Directory map

| Directory | Contents |
|---|---|
| [`module-spec/`](module-spec/) | Standing module ownership and requirements (`ANL`, `BKT`, `CON`, `GRK`, `INF`, `MIG`, `NAT`, `RSK`, `SIG`, `SUR`, `VOL`) |
| [`sig-claims/`](sig-claims/) | Pre-registered hypothesis ledger, frozen `H-*` protocols, dated amendments, and the binding method |
| [`results/`](results/) | Curated result artifacts and reports for completed studies |
| [`live-evidence/`](live-evidence/) | Dated exploratory/live evidence records tied to specific sessions or tapes |
| [`research/`](research/) | Literature reviews and background research |
| [`specs/`](specs/) | Research tooling and pipeline specifications |
| [`legacy/`](legacy/) | Superseded or closed specifications, task ledgers, handoff notes, and historical change records |

## Standing references

The following top-level documents remain current references rather than closed study artifacts:

| Document | Purpose |
|---|---|
| [`CONTRACTS.md`](CONTRACTS.md) | Research-facing interface and data contracts |
| [`SURFACES.md`](SURFACES.md) | Options/futures surface objects and semantics |
| [`SIG-21-CALIBRATION-RUNBOOK.md`](SIG-21-CALIBRATION-RUNBOOK.md) | Standing SIG-21 calibration procedure |
| [`SURFACE-MISPRICING-SPEC-2026-08-20.md`](SURFACE-MISPRICING-SPEC-2026-08-20.md) | Active surface-mispricing specification |
| [`D39-FIXED-TARGET-PANEL-SPEC-2026-08-21.md`](D39-FIXED-TARGET-PANEL-SPEC-2026-08-21.md) | Fixed-target panel specification |
| [`D49-C8-RESPONSE-SURFACE-SPEC-2026-08-21.md`](D49-C8-RESPONSE-SURFACE-SPEC-2026-08-21.md) | C8 response-surface specification |
| [`D51-10S-FEATURE-SELECTION-SPEC-2026-08-21.md`](D51-10S-FEATURE-SELECTION-SPEC-2026-08-21.md) | D51 feature-selection specification |

## Provenance rules

- A registered protocol is not rewritten after outcomes are inspected; use a dated amendment or successor protocol.
- A historical evidence file may retain machine/session details necessary for provenance, but those details are not package defaults or current deployment guidance.
- Result files state the design and sample they support; they are not generalized into trading-performance claims.
- Superseded documents remain traceable in `legacy/` rather than being deleted.

For the executable package surface, return to [../README.md](../README.md).
