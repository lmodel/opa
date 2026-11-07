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
  ResultSetAddStmt adds a value into the result set returned by the query plan.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaResultSetAddStmtBody extends OpaStmtBody {

  private int value;


}