import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V02_unprefixed_call {
  byte[] unprefixed(byte[] data) {
    return getMd5Digest().digest(data); // TARGET
  }
}
