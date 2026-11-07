---
type: Dataset
id: https://w3id.org/lmodel/opa/knowledge/datasets/parity-allowances
genre: reference
title: Parity allowances
description: "`.linkml/parity/structural.yaml`: each case where the schema's verdict differs from OPA's JSON Schema's, with its reason."
resource: .linkml/parity/structural.yaml
about:
  - https://w3id.org/lmodel/opa/knowledge/datasets/opa-linkml-schema
sources:
  - id: structural.yaml
    resource: .linkml/parity/structural.yaml
    title: the header
  - id: test_parity.py
    resource: .linkml/tests/test_parity.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-07T11:24:45Z"
status: draft
---

# Parity allowances

The file lists each case of the parity corpus on which the schema and OPA's JSON Schema give different verdicts, and says which verdict the schema gives.[^structural.yaml] The test fails when a case the file does not list differs, or when a listed case no longer differs.[^test_parity.py]

[^structural.yaml]: .linkml/parity/structural.yaml, the header
[^test_parity.py]: .linkml/tests/test_parity.py, the docstring
