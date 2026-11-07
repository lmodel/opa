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
  A function, with its arguments, its result and a variadic argument type.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaFunctionType extends OpaType {

  private String type;
  private List<OpaType> args;
  private OpaType result;
  private OpaType variadic;


}