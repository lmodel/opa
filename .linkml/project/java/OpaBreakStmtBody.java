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
  BreakStmt represents a jump out of the current block. The index specifies how many blocks to jump starting from zero (the current block).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaBreakStmtBody extends OpaStmtBody {

  private int index;


}