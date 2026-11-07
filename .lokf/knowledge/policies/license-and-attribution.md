---
type: Policy
id: https://w3id.org/lmodel/opa/knowledge/policies/license-and-attribution
genre: reference
title: Licence and attribution
description: The schema project is under the Apache License 2.0 and the bundle under CC BY 4.0; OPA's tree is the OPA Authors', and NOTICE says what comes from where.
resource: .linkml/NOTICE
sources:
  - id: notice
    resource: .linkml/NOTICE
  - id: linkml-readme.md
    resource: .linkml/README.md
    title: License
generated:
  by: process:ktl-librarian
  at: "2026-11-07T10:42:51Z"
status: draft
---

# Licence and attribution

The schema project is under the Apache License 2.0, and the bundle under CC BY 4.0.[^linkml-readme.md] The descriptions of the plan's classes open with OPA's Go comments. The description of the authorization input's class and that of the plan's legacy `Index` key come from OPA's JSON Schemas. These are OPA's words, under the same licence.[^notice]

[^notice]: .linkml/NOTICE
[^linkml-readme.md]: .linkml/README.md, License
