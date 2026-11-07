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
  IsDefinedStmt represents a check of whether a local variable is defined.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaIsDefinedStmtBody extends OpaStmtBody {

  private int source;


}