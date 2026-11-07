"""Checks OPA's tree, the converter and the schema headers against the merged release.

OPA's tree at the release is beside .linkml/, unchanged. These tests show that it
matches its pin byte for byte, that the schema is what the converter writes from it,
and that the schema, the converter and the watch name one release.
"""

import hashlib
import importlib.util
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
TREE = ROOT.parent
SCHEMA_DIR = ROOT / "src" / "opa" / "schema"
MANIFEST = Path(__file__).parent / "upstream_tree.tsv"


def _module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=1)
def _watch():
    return _module("watch_pins", ROOT / "scripts" / "check_upstream_release.py")


@lru_cache(maxsize=1)
def _converter():
    return _module("converter_pins", ROOT / "scripts" / "opa_to_linkml.py")


def _blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_opa_tree_is_the_merged_release():
    """Every file OPA's release holds is here, byte for byte."""
    differing = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        sha, path = line.split("\t", 1)
        local = TREE / path
        if not local.is_file() or _blob_sha(local) != sha:
            differing.append(path)
    assert not differing


def test_nothing_but_the_sidecars_sits_beside_opas_tree():
    """Every tracked file outside OPA's tree is this project's: the sidecars, their
    doorways, and the workflows and release files the family adds."""
    pinned = {
        line.split("\t", 1)[1]
        for line in MANIFEST.read_text(encoding="utf-8").splitlines()
    }
    tracked = subprocess.run(
        ["git", "-C", str(TREE), "ls-files", "-z"], capture_output=True, check=True
    ).stdout.decode("utf-8")
    own = (".linkml/", ".lokf/", "website/", ".github/")
    extra = sorted(
        path
        for path in filter(None, tracked.split("\0"))
        if path not in pinned and not path.startswith(own)
    )
    assert set(extra) <= {
        "knowledge_bundle",
        "linkml_schema",
        "llms.txt",
        ".releaserc.json",
    }


def test_converter_watch_and_headers_name_one_release():
    edition = _watch().EDITION
    converter = _converter()
    assert converter.TAG == edition["tag"] == f"v{edition['version']}"
    assert converter.COMMIT == edition["commit"]
    for path in sorted(SCHEMA_DIR.glob("*.yaml")):
        head = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert head["version"] == edition["version"], path.name
        assert head["annotations"]["upstream_tag"] == edition["tag"], path.name
        assert head["annotations"]["upstream_commit"] == edition["commit"], path.name
        assert edition["commit"] in head["source"], path.name


def test_schema_is_what_the_converter_writes():
    """src/opa/schema/ is the converter's output from OPA's files, unedited."""
    script = ROOT / "scripts" / "opa_to_linkml.py"
    result = subprocess.run(
        [sys.executable, str(script), "--check"], capture_output=True
    )
    assert result.returncode == 0, result.stderr.decode()
