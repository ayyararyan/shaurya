# Portable `kotak` Operator

The `kotak` package is Shaurya Execution's portable, once-per-session operator control plane. It is not an order router and does not ship a live broker transport.

## Command classes

### Offline

```text
kotak help
kotak version
kotak doctor
```

These commands require no broker credential and do not contact a remote host.

### Explicit remote/shadow operations

Remote diagnostics and shadow-session operations are deliberately narrow, non-interactive, and fail closed. Commands that alter session state require their documented confirmation markers even in dry-run mode.

See [../docs/SHADOW_OPERATIONS.md](../docs/SHADOW_OPERATIONS.md) for the supported operator sequence.

## Trust model

The package:

- uses a fixed operator identity and strict known-hosts verification;
- disables password, keyboard-interactive, forwarding, and implicit shell behavior;
- validates file ownership, modes, path ancestry, and content digests before use;
- binds remote compatibility to source/build/protocol evidence; and
- emits a closed result-marker grammar rather than arbitrary remote response bodies.

Operator-provisioned identity and known-hosts files are external configuration. They are never created, copied, or embedded by the release package.

## Package a release

Packaging is deterministic and binds the archive to the verified Git commit:

```bash
commit=$(git rev-parse HEAD)
epoch=$(git show -s --format=%ct HEAD)
mkdir -p /private/tmp/kotak-release

execution/ops/package_release.sh \
  --output-dir /private/tmp/kotak-release \
  --version 1.0.0 \
  --source-epoch "$epoch" \
  --source-commit "$commit"
```

Outputs:

```text
kotak-1.0.0.tar.gz
kotak-1.0.0.manifest.json
```

Verify before installation:

```bash
execution/ops/verify_manifest.sh \
  /private/tmp/kotak-release/kotak-1.0.0.manifest.json \
  /private/tmp/kotak-release/kotak-1.0.0.tar.gz
```

The manifest covers package paths, modes, sizes, SHA-256 digests, release version, compatibility version, source commit, and archive digest.

## Install, update, and rollback

See [../docs/INSTALL.md](../docs/INSTALL.md) for the authoritative commands.

The installer uses a caller-owned prefix, stages and verifies every file, then atomically switches the active release. The previous verified release remains available for rollback. Uninstall is manifest-scoped and preserves foreign or modified paths.

## State and concurrency

Configuration, state, and installed releases are kept outside the source tree. Release mutations use a kernel advisory lock and identity-checked paths. Interrupted updates are journaled and recovered without treating stale pathnames as trusted state.

## Testing

The portable release tests use isolated temporary homes and synthetic/recording dependencies. They do not contact a broker, authenticate to a real host, invoke a production service manager, or install into the operator's real home.

Cross-platform test success is portability evidence only; it is not certification of a particular deployment.
