import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V00_chained_baseline {
  byte[] chained(byte[] data) {
    return DigestUtils.getMd5Digest().digest(data); // TARGET
  }
}
