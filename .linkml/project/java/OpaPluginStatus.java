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
  The state of a plugin.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaPluginStatus  {

  private String name;
  private String state;
  private String message;


}