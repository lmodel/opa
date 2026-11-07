---
type: Playbook
id: https://w3id.org/lmodel/opa/knowledge/playbooks/take-a-new-opa-release
genre: how-to
title: Take a new OPA release
description: Merge the release's tag with a merge commit, pin its tree, move the release in the converter, the watch and the capture script, regenerate, and capture OPA's documents again.
resource: .linkml/CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/opa/knowledge/datasets/opa-tree
sources:
  - id: contributing.md
    resource: .linkml/CONTRIBUTING.md
    title: Taking a new release of OPA
generated:
  by: process:ktl-librarian
  at: "2026-11-07T10:31:22Z"
status: draft
---

# Take a new OPA release

The weekly watch opens an issue when OPA publishes a release. Merge its tag, run `just pin-opa-tree <commit>`, update `TAG`, `COMMIT` and `RELEASE_DATE` in the converter, `EDITION` in the watch and `IMAGE` in the capture script, then regenerate and run `just capture-opa-documents`. Merge with a merge commit: a squash loses OPA's history.[^contributing.md]

[^contributing.md]: .linkml/CONTRIBUTING.md, Taking a new release of OPA
