# SIG Claim Ledger

This directory is the pre-registration and claim ledger for Shaurya's signal-research programme. Its central rule is chronological: a hypothesis or material protocol change is recorded before the outcomes governed by it are inspected.

Literature can motivate a claim; it does not settle the claim.

## Claim IDs

One file is maintained for each `SIG-01` taxonomy cell. Claim IDs use `<CELL>-nn` and are stable once assigned.

| Cell | Prefix | File | SIG task |
|---|---|---|---|
| Book state | `BK` | [`book-state.md`](book-state.md) | SIG-02 |
| Event flow | `EF` | [`event-flow.md`](event-flow.md) | SIG-03 |
| Price-path derived | `PP` | `price-path.md` | SIG-04 |
| Cross-asset | `XA` | `cross-asset.md` | SIG-05 |
| Options-specific | `OP` | `options.md` | SIG-06 |
| Time and regime | `TR` | `time-regime.md` | SIG-16 |

Programme gates and market claims are distinct objects: a gate can require a measurement before inference is justified; a claim states a proposition about market behavior.

## Registered execution hypotheses

`H-*` files are frozen execution protocols committed before outcome inspection. Their registering commit is part of the audit trail.

| Registration | File | Registering commit | Status |
|---|---|---|---|
| `H-SIG21` — deep-book anomaly to later NIFTY-futures response | [`H-SIG21.md`](H-SIG21.md) | `f2cf650` (2026-08-19) | Active; outcome gate closed |

### Amendments

A registration body is never edited in place after registration. Meaning-changing corrections are recorded as dated, numbered amendments.

| Amendment | Amends | Timing | Summary |
|---|---|---|---|
| [`H-SIG21-A1.md`](H-SIG21-A1.md) | `H-SIG21` §6 | Pre-data | Primary non-overlap window changed to each cell's own `Z + h2`; family-maximum window retained as robustness |
| [`H-SIG21-A2.md`](H-SIG21-A2.md) | Session calendar/derived ceilings | Pre-data | Corrected the date-versioned NSE F&O close and derived session ceilings |

The amendment files contain the full approval and timing evidence.

## Binding method

[`METHOD.md`](METHOD.md) governs claim registration, hypotheses, trial logs, measurement axes, resolution statements, power requirements, verdict vocabulary, and commit-order pre-registration.

Read it before adding or testing a claim.

## Required fields

Each claim records:

- economic or microstructure mechanism;
- resolved citations;
- observable capture path;
- confirming test;
- falsifying test; and
- identification status under the relevant contract.

## Status vocabulary

`Proposed` → `Agreed` → `Tested` → `Confirmed` / `Falsified` / `Inconclusive`.

Claims are retained after testing. Falsification changes status; it does not erase the registered record.
