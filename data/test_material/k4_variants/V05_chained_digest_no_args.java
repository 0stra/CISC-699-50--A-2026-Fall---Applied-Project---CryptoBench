import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V05_chained_digest_no_args {
  byte[] noargs() {
    return DigestUtils.getMd5Digest().digest(); // TARGET
  }
}
