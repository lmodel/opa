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
  MakeArrayStmt constructs a local variable that refers to an array value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaMakeArrayStmtBody extends OpaStmtBody {

  private int capacity;
  private int target;


}