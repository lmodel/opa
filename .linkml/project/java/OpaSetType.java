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
  A set, whose members have the type in `of`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaSetType extends OpaType {

  private String type;
  private OpaType of;


}