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
  BlockStmt represents a nested block. Nested blocks and break statements can be used to short-circuit execution.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaBlockStmtBody extends OpaStmtBody {

  private List<OpaBlock> blocks;


}