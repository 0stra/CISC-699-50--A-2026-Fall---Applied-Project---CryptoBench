# analysis/raw/

Unmodified output from each discovery method, one subfolder or file set per
method, written once per run and never edited in place (FR-8).

Expected contents once the main run begins:

- Semgrep's findings output, run with unmodified rule files pinned by commit
  (no custom rules — NFR-6). The registry ruleset `p/cryptography` does not
  exist (ISSUE-06), so it is not used.
- The Sonar Cryptography Plugin's native `cbom.json` output.
- The TLS scanning tool's per-endpoint negotiated-parameter output.

As of 29 October 2026 this folder holds only pilot records on validation inputs (one public Java file and the rule authors' test file), not main-run output. Files ending `REFERENCE` were run by Claude in a cloud container, and files ending `PERSONAL` are my own runs on my MacBook. Nothing from the pilot set is written here until the reference inventory (`data/reference_inventory/`) is frozen and each method has passed its known-positive and known-negative validation gate. See `docs/PROCEDURE_NOTES.md` and `docs/ENVIRONMENT.md` for why that sequencing is enforced rather than optional.
