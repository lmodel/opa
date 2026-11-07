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
  A Wasm module in a bundle, and the entrypoint it resolves.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaWasmResolver  {

  private List<OpaObject> annotations;
  private String entrypoint;
  private String module;


}