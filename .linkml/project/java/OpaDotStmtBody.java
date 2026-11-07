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
  DotStmt represents a lookup operation on a value (e.g., array, object, etc.) The source of a DotStmt may be a scalar value in which case the statement will be undefined.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaDotStmtBody extends OpaStmtBody {

  private OpaOperand source;
  private int target;
  private OpaOperand key;


}