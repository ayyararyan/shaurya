# Secret Handling

This repository-level compatibility document preserves links from historical Shaurya specifications. The active security policy is [../SECURITY.md](../SECURITY.md).

## Binding rules

- Configuration may identify a credential by environment-variable name or by an external file path; credential values must not be committed.
- Secret-bearing directories and files must be access-restricted by the operator. On POSIX systems, the normal baseline is `0700` for directories and `0600` for files.
- Credentials, tokens, private keys, broker sessions, account identifiers, and private deployment details must not appear in release artifacts, logs, fixtures, screenshots, or documentation examples.
- Historical migration inventories and machine-specific deployment notes are operational records, not package documentation, and are intentionally excluded from this public-facing policy.

Component-specific market-data guidance is in [../data/SECURITY.md](../data/SECURITY.md).
