# About

This page says where each module of the schema comes from, how the model differs from OPA's own JSON Schemas, and what it leaves out.

## Where each module comes from

`scripts/opa_to_linkml.py` writes every module from OPA's files at the merged release. Edit the converter, then run `just gen-linkml`. A test fails when a module differs from what the converter writes.

| Module | Format | Source |
| --- | --- | --- |
| `ir_plan` | The IR plan `opa build -t plan` writes | `v1/ir/plan.schema.json`, with descriptions from `v1/ir/ir.go` |
| `bundle_manifest` | A bundle's `.manifest` | `v1/bundle/manifest.schema.json` |
| `authorization_input` | The input of the `system.authz` policy | `v1/schemas/authorizationPolicy.json`, and what `v1/server/authorizer/authorizer.go` writes |
| `capabilities` | The capabilities document | `capabilities.json`, every file in `capabilities/`, and the Go types in `v1/ast/capabilities.go` and `v1/types/types.go` |
| `builtin_metadata` | `builtin_metadata.json` | The file, and `internal/cmd/genbuiltinmetadata/main.go` |
| `version_index` | `v1/ast/version_index.json` | The file, and `internal/cmd/genversionindex/main.go` |
| `decision_log` | The decision log event | The Go structs in `v1/plugins/logs/plugin.go` |
| `status_report` | The status report | The Go structs in `v1/plugins/status/plugin.go`, `v1/plugins/bundle/status.go`, `v1/plugins/logs/status/status.go` and `v1/plugins/plugins.go`, and the bundle types in `v1/bundle/bundle.go` |
| `common` | Open objects and values, labels, HTTP headers, and the Rego type declarations | `v1/types/types.go` |
| `opa` | The umbrella that imports the rest | |

The plan's `{type, stmt}` statements and `{type, value}` operands become one class per kind under an abstract class. A range over the abstract class admits each kind, as OPA's `oneOf` does. The capabilities' type declarations follow the same pattern: one class per Rego type, picked by `type`.

The enumerations of future keywords and features take every value that the capabilities files included with OPA use, so each of those files validates.

The decision log and status modules render Go structs key for key, from the structs' JSON tags. A key is required when its tag has no `omitempty` and its Go type cannot hold null. The converter stops when a struct gains or loses a key, and `tests/test_parity.py` compares each class with its struct.

`tests/data/captured/` holds documents OPA's own binary wrote: a plan, three manifests, five decision log events, a status report and five authorization inputs. `just capture-opa-documents` writes them again from OPA's release image, and every one must validate.

## How the model differs from OPA's JSON Schemas

`tests/test_parity.py` compares the two in three tiers: every definition has a class, a corpus of over 1,300 documents gets the same verdicts, and `parity/structural.yaml` gives the reason for each case that differs. Four reasons cover them all:

- OPA requires some keys whose value may be null. LinkML cannot state that, so those keys are optional here.
- LinkML's JSON Schema lets an optional key hold null.
- A built-in function's `decl` is the function type OPA writes, where OPA's schema leaves it opaque.
- OPA type-checks the authorization policy against its schema, which requires `identity`, `client_certificates` and `body` and makes the body an object. OPA's server leaves those keys out when a request has none, and parses a body as any JSON value, so here they are optional and the body takes any value.

## What it leaves out

The configuration file and the discovery bundle are left out. OPA's configuration type keeps most sections as raw JSON, which each plugin and service parses with its own types and defaults. A discovery bundle is an ordinary bundle whose data holds a configuration. Either can follow as a module that renders those types.
