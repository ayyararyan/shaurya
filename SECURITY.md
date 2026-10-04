# Security Policy

Shaurya handles market-data credentials and execution-adjacent configuration, so release hygiene is intentionally conservative.

## Secret handling

- Store credential values, private keys, access tokens, and account-specific secrets outside the repository.
- Pass secrets through external credential handles, environment variables, or explicitly supplied files; do not embed values in source code, fixtures, documentation, or manifests.
- On POSIX systems, secret directories should be owner-only (`0700`) and secret files owner-readable/writable only (`0600`) unless a stricter deployment policy applies.
- Release artifacts must contain no runtime credentials, broker sessions, private host keys, local state, or captured market data.
- Logs and error messages must avoid printing secret values.

## Reporting a security issue

Do not open a public issue containing credentials, account identifiers, private hostnames, deployment topology, or a working exploit. Contact the repository owner through a private channel and include the minimum reproduction detail necessary to diagnose the issue.

If a credential may have been exposed, rotate or revoke it before continuing investigation. Removing a secret from the latest commit is not sufficient if it has entered Git history.

## Execution safety

Supported release builds keep live broker routing disabled and fail closed when live-routing build options are requested. Changes that alter authentication, broker transport, risk gates, order lifecycle, reconciliation, ledger integrity, or release verification require focused security review and negative-path tests.

## Supply-chain and release integrity

Official artifacts are generated from an exact Git commit, validated by CI, and distributed with SHA-256 checksums. Do not install or redistribute locally modified release archives under an official release name.

Component-specific guidance is available in [data/SECURITY.md](data/SECURITY.md) and the Execution security/runbook documentation.
