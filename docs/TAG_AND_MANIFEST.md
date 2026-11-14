# TAG_AND_MANIFEST.md

How tags, commits and the release manifest relate. Written 14 November 2026 in answer to the Assignment 10 feedback ("stabilize the final tag/manifest relationship").

## Rules

1. A **tag** names one commit. The **manifest** (`docs/RELEASE_MANIFEST.md`) at that commit lists the SHA-256 of every tracked file at that commit except the manifest itself.
2. A file cannot contain the hash of the commit that contains it. So the commit hash of a release is written outside the repository (in the memo or thesis and in Canvas) and in the list below, which is updated in a later commit. The tag is the stable name; the list below is a convenience.
3. The manifest is generated from the committed files and is committed before the tag is created. Nothing is edited between the manifest commit and the tag.
4. Anything committed after a tag is a **later change**. A document that cites a tag cites the files as they were at that tag, and names any later change that matters.
5. Submission copies of the memo and thesis are kept in Canvas. They cite the record commit; they are not part of the record commit.

## Tags

- `a10-rc2`: commit `baa4134`. Early release candidate (my own checks D and E added).
- `a10-rc3`: commit `81e88b0`. Check F, claim K9, trimmed records.
- `a10-rc6`: commit `e4c4687` (full hash `e4c46874f17ebc6c05c501e4ef48fe9ea2ee4d8c`). **The final Assignment 10 release.** The Assignment 10 memo cites it. The audited first candidate ("rc1") was commit `aeec71de620e5d8a000adbd79af4bd50ce929886`; it has no tag.
- `a10-rc4`, `a10-rc5`: never created. Some documents named `a10-rc5` before the final tag was chosen; they were corrected.
- `a11-draft1`: the Assignment 11 record release. Created from the commit named in the Assignment 11 cover note.

## Check performed on 14 November 2026

For `a10-rc6`, `a10-rc3` and `a10-rc2` I compared every manifest entry with the file at the tagged commit. At `a10-rc6`: 56 files tracked, 56 manifest entries, 0 hash differences, 0 missing, 0 extra. The tags at `a10-rc3` (43 files) and `a10-rc2` (42 files) also match their manifests. So the tag and manifest relationship holds at each tag. The only mismatch was at the branch tip, below.

To repeat the check, run `git show a10-rc6:docs/RELEASE_MANIFEST.md`, and for each listed path compare `git show a10-rc6:<path> | shasum -a 256` with the listed value.

## Drift found after `a10-rc6`

Between 18:33 and 19:01 on 5 November 2026, after the tag, nine files were edited in the GitHub web editor (commits `3722947`, `f918d70`, `153503d`, `f0fdd25`, `3c3bbd6`, `36a88ef`, `5d802a3`, `ae744d2`, `fa8cb22`). The branch tip therefore no longer matched the manifest at `a10-rc6` for `README.md`, the claims register v3, the audit record, the correction history, the issue log, the reproduction steps, the response log, the source ledger and the AI validation ledger. Those edits changed several statements about who wrote what and the status of ISSUE-09 (see `docs/CORRECTION_HISTORY.md`). On 14 November 2026 the nine files were restored to their tagged text. The edited versions stay in git history.

## Working rule from now on

Edits to files named in the manifest are made in a normal commit followed by a regenerated manifest, never directly in the web editor after a tag. A change to a tagged file's meaning is recorded in `docs/CORRECTION_HISTORY.md` with the commit hash.
