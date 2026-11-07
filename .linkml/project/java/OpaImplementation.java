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
  An implementation of Rego besides OPA.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaImplementation  {

  private String version;
  private String id;
  private String label;
  private String repo;


}