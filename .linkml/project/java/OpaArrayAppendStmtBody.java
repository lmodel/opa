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
  ArrayAppendStmt represents a dynamic append operation of a value onto an array.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaArrayAppendStmtBody extends OpaStmtBody {

  private int array;
  private OpaOperand value;


}