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
  The key type and value type that an object type gives its other keys.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaDynamicProperty  {

  private OpaType key;
  private OpaType value;


}