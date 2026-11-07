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
  CallDynamicStmt represents an indirect (data) function call. The result should be stored in the result local.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaCallDynamicStmtBody extends OpaStmtBody {

  private List<Integer> args;
  private List<OpaOperand> path;
  private int result;


}