# Response and remaining-work note, Assignment 12

Nitin Prakash, CISC 699, 19 November 2026. Supervisor: Dr. Majid Shaalan. Nothing here has been confirmed by my supervisor.

## What this submission is

A near-final thesis, a research deck with speaking outline, a final-evidence appendix (EV-01 to EV-47), a cross-check record and a walkthrough script. The thesis is framed as a feasibility study of the Semgrep arm. The comparison across three methods has not been run, and no claim about tool performance is made. The framing is subject to your agreement; I have no reply yet.

## Response to the Assignment 11 feedback

Full entries, with change, evidence location and what is unresolved, are in `docs/RESPONSE_LOG.md` (H1 to H5).

- **H1, reference inventory: partly completed.** I decided that the operation is the primary unit. The 53 agreed lines are now a 10-item candidate inventory with asset or operation, algorithm, file, lines and a reason for each item; it validates against CycloneDX 1.6 (with a failing negative control) and is hashed (SHA-256 fa216520…f9cc). It is not frozen. The same helper wrote an independent list of operations from the source (`data/reference_inventory/independent_pass_REVIEWER_2026-11-19.txt`); a draft comparison by operation shows most items agree and that his list has wrapper-level salt and prefix operations the candidate lacks. His line numbers do not match the pinned file. Claude wrote the grouping and the draft comparison; I have not yet reviewed either.
- **H2, zero findings: partly completed.** The pinned rule was read and its matching conditions written down. Twelve one-feature variants, with expected outcomes committed first, were run once: 12 of 12 matched the prediction, including the unprefixed call (V02) and a fully qualified receiver (V03). K4 now has three separate conclusions in the register and thesis and stays provisional. Claude wrote and ran this; I still need to read the rule myself and re-run the variants.
- **H3, independent reproducibility: done by one person, with limits.** On 19 November Gaurav Sharma ran checks A to F in an Ubuntu container (Semgrep 1.186.0) and all 33 comparisons matched the expected values (`analysis/raw/semgrep_checks_A_to_F_REVIEWER_2026-11-19.txt`). Limits: he used a helper script that wraps the commands in `docs/REPRODUCE.md`; his statements that he used no AI tool and had no help are relayed by me and unverified; and his run output is time-stamped three minutes before the reported end of his source pass. My own Docker re-run is still described as repeatability. The original transcript of my 14 November run is to be attached.
- **H4, align findings with contribution: completed for the framing.** The question, contribution and conclusion are narrowed to a Semgrep feasibility study. The thesis states how true positives, false positives, false negatives and effort by phase would be counted once an inventory is frozen, and that undefined measures would be “not estimable”. No such figure is calculated. Sonar and TLS were not started and I did not invent results.
- **H5, human verification of AI-supported material: pending.** The verification matrix links each literature claim to its source, the AI step and my check. Every source is still marked † or ‡; I have not read them.

## Changes in this version

Chapter 1 (framing), §3.3 (unit, candidate, schema, freeze rule), §3.4 to §3.6 (new runs, register 4), §4.3 (twelve variants, three conclusions), §4.4, §5.2, §6 and §7.3 (dated work), the abstract, Appendix A (stable evidence identifiers) and Appendix B (AI log). Only K4 and K9 and limits L2, L4, L5, L8 and L9 changed in the register. Results audited again: the twelve variants, the inventory and the reviewer run; earlier results were not re-audited.

## Remaining work, with dates

- **20 November:** read the rule file and re-run the twelve variants in my container; file the output as a `PERSONAL` record; update K4. Email you about the unit, the freeze and the framing. Ask Gaurav for the placeholder initials and the hesitation notes he did not send.
- **21 November:** review the 10 inventory items and the draft comparison with the independent list; decide whether wrapper-level salt and prefix operations belong in the inventory; read Näther and Hirsch, Ami et al. (confirm year, authors, DOI) and Amann et al.
- **22 November:** if the candidate changes, validate it again; then freeze and hash the inventory.
- **Not started:** Sonar plugin, TLS scanner, sample set, scoring. If the feasibility framing is not accepted, each needs its own plan.

## Unresolved issue

Independence is limited. One person other than me has now reproduced checks A to F and written an independent list of operations, but his statements are relayed and unverified, his line numbers do not match the file, and the variants and the inventory grouping were written and run by Claude. The thesis says so wherever a claim depends on it.
