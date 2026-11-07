---
type: Service
id: https://w3id.org/lmodel/opa/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: Checks every week for a newer KTL release and opens a pull request that syncs the sidecar's copies.
resource: .github/workflows/knowledge-sync.yaml
sources:
  - id: knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

The workflow is a copy of the KTL sidecar's template.[^knowledge-sync.yaml]

[^knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml
