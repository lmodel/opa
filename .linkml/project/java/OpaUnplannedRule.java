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
  UnplannedRule represents a rule that was parsed but not included in the plan because it is not reachable from the entrypoint. This is used for coverage reporting, to distinguish rules that were never planned from rules that were planned but never executed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaUnplannedRule  {

  private OpaLocation location;
  private String path;


}