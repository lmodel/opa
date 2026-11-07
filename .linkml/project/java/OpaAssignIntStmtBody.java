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
  AssignIntStmt represents an assignment of an integer value to a local variable.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaAssignIntStmtBody extends OpaStmtBody {

  private int target;
  private int value;


}