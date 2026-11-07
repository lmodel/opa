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
  A known key of an object type and the type of its value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaStaticProperty  {

  private Object key;
  private OpaType value;


}