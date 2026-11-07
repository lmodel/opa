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
  A decision OPA made: the query or path, the input and result, the bundles and the instance behind it, and when and for whom it was made.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaDecisionLogEvent  {

  private String revision;
  private ZonedDateTime timestamp;
  private OpaLabels labels;
  private String decisionId;
  private String batchDecisionId;
  private String traceId;
  private String spanId;
  private List<OpaDecisionBundle> bundles;
  private String path;
  private String query;
  private Object input;
  private Object result;
  private OpaObject intermediateResults;
  private Object mappedResult;
  private OpaObject ndBuiltinCache;
  private List<String> erased;
  private List<String> masked;
  private Object error;
  private String requestedBy;
  private OpaObject metrics;
  private Integer reqId;
  private List<OpaObject> ruleLabels;
  private OpaRequestContext requestContext;
  private OpaObject custom;


}