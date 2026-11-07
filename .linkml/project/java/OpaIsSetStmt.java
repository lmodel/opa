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
  A statement of kind IsSetStmt, with its fields in `stmt`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaIsSetStmt extends OpaStmt {

  private String type;
  private OpaIsSetStmtBody stmt;


}