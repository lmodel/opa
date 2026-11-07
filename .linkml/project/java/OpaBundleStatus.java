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
  The status of a bundle: its active revision, when OPA last asked for, downloaded and activated it, and the errors of the last attempt.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaBundleStatus  {

  private String type;
  private String name;
  private String activeRevision;
  private ZonedDateTime lastSuccessfulActivation;
  private Integer size;
  private ZonedDateTime lastSuccessfulDownload;
  private ZonedDateTime lastSuccessfulRequest;
  private ZonedDateTime lastRequest;
  private String code;
  private String message;
  private List<OpaObject> errors;
  private OpaObject metrics;
  private Integer httpCode;


}