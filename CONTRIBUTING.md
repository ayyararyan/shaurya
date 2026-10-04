# Contributing to Shaurya

Shaurya is maintained as a controlled research and execution codebase. Changes should be small enough to review, reproducible from a clean checkout, and explicit about whether they affect Data, Research, Execution, or release infrastructure.

## Development workflow

1. Create a focused branch from the current default branch.
2. Keep generated data, local credentials, runtime state, caches, and machine-specific files out of Git.
3. Run the component's full local quality gate before opening a pull request.
4. Document observable behavior changes and any compatibility implications.
5. Merge only after the relevant CI checks pass.

## Component checks

### Data

```bash
cd data
uv sync --extra dev
uv run ruff check .
uv run mypy
uv run pytest
```

### Research

```bash
cd research
uv sync --extra dev
uv run ruff check .
uv run mypy
uv run pytest
```

### Execution

```bash
execution/scripts/validate_integration.sh
```

Execution builds used for review must keep live-routing options disabled.

## Research integrity

Registered hypotheses, frozen protocols, and dated amendments are part of the research audit trail. Do not silently rewrite a registration after outcomes have been inspected. A meaning-changing correction belongs in a dated amendment or successor specification with a clear link to the original record.

Implementation status and empirical support are separate claims. A passing software test does not establish market validity, profitability, causality, or external validity.

## Security

Never commit or paste credentials, private keys, tokens, account identifiers, broker responses containing secrets, private host details, or secret-bearing configuration. Use synthetic fixtures and redacted examples. Follow [SECURITY.md](SECURITY.md).

## Release discipline

Do not hand-edit generated release archives. Releases are built from a clean, attested Git commit through the documented release workflow. Component versions are independent; change a component version only when that component's compatibility or release contract requires it.

See [RELEASING.md](RELEASING.md).
