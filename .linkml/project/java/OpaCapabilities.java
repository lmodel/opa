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
  What an OPA version supports, which a policy can be checked against.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaCapabilities  {

  private List<OpaBuiltin> builtins;
  private List<String> futureKeywords;
  private List<OpaWasmAbiVersion> wasmAbiVersions;
  private List<String> features;
  private List<String> allowNet;


}