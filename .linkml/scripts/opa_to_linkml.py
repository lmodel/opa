#!/usr/bin/env python3
"""Write the LinkML schema of OPA's JSON formats from the OPA release this fork holds.

The script reads OPA's own files from the repository root, which is OPA's tree at
the merged release, and writes one module per format under src/opa/schema/.

- v1/ir/plan.schema.json, v1/bundle/manifest.schema.json and
  v1/schemas/authorizationPolicy.json are OPA's JSON Schemas. The plan, the bundle
  manifest and the authorization input render them key for key.
- capabilities.json and capabilities/*.json, builtin_metadata.json and
  v1/ast/version_index.json have no JSON Schema. Their modules render the Go types
  that write them (ast.Capabilities, ast.Builtin, types.Type, the generators under
  internal/cmd/) and take each enumeration from the values every shipped file uses.
- v1/ir/ir.go gives the plan's descriptions: the opening sentences of its doc
  comments.

Run `just gen-linkml` after a merge of an OPA release. `--check` exits 1 when a
module differs from what the files give.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
OPA = PROJECT.parent
SCHEMA_DIR = PROJECT / "src" / "opa" / "schema"

TAG = "v1.22.2"
COMMIT = "482d9e368c2ddfed67ced59259fa6a247bb5f1e5"
RELEASE_DATE = "2026-11-05"
BLOB = f"https://github.com/open-policy-agent/opa/blob/{COMMIT}/"
NAMESPACE = "https://w3id.org/lmodel/opa/"

PLAN_SCHEMA = "v1/ir/plan.schema.json"
MANIFEST_SCHEMA = "v1/bundle/manifest.schema.json"
AUTHZ_SCHEMA = "v1/schemas/authorizationPolicy.json"
IR_GO = "v1/ir/ir.go"
VERSION_GO = "v1/version/version.go"

LOCATION_KEYS = ("file", "col", "row", "end_col", "end_row")


def read_json(rel: str) -> Any:
    return json.loads((OPA / rel).read_text(encoding="utf-8"))


def opa_version() -> str:
    m = re.search(r'^var Version = "([^"]+)"', (OPA / VERSION_GO).read_text(), re.M)
    if not m or f"v{m.group(1)}" != TAG:
        sys.exit(
            f"{VERSION_GO} says {m and m.group(1)!r}, not {TAG}: update TAG and COMMIT"
        )
    return m.group(1)


def go_doc_comments(rel: str) -> dict[str, str]:
    """Map each type in a Go file to the opening of its doc comment, up to a TODO."""
    docs: dict[str, str] = {}
    lines: list[str] = []
    for raw in (OPA / rel).read_text(encoding="utf-8").splitlines():
        text = raw.strip()
        if text.startswith("//"):
            lines.append(text[2:].strip())
            continue
        top = raw.startswith("type ") or (
            raw.startswith("\t") and not raw.startswith("\t\t")
        )
        m = re.match(r"^(?:type\s+)?([A-Z]\w*)\s+(struct|interface|int|bool)\b", text)
        if top and m and lines:
            words = " ".join(lines).split("TODO")[0]
            sentences = re.split(r"(?<=[.])\s+", words.strip())
            docs[m.group(1)] = " ".join(sentences[:2]).strip()
        lines = []
    return docs


def header(
    module: str, title: str, description: str, source: str | None, imports: list[str]
) -> dict:
    head: dict[str, Any] = {
        "id": f"{NAMESPACE}{module}" if module != "opa" else NAMESPACE.rstrip("/"),
        "name": module,
        "title": title,
        "description": description,
        "version": opa_version(),
    }
    if source:
        head["source"] = source
    head["license"] = "Apache-2.0"
    head["see_also"] = [
        "https://lmodel.github.io/opa",
        "https://www.openpolicyagent.org/docs",
    ]
    head["annotations"] = {
        "upstream_tag": TAG,
        "upstream_commit": COMMIT,
        "upstream_release_date": RELEASE_DATE,
        "upstream_license": "Apache-2.0",
    }
    # The prefix is openpolicyagent, not opa: the Bioregistry gives opa another namespace.
    head["prefixes"] = {
        "openpolicyagent": NAMESPACE,
        "linkml": "https://w3id.org/linkml/",
        "schema": "http://schema.org/",
    }
    head["default_prefix"] = "openpolicyagent"
    head["default_range"] = "string"
    head["imports"] = ["linkml:types", *imports]
    return head


def kind_attr(kind: str, description: str) -> dict:
    """The `type` key that names a variant: a string that must equal the variant's kind.

    The base class declares no `type`, since gen-python's loader refuses equals_string on
    an enumeration and slot_usage on an inherited attribute.
    """
    return {
        "description": description,
        "range": "string",
        "required": True,
        "equals_string": kind,
    }


def attr(rng: str | None = None, description: str | None = None, **extra: Any) -> dict:
    out: dict[str, Any] = {}
    if description:
        out["description"] = description
    if rng:
        out["range"] = rng
    out.update({k: v for k, v in extra.items() if v is not None and v is not False})
    return out


# ---------------------------------------------------------------- common


TYPE_MARKERS = {
    "any": "A union of the types it lists in `of`, or any value when it lists none.",
    "array": "An array, with a type per position in `static` and one for the rest in `dynamic`.",
    "boolean": "A boolean.",
    "function": "A function, with its arguments, its result and a variadic argument type.",
    "null": "The null value.",
    "number": "A number.",
    "object": "An object, with typed known keys in `static` and a key and value type for the rest in `dynamic`.",
    "set": "A set, whose members have the type in `of`.",
    "string": "A string.",
}


def build_common() -> dict:
    schema = header(
        "common",
        "OPA common types",
        "Types that more than one OPA format uses: an open JSON object, and the Rego type "
        "declarations that capabilities and plans carry for built-in functions.",
        f"{BLOB}v1/types/types.go",
        [],
    )
    classes: dict[str, Any] = {
        "OpaObject": {
            "description": "A JSON object whose keys OPA leaves open.",
            "extra_slots": {"allowed": True},
        },
        "OpaValue": {
            "description": "Any JSON value.",
            "class_uri": "linkml:Any",
        },
        "OpaType": {
            "abstract": True,
            "description": "A Rego type, as OPA's types package writes it in JSON. A named type is "
            "an argument or result of a built-in function, with a name and a description.",
            "attributes": {
                "name": attr(None, "The argument's or result's name, on a named type."),
                "description": attr(
                    None, "What the argument or result holds, on a named type."
                ),
            },
        },
    }
    of_one = "The type of the set's members."
    for marker, text in TYPE_MARKERS.items():
        name = f"Opa{marker.capitalize()}Type"
        cls: dict[str, Any] = {
            "is_a": "OpaType",
            "description": text,
        }
        attrs: dict[str, Any] = {"type": kind_attr(marker, "The kind of type.")}
        if marker == "any":
            attrs["of"] = attr(
                "OpaType",
                "The types the union admits.",
                multivalued=True,
                inlined=True,
                inlined_as_list=True,
            )
        elif marker == "set":
            attrs["of"] = attr("OpaType", of_one, inlined=True)
        elif marker in ("array", "object"):
            attrs["static"] = attr(
                "OpaType" if marker == "array" else "OpaStaticProperty",
                "The type of each element by position."
                if marker == "array"
                else "The known keys and the types of their values.",
                multivalued=True,
                inlined=True,
                inlined_as_list=True,
            )
            attrs["dynamic"] = attr(
                "OpaType" if marker == "array" else "OpaDynamicProperty",
                "The type of the elements after the static ones."
                if marker == "array"
                else "The key type and value type of the other keys.",
                inlined=True,
            )
        elif marker == "function":
            attrs["args"] = attr(
                "OpaType",
                "The argument types, in order.",
                multivalued=True,
                inlined=True,
                inlined_as_list=True,
            )
            attrs["result"] = attr("OpaType", "The result type.", inlined=True)
            attrs["variadic"] = attr(
                "OpaType", "The type of any further arguments.", inlined=True
            )
        cls["attributes"] = attrs
        classes[name] = cls
    classes["OpaStaticProperty"] = {
        "description": "A known key of an object type and the type of its value.",
        "attributes": {
            "key": attr("OpaValue", "The key, as a JSON value.", required=True),
            "value": attr(
                "OpaType", "The type of the key's value.", required=True, inlined=True
            ),
        },
    }
    classes["OpaDynamicProperty"] = {
        "description": "The key type and value type that an object type gives its other keys.",
        "attributes": {
            "key": attr(
                "OpaType", "The type of the keys.", required=True, inlined=True
            ),
            "value": attr(
                "OpaType", "The type of the values.", required=True, inlined=True
            ),
        },
    }
    schema["classes"] = classes
    return schema


# ---------------------------------------------------------------- capabilities


def capabilities_files() -> list[Path]:
    return [OPA / "capabilities.json", *sorted((OPA / "capabilities").glob("*.json"))]


def build_capabilities() -> dict:
    keywords: set[str] = set()
    features: set[str] = set()
    for path in capabilities_files():
        doc = json.loads(path.read_text(encoding="utf-8"))
        keywords.update(doc.get("future_keywords") or [])
        features.update(doc.get("features") or [])
    schema = header(
        "capabilities",
        "OPA capabilities",
        "The capabilities document: the built-in functions, future keywords, Wasm ABI versions "
        "and language features an OPA version supports, and the hosts it may reach. OPA ships one "
        "per release in capabilities/, and `opa capabilities` prints it.",
        f"{BLOB}v1/ast/capabilities.go",
        ["common"],
    )
    schema["classes"] = {
        "OpaCapabilities": {
            "tree_root": True,
            "description": "What an OPA version supports, which a policy can be checked against.",
            "attributes": {
                "builtins": attr(
                    "OpaBuiltin",
                    "The built-in functions.",
                    multivalued=True,
                    inlined=True,
                    inlined_as_list=True,
                ),
                "future_keywords": attr(
                    "OpaFutureKeyword",
                    "The keywords a policy may import from future.keywords.",
                    multivalued=True,
                ),
                "wasm_abi_versions": attr(
                    "OpaWasmAbiVersion",
                    "The Wasm ABI versions supported.",
                    multivalued=True,
                    inlined=True,
                    inlined_as_list=True,
                ),
                "features": attr(
                    "OpaFeature", "The language features supported.", multivalued=True
                ),
                "allow_net": attr(
                    None,
                    "The hosts OPA may connect to, as host names or IP addresses. OPA reaches any "
                    "host when the key is absent, and none when the list is empty.",
                    multivalued=True,
                ),
            },
        },
        "OpaBuiltin": {
            "description": "A built-in function and its type declaration.",
            "attributes": {
                "name": attr(
                    None, "The function's name, such as `array.concat`.", required=True
                ),
                "description": attr(None, "What the function does."),
                "categories": attr(
                    None, "The categories the function belongs to.", multivalued=True
                ),
                "decl": attr(
                    "OpaFunctionType",
                    "The function's type declaration.",
                    required=True,
                    inlined=True,
                ),
                "infix": attr(
                    None, "The infix operator that calls the function, such as `+`."
                ),
                "relation": attr("boolean", "Whether the function acts as a relation."),
                "deprecated": attr("boolean", "Whether the function is deprecated."),
                "nondeterministic": attr(
                    "boolean",
                    "Whether the function may return different results for the same arguments.",
                ),
            },
        },
        "OpaWasmAbiVersion": {
            "description": "A Wasm ABI version, as a major and a minor number.",
            "attributes": {
                "version": attr("integer", "The major version.", required=True),
                "minor_version": attr("integer", "The minor version.", required=True),
            },
        },
    }
    schema["enums"] = {
        "OpaFutureKeyword": {
            "description": "The future keywords the shipped capabilities files name.",
            "permissible_values": {k: {} for k in sorted(keywords)},
        },
        "OpaFeature": {
            "description": "The language features the shipped capabilities files name.",
            "permissible_values": {f: {} for f in sorted(features)},
        },
    }
    return schema


# ---------------------------------------------------------------- builtin metadata


def build_builtin_metadata() -> dict:
    schema = header(
        "builtin_metadata",
        "OPA built-in function metadata",
        "builtin_metadata.json, which OPA's genbuiltinmetadata command writes for the "
        "documentation: each built-in function with its arguments, its result, the OPA versions "
        "that have it and the other implementations that support it, keyed by name.",
        f"{BLOB}internal/cmd/genbuiltinmetadata/main.go",
        [],
    )
    schema["classes"] = {
        "OpaBuiltinMetadataCatalog": {
            "tree_root": True,
            "description": "The catalogue: two keys that start with an underscore, and one key per "
            "built-in function, whose value describes it.",
            "attributes": {
                "categories": attr(
                    "OpaBuiltinCategory",
                    "The categories, each with the names of its functions.",
                    alias="_categories",
                    multivalued=True,
                    inlined=True,
                ),
                "implementations": attr(
                    "OpaImplementation",
                    "The implementations of Rego besides OPA that the catalogue tracks.",
                    alias="_implementations",
                    multivalued=True,
                    inlined=True,
                    inlined_as_list=True,
                ),
            },
            "extra_slots": {"range_expression": {"range": "OpaBuiltinMetadata"}},
        },
        "OpaBuiltinCategory": {
            "description": "A category of built-in functions.",
            "attributes": {
                "name": attr(None, "The category's name.", key=True),
                "builtins": attr(
                    None,
                    "The names of the category's functions.",
                    multivalued=True,
                    required=True,
                ),
            },
        },
        "OpaImplementation": {
            "description": "An implementation of Rego besides OPA.",
            "attributes": {
                "id": attr(
                    None,
                    "The implementation's key in each function's `implementations`.",
                    required=True,
                ),
                "label": attr(
                    None, "The implementation's display name.", required=True
                ),
                "repo": attr(
                    None,
                    "The implementation's GitHub repository, as owner/name.",
                    required=True,
                ),
                "version": attr(
                    None,
                    "The implementation's version the catalogue reflects.",
                    required=True,
                ),
            },
        },
        "OpaBuiltinMetadata": {
            "description": "What the catalogue says about one built-in function.",
            "attributes": {
                "description": attr(None, "What the function does."),
                "introduced": attr(
                    None, "The OPA version that added the function.", required=True
                ),
                "available": attr(
                    None,
                    "The OPA versions that have the function, and `edge`.",
                    multivalued=True,
                    required=True,
                ),
                "wasm": attr(
                    "boolean",
                    "Whether OPA's Wasm target implements the function.",
                    required=True,
                ),
                "args": attr(
                    "OpaBuiltinArgument",
                    "The arguments, in order.",
                    multivalued=True,
                    inlined=True,
                    inlined_as_list=True,
                    required=True,
                ),
                "result": attr(
                    "OpaBuiltinResult", "The result.", inlined=True, required=True
                ),
                "implementations": attr(
                    "OpaImplementationSupport",
                    "The other implementations that support the function, with the version that added it.",
                    multivalued=True,
                    inlined=True,
                    required=True,
                ),
                "infix": attr(None, "The infix operator that calls the function."),
                "relation": attr("boolean", "Whether the function acts as a relation."),
                "deprecated": attr("boolean", "Whether the function is deprecated."),
            },
        },
        "OpaBuiltinArgument": {
            "description": "An argument of a built-in function.",
            "attributes": {
                "name": attr(None, "The argument's name."),
                "description": attr(None, "What the argument holds."),
                "type": attr(
                    None,
                    "The argument's type, written as OPA prints types, such as `array[string]`.",
                    required=True,
                ),
            },
        },
        "OpaBuiltinResult": {
            "description": "The result of a built-in function. Some functions declare none.",
            "attributes": {
                "name": attr(None, "The result's name."),
                "description": attr(None, "What the result holds."),
                "type": attr(None, "The result's type, written as OPA prints types."),
            },
        },
        "OpaImplementationSupport": {
            "description": "An implementation that supports a function, and the version that added it.",
            "attributes": {
                "implementation": attr(None, "The implementation's id.", key=True),
                "version": attr(
                    None,
                    "The implementation's version that added the function.",
                    required=True,
                ),
            },
        },
    }
    return schema


# ---------------------------------------------------------------- version index


def build_version_index() -> dict:
    schema = header(
        "version_index",
        "OPA version index",
        "v1/ast/version_index.json, which OPA's genversionindex command writes: the OPA version "
        "that introduced each built-in function, feature and keyword.",
        f"{BLOB}internal/cmd/genversionindex/main.go",
        [],
    )
    entries = "keyed by name, each with the version that introduced it."
    schema["classes"] = {
        "OpaVersionIndex": {
            "tree_root": True,
            "description": "The version index.",
            "attributes": {
                key: attr(
                    "OpaVersionEntry",
                    f"The {key}, {entries}",
                    multivalued=True,
                    inlined=True,
                    required=True,
                )
                for key in ("builtins", "features", "keywords")
            },
        },
        "OpaVersionEntry": {
            "description": "A built-in function, feature or keyword, and the OPA version that introduced it.",
            "attributes": {
                "name": attr(
                    None, "The name of the function, feature or keyword.", key=True
                ),
                "major": attr(
                    "integer", "The major version.", alias="Major", required=True
                ),
                "minor": attr(
                    "integer", "The minor version.", alias="Minor", required=True
                ),
                "patch": attr(
                    "integer", "The patch version.", alias="Patch", required=True
                ),
                "pre_release": attr(
                    None, "The pre-release label, such as `rc2`.", alias="PreRelease"
                ),
            },
        },
    }
    return schema


# ---------------------------------------------------------------- JSON Schema modules


def range_of(spec: dict, names: dict[str, str]) -> tuple[dict, bool]:
    """Return a LinkML slot for a JSON Schema property, and whether null is allowed."""
    nullable = False
    if "oneOf" in spec:
        branches = [b for b in spec["oneOf"] if b.get("type") != "null"]
        nullable = len(branches) < len(spec["oneOf"])
        spec = branches[0]
    types = spec.get("type")
    if isinstance(types, list):
        nullable = nullable or "null" in types
        types = [t for t in types if t != "null"][0]
    if "$ref" in spec:
        target = names[spec["$ref"].rsplit("/", 1)[1]]
        return {"range": target, "inlined": True}, nullable
    if types == "array":
        inner, _ = range_of(spec["items"], names)
        out = {**inner, "multivalued": True}
        if inner.get("inlined"):
            out["inlined_as_list"] = True
        return out, nullable
    if types == "object":
        extra = spec.get("additionalProperties")
        if isinstance(extra, dict):
            return {"range": "__map__", "value": extra}, nullable
        return {"range": "OpaObject", "inlined": True}, nullable
    return {
        "range": {
            "string": "string",
            "integer": "integer",
            "boolean": "boolean",
            "number": "float",
        }[types]
    }, nullable


def object_class(
    defn: dict,
    names: dict[str, str],
    description: str,
    mapping: str | None,
    shared: tuple[str, ...] = (),
) -> dict:
    cls: dict[str, Any] = {"description": description}
    if mapping:
        cls["exact_mappings"] = [mapping]
    if defn.get("additionalProperties") is not False:
        cls["extra_slots"] = {"allowed": True}
    required = set(defn.get("required", []))
    attrs: dict[str, Any] = {}
    for key, spec in defn.get("properties", {}).items():
        if key in shared:
            continue
        slot, nullable = range_of(spec, names)
        if spec.get("description"):
            slot["description"] = spec["description"]
        if spec.get("deprecated"):
            slot["deprecated"] = spec.get("description", "Deprecated in OPA's schema.")
        if key in required and not nullable:
            slot["required"] = True
        attrs[key] = slot
    if attrs:
        cls["attributes"] = attrs
    return cls


PLAN_TEXT = {
    "file": "Index, in the plan's static files, of the policy file the statement comes from.",
    "col": "Column where the statement's source text starts.",
    "row": "Line where the statement's source text starts.",
    "end_col": "Column where the statement's source text ends.",
    "end_row": "Line where the statement's source text ends.",
}

FIELD_TEXT = {
    ("Policy", "static"): "The constants the plan indexes into.",
    ("Policy", "plans"): "The query plans the policy exposes.",
    ("Policy", "funcs"): "The functions the plans call.",
    (
        "Policy",
        "unplanned_rules",
    ): "The rules left out because no entrypoint reaches them.",
    (
        "Static",
        "strings",
    ): "The string constants, which a string index refers to by position.",
    ("Static", "builtin_funcs"): "The built-in functions the plan calls.",
    (
        "Static",
        "files",
    ): "The names of the policy files, which a location refers to by position.",
    ("StringConst", "value"): "The string.",
    ("BuiltinFunc", "name"): "The function's name.",
    (
        "BuiltinFunc",
        "decl",
    ): "The function's type declaration. OPA's schema leaves it opaque; OPA writes a function type.",
    ("Plans", "plans"): "The plans.",
    ("Plan", "name"): "The plan's name, which is its entrypoint.",
    ("Plan", "blocks"): "The blocks, run in order.",
    ("Funcs", "funcs"): "The functions.",
    ("Func", "name"): "The function's name.",
    (
        "Func",
        "params",
    ): "The locals that hold the parameters. The first two are the input and data documents.",
    ("Func", "return"): "The local that holds the return value.",
    ("Func", "blocks"): "The blocks, run in order.",
    ("Func", "path"): "Where the function sits in the data tree, when it has a path.",
    ("Block", "stmts"): "The statements, run in order.",
    ("UnplannedRule", "path"): "The rule's path.",
    ("UnplannedRule", "location"): "Where the rule is defined.",
}

GENERIC_TEXT = {
    "target": "The local that receives the result.",
    "source": "What the statement reads.",
    "a": "The first value.",
    "b": "The second value.",
    "key": "The key.",
    "value": "The value.",
    "block": "The block the statement runs.",
    "blocks": "The blocks the statement runs.",
    "args": "The arguments.",
    "result": "The local that receives the result.",
    "func": "The name of the function called.",
    "path": "The path.",
    "index": "The index.",
    "capacity": "The capacity to allocate.",
    "local": "The local.",
    "set": "The local that holds the set.",
    "array": "The local that holds the array.",
    "object": "The local that holds the object.",
}

STMT_FIELD_TEXT = {
    (
        "BreakStmt",
        "index",
    ): "How many enclosing blocks to leave, counting the current block as zero.",
    (
        "CallDynamicStmt",
        "path",
    ): "The path of the function in the data tree, one operand per segment.",
    ("CallDynamicStmt", "args"): "The locals passed as arguments.",
    ("ScanStmt", "source"): "The local whose value is scanned.",
    ("ScanStmt", "key"): "The local that receives each key.",
    ("ScanStmt", "value"): "The local that receives each value.",
    ("ScanStmt", "block"): "The block run for each key and value.",
    (
        "MakeNumberRefStmt",
        "index",
    ): "Index, in the plan's static strings, of the number written as a string.",
    ("WithStmt", "local"): "The local whose value, or part of it, is replaced.",
    (
        "WithStmt",
        "path",
    ): "The path within the local's value to replace, as indices of static strings. Empty replaces the whole value.",
    ("WithStmt", "value"): "The replacement value.",
    ("ResultSetAddStmt", "value"): "The local added to the result set.",
    ("ReturnLocalStmt", "source"): "The local returned.",
    ("IsDefinedStmt", "source"): "The local checked.",
    ("IsUndefinedStmt", "source"): "The local checked.",
    ("ObjectMergeStmt", "a"): "The local that holds the first object.",
    ("ObjectMergeStmt", "b"): "The local that holds the second object.",
}


def build_ir_plan() -> dict:
    doc = read_json(PLAN_SCHEMA)
    defs = doc["$defs"]
    go = go_doc_comments(IR_GO)
    stmt_kinds = [b["properties"]["type"]["const"] for b in defs["Stmt"]["oneOf"]]
    names = {k: f"Opa{k}" for k in defs}
    for kind in stmt_kinds:
        names[kind] = f"Opa{kind}Body"
    names["Operand"] = names["Val"] = "OpaOperand"
    prefix = "opa_plan"
    schema = header(
        "ir_plan",
        "OPA IR plan",
        "The intermediate representation that `opa build -t plan` writes: query plans and "
        "functions as blocks of statements over numbered locals, for an evaluator outside OPA "
        "to run. It renders OPA's JSON Schema for the plan, generated from v1/ir/ir.go.",
        f"{BLOB}{PLAN_SCHEMA}",
        ["common"],
    )
    schema["prefixes"][prefix] = doc["$id"] + "#/$defs/"
    schema["see_also"].append(doc["$id"])
    schema["slots"] = {
        key: {"description": text, "range": "integer"}
        for key, text in PLAN_TEXT.items()
    }

    classes: dict[str, Any] = {}
    for name in (
        "Policy",
        "Static",
        "StringConst",
        "BuiltinFunc",
        "Plans",
        "Plan",
        "Funcs",
        "Func",
        "Block",
        "UnplannedRule",
        "Location",
    ):
        cls = object_class(
            defs[name],
            names,
            go[name],
            f"{prefix}:{name}",
            LOCATION_KEYS if name == "Location" else (),
        )
        for key, slot in cls.get("attributes", {}).items():
            slot.setdefault("description", FIELD_TEXT[(name, key)])
        if name == "Location":
            cls["slots"] = list(LOCATION_KEYS)
            cls["slot_usage"] = {k: {"required": True} for k in LOCATION_KEYS}
        classes[names[name]] = cls
    classes["OpaPolicy"]["tree_root"] = True
    classes["OpaBuiltinFunc"]["attributes"]["decl"]["range"] = "OpaFunctionType"
    # Python keyword: the slot is return_local, and OPA's key is its alias.
    classes["OpaFunc"]["attributes"]["return_local"] = {
        **classes["OpaFunc"]["attributes"].pop("return"),
        "alias": "return",
    }
    classes["OpaFunc"]["attributes"]["return_local"]["description"] = FIELD_TEXT[
        ("Func", "return")
    ]
    classes["OpaFunc"]["attributes"] = dict(
        sorted(classes["OpaFunc"]["attributes"].items())
    )

    classes["OpaStmt"] = {
        "abstract": True,
        "description": go["Stmt"]
        + " OPA writes each statement as its kind in `type` and its fields in `stmt`.",
        "exact_mappings": [f"{prefix}:Stmt"],
    }
    classes["OpaStmtBody"] = {
        "abstract": True,
        "description": "The fields of a statement. Every kind carries the location of its source text.",
        "slots": list(LOCATION_KEYS),
        "slot_usage": {k: {"required": True} for k in LOCATION_KEYS},
    }
    for kind in stmt_kinds:
        classes[f"Opa{kind}"] = {
            "is_a": "OpaStmt",
            "description": f"A statement of kind {kind}, with its fields in `stmt`.",
            "attributes": {
                "type": kind_attr(kind, "The kind of statement."),
                "stmt": attr(
                    f"Opa{kind}Body",
                    "The statement's fields.",
                    required=True,
                    inlined=True,
                ),
            },
        }
        body = object_class(
            defs[kind], names, go[kind], f"{prefix}:{kind}", LOCATION_KEYS
        )
        body["is_a"] = "OpaStmtBody"
        for key, slot in body.get("attributes", {}).items():
            if key == "Index":
                continue
            slot.setdefault(
                "description", STMT_FIELD_TEXT.get((kind, key), GENERIC_TEXT[key])
            )
        for short, long in (("a", "operand_a"), ("b", "operand_b")):
            if short in body.get("attributes", {}):
                body["attributes"][long] = {
                    **body["attributes"].pop(short),
                    "alias": short,
                }
        if "Index" in body.get("attributes", {}):
            legacy = body["attributes"].pop("Index")
            legacy["alias"] = "Index"
            body["attributes"]["index_legacy"] = legacy
        classes[f"Opa{kind}Body"] = body

    classes["OpaOperand"] = {
        "abstract": True,
        "description": go["Operand"]
        + " OPA writes it as its kind in `type` and the value in `value`.",
        "exact_mappings": [f"{prefix}:Operand", f"{prefix}:Val"],
    }
    operand_text = {
        "bool": go["Bool"],
        "local": "A local variable, by its number.",
        "string_index": go["StringIndex"],
    }
    for branch in defs["Val"]["oneOf"]:
        kind = branch["properties"]["type"]["const"]
        rng = {"boolean": "boolean", "integer": "integer"}[
            branch["properties"]["value"]["type"]
        ]
        classes[f"Opa{''.join(p.capitalize() for p in kind.split('_'))}Operand"] = {
            "is_a": "OpaOperand",
            "description": operand_text[kind],
            "attributes": {
                "type": kind_attr(kind, "The kind of operand."),
                "value": attr(rng, "The operand's value.", required=True),
            },
        }
    schema["classes"] = classes
    return schema


def build_bundle_manifest() -> dict:
    doc = read_json(MANIFEST_SCHEMA)
    defs = doc["$defs"]
    names = {k: f"Opa{k}" for k in defs}
    prefix = "opa_manifest"
    schema = header(
        "bundle_manifest",
        "OPA bundle manifest",
        "The `.manifest` file of an OPA bundle: the bundle's revision, the data roots it owns, "
        "its Wasm modules, its Rego version and any metadata. It renders OPA's JSON Schema for the "
        "manifest, generated from v1/bundle/bundle.go.",
        f"{BLOB}{MANIFEST_SCHEMA}",
        ["common"],
    )
    schema["prefixes"][prefix] = doc["$id"] + "#/$defs/"
    schema["see_also"].append(doc["$id"])
    text = {
        (
            "Manifest",
            "revision",
        ): "The bundle's revision, a string the bundle's author chooses.",
        (
            "Manifest",
            "roots",
        ): "The paths in the data tree the bundle owns. A bundle without the key owns the whole tree.",
        (
            "Manifest",
            "wasm",
        ): "The Wasm modules the bundle holds, and the entrypoints they resolve.",
        (
            "Manifest",
            "rego_version",
        ): "The Rego version of the bundle's files: 0 for v0, 1 for v1.",
        (
            "Manifest",
            "file_rego_versions",
        ): "Rego versions for single files, which override `rego_version`.",
        ("Manifest", "metadata"): "Metadata the bundle's author adds.",
        ("WasmResolver", "entrypoint"): "The entrypoint the module resolves.",
        ("WasmResolver", "module"): "The module's path in the bundle.",
        (
            "WasmResolver",
            "annotations",
        ): "The entrypoint's Rego annotations. OPA's schema leaves their shape open.",
    }
    classes: dict[str, Any] = {}
    for name in ("Manifest", "WasmResolver"):
        description = {
            "Manifest": "A bundle manifest. OPA's schema leaves the manifest open to other keys.",
            "WasmResolver": "A Wasm module in a bundle, and the entrypoint it resolves.",
        }[name]
        cls = object_class(defs[name], names, description, f"{prefix}:{name}")
        for key, slot in cls["attributes"].items():
            slot["description"] = text[(name, key)]
        classes[names[name]] = cls
    frv = classes["OpaManifest"]["attributes"]["file_rego_versions"]
    frv.pop("value")
    frv.update(range="OpaFileRegoVersion", multivalued=True, inlined=True)
    classes["OpaManifest"]["tree_root"] = True
    classes["OpaFileRegoVersion"] = {
        "description": "The Rego version of one file in the bundle.",
        "attributes": {
            "path": attr(None, "The file's path in the bundle.", key=True),
            "version": attr("integer", "The file's Rego version.", required=True),
        },
    }
    schema["classes"] = classes
    return schema


def build_authorization_input() -> dict:
    doc = read_json(AUTHZ_SCHEMA)
    schema = header(
        "authorization_input",
        "OPA authorization policy input",
        "The input document OPA's REST API gives the system.authz policy when OPA runs with "
        "--authorization=basic. It renders OPA's JSON Schema for that input.",
        f"{BLOB}{AUTHZ_SCHEMA}",
        ["common"],
    )
    text = {
        "identity": "The bearer token or client certificate subject that identifies the caller.",
        "client_certificates": "The client's TLS certificates.",
        "method": "The HTTP method of the request.",
        "path": "The request path, one segment per element.",
        "params": "The query parameters.",
        "headers": "The request headers.",
        "body": "The request body.",
    }
    cls = object_class(
        doc, {}, doc["description"].replace("Schema for the", "The") + ".", None
    )
    for key, slot in cls["attributes"].items():
        slot["description"] = text[key]
    cls["tree_root"] = True
    schema["classes"] = {"OpaAuthorizationInput": cls}
    return schema


def build_umbrella() -> dict:
    schema = header(
        "opa",
        "Open Policy Agent (OPA)",
        "A LinkML model of the JSON formats Open Policy Agent defines: the IR plan, the bundle "
        "manifest, the authorization policy input, the capabilities document, the built-in "
        "function metadata and the version index. Each module renders one format, and keeps "
        "OPA's keys, so a document OPA writes validates here unchanged.",
        f"https://github.com/open-policy-agent/opa/tree/{COMMIT}",
        [m for m in MODULES if m != "opa"],
    )
    schema["keywords"] = ["policy as code", "Open Policy Agent", "Rego", "CNCF"]
    return schema


MODULES = {
    "common": build_common,
    "capabilities": build_capabilities,
    "builtin_metadata": build_builtin_metadata,
    "version_index": build_version_index,
    "authorization_input": build_authorization_input,
    "bundle_manifest": build_bundle_manifest,
    "ir_plan": build_ir_plan,
    "opa": build_umbrella,
}


class _Dumper(yaml.SafeDumper):
    def increase_indent(self, flow: bool = False, indentless: bool = False) -> Any:
        return super().increase_indent(flow, False)


def _str(dumper: yaml.Dumper, data: str) -> Any:
    style = ">" if len(data) > 72 else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


_Dumper.add_representer(str, _str)


# Keys whose meaning is LOKF's carry LOKF's IRI, so a composite's JSON-LD context reads
# them alike in a concept and in a copy of this schema.
SHARED_IRIS = {
    "description": "schema:description",
    "name": "schema:name",
    "version": "schema:version",
    "id": "schema:identifier",
}


def share_lokf_iris(schema: dict) -> None:
    for cls in (schema.get("classes") or {}).values():
        for key, slot in (cls.get("attributes") or {}).items():
            # An integer version, a Wasm ABI's major number or a file's Rego
            # version, is not LOKF's version string.
            if (
                key in SHARED_IRIS
                and "alias" not in slot
                and slot.get("range") != "integer"
            ):
                slot["slot_uri"] = SHARED_IRIS[key]


def render(schema: dict) -> str:
    body = yaml.dump(
        schema, Dumper=_Dumper, sort_keys=False, width=88, allow_unicode=True
    )
    note = "# Written by scripts/opa_to_linkml.py from OPA's files. Edit the script, not this file.\n"
    return "---\n" + note + body


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check", action="store_true", help="exit 1 when a module differs"
    )
    args = parser.parse_args(argv)
    stale = []
    for module, build in MODULES.items():
        path = SCHEMA_DIR / f"{module}.yaml"
        schema = build()
        share_lokf_iris(schema)
        text = render(schema)
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(path.name)
        else:
            path.write_text(text, encoding="utf-8")
    if stale:
        print(
            "stale: " + ", ".join(stale) + " (run `just gen-linkml`)", file=sys.stderr
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
