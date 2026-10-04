# Releasing Shaurya

Shaurya uses repository releases to bundle independently versioned components from one exact Git commit.

## Release contents

A complete release contains:

| Artifact | Source |
|---|---|
| `shaurya-data` wheel and sdist | `data/` |
| `shaurya-research` wheel and sdist | `research/` |
| `kotak-<version>.tar.gz` | `execution/ops/` |
| `kotak-<version>.manifest.json` | deterministic Execution package manifest |
| `SHA256SUMS` | checksums for all distributable artifacts |
| release metadata | component versions + exact Git commit |

Component versions remain authoritative in their own metadata. A repository release must record them; it must not rewrite them merely to create a common version number.

## Release gate

From a clean checkout, the release workflow must establish all of the following:

1. Data: dependency sync, Ruff, mypy, pytest, wheel/sdist build.
2. Research: dependency sync, Ruff, mypy, pytest, wheel/sdist build.
3. Execution: clean out-of-tree CMake configure/build, CTest, script/Python syntax checks.
4. Portable operator: deterministic package build followed by canonical-manifest verification.
5. Package integration: install the freshly built Data and Research wheels together in a clean environment and import their public packages.
6. Artifact integrity: generate SHA-256 checksums after all artifacts are assembled.
7. Provenance: bind artifacts to the exact Git commit used by the workflow.

A failing gate blocks publication. Do not waive a failed test by editing the artifact after CI.

## Candidate workflow

Release preparation happens on a dedicated `release/*` branch. The release workflow creates or refreshes a **draft prerelease** from the branch's attested commit. Draft status is intentional: it provides a final inspection point for documentation, artifact names, checksums, and package contents before anything is published.

## Final publication

Before publishing a draft:

- confirm the intended repository visibility;
- confirm no release artifact contains secrets, private machine paths, runtime state, captured market data, or unreviewed generated output;
- review `CHANGELOG.md` and component versions;
- verify the release commit is the reviewed commit intended for distribution;
- verify `SHA256SUMS` against the uploaded artifacts.

Public package-index publication is not part of the default Shaurya release process. Any PyPI or other registry publication requires a separate explicit decision and registry-specific credential handling.

## Rollback

A bad draft is replaced, not patched in place. A published release that must be withdrawn should remain traceable: mark it superseded, document why, and issue a new release from a reviewed commit rather than mutating already distributed bytes.
