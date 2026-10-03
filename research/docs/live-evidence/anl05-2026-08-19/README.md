# ANL-05 Dashboard Presentation Evidence — 2026-08-19

This directory records the presentation-only redesign of the ANL-03 surface dashboard. The change preserved model meaning, thresholds, and measured values. Two visible panels were removed through an explicit owner-approved specification amendment while their underlying objects remained available through the state API.

## Presentation changes

- light/dark theme with persisted preference;
- monospaced, tabular-numeral typography for stable live values;
- hairline rules and a full-width status rail in place of card-heavy framing;
- muted slate/brass/brick/sage status palette with redundant glyph/text encoding;
- explicit plotting of `SUR-05` violating points;
- fitted ATM-IV hero values by expiry;
- persistent rotate/pan/zoom camera state across refresh; and
- removal of the sustained-latency chart and forward-source table from the visible shell, while retaining both objects in `/api/state`.

The binding specification history remains in the relevant task and module-spec records.

## Verification recorded at the time

- dashboard-focused tests and the broader suite passed;
- changed files passed Ruff and mypy;
- ATM hero values matched the `k = 0` surface grid to numerical precision in the recorded replay;
- camera persistence, drag modes, and reset behavior were exercised in a headless browser; and
- the presentation palette was checked for status distinguishability with redundant non-color cues.

## Screenshots

The retained screenshots were rendered from the documented replay sample:

| File | State |
|---|---|
| `anl05-light.png` | healthy, light |
| `anl05-dark.png` | healthy, dark |
| `anl05-degraded-light.png` | degraded feed + forced `SUR-05` violations, light |
| `anl05-degraded-dark.png` | degraded feed + forced `SUR-05` violations, dark |

## Scope of evidence

These files are dated verification evidence, not a claim about current production rendering or live trading. The recorded verification was headless/replay based; it did not establish live-session performance.
