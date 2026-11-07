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
  The OPA Authorization Policy Input document.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaAuthorizationInput  {

  private Object body;
  private String identity;
  private List<OpaObject> clientCertificates;
  private String method;
  private List<String> path;
  private OpaStringListMap params;
  private OpaStringListMap headers;


}