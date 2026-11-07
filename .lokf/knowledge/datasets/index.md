# Datasets

* [OPA's tree at v1.22.2](opa-tree.md) - Every file of OPA's release v1.22.2, listed with its git object hash in `.linkml/tests/upstream_tree.tsv`, which a test holds the checkout to.
* [The OPA LinkML schema](opa-linkml-schema.md) - The LinkML model of OPA v1.22.2's JSON formats in `.linkml/src/opa/schema/`: one module per format, `Opa` classes that keep OPA's keys, and the umbrella `opa.yaml`.
* [The adapt copy](adapt-copy.md) - `.lokf/schema/opa.yaml`, the copy `just lokf-adapt` writes from the schema for the bundle to validate against, which a release attaches as `schema-<tag>-opa.yaml`.
* [Parity allowances](parity-allowances.md) - `.linkml/parity/structural.yaml`: each case where the schema's verdict differs from OPA's JSON Schema's, with its reason.
* [Example data](example-data.md) - The examples under `.linkml/tests/data/problem/`: a valid document per format, and documents that each break one rule.
* [The neighbours' adapt copies](neighbour-copies.md) - The adapt copies other lmodel repositories release, under `.linkml/tests/neighbours/`, each pinned by the checksum of its release asset.
