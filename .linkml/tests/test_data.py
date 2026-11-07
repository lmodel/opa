"""Checks each example against the schema, and against OPA's JSON Schema where OPA has one.

An example is a document OPA writes, with OPA's keys, such as `_categories`, `Major` or
`return`. linkml-validate and the example runner read keys by slot name, so they cannot
read one. The examples are kept under tests/data/problem/, where the runner does not look.
This test validates them against the JSON Schema LinkML generates, in which each key is
the slot's alias. `tests/data/problem/valid/<Class>-<anything>.yaml` must pass,
and `tests/data/problem/invalid/<Class>-<anything>.yaml` must fail. The plan and the
manifest must get the same verdict from OPA's schema. The authorization input is left
out of that comparison: OPA's schema for it requires keys that OPA's server leaves out.

`tests/data/captured/<Class>-<anything>.json` are documents OPA's own binary wrote, and
every one must pass.
"""

import json
from pathlib import Path

import pytest
import yaml

import opa_parity as parity

DATA = Path(__file__).parent / "data"
VALID = sorted((DATA / "problem" / "valid").glob("*.yaml"))
INVALID = sorted((DATA / "problem" / "invalid").glob("*.yaml"))
CAPTURED = sorted((DATA / "captured").glob("*.json"))
OPA = {
    "OpaPolicy": "v1/ir/plan.schema.json#Policy",
    "OpaManifest": "v1/bundle/manifest.schema.json#Manifest",
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


@pytest.mark.parametrize("path", CAPTURED, ids=lambda p: p.stem)
def test_a_document_opa_wrote_validates(path):
    cls = path.stem.split("-")[0]
    data = json.loads(path.read_text(encoding="utf-8"))
    assert parity.verdict("generated", cls, data), parity.errors(
        "generated", cls, data
    )[:3]
    if cls in OPA:
        assert parity.verdict("published", OPA[cls], data)


def test_every_document_class_has_an_example():
    roots = {name for name, cls in parity.classes().items() if cls.get("tree_root")}
    assert roots == {path.stem.split("-")[0] for path in VALID}


def test_opa_wrote_a_document_of_each_format_it_writes_here():
    """The capture covers every format OPA's binary writes in the capture script's
    runs: all but the capabilities document, the built-in function metadata and the
    version index, which OPA's tree holds as files and tests/test_parity.py reads."""
    roots = {name for name, cls in parity.classes().items() if cls.get("tree_root")}
    from_files = {"OpaCapabilities", "OpaBuiltinMetadataCatalog", "OpaVersionIndex"}
    assert {path.stem.split("-")[0] for path in CAPTURED} == roots - from_files
