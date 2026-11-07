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
  NotEqualStmt represents a != check of two local variables.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaNotEqualStmtBody extends OpaStmtBody {

  private OpaOperand operandA;
  private OpaOperand operandB;


}