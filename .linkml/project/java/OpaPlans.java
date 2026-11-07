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
  Plans represents a collection of named query plans to expose in the policy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaPlans  {

  private List<OpaPlan> plans;


}