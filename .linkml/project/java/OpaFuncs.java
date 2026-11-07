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
  Funcs represents a collection of planned functions to include in the policy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaFuncs  {

  private List<OpaFunc> funcs;


}