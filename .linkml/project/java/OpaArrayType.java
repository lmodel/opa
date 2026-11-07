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
  An array, with a type per position in `static` and one for the rest in `dynamic`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaArrayType extends OpaType {

  private String type;
  private List<OpaType> static_;
  private OpaType dynamic;


}