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
  The catalogue: two keys that start with an underscore, and one key per built-in function, whose value describes it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaBuiltinMetadataCatalog  {

  private List<OpaBuiltinCategory> categories;
  private List<OpaImplementation> implementations;


}