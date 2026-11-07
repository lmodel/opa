---
type: Dataset
id: https://w3id.org/lmodel/opa/knowledge/datasets/adapt-copy
genre: reference
title: The adapt copy
description: "`.lokf/schema/opa.yaml`, the copy `just lokf-adapt` writes from the schema for the bundle to validate against, which a release attaches as `schema-<tag>-opa.yaml`."
resource: .lokf/schema/opa.yaml
derivedFrom:
  - https://w3id.org/lmodel/opa/knowledge/datasets/opa-linkml-schema
sources:
  - id: linkml-readme.md
    resource: .linkml/README.md
    title: Knowledge Trust Ladder (KTL)
  - id: test_schema_rules.py
    resource: .linkml/tests/test_schema_rules.py
    title: the module docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-07T10:31:22Z"
status: draft
---

# The adapt copy

In the copy, `OpaManifest`, `OpaCapabilities`, `OpaBuiltin` and `OpaPolicy` descend from LOKF's `Concept`, and `description` folds into LOKF's.[^linkml-readme.md] Seven of OPA's keys are words LOKF defines with another meaning, and the copy renames each with the prefix, such as `type` to `openpolicyagent_type`.[^linkml-readme.md] A test compares the copy's names and slot IRIs with LOKF's and the neighbours' copies'.[^test_schema_rules.py]

[^linkml-readme.md]: .linkml/README.md, Knowledge Trust Ladder (KTL)
[^test_schema_rules.py]: .linkml/tests/test_schema_rules.py, the module docstring
