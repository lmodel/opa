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
  A built-in function and its type declaration.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OpaBuiltin  {

  private String name;
  private String description;
  private List<String> categories;
  private OpaFunctionType decl;
  private String infix;
  private Boolean relation;
  private Boolean deprecated;
  private Boolean nondeterministic;


}