#!/usr/bin/env bash
# CryptoBench independent run helper. Follows docs/REPRODUCE.md (checks A to F) step by step.
# It changes nothing outside the folder ~/cb-work. It makes no network scan: it only downloads
# public files from github.com and raw.githubusercontent.com.
# Usage:  bash cb_run.sh 2>&1 | tee cb_run_output.txt
echo "=== CryptoBench independent run ==="
echo "Runner (your name or initials): ${RUNNER:-NOT SET}"
echo "Date: $(date)"; echo "OS: $(uname -a)"
echo "Semgrep version: $(semgrep --version 2>&1 | tail -1)"
echo "Python: $(python3 --version 2>&1)"
mkdir -p ~/cb-work && cd ~/cb-work || exit 1
PASS=0; FAIL=0
ok(){ echo "  RESULT: MATCHES EXPECTED  ($1)"; PASS=$((PASS+1)); }
bad(){ echo "  RESULT: DIFFERS FROM EXPECTED  ($1)"; FAIL=$((FAIL+1)); }

echo; echo "=== STEP 1: fetch pinned rules ==="
[ -d semgrep-rules ] || git clone -q https://github.com/semgrep/semgrep-rules.git
cd semgrep-rules && git checkout -q 17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9
H=$(git rev-parse HEAD); echo "rules commit: $H"
[ "$H" = 17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9 ] && ok "rules commit" || { bad "rules commit"; echo "STOP: wrong rules commit"; exit 1; }

echo; echo "=== STEP 2: fetch pinned Apache files and verify SHA-256 ==="
B=https://raw.githubusercontent.com/apache/commons-codec/f13dd50f566c318283c4138820b15d75c26a0217/src
curl -fsSL -o ../Md5Crypt.java $B/main/java/org/apache/commons/codec/digest/Md5Crypt.java
curl -fsSL -o ../StringUtils.java $B/main/java/org/apache/commons/codec/binary/StringUtils.java
curl -fsSL -o ../DigestUtils.java $B/main/java/org/apache/commons/codec/digest/DigestUtils.java
curl -fsSL -o ../DigestUtilsTest.java $B/test/java/org/apache/commons/codec/digest/DigestUtilsTest.java
cat > ../SameShapeControl.java <<'JAVA'
import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class SameShapeControl {
  public byte[] chainedForm(byte[] data) {
    return DigestUtils.getMd5Digest().digest(data);
  }

  public byte[] variableForm(byte[] data) {
    final MessageDigest ctx = DigestUtils.getMd5Digest();
    ctx.update(data);
    return ctx.digest();
  }
}
JAVA
sha(){ if command -v sha256sum >/dev/null; then sha256sum "$1" | cut -d' ' -f1; else shasum -a 256 "$1" | cut -d' ' -f1; fi; }
chk(){ got=$(sha "$1"); echo "$1"; echo "  got      $got"; echo "  expected $2"; [ "$got" = "$2" ] && ok "hash" || { bad "hash"; echo "STOP: input differs from the one the records describe"; exit 1; }; }
chk ../Md5Crypt.java fa779456b25d2d36a6c464e200e106c2fa8e94a45dc608844ceb04407ea90747
chk ../StringUtils.java 6c44ebc7424c69fd04b6f3df10332934a149e6901fd29e86d96df4176527a99a
chk ../DigestUtils.java 427fa77411e7a0ea7798151b199aa17892b7f1043ad7d26baf566d2d97e36347
chk ../DigestUtilsTest.java b886f74b8450318218366af7d486666de1e1a94945e81f3ba191ef36cbbda426
chk ../SameShapeControl.java 657e8eb1ac803fecb27dcbe7808781c5fd315a4981c7f33424645d25ae7c8539
chk java/lang/security/audit/crypto/use-of-md5-digest-utils.java bd22fdb5ef195e383ec69aa9dbf1d0fd8f6cb5d41aef3f725f1aba5e5aa05908
chk java/lang/security/audit/crypto/use-of-md5-digest-utils.yaml a0614baf029418dd9b298713c3328f371faa1edb0eac7cc2c4a3a99ce1a220a5

echo; echo "=== STEP 3: run the checks (each twice; run 2 is compared with run 1) ==="
O="--metrics=off --disable-version-check"
C=java/lang/security/audit
R1=$C/crypto/use-of-md5-digest-utils.yaml
FOUR="--config $R1 --config $C/crypto/use-of-md5.yaml --config $C/crypto/weak-random.yaml --config $C/md5-used-as-password.yaml"
run(){ # name, expected summary text, extra expected text ("" if none), semgrep args...
  n=$1; es=$2; ex=$3; shift 3
  echo; echo "--- Check $n ---"; echo "command: semgrep scan $O $*"
  semgrep scan $O "$@" >run1.txt 2>&1; semgrep scan $O "$@" >run2.txt 2>&1
  echo "----- full output of run 1 -----"; cat run1.txt; echo "----- end -----"
  s=$(grep -E "^Ran [0-9]+ rules? on [0-9]+ files?:" run1.txt | tail -1)
  echo "summary line: $s"; echo "expected:     $es"
  [ "$s" = "$es" ] && ok "summary" || bad "summary"
  if [ -n "$ex" ]; then grep -q "$ex" run1.txt && ok "expected marker $ex" || bad "marker $ex not found"; fi
  if diff -q run1.txt run2.txt >/dev/null; then ok "run 2 identical to run 1"; else bad "run 2 differs from run 1"; diff run1.txt run2.txt | head -20; fi
}
run A "Ran 1 rule on 1 file: 1 finding." "15┆" --config $R1 $C/crypto/use-of-md5-digest-utils.java
run B "Ran 4 rules on 1 file: 0 findings." "" $FOUR ../Md5Crypt.java
run C "Ran 4 rules on 1 file: 0 findings." "" $FOUR ../StringUtils.java
run D "Ran 1 rule on 1 file: 1 finding." "6┆" --config $R1 ../SameShapeControl.java
run E "Ran 1 rule on 2 files: 0 findings." "" --config $R1 ../DigestUtils.java ../DigestUtilsTest.java
echo "--- Check E, lines to look at ---"
sed -n '259p;275p;312p' ../Md5Crypt.java; echo "(DigestUtils.java line 469:)"; sed -n 469p ../DigestUtils.java
echo "expected: lines 259, 275, 312 assign DigestUtils.getMd5Digest() to a variable; line 469 is getMd5Digest().digest(data) without 'DigestUtils.'"
run F1a "Ran 1 rule on 1 file: 3 findings." "" --config $C/crypto/use-of-md5.yaml $C/crypto/use-of-md5.java
run F1b "Ran 1 rule on 1 file: 0 findings." "" --config $C/crypto/use-of-md5.yaml ../Md5Crypt.java
run F2a "Ran 1 rule on 1 file: 3 findings." "" --config $C/crypto/weak-random.yaml $C/crypto/weak-random.java
run F2b "Ran 1 rule on 1 file: 0 findings." "" --config $C/crypto/weak-random.yaml ../Md5Crypt.java
run F3a "Ran 1 rule on 1 file: 1 finding." "" --config $C/md5-used-as-password.yaml $C/md5-used-as-password.java
run F3b "Ran 1 rule on 1 file: 0 findings." "" --config $C/md5-used-as-password.yaml ../Md5Crypt.java
n=$(grep -c getInstance ../Md5Crypt.java); echo; echo "getInstance count in Md5Crypt.java: $n (expected 0)"
[ "$n" = 0 ] && ok "getInstance" || bad "getInstance"

echo; echo "=== SUMMARY: $PASS matched, $FAIL differed ==="
echo "Now answer the questions in the SOP (where you hesitated, and whether you had help)."
