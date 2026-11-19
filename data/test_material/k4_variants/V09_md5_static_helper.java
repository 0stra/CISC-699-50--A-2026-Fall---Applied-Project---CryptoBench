import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V09_md5_static_helper {
  byte[] helper(byte[] data) {
    return DigestUtils.md5(data); // TARGET
  }
}
