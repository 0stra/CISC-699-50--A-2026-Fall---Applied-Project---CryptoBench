# data/

This folder holds the project's test material and the frozen reference
inventory, kept in two separate, non-overlapping subfolders so the answer
key can never be contaminated by the material it is built from.

- test_material — the selected Java code samples and the list of
  authorised TLS endpoints (FR-1). Populated once selection is complete;
  locked after that.
- reference_inventory — the independently built, frozen answer key
  (FR-2, NFR-4). Built by two independent manual review passes over
  test_material/ before any discovery tool is run. Read-only after freeze.

No discovery tool writes to this folder. Tool output lives under
`analysis/raw/`, never here — that separation is what makes the reference
inventory trustworthy as ground truth (see `docs/ENVIRONMENT.md` and the
Literature and Requirements Brief, Section 3.5, for why this matters).
