---
type: Explanation
id: https://w3id.org/lmodel/opa/knowledge/explanations/what-is-left-out
genre: explanation
title: What the schema leaves out
description: The first release covers the formats OPA publishes a JSON Schema for or ships as a data file; the decision log event, the status report, the discovery bundle and the configuration file can follow.
resource: .linkml/docs/about.md
about:
  - https://w3id.org/lmodel/opa/knowledge/datasets/opa-linkml-schema
sources:
  - id: about.md
    resource: .linkml/docs/about.md
    title: What it leaves out
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# What the schema leaves out

OPA documents more formats in prose: the decision log event, the status report, the discovery bundle and the configuration file. Their shapes are defined by Go types under `plugins/` and `config/`, and OPA publishes no schema for them.[^about.md]

[^about.md]: .linkml/docs/about.md, What it leaves out
