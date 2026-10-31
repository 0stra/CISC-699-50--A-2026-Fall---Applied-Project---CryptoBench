# Own pass 1 over Md5Crypt.java (commit f13dd50f566c318283c4138820b15d75c26a0217)

Written by me (Nitin Prakash) on 31 October 2026 from my own reading of the file (361 lines, sha256 fa779456b25d2d36a6c464e200e106c2fa8e94a45dc608844ceb04407ea90747). Started: not recorded. Finished: before 16:31 EDT on 31 October 2026.

Limitation: I had seen the Hard Stop 4 list and a grep output before this pass, so it is not fully independent. This is pass 1 of 2. Pass 2 and the agreed list are still to do, so the reference inventory is not frozen and ISSUE-09 stays open.

Help received: Checked that each of my line numbers points at the code I described, and told me when numbers pointed at comments or braces so that I could correct them. It formatted my first six entries into this layout from my notes. It did not choose which lines to include.

Line numbers refer to the file as printed by `cat -n` (the numbers in `p1_lines.txt`, one per line, with ranges expanded).

## Entries

Line(s): 58
What the code does: Identifies the Apache APR1 MD5-based hashing variant with the "$apr1$" prefix.
Why it matters for cryptography: It identifies a legacy MD5-based password scheme.

Line(s): 61
What the code does: Defines the fixed MD5 digest block size of 16 bytes.
Why it matters for cryptography: It matches the MD5 digest length.

Line(s): 64
What the code does: Identifies the standard MD5-crypt variant with the "$1$" prefix.
Why it matters for cryptography: It identifies a legacy MD5-based password scheme.

Line(s): 67
What the code does: Defines the fixed hashing work factor of 1,000 rounds.
Why it matters for cryptography: A low, fixed iteration count weakens password hashing.

Line(s): 81
What the code does: Generates an eight-character salt using the default random source.
Why it matters for cryptography: The salt is randomised by a secure source.

Line(s): 98
What the code does: Generates an eight-character salt using a caller-supplied Random instance.
Why it matters for cryptography: Security depends on which Random the caller supplies.

Line(s): 150
My reason (from my notes): Converts the password string into bytes.

Line(s): 188
My reason (from my notes): Generates a random salt using the supplied Random for MD5 crypt.

Line(s): 222
My reason (from my notes): Creates a SecureRandom instance for salt generation.

Line(s): 241
What the code does: Gets the password length.
Why it matters for cryptography: The password length controls how many password bytes are incorporated into the hashing process.

Line(s): 245
What the code does: Generates an eight-character random salt using the supplied Random instance.
Why it matters for cryptography: A random salt helps ensure that identical passwords produce different hashes.

Line(s): 251-256
What the code does: Validates the salt format and extracts the actual salt value.
Why it matters for cryptography: Salt validation ensures that only correctly formatted salt values are used in the hashing process.

Line(s): 258
What the code does: Converts the salt string into UTF-8 bytes.
Why it matters for cryptography: The hashing algorithm processes the salt as bytes rather than as a Java string.

Line(s): 259
What the code does: Creates the main MD5 digest instance using DigestUtils.getMd5Digest().
Why it matters for cryptography: This selects MD5 as the cryptographic hashing algorithm used to generate the password hash.

Line(s): 263
What the code does: Adds the password bytes to the main MD5 digest.
Why it matters for cryptography: The password is the secret input used to calculate the resulting password hash.

Line(s): 267
What the code does: Adds the algorithm prefix to the MD5 digest.
Why it matters for cryptography: The prefix distinguishes the APR1 and standard MD5-crypt hashing variants.

Line(s): 271
What the code does: Adds the salt bytes to the main MD5 digest.
Why it matters for cryptography: Including the salt makes the resulting hash dependent on both the password and salt.

Line(s): 275-279
What the code does: Creates an alternate MD5 digest, adds password and salt bytes, and calculates its digest.
Why it matters for cryptography: This generates intermediate cryptographic data required by the MD5-crypt algorithm.

Line(s): 282-283
What the code does: Adds intermediate digest bytes to the main MD5 digest in chunks of up to 16 bytes.
Why it matters for cryptography: It incorporates intermediate hash material into the main hashing calculation.

Line(s): 288
What the code does: Clears the intermediate digest byte array.
Why it matters for cryptography: It attempts to reduce the amount of sensitive intermediate cryptographic data remaining in memory.

Line(s): 296-298
What the code does: Adds either an intermediate digest byte or a password byte depending on the password-length bit-processing logic.
Why it matters for cryptography: This implements a password-dependent step in the MD5-crypt algorithm.

Line(s): 305-306
What the code does: Prepares the output prefix and salt, then calculates the initial MD5 digest.
Why it matters for cryptography: This produces the initial digest that becomes the input for the repeated hashing rounds.

Line(s): 311-312
What the code does: Starts the 1,000-round hashing loop and creates an MD5 digest for each round.
Why it matters for cryptography: Repeated hashing increases the computational work required to calculate a password hash.

Line(s): 314-316
What the code does: Adds password bytes or previous digest bytes to the current MD5 digest.
Why it matters for cryptography: These inputs ensure that each hashing round depends on the password and previous digest.

Line(s): 318-319
What the code does: Adds salt bytes when the iteration number is not divisible by three.
Why it matters for cryptography: The salt is incorporated into selected hashing rounds, making the calculation dependent on the salt.

Line(s): 321-322
What the code does: Adds password bytes when the iteration number is not divisible by seven.
Why it matters for cryptography: The password is incorporated into selected hashing rounds according to the algorithm's iteration rules.

Line(s): 325-329
What the code does: Adds password or previous digest bytes and calculates the next MD5 digest.
Why it matters for cryptography: This produces the successive intermediate hashes used throughout the repeated hashing process.

Line(s): 334-339
What the code does: Encodes the final MD5 digest bytes using the crypt Base64 encoding method.
Why it matters for cryptography: It converts the binary digest into the textual password-hash representation.

Line(s): 344-345
What the code does: Resets the main and alternate MD5 digest instances.
Why it matters for cryptography: It clears the digest instances' internal processing state after hashing.

Line(s): 346-348
What the code does: Clears the password, salt and final digest byte arrays.
Why it matters for cryptography: It attempts to remove sensitive password and cryptographic data from memory after processing.

Unsure about: nothing recorded.
