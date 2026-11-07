---
type: Dataset
id: https://w3id.org/lmodel/opa/knowledge/datasets/example-data
genre: reference
title: Example data
description: "The examples under `.linkml/tests/data/problem/`: a valid document per format, and documents that each break one rule."
resource: .linkml/tests/data/problem
about:
  - https://w3id.org/lmodel/opa/knowledge/datasets/opa-linkml-schema
sources:
  - id: data-readme.md
    resource: .linkml/tests/data/README.md
  - id: test_data.py
    resource: .linkml/tests/test_data.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# Example data

Each file is named after the class it must validate against. `problem/valid/` holds documents that must pass, and `problem/invalid/` documents that must fail.[^data-readme.md] The test also checks the examples of the plan, the manifest and the authorization input against OPA's own JSON Schema for each.[^test_data.py]

[^data-readme.md]: .linkml/tests/data/README.md
[^test_data.py]: .linkml/tests/test_data.py, the docstring
