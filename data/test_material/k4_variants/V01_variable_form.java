import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class V01_variable_form {
  byte[] variable(byte[] data) {
    MessageDigest ctx = DigestUtils.getMd5Digest(); // TARGET (creation)
    ctx.update(data);
    return ctx.digest();
  }
}
