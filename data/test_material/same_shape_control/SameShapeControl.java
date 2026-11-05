import java.security.MessageDigest;
import org.apache.commons.codec.digest.DigestUtils;

public class SameShapeControl {
  public byte[] chainedForm(byte[] data) {
    return DigestUtils.getMd5Digest().digest(data);
  }

  public byte[] variableForm(byte[] data) {
    final MessageDigest ctx = DigestUtils.getMd5Digest();
    ctx.update(data);
    return ctx.digest();
  }
}
