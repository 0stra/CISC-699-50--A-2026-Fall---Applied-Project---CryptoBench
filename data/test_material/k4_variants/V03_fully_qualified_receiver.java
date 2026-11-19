import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V03_fully_qualified_receiver {
  byte[] qualified(byte[] data) {
    return org.apache.commons.codec.digest.DigestUtils.getMd5Digest().digest(data); // TARGET
  }
}
