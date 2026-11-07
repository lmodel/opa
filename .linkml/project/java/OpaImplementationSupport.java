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
  An implementation that supports a function, and the version that added it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaImplementationSupport  {

  private String implementation;
  private String version;


}