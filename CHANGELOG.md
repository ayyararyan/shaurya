# Changelog

This changelog tracks repository-level release engineering and packaging changes. Component-specific research and implementation history remains in Git and in the component documentation.

## Unreleased

### Release hardening

- Standardized the repository and component READMEs around the supported Data, Research, and Execution boundaries.
- Added repository-level security, contribution, licensing, and release policies.
- Defined one reproducible monorepo release bundle while preserving independent component versions.
- Added CI release gates for Python lint/type/test/build checks, C++ integration tests, deterministic Execution packaging, artifact checksums, and package smoke installation.
- Removed machine-specific operational details from the package-facing security documentation.
- Clarified that supported Execution builds are shadow-only and that research results are not trading-performance claims.

## Component versions in the current release line

| Component | Version source | Current version |
|---|---|---:|
| Shaurya Data | `data/pyproject.toml` | 0.2.0 |
| Shaurya Research | `research/pyproject.toml` | 0.2.0 |
| Shaurya Execution | `execution/CMakeLists.txt` | 0.1.0 |
| Portable `kotak` operator | `execution/ops/kotak` | 1.0.0 |

A repository release records these versions together with the exact source commit. See [RELEASING.md](RELEASING.md).
