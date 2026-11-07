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
  A report on an OPA instance: the state of its bundles, its decision log uploads and its plugins, and its metrics.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaStatusReport  {

  private OpaLabels labels;
  private OpaBundleStatus bundle;
  private List<OpaBundleStatus> bundles;
  private OpaBundleStatus discovery;
  private OpaDecisionLogStatus decisionLogs;
  private OpaObject metrics;
  private List<OpaPluginStatus> plugins;


}