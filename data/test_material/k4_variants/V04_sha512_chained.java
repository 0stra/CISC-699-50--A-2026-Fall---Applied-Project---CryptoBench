import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V04_sha512_chained {
  byte[] sha(byte[] data) {
    return DigestUtils.getSha512Digest().digest(data); // not MD5
  }
}
