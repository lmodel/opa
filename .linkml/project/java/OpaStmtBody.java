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
  The fields of a statement. Every kind carries the location of its source text.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class OpaStmtBody  {

  private int file;
  private int col;
  private int row;
  private int endCol;
  private int endRow;


}