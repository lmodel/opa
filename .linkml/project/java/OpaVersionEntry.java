package example;

/* metamodel_version: 1.12.0 */
/* version: 1.22.2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A built-in function, feature or keyword, and the OPA version that introduced it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaVersionEntry  {

  private String name;
  private int major;
  private int minor;
  private int patch;
  private String preRelease;
  private String metadata;


}