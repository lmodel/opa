---
type: Service
id: https://w3id.org/lmodel/opa/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: Checks every week whether OPA has released past the merged tag, and opens an issue when it has.
resource: .github/workflows/upstream-watch.yaml
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
  - id: check_upstream_release.py
    resource: .linkml/scripts/check_upstream_release.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-07T10:31:22Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

The workflow runs every Monday.[^upstream-watch.yaml] A later OPA release, a moved tag or a changed licence fails it, and a change on its default branch to a file that defines a format the schema renders key for key, a JSON Schema or a Go file, is reported for information.[^check_upstream_release.py]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml
[^check_upstream_release.py]: .linkml/scripts/check_upstream_release.py, the docstring
