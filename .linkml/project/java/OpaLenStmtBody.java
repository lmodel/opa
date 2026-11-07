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
  LenStmt represents a length() operation on a local variable. The result is stored in the target local variable.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaLenStmtBody extends OpaStmtBody {

  private OpaOperand source;
  private int target;


}