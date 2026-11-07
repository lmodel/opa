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
  ScanStmt represents a linear scan over a composite value. The source may be a scalar in which case the block will never execute.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaScanStmtBody extends OpaStmtBody {

  private int source;
  private OpaBlock block;
  private int key;
  private int value;


}