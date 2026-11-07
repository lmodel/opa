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
  Plan represents an ordered series of blocks to execute. Plan execution stops when a return statement is reached.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaPlan  {

  private List<OpaBlock> blocks;
  private String name;


}