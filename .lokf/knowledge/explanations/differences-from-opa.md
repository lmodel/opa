---
type: Explanation
id: https://w3id.org/lmodel/opa/knowledge/explanations/differences-from-opa
genre: explanation
title: Where the model differs from OPA's JSON Schemas
description: Three reasons cover every case where the schema and OPA's JSON Schemas decide a document differently.
resource: .linkml/docs/about.md
about:
  - https://w3id.org/lmodel/opa/knowledge/datasets/parity-allowances
sources:
  - id: about.md
    resource: .linkml/docs/about.md
    title: How the model differs from OPA's JSON Schemas
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# Where the model differs from OPA's JSON Schemas

OPA requires some keys whose value may be null, which LinkML cannot state, so those keys are optional here. LinkML's JSON Schema lets an optional key hold null. A built-in function's `decl` is the function type OPA writes, where OPA's schema leaves it opaque.[^about.md]

[^about.md]: .linkml/docs/about.md, How the model differs from OPA's JSON Schemas
