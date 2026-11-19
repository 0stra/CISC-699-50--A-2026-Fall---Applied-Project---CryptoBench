# Quick guide for the independent run (about 1 hour in total)

Thank you for helping. I need two things from you, done in this order, **without asking me for help** (if something is unclear, write down what you did and carry on). You may not look at my own results before you finish. Nobody needs to log in anywhere, and nothing here scans any website or server.

## Part 1: read one Java file (45 to 60 minutes, browser or text editor only)

Do this first, before you run anything.

1. Open this public file (361 lines): https://github.com/apache/commons-codec/blob/f13dd50f566c318283c4138820b15d75c26a0217/src/main/java/org/apache/commons/codec/digest/Md5Crypt.java
2. List every place where the file performs, or prepares for, a cryptographic operation. Work from the source only. For each one write: a short name for the operation; the algorithm or kind of material (for example a hash algorithm, a random source, a salt, a password); the line number or numbers; and one sentence on why you think it counts.
3. Note where you were unsure and what you decided. Do not ask me what counts. If a rule is unclear, write down how you interpreted it.
4. Do not use any scanner or AI tool for this part.

Write it in a plain text file called `part1_list.txt`. Start the file with your name or initials, the date, and how long it took.

## Part 2: run the checks (about 20 minutes)

You need a Mac or Linux terminal. On Windows, use Docker (option B). Do not use a computer you are not allowed to install software on.

### Step 1. Get a terminal with Semgrep

**Option A, Mac or Linux terminal (needs `git`, `curl` and Python 3.8 or newer):**

    python3 -m venv ~/cb-venv
    source ~/cb-venv/bin/activate
    pip install semgrep
    semgrep --version

**Option B, Docker (any computer with Docker Desktop):**

    docker run -it --name cb-friend ubuntu:24.04 bash

Then, inside that container:

    apt-get update && apt-get install -y git curl python3 python3-venv
    python3 -m venv ~/cb-venv
    . ~/cb-venv/bin/activate
    pip install semgrep
    semgrep --version

(Use `bash`, not `sh`. If you leave the container, `docker start -ai cb-friend` takes you back in.)

If a different Semgrep version prints, that is fine. Just keep the output.

### Step 2. Download the helper script and run it

Replace `YOURINITIALS` with your name or initials.

    curl -fsSL -o cb_run.sh https://raw.githubusercontent.com/0stra/CISC-699-50--A-2026-Fall---Applied-Project---CryptoBench/main/docs/independent_run/cb_run.sh
    RUNNER=YOURINITIALS bash cb_run.sh 2>&1 | tee cb_run_output.txt

It downloads public files, checks their fingerprints, runs the checks A to F twice each, and prints for every check what it expected and what it got. It takes a few minutes (the rules repository is large). At the end it prints a line such as `SUMMARY: 33 matched, 0 differed`. It is a convenience wrapper around the commands in `docs/REPRODUCE.md`; it adds no analysis.

### Step 3. If something stops or fails

Do not fix it quietly. Copy the error text, say what you did, and carry on if you can. The script stops by itself if a downloaded file does not have the expected fingerprint; send me that output too.

## What to send back

Send me these four things:

1. `part1_list.txt` (Part 1).
2. `cb_run_output.txt` (Part 2, the whole file, unedited). In Docker: `docker cp cb-friend:/root/cb_run_output.txt .` from a second terminal, or simply copy and paste the text.
3. A few lines about Part 2: where you hesitated, guessed or got stuck, and which instruction was confusing.
4. Two sentences, true or false: “I did Part 1 from the source only, without help from the author.” and “I followed Part 2 without help from the author.” If false, say what help was given.

Please send everything by **Saturday 21 November, evening**. If you are late, send what you have. A partial result is still useful. Thank you!
