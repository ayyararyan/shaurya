# Catalogue Maintenance Tools

The tools in this directory validate and update the mechanical parts of the hypothesis/feature catalogue. They do not invent hypotheses, feature meanings, economic rationales, or evidence conclusions.

Run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 research/hypothesis_feature_research/tools/catalogue.py --check
PYTHONDONTWRITEBYTECODE=1 python3 research/hypothesis_feature_research/tools/catalogue.py --update-inventory
```

## `--check`

The validator checks, among other things:

- exact CSV shape and UTF-8 parsing;
- required fields and stable-ID syntax;
- uniqueness and cross-references;
- allowed implementation/evidence statuses;
- repository paths;
- feature-data integrity metadata;
- recursive coverage of `research/tests`; and
- whether the checked-in test inventory matches the source tree.

## `--update-inventory`

This mode updates only the deterministic test inventory. It uses stable path order and content hashes and avoids rewriting the file when the bytes would be unchanged.

Human-maintained hypothesis, feature, traceability, methodology, and evidence interpretations remain untouched.
