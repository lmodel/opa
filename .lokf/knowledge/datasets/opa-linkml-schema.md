---
type: Dataset
id: https://w3id.org/lmodel/opa/knowledge/datasets/opa-linkml-schema
genre: reference
title: The OPA LinkML schema
description: "The LinkML model of OPA v1.22.2's JSON formats in `.linkml/src/opa/schema/`: one module per format, `Opa` classes that keep OPA's keys, and the umbrella `opa.yaml`."
resource: .linkml/src/opa/schema/opa.yaml
derivedFrom:
  - https://w3id.org/lmodel/opa/knowledge/datasets/opa-tree
sources:
  - id: about.md
    resource: .linkml/docs/about.md
    title: Where each module comes from
  - id: linkml-readme.md
    resource: .linkml/README.md
    title: Repository Structure
  - id: opa.yaml
    resource: .linkml/src/opa/schema/opa.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:58Z"
status: draft
---

# The OPA LinkML schema

The umbrella `opa.yaml` imports seven modules: the IR plan, the bundle manifest, the authorization input, the capabilities document, the built-in function metadata, the version index and the types they share.[^opa.yaml] A converter writes every module from OPA's files.[^about.md] `linkml_schema` at the repository's root is a link to this folder.[^linkml-readme.md]

[^about.md]: .linkml/docs/about.md, Where each module comes from
[^linkml-readme.md]: .linkml/README.md, Repository Structure
[^opa.yaml]: .linkml/src/opa/schema/opa.yaml
