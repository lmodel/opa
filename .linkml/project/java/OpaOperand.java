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
  Operand represents a value that a statement operates on. OPA writes it as its kind in `type` and the value in `value`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class OpaOperand  {



}