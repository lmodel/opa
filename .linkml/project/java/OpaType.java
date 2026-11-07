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
  A Rego type, as OPA's types package writes it in JSON. A named type is an argument or result of a built-in function, with a name and a description.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class OpaType  {

  private String name;
  private String description;


}