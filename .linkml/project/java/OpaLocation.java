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
  Location records the filen index, and the row and column inside that file that a statement can be connected to.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaLocation  {

  private int file;
  private int col;
  private int row;
  private int endCol;
  private int endRow;


}