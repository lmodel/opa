---
type: Explanation
id: https://w3id.org/lmodel/opa/knowledge/explanations/fork-layout
genre: explanation
title: The fork layout
description: OPA's tree sits unchanged at the repository's root, and everything this project adds is listed in `.linkml/NOTICE`.
resource: .linkml/NOTICE
about:
  - https://w3id.org/lmodel/opa/knowledge/references/opa
sources:
  - id: notice
    resource: .linkml/NOTICE
  - id: contributing.md
    resource: .linkml/CONTRIBUTING.md
    title: What this project is
generated:
  by: process:ktl-librarian
  at: "2026-11-07T10:43:46Z"
status: draft
---

# The fork layout

The schema project is under `.linkml/`, the bundle under `.lokf/` and the site under `website/`, beside the doorways `knowledge_bundle` and `linkml_schema`, `llms.txt`, `.releaserc.json`, `.github/SECURITY.md`, `.github/PULL_REQUEST_TEMPLATE/`, `.github/scripts/`, `.github/release/` and the project's own workflows.[^notice] Everything else is OPA's.[^contributing.md]

[^notice]: .linkml/NOTICE
[^contributing.md]: .linkml/CONTRIBUTING.md, What this project is
