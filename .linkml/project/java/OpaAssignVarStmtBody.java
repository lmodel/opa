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
  AssignVarStmt represents an assignment of one local variable to another.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaAssignVarStmtBody extends OpaStmtBody {

  private OpaOperand source;
  private int target;


}