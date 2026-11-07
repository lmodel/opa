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
  ObjectMergeStmt performs a recursive merge of two object values. If either of the locals refer to non-object values this operation will abort with a conflict error.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaObjectMergeStmtBody extends OpaStmtBody {

  private int target;
  private int operandA;
  private int operandB;


}