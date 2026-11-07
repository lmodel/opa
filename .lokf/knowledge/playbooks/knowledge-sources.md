---
type: Playbook
id: https://w3id.org/lmodel/opa/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "Where this repository's knowledge lives: the schema project, its docs and tests, OPA's tree, the workflows and the governance files."
resource: .
references:
  - https://w3id.org/lmodel/opa/knowledge/datasets/opa-linkml-schema
  - https://w3id.org/lmodel/opa/knowledge/references/opa
  - https://w3id.org/lmodel/opa/knowledge/explanations/fork-layout
sources:
  - id: linkml-readme.md
    resource: .linkml/README.md
    title: Repository Structure
  - id: notice
    resource: .linkml/NOTICE
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# Knowledge sources map

| Source | What it holds |
| --- | --- |
| `.linkml/` | The schema project: the converter, the schema, its tests and docs |
| `.github/workflows/` | This project's workflows beside OPA's |
| `website/` | The knowledge website |
| The rest of the tree | OPA's release v1.22.2, unchanged |

The schema project's README gives its structure.[^linkml-readme.md] NOTICE lists what this project adds beside OPA's tree.[^notice]

[^linkml-readme.md]: .linkml/README.md, Repository Structure
[^notice]: .linkml/NOTICE
