# Response and remaining-work note, Assignment 12

Nitin Prakash, CISC 699, 19 November 2026. Supervisor: Dr. Majid Shaalan. Nothing here has been confirmed by my supervisor.

## What this submission is

A near-final thesis, a research deck with speaking outline, a final-evidence appendix (EV-01 to EV-47), a cross-check record and a walkthrough script. The thesis is framed as a feasibility study of the Semgrep arm. The comparison across three methods has not been run, and no claim about tool performance is made. The framing is subject to your agreement; I have no reply yet.

## Response to the Assignment 11 feedback

Full entries, with change, evidence location and what is unresolved, are in `docs/RESPONSE_LOG.md` (H1 to H5).

- **H1, reference inventory: partly completed.** I decided that the operation is the primary unit. The 53 agreed lines are now a 10-item candidate inventory with asset or operation, algorithm, file, lines and a reason for each item; it validates against CycloneDX 1.6 (with a failing negative control) and is hashed (SHA-256 fa216520…f9cc). It is not frozen, because no independent person has read the source. Claude wrote the grouping and I have not yet reviewed it.
- **H2, zero findings: partly completed.** The pinned rule was read and its matching conditions written down. Twelve one-feature variants, with expected outcomes committed first, were run once: 12 of 12 matched the prediction, including the unprefixed call (V02) and a fully qualified receiver (V03). K4 now has three separate conclusions in the register and thesis and stays provisional. Claude wrote and ran this; I still need to read the rule myself and re-run the variants.
- **H3, independent reproducibility: pending.** My Docker re-run is described as repeatability, as you said. A person has agreed to follow `docs/REPRODUCE.md`; I am sending the package this week. The original transcript of my 14 November run will be attached.
- **H4, align findings with contribution: completed for the framing.** The question, contribution and conclusion are narrowed to a Semgrep feasibility study. The thesis states how true positives, false positives, false negatives and effort by phase would be counted once an inventory is frozen, and that undefined measures would be “not estimable”. No such figure is calculated. Sonar and TLS were not started and I did not invent results.
- **H5, human verification of AI-supported material: pending.** The verification matrix links each literature claim to its source, the AI step and my check. Every source is still marked † or ‡; I have not read them.

## Changes in this version

Chapter 1 (framing), §3.3 (unit, candidate, schema, freeze rule), §3.4 to §3.6 (new runs, register 4), §4.3 (twelve variants, three conclusions), §4.4, §5.2, §6 and §7.3 (dated work), the abstract, Appendix A (stable evidence identifiers) and Appendix B (AI log). Only K4 and K9 and limits L2, L4, L5, L8 and L9 changed in the register. Results audited again: the twelve variants and the inventory; earlier results were not re-audited.

## Remaining work, with dates

- **20 November:** read the rule file and re-run the twelve variants in my container; file the output as a `PERSONAL` record; update K4. Email you about the unit, the freeze and the framing. Send the independent-run and source-pass packages.
- **21 November:** review the 10 inventory items; read Näther and Hirsch, Ami et al. (confirm year, authors, DOI) and Amann et al.
- **22 November:** collect the independent run and source pass if they arrive; compare them item by item; only then freeze and hash the inventory.
- **Not started:** Sonar plugin, TLS scanner, sample set, scoring. If the feasibility framing is not accepted, each needs its own plan.

## Unresolved issue

Independence. Everything run so far was run by me or by Claude, and the inventory is not independent. The thesis says so wherever a claim depends on it.
