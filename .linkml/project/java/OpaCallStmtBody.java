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
  CallStmt represents a named function call. The result should be stored in the result local.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaCallStmtBody extends OpaStmtBody {

  private List<OpaOperand> args;
  private String func;
  private int result;


}