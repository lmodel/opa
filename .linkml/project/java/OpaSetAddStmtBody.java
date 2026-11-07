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
  SetAddStmt represents a dynamic add operation of an element into a set.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaSetAddStmtBody extends OpaStmtBody {

  private int set;
  private OpaOperand value;


}