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
  A Wasm ABI version, as a major and a minor number.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaWasmAbiVersion  {

  private int version;
  private int minorVersion;


}