# Ledger Test Fixtures

This directory documents the synthetic fixture lane used by execution-ledger tests.

Tests generate deterministic runtime records beneath isolated `/private/tmp` directories so filesystem identity, permissions, locking, truncation, and fsync behavior are exercised rather than mocked.

Generated ledgers are test runtime state and are not committed as production evidence.
