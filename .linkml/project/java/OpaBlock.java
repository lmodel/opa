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
  Block represents an ordered sequence of statements to execute. Blocks are executed until a return statement is encountered, a statement is undefined, or there are no more statements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaBlock  {

  private List<OpaStmt> stmts;


}