import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V07_chained_across_lines {
  byte[] lines(byte[] data) {
    return DigestUtils
        .getMd5Digest()
        .digest(data); // TARGET
  }
}
