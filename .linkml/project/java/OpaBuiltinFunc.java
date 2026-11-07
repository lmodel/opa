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
  BuiltinFunc represents a built-in function that may be required by the policy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaBuiltinFunc  {

  private OpaFunctionType decl;
  private String name;


}