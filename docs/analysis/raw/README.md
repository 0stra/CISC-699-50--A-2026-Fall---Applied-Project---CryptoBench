# analysis/raw/

Unmodified output from each discovery method, one subfolder or file set per
method, written once per run and never edited in place (FR-8).

Expected contents once the main run begins:

- Semgrep's findings output, run against the registry cryptography ruleset
  (no custom rules — NFR-6).
- The Sonar Cryptography Plugin's native `cbom.json` output.
- The TLS scanning tool's per-endpoint negotiated-parameter output.

This folder is empty as of this check-in. Nothing is written here until
after the reference inventory (`data/reference_inventory/`) is frozen and
each method has passed its known-positive and known-negative validation
gate — see `docs/ENVIRONMENT.md` and the Design Review Package's build
order for why that sequencing is enforced rather than optional.
