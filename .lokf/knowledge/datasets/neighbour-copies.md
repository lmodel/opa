---
type: Dataset
id: https://w3id.org/lmodel/opa/knowledge/datasets/neighbour-copies
genre: reference
title: The neighbours' adapt copies
description: The adapt copies other lmodel repositories release, under `.linkml/tests/neighbours/`, each pinned by the checksum of its release asset.
resource: .linkml/tests/neighbours
about:
  - https://w3id.org/lmodel/opa/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: .linkml/tests/test_schema_rules.py
    title: NEIGHBOURS
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# The neighbours' adapt copies

Each file is the schema asset of an lmodel release, checked against the release's checksum and attestation. The test checks each copy against its checksum, and lists the keys this schema's copy shares with each.[^test_schema_rules.py]

[^test_schema_rules.py]: .linkml/tests/test_schema_rules.py, NEIGHBOURS
