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
  An object, with typed known keys in `static` and a key and value type for the rest in `dynamic`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaObjectType extends OpaType {

  private String type;
  private List<OpaStaticProperty> static_;
  private OpaDynamicProperty dynamic;


}