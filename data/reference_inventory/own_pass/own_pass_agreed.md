# Agreed list for Md5Crypt.java (commit f13dd50f566c318283c4138820b15d75c26a0217)

Written by me (Nitin Prakash) on 4 November 2026 from my own pass 1 (own_pass_1.md, 31 October) and pass 2 (own_pass_2.md, 4 November).

Help received: Claude (AI assistant) printed the numbered file for me to read; told me that many line numbers in my first draft of pass 2 pointed at comments, imports or braces; offered wordings for my three rules (I chose 1A, 2A and 3B); showed me the disputed lines with their surrounding code; and transcribed my decisions into this file at my request, and grouped the shared lines using the reasons from my own entries. It did not choose which lines to keep. The keep/drop decision for every disputed line is mine, given in chat on 4 November 2026.

## My rules

Rule 1 (ranges): I keep single code lines. Comments and brace-only lines are never entries.
Rule 2 (imports and signatures): Imports and signatures are not counted, because the cryptographic work is in the method bodies.
Rule 3 (constants, salt checks, length): Format identifiers and salt validation count, because they decide what goes into the hash. A plain length read does not.

## Lines in both passes (43 lines, kept)

Reasons are condensed from my pass 2 entries.

- 61: block size of the MD5 digest (16 bytes).
- 67: the number of hashing rounds (1,000).
- 81, 98: APR1 hash with a generated 8-character salt (default generator; caller-provided generator).
- 245: generates a random 8-character salt when none is supplied.
- 251: the salt pattern (supported characters, maximum length eight).
- 259: obtains the MD5 message digest.
- 263, 267, 271: update the digest with the password, the prefix and the salt.
- 275-279: alternate MD5 digest from password, salt and password again.
- 282, 283: add bytes of the alternate digest to the main digest until the password length is covered.
- 288: clears the intermediate digest bytes.
- 296, 298: add digest or password bytes according to the bits of the password length.
- 306: finalises the initial digest.
- 311, 312: start of the 1,000-round loop and a fresh MD5 digest for each round.
- 314, 316, 318, 319, 321, 322, 325, 327, 329: digest updates inside each round with password, salt and previous digest, and the digest that closes the round.
- 334-339: encodes the final digest bytes into the crypt Base64 form.
- 344-348: resets the digest and overwrites password, salt and final digest bytes with zeros.

## Lines in only one pass

### Kept (10 lines)

- Line 58: kept (Rule 3). Format identifier.
- Line 64: kept (Rule 3). Format identifier.
- Line 150: kept. Handles secret bytes by converting the password string to UTF-8 bytes.
- Line 188: kept. Generates random data by calling getRandomSalt().
- Line 222: kept. Creates a SecureRandom instance.
- Line 252: kept (Rule 3). Salt matching.
- Line 253: kept (Rule 3). Salt validation.
- Line 254: kept (Rule 3). Invalid salt rejection.
- Line 256: kept (Rule 3). Salt extraction.
- Line 258: kept (Rule 3). Salt converted to bytes; counts as salt handling.

### Dropped (29 lines)

- Line 241: dropped (Rule 3). Plain length read.
- Line 305: dropped. Only builds the output string; does not generate random data, run a digest or directly handle secret bytes.
- Lines 281, 294, 295, 300, 313, 324: dropped. Control flow around digest updates (loop condition, branch, shift).
- Lines 21, 23: dropped (Rule 2). Imports.
- Lines 113, 132, 149, 167, 187, 204, 221: dropped (Rule 2). Method signatures.
- Lines 264, 265, 266, 268, 269, 270: dropped (Rule 1). Comments.
- Lines 255, 284, 299, 317, 320, 323: dropped (Rule 1). Brace-only lines.

### Dropped from the shared lines (4 lines)

- Lines 297, 315, 326: dropped (Rule 1). Brace-only `} else {`.
- Line 328: dropped (Rule 1). Closing brace only.

## Result

53 lines kept: 43 from both passes and 10 from only one pass.
