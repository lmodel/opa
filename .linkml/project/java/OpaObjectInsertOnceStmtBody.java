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
  ObjectInsertOnceStmt represents a dynamic insert operation of a key/value pair into an object. If the key already exists and the value differs, execution aborts with a conflict error.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaObjectInsertOnceStmtBody extends OpaStmtBody {

  private OpaOperand key;
  private int object;
  private OpaOperand value;


}