---
type: Playbook
id: https://w3id.org/lmodel/opa/knowledge/playbooks/release
genre: how-to
title: Release
description: A merge to `main` whose commits carry a releasing type is released by semantic-release, which promotes the changelog's Unreleased section.
resource: .linkml/CONTRIBUTING.md
sources:
  - id: contributing.md
    resource: .linkml/CONTRIBUTING.md
    title: Releasing (maintainers)
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# Release

Only `feat:`, `fix:`, `security:` and a breaking `!` start a release, and OPA's commits in a merge count too.[^contributing.md] The `v0.0.0` baseline tag sits on the merge of OPA's release, so OPA's older commits do not count.[^contributing.md]

[^contributing.md]: .linkml/CONTRIBUTING.md, Releasing (maintainers)
