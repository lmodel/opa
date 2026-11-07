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
  IsSetStmt represents a dynamic type check on a local variable.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaIsSetStmtBody extends OpaStmtBody {

  private OpaOperand source;


}