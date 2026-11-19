# Speaking outline for the research presentation, Assignment 12

Deck: eleven slides, about nine to ten minutes. The course presentation time was not given in the brief, so this length is my assumption; the deck can be cut to eight slides by dropping slides 3, 5 and 10. Speaker notes are also stored on each slide of the deck. Claims on every slide are the thesis’s own and are not stronger. Evidence identifiers (EV-xx) are in Appendix A of the thesis.

1. **Cover (0:30).** A feasibility pilot. The comparison has not been run. Nothing is approved by my supervisor.
2. **Problem (0:45).** Post-quantum migration needs an inventory. Free tools claim to discover cryptography. Guidance says no single method suffices, and there is little evidence against an independent answer key.
3. **Literature and gap (1:00).** Policy documents assert the need; the format exists; the two tool papers are preprints with their own benchmarks; a score depends on the counting unit. The gap is a comparison of free methods against one independent key. Sources not yet read by me.
4. **Questions (0:45).** RQ1 answered for one file, RQ2 in part, RQ3 and RQ4 not answered. The feasibility framing awaits Dr. Shaalan’s agreement.
5. **Method (1:00).** Designed for three tools, executed for one. Pinned inputs. Checks A to F. Twelve variants.
6. **Evidence: the procedure repeats (1:00).** 1, 0, 0, 1 across checks A to D; four Semgrep versions; all runs by me or Claude; no independent run.
7. **Evidence: the zero (1:30).** Three conclusions. The rule needs the chained form; twelve variants agree. Conclusion 3 is not established. K4 stays provisional until I read the rule and re-run the variants.
8. **Evidence: the inventory (1:00).** 60 and 73 lines, 39 disagreements, 53 agreed, 10 operation items, valid CycloneDX 1.6, hashed, not frozen, grouping not yet reviewed by me.
9. **Contribution (0:45).** A bounded method: the three-way reading, shape-matched controls, the unit effect, and the trail from claim to record.
10. **Limits and remaining work (0:45).** One file, four rules, no independent run, Sonar and TLS not started; dated next steps.
11. **AI use (0:30).** What Claude did, what I decided, what I have not yet checked.

Likely questions and honest answers: *Why not run Sonar or TLS?* Not installed, no authorised target. *Is K4 established?* No, provisional. *Why the operation as unit?* The feedback pointed to assets or operations, and a line unit is not comparable with asset-level tools; the choice is unconfirmed. *Who ran the variants?* Claude; I will re-run them.
