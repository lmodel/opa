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
  What the catalogue says about one built-in function.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaBuiltinMetadata  {

  private String description;
  private String introduced;
  private List<String> available;
  private boolean wasm;
  private List<OpaBuiltinArgument> args;
  private OpaBuiltinResult result;
  private List<OpaImplementationSupport> implementations;
  private String infix;
  private Boolean relation;
  private Boolean deprecated;


}