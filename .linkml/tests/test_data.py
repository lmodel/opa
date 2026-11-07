"""Checks each example against the schema, and against OPA's JSON Schema where OPA has one.

An example is a document OPA writes, with OPA's keys, such as `_categories`, `Major` or
`return`. linkml-validate and the example runner read keys by slot name, so they cannot
read one; the examples sit under tests/data/problem/, where the runner does not look,
and this test validates them against the JSON Schema LinkML generates, in which each
key is the slot's alias. `tests/data/problem/valid/<Class>-<anything>.yaml` must pass,
and `tests/data/problem/invalid/<Class>-<anything>.yaml` must fail. The plan, the
manifest and the authorization input must get the same verdict from OPA's schema.
"""

from pathlib import Path

import pytest
import yaml

import opa_parity as parity

DATA = Path(__file__).parent / "data" / "problem"
VALID = sorted((DATA / "valid").glob("*.yaml"))
INVALID = sorted((DATA / "invalid").glob("*.yaml"))
OPA = {
    "OpaPolicy": "v1/ir/plan.schema.json#Policy",
    "OpaManifest": "v1/bundle/manifest.schema.json#Manifest",
    "OpaAuthorizationInput": parity.AUTHZ,
}


def _case(path: Path):
    return path.stem.split("-")[0], yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_valid_example(path):
    cls, data = _case(path)
    assert parity.verdict("generated", cls, data), parity.errors(
        "generated", cls, data
    )[:3]
    if cls in OPA:
        assert parity.verdict("published", OPA[cls], data)


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.stem)
def test_counter_example(path):
    cls, data = _case(path)
    assert not parity.verdict("generated", cls, data)
    if cls in OPA:
        assert not parity.verdict("published", OPA[cls], data)


def test_every_document_class_has_an_example():
    roots = {name for name, cls in parity.classes().items() if cls.get("tree_root")}
    assert roots == {path.stem.split("-")[0] for path in VALID}
