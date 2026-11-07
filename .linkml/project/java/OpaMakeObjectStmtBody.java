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
  MakeObjectStmt constructs a local variable that refers to an object value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaMakeObjectStmtBody extends OpaStmtBody {

  private int target;


}