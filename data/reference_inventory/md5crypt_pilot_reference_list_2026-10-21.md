# Pilot reference list for one file (not the frozen CryptoBench inventory)

File: Md5Crypt.java, Apache Commons Codec (Apache License 2.0), commit f13dd50f566c318283c4138820b15d75c26a0217, 361 lines. Line numbers below were checked against this copy and also match the copy on my laptop (361 lines, same crypto lines).

Status: this list was drafted by reading the file on 21 October 2026. So it does not meet the CryptoBench freeze rule (two independent passes by me with full agreement). It is used only to test the comparison procedure on one file. I check each entry against the file in my recorded walkthrough.

Scope: only cryptographic uses a source-code scanner could see in this one file.

1. Line 259. MD5 digest created with DigestUtils.getMd5Digest(), assigned to a variable (main hash).
2. Line 275. A second MD5 digest created the same way (alternate sum).
3. Line 312. A third MD5 digest creation, inside the loop at line 311, so it is repeated each round.
4. Lines 58, 64 and 240. The MD5-based password hash scheme itself: the $apr1$ and $1$ prefixes and the md5Crypt method.
5. Line 67 (used at line 311). Fixed work factor: 1000 rounds.
6. Line 98. Salt generated from a caller-supplied java.util.Random (apr1Crypt).
7. Line 188. Salt generated from a caller-supplied java.util.Random (md5Crypt).
8. Line 245. Salt generated from a caller-supplied java.util.Random (inside the four-argument md5Crypt).
9. Line 222. Default salt source is java.security.SecureRandom (a secure choice, recorded as present).

Total: 9 entries. Entries 1 to 3 are the ones the official Semgrep MD5 rule for DigestUtils is meant to see.
