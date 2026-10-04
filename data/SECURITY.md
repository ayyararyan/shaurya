# Shaurya Data Security

Shaurya Data connects to market-data services and therefore treats credentials and local storage configuration as external operator concerns.

## Credentials

- Supply Dhan credentials through an external credential file or another explicitly supported credential handle.
- Never commit credential values, access tokens, refresh tokens, private keys, session cookies, or broker account identifiers.
- On POSIX systems, credential directories should normally be mode `0700` and credential files mode `0600`.
- Do not print credential values in logs or include them in bug reports, fixtures, screenshots, notebooks, or release artifacts.

Example:

```bash
shaurya-dhan-capture \
  --credentials /path/to/private/dhan.env \
  --security-master /path/to/dhan_instrument_master.csv \
  --security-id <id> \
  --expected-symbol <symbol>
```

The paths above are placeholders. Release documentation must not depend on a particular workstation, home directory, network share, or private host.

## Storage

Use `SHAURYA_NSE_ARCHIVE_ROOT` or an explicit supported output root to point Shaurya at an operator-controlled archive. Production capture is designed to fail closed when its configured archive is unavailable rather than silently falling back to an unintended local path.

Captured market data, catalogues, runtime state, and generated research output are not source artifacts and must remain outside Git unless a small synthetic or curated fixture is deliberately reviewed and committed.

## Release boundary

The `shaurya-data` distribution contains source code and package metadata only. Official release artifacts must not contain:

- credentials or secret-bearing configuration;
- captured market data;
- runtime catalogues or state;
- private SSH material;
- machine-specific logs; or
- unreviewed generated results.

For repository-wide reporting and supply-chain guidance, see [../SECURITY.md](../SECURITY.md).
