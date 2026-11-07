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
  MakeNumberRefStmt constructs a local variable that refers to a number stored as a string.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaMakeNumberRefStmtBody extends OpaStmtBody {

  private int target;
  private int index;
  private Integer indexLegacy;


}