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
  Static represents a static data segment that is indexed into by the policy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaStatic  {

  private List<OpaBuiltinFunc> builtinFuncs;
  private List<OpaStringConst> files;
  private List<OpaStringConst> strings;


}