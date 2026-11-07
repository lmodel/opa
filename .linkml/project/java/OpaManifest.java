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
  A bundle manifest. OPA's schema leaves the manifest open to other keys.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaManifest  {

  private String revision;
  private List<OpaFileRegoVersion> fileRegoVersions;
  private OpaObject metadata;
  private Integer regoVersion;
  private List<String> roots;
  private List<OpaWasmResolver> wasm;


}