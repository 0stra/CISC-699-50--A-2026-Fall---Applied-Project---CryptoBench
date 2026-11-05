# Same-shape control (added 4 November 2026, Assignment 10)

`SameShapeControl.java` is a 14-line test input with two methods that do the same thing (MD5 through Apache `DigestUtils`) in two code shapes:

- `chainedForm` (line 6): `DigestUtils.getMd5Digest().digest(data)`. This is the shape the official rule `use-of-md5-digest-utils` describes.
- `variableForm` (lines 10-12): the digest object is stored in a variable, then `update` and `digest` are called on it. This is the shape `Md5Crypt.java` uses (lines 259, 275, 312).

**Provenance.** The file was written by Claude (AI assistant) at my request on 4 November 2026, as a minimal pair of the two shapes. It is a control input, not a sample for the benchmark, and it is the only file in `data/test_material/` that was authored rather than selected (an exception to the selection criteria in `data/test_material/README.md`). It contains no custom Semgrep rule. It must never be counted in any result as a code sample.

**Result.** The unmodified official rule finds line 6 only. See `analysis/raw/semgrep_samshape_control_REFERENCE_2026-11-04.txt`. Run by Claude in its container, not by me.

**sha256.** `657e8eb1ac803fecb27dcbe7808781c5fd315a4981c7f33424645d25ae7c8539`

**Limit.** A synthetic pair shows what this one rule does with these two shapes. It does not show how often real code uses either shape.
