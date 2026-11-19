import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V10_md5Hex_helper {
  String hex(String s) {
    return DigestUtils.md5Hex(s); // TARGET
  }
}
