# Shaurya Execution

Shaurya Execution is the C++20 broker-neutral order-control component of Shaurya. It owns intent validation, deterministic risk checks, idempotency, order lifecycle, reconciliation, and the append-only execution ledger.

**Supported release mode:** shadow only. Ordinary builds contain no live broker-order transport.

## Build and test

Use a clean, out-of-tree build:

```bash
mkdir -p /private/tmp/shaurya-execution-build
cmake -S execution -B /private/tmp/shaurya-execution-build \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=ON \
  -DSHAURYA_ENABLE_LIVE_ROUTER=OFF \
  -DSHAURYA_ENABLE_KOTAK_LIVE=OFF
cmake --build /private/tmp/shaurya-execution-build --parallel
ctest --test-dir /private/tmp/shaurya-execution-build --output-on-failure
```

The complete release gate is:

```bash
execution/scripts/validate_integration.sh
```

It performs a clean configure/build/test pass plus script and Python syntax checks. The build attests the exact Git commit and refuses unverifiable source metadata.

## Public surfaces

- `include/shaurya/execution/` — public C++ contracts and interfaces
- `contracts/` — versioned wire schemas and conformance fixtures
- `ledger/` — ledger format documentation and synthetic fixtures
- `tools/` — parity and ledger-repair executables
- `ops/` — portable `kotak` operator package
- `docs/` — contracts, recovery, installation, shadow operation, routing, and safety runbooks

## Operator package

The portable `kotak` lane is packaged independently from the CMake build:

```bash
commit=$(git rev-parse HEAD)
epoch=$(git show -s --format=%ct HEAD)
mkdir -p /private/tmp/shaurya-kotak-release

execution/ops/package_release.sh \
  --output-dir /private/tmp/shaurya-kotak-release \
  --version 1.0.0 \
  --source-epoch "$epoch" \
  --source-commit "$commit"
```

Verify the resulting archive against its canonical manifest before installation:

```bash
execution/ops/verify_manifest.sh \
  /private/tmp/shaurya-kotak-release/kotak-1.0.0.manifest.json \
  /private/tmp/shaurya-kotak-release/kotak-1.0.0.tar.gz
```

See [ops/README.md](ops/README.md) and [docs/INSTALL.md](docs/INSTALL.md).

## Shadow operation

Safe local operator entrypoints include:

```text
kotak help
kotak version
kotak doctor
```

Shadow-session actions require their documented explicit confirmation markers. See [docs/SHADOW_OPERATIONS.md](docs/SHADOW_OPERATIONS.md).

## Safety boundary

Supported builds intentionally reject live-routing options. Setting `SHAURYA_ENABLE_LIVE_ROUTER=ON` or `SHAURYA_ENABLE_KOTAK_LIVE=ON` is a build-time failure, not a dormant feature toggle.

Shadow fills and proxy evidence are not broker-confirmed executions. Live enablement requires a separate implementation/evidence review and is outside the supported release described here.

See:

- [EXECUTION_CONTROL_PLANE_SPEC.md](EXECUTION_CONTROL_PLANE_SPEC.md)
- [docs/SHADOW_SAFETY.md](docs/SHADOW_SAFETY.md)
- [docs/LIVE_ENABLEMENT_CHECKLIST.md](docs/LIVE_ENABLEMENT_CHECKLIST.md)
- [docs/LEDGER_AND_RECOVERY.md](docs/LEDGER_AND_RECOVERY.md)
- [docs/CONTRACTS.md](docs/CONTRACTS.md)

## Release provenance

Execution artifacts are tied to an exact source commit. Do not redistribute a locally edited archive under an official release name. Repository-level release policy is documented in [../RELEASING.md](../RELEASING.md).
