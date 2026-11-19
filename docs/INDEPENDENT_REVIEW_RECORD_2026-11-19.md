# Record of the independent run and independent source pass, 19 November 2026

Filed by Nitin Prakash on 19 November 2026 (drafted by Claude). This is a record of what was received and what is and is not known. It is not a finding that the work was independent beyond what the helper stated.

## Who and what

- **Helper:** Gaurav Sharma, named in the header of his source-pass file. He is not Nitin Prakash and not an AI assistant. His relationship to the project and his experience are not recorded.
- **Part 1, source pass:** `data/reference_inventory/independent_pass_REVIEWER_2026-11-19.txt` (his list, unedited, as received). His annotated copy of the Java file is `data/reference_inventory/independent_pass_REVIEWER_annotated_copy_Md5Crypt_2026-11-19.java.txt` (unedited; a header line was added at line 2, so it is not the pinned file).
- **Part 2, run:** `analysis/raw/semgrep_checks_A_to_F_REVIEWER_2026-11-19.txt` (terminal text, unedited, as received). Ubuntu container, Python 3.12.3, Semgrep 1.186.0, run dated 19 November 18:22 (EST). He used `docs/independent_run/cb_run.sh`, a helper that wraps the commands of `docs/REPRODUCE.md`; it was not the document followed by hand.

## What the run shows

All seven input hashes and the rules commit matched. Checks A to F gave the expected counts (A 1 at line 15; B and C 0; D 1 at line 6; E 0 on two files with the three variable-form lines and DigestUtils line 469 shown; F 3, 3 and 1 on the rules’ own test files and 0 on Md5Crypt.java; getInstance 0). The script’s summary reads 33 matched, 0 differed. Each check ran twice and the two runs were identical. No difference from the expected results was found.

## Statements about independence

These statements were made by Gaurav and relayed to me by Nitin on 19 November at about 18:36. I have not verified them.
- No AI tool was used.
- Both parts were done without help from the author.
- Part 1 was started at 17:50 and finished at 18:25.

## Discrepancies and open points

- **Runner field.** The script was run with `RUNNER=YOURINITIALS` unchanged. The runner is identified only by the shell prompt (`gaurav@…`) and the Part 1 header.
- **Time.** The Part 1 header says about 50 minutes; the reported times give 35 minutes.
- **Order.** The guide asks for Part 1 to be finished before any Semgrep output is seen. The run output is time-stamped 18:22, three minutes before the reported end of Part 1 at 18:25. I do not know whether he had finished the list by then.
- **Line numbers.** His line numbers do not match the pinned file (for example, salt generation at 44 to 45 where the file has line 82, and cleanup at 292 to 296 where the file has 345 to 349). He wrote that the numbers are estimates, so only the operations can be compared, not the lines.
- **Wording and format.** The list is formatted as a numbered report with a “Final decision” section. I noted this to Nitin; Gaurav’s answer was that no AI tool was used. The record keeps both facts.
- **Missing items.** His hesitations during Part 2 were not reported.

## Status

- **Independent run (ISSUE-11):** received; the results match the expected values. Status: done by one person other than the author, with the points above. I treat it as the independent run, with those limits.
- **Independent source pass (ISSUE-09):** received; compared by operation, not by line (see `data/reference_inventory/independent_pass_comparison_2026-11-19.md`, a draft by Claude that Nitin has not yet reviewed). The inventory is not frozen.
