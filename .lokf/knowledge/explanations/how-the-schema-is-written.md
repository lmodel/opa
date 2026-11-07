---
type: Explanation
id: https://w3id.org/lmodel/opa/knowledge/explanations/how-the-schema-is-written
genre: explanation
title: How the schema is written
description: "`.linkml/scripts/opa_to_linkml.py` writes each module from OPA's JSON Schemas, data files and Go types at the merged release, and a test fails when a module differs."
resource: .linkml/scripts/opa_to_linkml.py
about:
  - https://w3id.org/lmodel/opa/knowledge/datasets/opa-linkml-schema
sources:
  - id: about.md
    resource: .linkml/docs/about.md
    title: Where each module comes from
  - id: converter
    resource: .linkml/scripts/opa_to_linkml.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# How the schema is written

The plan, the bundle manifest and the authorization input render OPA's JSON Schemas key for key. The capabilities document, the built-in function metadata and the version index render the Go types that write them.[^converter] A statement or an operand of the plan is one class per kind under an abstract class, picked by its `type`.[^about.md] Edit the converter and run `just gen-linkml`, never the modules.[^about.md]

[^about.md]: .linkml/docs/about.md, Where each module comes from
[^converter]: .linkml/scripts/opa_to_linkml.py, the docstring
