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
  A statement of kind EqualStmt, with its fields in `stmt`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaEqualStmt extends OpaStmt {

  private String type;
  private OpaEqualStmtBody stmt;


}