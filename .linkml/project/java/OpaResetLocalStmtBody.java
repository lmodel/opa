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
  ResetLocalStmt resets a local variable to 0.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaResetLocalStmtBody extends OpaStmtBody {

  private int target;


}