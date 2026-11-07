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
  AssignVarOnceStmt represents an assignment of one local variable to another. If the target is defined, execution aborts with a conflict error.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaAssignVarOnceStmtBody extends OpaStmtBody {

  private OpaOperand source;
  private int target;


}