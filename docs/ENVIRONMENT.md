# CryptoBench — Environment Configuration and Reproducibility

This file is the environment
record itself, kept in the repository and updated in place as each version is
actually installed — not a description of an environment that exists elsewhere.

## Pinned versions

- **Operating system:** `[laptop OS and version — fill in at first setup]`
- **Java (JDK):** `[version pinned at first build]`
- **Build tool:** whichever build file ships with the selected Java project
  (Maven or Gradle — recorded once the project is selected)
- **Git:** `[version]`
- **Semgrep:** `[version]`, registry cryptography ruleset, unmodified
- **SonarQube:** pinned to a version within the Sonar Cryptography Plugin's
  documented compatible range — releases of the plugin from 1.3.7 onward
  require SonarQube 9.9 LTS or later, and SonarQube 10.5.0 and above is
  documented to break the plugin's cryptography rules, so the version
  actually installed must fall strictly between those two bounds.
  **Exact version:** `[to be recorded at installation]`
- **Sonar Cryptography Plugin:** `[version]`, paired explicitly with the
  SonarQube version above
- **TLS scanning tool:** `[version]`

These entries are left as an honestly filled template rather than invented
placeholder numbers. A fabricated version string would be worse than a
recorded gap — see `ISSUE-01` in the risk log: the Sonar Cryptography Plugin
is not yet installed. This file gets updated with the real version the
moment that installation happens, not before.

## Setup instructions (for a peer to reproduce this environment)

1. Install the pinned JDK and Git.
2. Install Semgrep and confirm its registry cryptography ruleset is
   available, with no custom rules added.
3. Install SonarQube at a version inside the documented compatible range
   above and confirm it starts successfully.
4. Install the Sonar Cryptography Plugin at a version paired to that
   SonarQube installation.
5. Install the TLS scanning tool.
6. Record every installed version in this same file before running any
   discovery method against real test material.

No step in this sequence requires writing or compiling custom code; every
tool above is installed and configured, not authored.
