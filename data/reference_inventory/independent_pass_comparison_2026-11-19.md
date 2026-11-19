# Comparison of the independent source pass with candidate inventory v1, 19 November 2026

Draft by Claude, from the helper’s list and the candidate’s line numbers in the pinned file. Done by operation only, because the helper’s line numbers do not match the pinned file. No Semgrep output was used. Nitin Prakash has not reviewed this draft, and no item of the candidate has been changed.

## Agreement (the helper’s operation matches a candidate item)

- Helper 4 (password converted to UTF-8 bytes) and CB-INV-08.
- Helper 9 (SecureRandom created) and CB-INV-06.
- Helper 10 (salt validated and extracted) and CB-INV-07.
- Helper 11, 12, 13, 14 and 19 (the main MD5 digest: created, updated with password, prefix and salt, finalised) and CB-INV-01.
- Helper 15 (alternate MD5 of password, salt, password) and CB-INV-02.
- Helper 20 (1,000 rounds of MD5) and CB-INV-03.
- Helper 21 (final digest encoded to crypt Base64) and CB-INV-09.
- Helper 17 and 22 (clearing of digest, password, salt and final bytes) and CB-INV-10.

## Partly agreeing

- Helper 16 and 18 (the digest mixed into the main digest by password length and by bit) are in the MD5 main-digest flow. The candidate counts some of those lines under CB-INV-01 and has no separate item for them.
- CB-INV-04 (the scheme and its parameters: prefixes, block size, rounds) has no direct counterpart; the helper mentions the prefixes only inside item 13.

## Only in the helper’s list

- Helper 1, 2, 6 and 7: salt generation at the four public wrapper methods that call `B64.getRandomSalt`. The candidate’s CB-INV-05 lists two lines (188 and 245), which are in the longer overload and its null-salt branch.
- Helper 3 and 8: adding the `$apr1$` or `$1$` prefix to the salt in the wrapper methods.
- Helper 5: the call that hands the password and salt to the shared hashing method.

The question for Nitin is a scope question: does the candidate treat the wrapper call sites as part of the inventory? The 53 agreed lines include few of them. The unit decision (operation) points to adding them as call sites of CB-INV-05, or to a note that they are excluded.

## Only in the candidate

- CB-INV-04 (parameters and prefix constants), as above.

## Resolution

Not done. Nitin reviews this draft and the candidate, decides on the wrapper call sites, records each decision here, and, if the candidate changes, validates it again and writes a new hash before any freeze.
