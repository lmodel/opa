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
  The status of the decision log uploads.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaDecisionLogStatus  {

  private String code;
  private String message;
  private Integer httpCode;
  private OpaObject metrics;


}