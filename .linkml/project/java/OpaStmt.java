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
  Stmt represents an operation (e.g., comparison, loop, dot, etc.) to execute. OPA writes each statement as its kind in `type` and its fields in `stmt`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class OpaStmt  {



}