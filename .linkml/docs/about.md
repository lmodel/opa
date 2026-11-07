# About

This page says where each module of the schema comes from, how the model differs from OPA's own JSON Schemas, and what it leaves out.

## Where each module comes from

`scripts/opa_to_linkml.py` writes every module from OPA's files at the merged release. Edit the converter, then run `just gen-linkml`. A test fails when a module differs from what the converter writes.

| Module | Format | Source |
| --- | --- | --- |
| `ir_plan` | The IR plan `opa build -t plan` writes | `v1/ir/plan.schema.json`, with descriptions from `v1/ir/ir.go` |
| `bundle_manifest` | A bundle's `.manifest` | `v1/bundle/manifest.schema.json` |
| `authorization_input` | The input of the `system.authz` policy | `v1/schemas/authorizationPolicy.json` |
| `capabilities` | The capabilities document | `capabilities.json`, every file in `capabilities/`, and the Go types in `v1/ast/capabilities.go` and `v1/types/types.go` |
| `builtin_metadata` | `builtin_metadata.json` | The file, and `internal/cmd/genbuiltinmetadata/main.go` |
| `version_index` | `v1/ast/version_index.json` | The file, and `internal/cmd/genversionindex/main.go` |
| `common` | The open JSON object and the Rego type declarations | `v1/types/types.go` |
| `opa` | The umbrella that imports the rest | |

The plan's `{type, stmt}` statements and `{type, value}` operands become one class per kind under an abstract class. A range over the abstract class admits each kind, as OPA's `oneOf` does. The capabilities' type declarations follow the same pattern: one class per Rego type, picked by `type`.

The enumerations of future keywords and features take every value that the capabilities files included with OPA use, so each of those files validates.

## How the model differs from OPA's JSON Schemas

`tests/test_parity.py` compares the two in three tiers: every definition has a class, a corpus of over 1,300 documents gets the same verdicts, and `parity/structural.yaml` gives the reason for each case that differs. Three reasons cover them all:

- OPA requires some keys whose value may be null. LinkML cannot state that, so those keys are optional here.
- LinkML's JSON Schema lets an optional key hold null.
- A built-in function's `decl` is the function type OPA writes, where OPA's schema leaves it opaque.

## What it leaves out

The first release covers the formats OPA publishes a JSON Schema for or keeps as a data file: the capabilities files, `builtin_metadata.json` and `version_index.json`. OPA documents more formats in prose: the decision log event, the status report, the discovery bundle and the configuration file. Their shapes are defined by Go types in `v1/plugins/` and `v1/config/`, and OPA publishes no schema for them. Each can follow as a module that the converter reads from those types.
