import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V06_chained_update_not_digest {
  void upd(byte[] data) {
    DigestUtils.getMd5Digest().update(data); // TARGET (creation)
  }
}
