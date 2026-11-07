---
type: Dataset
id: https://w3id.org/lmodel/opa/knowledge/datasets/opa-tree
genre: reference
title: OPA's tree at v1.22.2
description: Every file of OPA's release v1.22.2, listed with its git object hash in `.linkml/tests/upstream_tree.tsv`, which a test holds the checkout to.
resource: .linkml/tests/upstream_tree.tsv
derivedFrom:
  - https://w3id.org/lmodel/opa/knowledge/references/opa
sources:
  - id: test_upstream.py
    resource: .linkml/tests/test_upstream.py
    title: the docstring
  - id: pin_opa_tree.py
    resource: .linkml/scripts/pin_opa_tree.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# OPA's tree at v1.22.2

`tests/upstream_tree.tsv` lists each file of OPA's tree at the merged release with its git object hash, and a test fails when a file differs.[^test_upstream.py] `just pin-opa-tree <commit>` writes the list again after a merge of another release.[^pin_opa_tree.py]

[^test_upstream.py]: .linkml/tests/test_upstream.py, the docstring
[^pin_opa_tree.py]: .linkml/scripts/pin_opa_tree.py, the docstring
