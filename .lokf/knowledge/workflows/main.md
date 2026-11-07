---
type: Service
id: https://w3id.org/lmodel/opa/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: Builds the project, lints the schema, runs the tests on five Python versions and checks the adapt copy.
resource: .github/workflows/main.yaml
sources:
  - id: main.yaml
    resource: .github/workflows/main.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# Build and test (main.yaml)

The workflow runs in `.linkml/`. It lints, and checks the adapt copy, on Python 3.13 only.[^main.yaml]

[^main.yaml]: .github/workflows/main.yaml
