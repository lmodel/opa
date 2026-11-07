# opa

This project is a LinkML model of the JSON formats Open Policy Agent (OPA) defines, at release v1.22.2. Each module renders one format and keeps OPA's keys, so a document OPA writes validates here unchanged.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): where each module comes from, how the model differs from OPA's JSON Schemas and what it leaves out
- [`opa.yaml`](schema/opa.yaml): the schema, its modules merged

## Validating a document

`linkml-validate` reads keys by slot name, and some of OPA's keys differ from the slot's name, such as `_categories`, `Major`, `return` and `Index`. Validate against the JSON Schema the schema generates instead, in which each such key is the slot's alias:

```bash
uv run gen-json-schema --include-range-class-descendants --top-class OpaManifest \
  src/opa/schema/opa.yaml > manifest.schema.json
uv run python -c '
import json, sys, jsonschema
schema = json.load(open("manifest.schema.json"))
for error in jsonschema.validators.validator_for(schema)(schema).iter_errors(json.load(open(sys.argv[1]))):
    print(error.json_path, error.message)
' .manifest
```

`--include-range-class-descendants` matters for the plan: a statement or an operand is one of several classes, picked by its `type`.
