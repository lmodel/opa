"""Compares the schema with OPA's JSON Schemas in three tiers, and with OPA's Go types.

1. Address: every definition in OPA's plan and manifest schemas is the exact mapping of a
   class here, and every exact mapping names a definition OPA's file holds. Every JSON
   key of the Go structs the decision log and status modules render is a key of the
   class, and back.
2. Verdicts: a corpus built from OPA's definitions gets the same verdict from the schema
   as from OPA, except in the cases parity/structural.yaml lists. The corpus holds, for
   each definition and each branch of a oneOf, a document with only the required keys,
   one with every key, and mutations of each: a required key dropped, an unknown key
   added, a key set to null or to a value of the wrong type, and a branch's kind given
   another branch's fields. OPA's data files that have no JSON Schema (every capabilities
   file it includes, builtin_metadata.json and the version index) all validate.
3. Shape: parity/structural.yaml gives the reason for each difference, and every case it
   lists still differs.
"""

import importlib.util
import json
from functools import lru_cache

import pytest
import yaml

import opa_parity as parity

ROOT = parity.ROOT
TREE = parity.TREE
STRUCTURAL = ROOT / "parity" / "structural.yaml"

# The classes that render a Go struct: the file, the struct, and the key the class
# adds for the map that holds it, where the struct has none.
GO_STRUCTS = {
    "OpaDecisionLogEvent": ("v1/plugins/logs/plugin.go", "EventV1", set()),
    "OpaDecisionBundle": ("v1/plugins/logs/plugin.go", "BundleInfoV1", {"name"}),
    "OpaRequestContext": ("v1/plugins/logs/plugin.go", "RequestContext", set()),
    "OpaHttpRequestContext": ("v1/plugins/logs/plugin.go", "HTTPRequestContext", set()),
    "OpaStatusReport": ("v1/plugins/status/plugin.go", "UpdateRequestV1", set()),
    "OpaBundleStatus": ("v1/plugins/bundle/status.go", "Status", set()),
    "OpaDecisionLogStatus": ("v1/plugins/logs/status/status.go", "Status", set()),
    "OpaPluginStatus": ("v1/plugins/plugins.go", "Status", {"name"}),
}


@lru_cache(maxsize=1)
def _converter():
    path = ROOT / "scripts" / "opa_to_linkml.py"
    spec = importlib.util.spec_from_file_location("converter_for_parity", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _class_for(prefix: str, definition: str) -> str:
    found = [
        name
        for name, cls in parity.classes().items()
        if f"{prefix}:{definition}" in (cls.get("exact_mappings") or [])
    ]
    assert len(found) == 1, (prefix, definition, found)
    return found[0]


def _value(node, defs, full):
    if "$ref" in node:
        return _value(defs[node["$ref"].rsplit("/", 1)[1]], defs, full)
    if "const" in node:
        return node["const"]
    if "oneOf" in node:
        branch = next(b for b in node["oneOf"] if b.get("type") != "null")
        return _value(branch, defs, full)
    kind = node.get("type", "object")
    if isinstance(kind, list):
        kind = next(k for k in kind if k != "null")
    if kind == "object":
        required = set(node.get("required", []))
        props = node.get("properties", {})
        return {
            k: _value(v, defs, full) for k, v in props.items() if full or k in required
        }
    if kind == "array":
        return [_value(node.get("items", {"type": "string"}), defs, full)]
    return {"string": "x", "integer": 1, "boolean": True, "number": 1.5}[kind]


def _wrong(node, defs):
    """A value of another JSON type than the property's."""
    while "$ref" in node:
        node = defs[node["$ref"].rsplit("/", 1)[1]]
    kind = node.get("type")
    if isinstance(kind, list):
        kind = next(k for k in kind if k != "null")
    return 1 if kind in ("string", "object", "array", None) else "x"


def _cases(node, defs):
    """Each (case label, document) for one object definition."""
    out = []
    for full in (False, True):
        base = _value(node, defs, full)
        label = "full" if full else "minimal"
        out.append((label, base))
        props = node.get("properties", {})
        for key in node.get("required", []):
            if not full:
                out.append((f"drop:{key}", {k: v for k, v in base.items() if k != key}))
        if full:
            out.append(("extra-key", {**base, "zz_extra": 1}))
            for key, spec in props.items():
                out.append((f"null:{key}", {**base, key: None}))
                out.append((f"wrong:{key}", {**base, key: _wrong(spec, defs)}))
    return out


@lru_cache(maxsize=1)
def corpus():
    """Each (OPA target, class here, case label, document) of the corpus."""
    items = []
    sources = [(prefix, rel) for prefix, rel in parity.PUBLISHED.items()]
    for prefix, rel in sources:
        defs = parity.published(rel)["$defs"]
        for name, node in sorted(defs.items()):
            target, cls = f"{rel}#{name}", _class_for(prefix, name)
            if "oneOf" in node:
                branches = node["oneOf"]
                for i, branch in enumerate(branches):
                    kind = branch["properties"]["type"]["const"]
                    for label, doc in _cases(branch, defs):
                        items.append((target, cls, f"{kind}/{label}", doc))
                    other = branches[(i + 1) % len(branches)]
                    swapped = {**_value(other, defs, False), "type": kind}
                    items.append((target, cls, f"{kind}/mismatch", swapped))
            elif "$ref" in node:
                continue
            else:
                for label, doc in _cases(node, defs):
                    items.append((target, cls, label, doc))
    authz = parity.published(parity.AUTHZ)
    for label, doc in _cases(authz, {}):
        items.append((parity.AUTHZ, "OpaAuthorizationInput", label, doc))
    return items


def _differences():
    found = set()
    for target, cls, label, doc in corpus():
        theirs = parity.verdict("published", target, doc)
        ours = parity.verdict("generated", cls, doc)
        if theirs != ours:
            found.add(
                (
                    target.rpartition("#")[2] or target,
                    label,
                    "accepts" if ours else "rejects",
                )
            )
    return found


@lru_cache(maxsize=1)
def _structural():
    return yaml.safe_load(STRUCTURAL.read_text(encoding="utf-8"))


def test_every_definition_has_a_class():
    for prefix, rel in parity.PUBLISHED.items():
        for name in parity.published(rel)["$defs"]:
            _class_for(prefix, name)


def test_every_mapping_names_a_definition():
    for name, cls in parity.classes().items():
        for mapping in cls.get("exact_mappings") or []:
            prefix, _, definition = mapping.partition(":")
            assert definition in parity.published(parity.PUBLISHED[prefix])["$defs"], (
                name
            )


@pytest.mark.parametrize("cls", sorted(GO_STRUCTS))
def test_every_key_of_the_go_struct_is_a_key_of_the_class(cls):
    rel, struct, added = GO_STRUCTS[cls]
    assert parity.keys(cls) == set(_converter().go_struct(rel, struct)) | added


def test_every_class_of_a_go_module_renders_a_struct():
    for module in ("decision_log", "status_report"):
        path = ROOT / "src" / "opa" / "schema" / f"{module}.yaml"
        names = yaml.safe_load(path.read_text(encoding="utf-8"))["classes"]
        assert set(names) <= set(GO_STRUCTS), module


def test_the_committed_json_schema_is_what_the_schema_generates():
    """project/jsonschema/opa.schema.json, which a user validates with, is the JSON
    Schema these tests read, so a schema change without `just gen-project` fails."""
    committed = ROOT / "project" / "jsonschema" / "opa.schema.json"
    assert json.loads(committed.read_text(encoding="utf-8")) == parity.generated()


def test_corpus_is_large():
    assert len(corpus()) > 900


def test_verdicts_agree_except_where_listed():
    listed = {
        (case["definition"], label, case["here"])
        for case in _structural()["differences"]
        for label in case["cases"]
    }
    assert _differences() == listed


def test_each_difference_has_a_reason():
    for case in _structural()["differences"]:
        assert case["reason"].strip(), case["definition"]
        assert case["here"] in ("accepts", "rejects"), case["definition"]


def _capabilities():
    return [TREE / "capabilities.json", *sorted((TREE / "capabilities").glob("*.json"))]


@lru_cache(maxsize=None)
def _builtin_errors(text: str) -> tuple[str, ...]:
    return tuple(parity.errors("generated", "OpaBuiltin", json.loads(text))[:3])


def test_a_capabilities_document_checks_its_builtins_one_by_one():
    """The generated schema checks each item of `builtins` against OpaBuiltin and
    nothing else, so the next test may check each distinct built-in once."""
    prop = parity.generated()["$defs"]["OpaCapabilities"]["properties"]["builtins"]
    assert prop["items"] == {"$ref": "#/$defs/OpaBuiltin"}
    assert set(prop) <= {"description", "items", "type"}


@pytest.mark.parametrize("path", _capabilities(), ids=lambda p: p.name)
def test_every_shipped_capabilities_file_validates(path):
    """The document with its builtins left out, and each built-in on its own. The
    files repeat most built-ins, and each distinct one is checked once."""
    doc = json.loads(path.read_text(encoding="utf-8"))
    builtins = doc.pop("builtins", [])
    assert parity.verdict("generated", "OpaCapabilities", {**doc, "builtins": []})
    for builtin in builtins:
        errors = _builtin_errors(json.dumps(builtin, sort_keys=True))
        assert not errors, (builtin.get("name"), errors)


@pytest.mark.parametrize(
    ("cls", "rel"),
    [
        ("OpaBuiltinMetadataCatalog", "builtin_metadata.json"),
        ("OpaVersionIndex", "v1/ast/version_index.json"),
    ],
)
def test_opas_data_files_validate(cls, rel):
    doc = json.loads((TREE / rel).read_text(encoding="utf-8"))
    assert parity.verdict("generated", cls, doc), parity.errors("generated", cls, doc)[
        :3
    ]
