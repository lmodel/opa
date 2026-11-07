---
type: Playbook
id: https://w3id.org/lmodel/opa/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test
description: Edit the converter, regenerate the schema and its artefacts, and run the tests from `.linkml/` before a pull request.
resource: .linkml/CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/opa/knowledge/datasets/opa-linkml-schema
sources:
  - id: contributing.md
    resource: .linkml/CONTRIBUTING.md
    title: Before opening a pull request
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# Regenerate and test

From `.linkml/`, run `just gen-linkml`, `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit the output. Then run `just test`.[^contributing.md]

[^contributing.md]: .linkml/CONTRIBUTING.md, Before opening a pull request
