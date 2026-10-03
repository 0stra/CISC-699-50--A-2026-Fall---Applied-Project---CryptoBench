# data/reference_inventory/

This folder holds the project's frozen ground truth (FR-2, NFR-4). It is
built by two independent manual review passes over `data/test_material/`
and is never written to by a discovery tool.

## Schema

`reference_inventory_template.json` is a CBOM-compatible (CycloneDX)
skeleton with the project's category schema and observability flag already
defined as fields, and zero component rows populated — population only
happens once test material is selected and both independent review passes
agree (FR-2).

Each populated row, once real entries exist, will carry:

- **CBOM-standard identifiers** — `type`, `name`, and the cryptographic
  `properties` fields CycloneDX already defines, so the file stays
  interoperable with other CycloneDX-compatible tooling (FR-3).
- **category** — a project-local field, one of: `key-establishment`,
  `digital-signature`, `hashing`, or `protocol-transport-configuration`
  (FR-4).
- **observability** — a project-local field recording which layer(s) can
  detect this asset: `source-visible`, `endpoint-visible`, or `both`. This
  is what lets coverage be scored against a defensible denominator instead
  of one blended total (see the Design Review Package, Section 7.1).

The `specVersion` field in the template is intentionally left as a
placeholder rather than hard-coded, to be filled in with whichever
CycloneDX version is actually in use once the Sonar Cryptography Plugin is
installed and its native output format is confirmed (see `ISSUE-01` in the
risk log).

## Freeze rule

This file is not edited after both independent review passes agree on its
contents. Any later correction is itself a disagreement and triggers a
re-run of both passes, not a silent edit (Literature and Requirements
Brief, Table 3).
