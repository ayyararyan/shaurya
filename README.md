# Shaurya

Shaurya is a monorepo for research-grade market data, derivatives research, and controlled order-execution infrastructure for Indian equity-index markets.

> **Release status:** research and shadow execution only. Ordinary release builds do not contain a live broker-order transport, and research outputs are not a trading track record.

## Components

| Component | Distribution / build | Purpose |
|---|---|---|
| [Data](data/) | `shaurya-data` (Python) | Capture, validate, catalogue, store, and replay market data |
| [Research](research/) | `shaurya-research` (Python) | Feature engineering, market-microstructure research, volatility surfaces, experiments, and reporting |
| [Execution](execution/) | C++20 + portable `kotak` operator bundle | Broker-neutral intent validation, risk checks, lifecycle control, reconciliation, and append-only execution records |

The components are intentionally independently buildable and independently versioned. A Shaurya repository release bundles the compatible component artifacts from one attested Git commit; it does not force the three projects to share a package version.

## Architecture

The dependency graph is deliberately one-way:

```text
Shaurya Data  ───────►  Shaurya Research

strategy clients ───►  Shaurya Execution
Shaurya Data ───────►  Shaurya Execution
                 offline routing metadata only
```

- **Data** owns market-data connectivity and storage. It has no order-placement authority.
- **Research** consumes the public Data catalogue/access interfaces. It has no broker or order authority.
- **Execution** is a C++ control plane. It does not import the Python Research project; only its offline routing-data path may consume Data's public instrument metadata.

## Repository layout

```text
.
├── data/        # Python market-data package
├── research/    # Python research package and research record
├── execution/   # C++ execution control plane and portable operator tooling
├── docs/        # repository-level policy documentation
└── .github/     # CI and repository-maintenance automation
```

Detailed maps and operating instructions live in each component README rather than being duplicated here.

## Quick start

### Data

Requires Python 3.11+ and `uv`.

```bash
cd data
uv sync --extra dev
uv run pytest
```

See [data/README.md](data/README.md) for capture, catalogue, validation, and replay usage.

### Research

Requires Python 3.11+ and `uv`. The source checkout resolves the sibling Data project through the declared local development source.

```bash
cd research
uv sync --extra dev
uv run pytest
```

See [research/README.md](research/README.md) for the research CLI, daily pipeline, dashboards, and evidence framework.

### Execution

Requires CMake 3.20+, a C++20 toolchain, Git, and Python for release tooling.

```bash
mkdir -p /private/tmp/shaurya-execution-build
cmake -S execution -B /private/tmp/shaurya-execution-build \
  -DCMAKE_BUILD_TYPE=Release \
  -DSHAURYA_ENABLE_LIVE_ROUTER=OFF \
  -DSHAURYA_ENABLE_KOTAK_LIVE=OFF
cmake --build /private/tmp/shaurya-execution-build --parallel
ctest --test-dir /private/tmp/shaurya-execution-build --output-on-failure
```

For the complete release gate, use `execution/scripts/validate_integration.sh`. See [execution/README.md](execution/README.md) for build attestation, shadow operation, and release packaging.

## Releases

A repository release contains:

- a wheel and source distribution for `shaurya-data`;
- a wheel and source distribution for `shaurya-research`;
- the deterministic `kotak` portable execution-operator archive and canonical manifest;
- a SHA-256 checksum manifest covering the release artifacts; and
- release metadata tied to one exact Git commit.

The authoritative procedure is [RELEASING.md](RELEASING.md). Repository-level changes are summarized in [CHANGELOG.md](CHANGELOG.md).

## Security and secrets

Credentials, private keys, access tokens, account identifiers, and runtime secrets must remain outside the repository and outside release artifacts. Shaurya code accepts external handles or explicitly supplied paths; secret-bearing files must be access-restricted by the operator.

See [SECURITY.md](SECURITY.md) and [data/SECURITY.md](data/SECURITY.md). Do not include sensitive deployment details in issues, logs, test fixtures, documentation examples, or generated release artifacts.

## Research and execution boundaries

Research documents may contain registered hypotheses, amendments, evidence logs, or historical experiment records. Those records are provenance, not product claims, and registered protocols must not be rewritten after outcomes are observed.

Execution release builds are deliberately fail-closed. Enabling `SHAURYA_ENABLE_LIVE_ROUTER` or `SHAURYA_ENABLE_KOTAK_LIVE` is rejected by the supported build. Shadow evidence is simulated or proxy evidence and must not be described as broker-confirmed execution.

## Development

Contribution and review expectations are documented in [CONTRIBUTING.md](CONTRIBUTING.md). Generated data, caches, credentials, runtime state, and local research outputs are excluded by [.gitignore](.gitignore).

## Documentation

- [Data documentation](data/README.md)
- [Research documentation](research/README.md)
- [Research documentation index](research/docs/README.md)
- [Execution documentation](execution/README.md)
- [Portable operator documentation](execution/ops/README.md)
- [Security policy](SECURITY.md)
- [Release procedure](RELEASING.md)

## License

Shaurya is proprietary software. See [LICENSE](LICENSE).
