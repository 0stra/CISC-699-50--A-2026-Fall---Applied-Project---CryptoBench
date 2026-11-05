# Comparison of my agreed list with the provisional list (4 November 2026)

Files compared: `own_pass_agreed.md` (and `agreed_lines.txt`, 53 line numbers) against `data/reference_inventory/md5crypt_pilot_reference_list_2026-10-21.md` (drafted by Claude, 9 entries, 11 line numbers). The line-number comparison was done by Claude from the two files and checked against the pinned file (sha256 fa779456b25d2d36a6c464e200e106c2fa8e94a45dc608844ceb04407ea90747). I have not yet gone through it line by line myself.

## What matches

- Every one of the 9 provisional entries has its main line or lines in my agreed list: entry 1 (line 259), entry 2 (275), entry 3 (312), entry 5 (67), entry 6 (98), entry 7 (188), entry 8 (245), entry 9 (222), and entry 4 (lines 58 and 64).
- Ten of the 11 provisional line numbers are in my agreed list.

## What differs

- Provisional line 240 (the four-argument `md5Crypt` signature, part of entry 4) is not in my agreed list, because my Rule 2 does not count method signatures.
- 43 lines of my agreed list are not in the provisional list. They are the lines that run or feed the digest and handle the secret bytes: the digest updates and the loop around them, the second-stage rounds, the Base64 encoding of the digest, the zeroing of password, salt and digest arrays, the salt checks, the block size (61) and the password-to-bytes conversion (150).
- So the provisional list names where MD5 digests and salts are created, and my list also includes where they are used and cleaned up. The two lists use different units (9 entries against 53 lines).

## How to read this

- This is not a recall or precision figure. Neither list is a verified answer key. Agreement between a list drafted by Claude and my own list does not show that either is correct, and differences mostly come from the rules I chose (Rules 1 to 3 in `own_pass_agreed.md`).
- Pass 1 was not independent of the provisional list (I had seen it). Pass 2 was written after I had read the numbered file, with help described in `own_pass_agreed.md`.
- The passes disagreed on 39 lines (13 only in pass 1, 26 only in pass 2). The agreed list is the result of applying my three rules to those lines, and I dropped four lines that both passes listed (brace-only lines). It is not full agreement of two independent passes, which is what the freeze rule asks for. Dr. Shaalan should confirm whether the reconciled list can be frozen.
