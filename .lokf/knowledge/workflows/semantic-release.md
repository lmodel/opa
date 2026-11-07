---
type: Service
id: https://w3id.org/lmodel/opa/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: Releases a merge to `main` whose commits carry a releasing type, and dispatches the knowledge release.
resource: .github/workflows/semantic-release.yml
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# Semantic release (semantic-release.yml)

The baseline tag sits on the merge of OPA's release, so OPA's older commits do not count.[^semantic-release.yml]

[^semantic-release.yml]: .github/workflows/semantic-release.yml
