# RESPONSE_LOG.md

Response log for the feedback on Assignment 09 (professor feedback, received before 4 November 2026). Each item: what was asked, the change made, where it is, and what is still unresolved. Updated 4 November 2026 (Assignment 10).

## F1. "Independently check the inventory"

- **Change made.** None that counts as an independent check yet. My own pass 1 over `Md5Crypt.java` (31 October) exists, but I had seen the provisional list first, so it is not independent.
- **Location.** `data/reference_inventory/own_pass/own_pass_1.md`, `p1_lines.txt`; ISSUE-09 in `docs/ISSUE_LOG.md`.
- **Unresolved.** Pass 2 (another day, without looking at pass 1), the agreed list and the comparison with the provisional list are not done. ISSUE-09 stays open. No recall figure may be computed from the provisional list.

## F2. "Create a same-shape control"

- **Change made.** Added a 14-line control with the same MD5 call in the chained and variable forms, and ran the unmodified official rule on it. Result: the rule finds the chained form (line 6) only.
- **Location.** `data/test_material/same_shape_control/`; `analysis/raw/semgrep_samshape_control_REFERENCE_2026-11-04.txt`; claim K8 and updated K4 in `analysis/results/claims_register_2026-11-04.md`; ISSUE-08 in `docs/ISSUE_LOG.md`; check D in `docs/REPRODUCE.md`.
- **Unresolved.** The control was written and run by Claude, once, in the container. I have not repeated it on my MacBook. Only one of the four rules was probed for shape.

## F3. "Attach stable claim records"

- **Change made.** Claims register version 2 with a stable evidence version (git tag), records, files, limits and "not claimed" lines for K1 to K8. Release manifest with SHA-256 for every file.
- **Location.** `analysis/results/claims_register_2026-11-04.md`; `docs/RELEASE_MANIFEST.md`.
- **Unresolved.** The register was written by Claude from the records; I have not yet checked every line against the raw files myself.

## F4. "Run the frozen procedure on the planned sample for Assignment 11"

- **Change made.** None yet. This is the Assignment 11 task.
- **Location.** Not applicable.
- **Unresolved.** The procedure cannot be called frozen while the reference inventory is not frozen (ISSUE-09) and no sample is selected. Fallback Rule 1 (continue with Semgrep and the TLS scanner) is in force; Rule 3 applies if fewer than 15 samples can be selected.

## Audit findings of 4 November 2026 (Assignment 10)

- **Tag did not exist.** Change: docs name the commit hash; I create the tag `a10-rc2`. Location: `docs/AUDIT_RECORD_A10.md` section 4. Unresolved until I push the tag.
- **K8 part not reproducible.** Change: check E added. Location: `docs/REPRODUCE.md` section 3. Unresolved: the re-test was by the author only.
- **Vague wording.** Change: placeholders, working folder, output wording and reviewer file delivery clarified. Location: `docs/REPRODUCE.md`. Unresolved: none known.
- **AI attribution removed from three files on 31 October.** Change: restored. Location: `data/reference_inventory/own_pass/own_pass_1.md`, `docs/PROCEDURE_NOTES.md`, `journal/2026-10-31.md`. Unresolved: none.
