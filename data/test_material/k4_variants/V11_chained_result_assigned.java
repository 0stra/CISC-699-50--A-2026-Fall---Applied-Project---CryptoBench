import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V11_chained_result_assigned {
  byte[] assigned(byte[] data) {
    byte[] h = DigestUtils.getMd5Digest().digest(data); // TARGET
    return h;
  }
}
