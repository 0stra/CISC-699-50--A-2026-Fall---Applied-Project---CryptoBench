import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V08_parenthesised_call {
  byte[] paren(byte[] data) {
    return (DigestUtils.getMd5Digest()).digest(data); // TARGET
  }
}
