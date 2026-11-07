---
type: Explanation
id: https://w3id.org/lmodel/opa/knowledge/explanations/what-is-left-out
genre: explanation
title: What the schema leaves out
description: The configuration file and the discovery bundle are left out, since OPA's configuration type keeps most sections as raw JSON that each plugin parses with its own types.
resource: .linkml/docs/about.md
about:
  - https://w3id.org/lmodel/opa/knowledge/datasets/opa-linkml-schema
sources:
  - id: about.md
    resource: .linkml/docs/about.md
    title: What it leaves out
generated:
  by: process:ktl-librarian
  at: "2026-11-07T10:31:22Z"
status: draft
---

# What the schema leaves out

The configuration file and the discovery bundle are left out. OPA's configuration type keeps most sections as raw JSON, which each plugin and service parses with its own types and defaults. A discovery bundle is an ordinary bundle whose data holds a configuration.[^about.md]

[^about.md]: .linkml/docs/about.md, What it leaves out
