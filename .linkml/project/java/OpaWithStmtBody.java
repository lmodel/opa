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
  WithStmt replaces the Local or a portion of the document referred to by the Local with the Value and executes the contained block. If the Path is non-empty, the Value is upserted into the Local.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaWithStmtBody extends OpaStmtBody {

  private OpaBlock block;
  private int local;
  private List<Integer> path;
  private OpaOperand value;


}