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
  Func represents a named plan (function) that can be invoked. Functions accept one or more parameters and return a value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaFunc  {

  private List<OpaBlock> blocks;
  private String name;
  private List<Integer> params;
  private List<String> path;
  private int returnLocal;


}