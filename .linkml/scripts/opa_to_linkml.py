#!/usr/bin/env python3
"""Write the LinkML schema of eight of OPA's JSON formats from the merged OPA release.

The script reads OPA's own files from the repository root, which is OPA's tree at
the merged release, and writes one module per format under src/opa/schema/.

- v1/ir/plan.schema.json and v1/bundle/manifest.schema.json are OPA's JSON Schemas,
  and the plan and the bundle manifest render them key for key.
- v1/schemas/authorizationPolicy.json is the schema OPA type-checks the system.authz
  policy against. The authorization input renders its keys, and leaves optional the
  three that OPA's server writes only when the request has them.
- capabilities.json and capabilities/*.json, builtin_metadata.json and
  v1/ast/version_index.json have no JSON Schema. Their modules render the Go types
  that write them (ast.Capabilities, ast.Builtin, types.Type, the generators under
  internal/cmd/) and take each enumeration from the values used in the files OPA includes.
- The decision log event and the status report have neither. Their modules render the
  Go structs OPA encodes, key for key from the structs' JSON tags. The script stops
  when one of their keys has no range and description here.
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
LOGS_GO = "v1/plugins/logs/plugin.go"
STATUS_GO = "v1/plugins/status/plugin.go"
BUNDLE_STATUS_GO = "v1/plugins/bundle/status.go"
LOGS_STATUS_GO = "v1/plugins/logs/status/status.go"
PLUGINS_GO = "v1/plugins/plugins.go"
BUNDLE_GO = "v1/bundle/bundle.go"

LOCATION_KEYS = ("file", "col", "row", "end_col", "end_row")


def read_json(rel: str) -> Any:
    return json.loads((OPA / rel).read_text(encoding="utf-8"))


# A field of a Go struct with a JSON tag: its type and the tag's text.
GO_FIELD = re.compile(r'^\s+[A-Z]\w*\s+(?P<type>\S+)\s+`[^`]*\bjson:"(?P<tag>[^"]*)"')


def go_struct(rel: str, name: str) -> dict[str, tuple[str, bool]]:
    """Each JSON key of a Go struct, in OPA's order, with the field's Go type and
    whether the tag says `omitempty`. An exported field without a JSON tag stops the
    script, since Go would write it under the field's own name."""
    text = (OPA / rel).read_text(encoding="utf-8")
    m = re.search(rf"^type {name} struct {{\n(.*?)^}}", text, re.M | re.S)
    if not m:
        sys.exit(f"{rel} defines no struct {name}: update the converter")
    fields: dict[str, tuple[str, bool]] = {}
    for line in m.group(1).splitlines():
        if found := GO_FIELD.match(line):
            key, *options = found["tag"].split(",")
            if key != "-":
                fields[key] = (found["type"], "omitempty" in options)
        elif re.match(r"^\s+[A-Z]", line):
            sys.exit(f"{rel} {name} has a field with no JSON tag: {line.strip()}")
    return fields


def go_class(rel: str, struct: str, keys: dict[str, dict], **cls: Any) -> dict:
    """A class with an attribute per JSON key of a Go struct, in the struct's order.

    `keys` gives each key's slot. A key is required when its tag has no `omitempty`
    and its Go type cannot hold null, as a map, a slice, a pointer or an interface
    can. The script stops when the struct's keys differ from those in `keys`.
    """
    fields = go_struct(rel, struct)
    if set(fields) != set(keys):
        sys.exit(
            f"{rel} {struct} has the keys {sorted(fields)}, and the converter "
            f"describes {sorted(keys)}: update the converter"
        )
    attrs = {}
    for key, (go_type, omitempty) in fields.items():
        slot = dict(keys[key])
        nullable = go_type.startswith(("map[", "[]", "*")) or go_type in (
            "any",
            "error",
        )
        if not omitempty and not nullable:
            slot["required"] = True
        attrs[key] = slot
    return {**cls, "attributes": attrs}


def go_enum(rel: str, pattern: str, texts: dict[str, str], description: str) -> dict:
    """An enumeration of the string constants a Go file declares, matched by a pattern
    whose group is the value. The script stops when a value has no text in `texts`."""
    found = re.findall(pattern, (OPA / rel).read_text(encoding="utf-8"), re.M)
    if sorted(found) != sorted(texts):
        sys.exit(
            f"{rel} declares {sorted(found)}, and the converter describes "
            f"{sorted(texts)}: update the converter"
        )
    return {
        "description": description,
        "permissible_values": {v: {"description": texts[v]} for v in found},
    }


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


def any_json(description: str) -> dict:
    """A slot that holds any JSON value. LinkML 1.12.1's JSON Schema leaves arrays out
    of linkml:Any, so the slot also admits a list of values."""
    return {
        "description": description,
        "range": "OpaValue",
        "any_of": [{"range": "OpaValue"}, {"range": "OpaValue", "multivalued": True}],
    }


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
        "Types that more than one OPA format uses: open JSON objects and values, maps of "
        "labels and of HTTP headers, and the Rego type declarations that capabilities and "
        "plans carry for built-in functions.",
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
            "comments": [
                "LinkML 1.12.1's JSON Schema leaves arrays out of linkml:Any. A slot that "
                "may hold an array also admits a list of values, so only an array nested "
                "directly in such a list fails."
            ],
            "class_uri": "linkml:Any",
        },
        "OpaLabels": {
            "description": "Labels as text keys and text values, such as an OPA instance's "
            "`id` and `version`.",
            "extra_slots": {"range_expression": {"range": "string"}},
        },
        "OpaStringListMap": {
            "description": "An object whose every value is a list of strings, as Go writes "
            "HTTP headers and query parameters.",
            "extra_slots": {
                "range_expression": {"range": "string", "multivalued": True}
            },
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
            "key": {**any_json("The key, as a JSON value."), "required": True},
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
    schema["slots"] = {
        key: {"description": text, "slot_uri": f"openpolicyagent:{key}"}
        for key, text in PROMOTED.items()
    }
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
        "and language features an OPA version supports, and the hosts it may reach. OPA includes "
        "one per release in capabilities/, and `opa capabilities` prints it.",
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
            "description": "The future keywords the capabilities files OPA includes name.",
            "permissible_values": {k: {} for k in sorted(keywords)},
        },
        "OpaFeature": {
            "description": "The language features the capabilities files OPA includes name.",
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
        ["common"],
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
                    required=True,
                ),
                "implementations": attr(
                    "OpaImplementation",
                    "The implementations of Rego besides OPA that the catalogue tracks.",
                    alias="_implementations",
                    multivalued=True,
                    inlined=True,
                    inlined_as_list=True,
                    required=True,
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
                    "The implementation's version that added the function, or null for "
                    "an implementation that publishes no version history.",
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
                "metadata": attr(
                    None,
                    "The build metadata, the part of a version after a plus sign.",
                    alias="Metadata",
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
    ("Func", "path"): "Where the function is in the data tree, when it has a path.",
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
    # OPA's schema describes decl as opaque, which it is not here.
    classes["OpaBuiltinFunc"]["attributes"]["decl"].update(
        range="OpaFunctionType", description=FIELD_TEXT[("BuiltinFunc", "decl")]
    )
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


# The keys OPA's schema requires that the server writes only when the request has them
# (makeInput in v1/server/authorizer/authorizer.go).
AUTHZ_ABSENT = ("identity", "client_certificates", "body")


def build_authorization_input() -> dict:
    doc = read_json(AUTHZ_SCHEMA)
    schema = header(
        "authorization_input",
        "OPA authorization policy input",
        "The input document OPA's REST API gives the system.authz policy when OPA runs with "
        "--authorization=basic. It renders the keys of OPA's JSON Schema for that input, "
        "which OPA type-checks the policy against.",
        f"{BLOB}{AUTHZ_SCHEMA}",
        ["common"],
    )
    text = {
        "identity": "The caller's identity: the bearer token under --authentication=token, "
        "or the client certificate's subject under --authentication=tls.",
        "client_certificates": "The client's TLS certificates under "
        "--authentication=tls, each as Go writes an x509 certificate in JSON.",
        "method": "The HTTP method of the request, in upper case.",
        "path": "The request path, one segment per element.",
        "params": "The query parameters, each with its list of values.",
        "headers": "The request headers, each with its list of values.",
        "body": "The request body, parsed from JSON or YAML, for a POST to the default "
        "decision, v0/data, v1/data, v1/compile or v1/query.",
    }
    cls = object_class(
        doc, {}, doc["description"].replace("Schema for the", "The") + ".", None
    )
    for key, slot in cls["attributes"].items():
        slot["description"] = text[key]
        if key in AUTHZ_ABSENT:
            slot.pop("required")
    cls["attributes"]["body"] = any_json(text["body"])
    for key in ("params", "headers"):
        cls["attributes"][key]["range"] = "OpaStringListMap"
    cls["comments"] = [
        "OPA's schema requires every key and makes the body an object. The server leaves "
        "out identity, client_certificates and body when the request has none, and a body "
        "can be any JSON value. So those three are optional here, and the body takes any "
        "value."
    ]
    cls["tree_root"] = True
    schema["classes"] = {"OpaAuthorizationInput": cls}
    return schema


# ---------------------------------------------------------------- decision logs


EVENT_KEYS = {
    "labels": attr(
        "OpaLabels",
        "The labels of the OPA instance that made the decision: its `id`, its "
        "`version` and those the configuration sets.",
        inlined=True,
    ),
    "decision_id": attr(
        None, "The decision's id, which OPA also returns to the client."
    ),
    "batch_decision_id": attr(
        None, "The id that groups the decisions of one batch request."
    ),
    "trace_id": attr(
        None, "The request's trace id in W3C trace context, with tracing on."
    ),
    "span_id": attr(
        None, "The request's span id in W3C trace context, with tracing on."
    ),
    "revision": attr(
        None,
        "The revision of the bundle that made the decision, under the legacy `bundle` "
        "configuration.",
        deprecated="OPA marks the key deprecated and writes `bundles` instead.",
    ),
    "bundles": attr(
        "OpaDecisionBundle",
        "The bundles whose policy made the decision, by name.",
        multivalued=True,
        inlined=True,
    ),
    "path": attr(
        None,
        "The decision's path in the data tree, such as `http/example/authz/allow`.",
    ),
    "query": attr(None, "The ad hoc query the Query API received."),
    "input": any_json("The input of the query."),
    "result": any_json("The result the client received."),
    "intermediate_results": attr(
        "OpaObject",
        "The intermediate results the evaluation recorded, when OPA runs with the "
        "environment variable OPA_DECISIONS_INTERMEDIATE_RESULTS set.",
        inlined=True,
    ),
    "mapped_result": any_json(
        "The result of a decision made through OPA's Go SDK, as its result mapper "
        "wrote it."
    ),
    "nd_builtin_cache": attr(
        "OpaObject",
        "What each non-deterministic built-in function returned, by function and "
        "arguments, with `nd_builtin_cache` on.",
        inlined=True,
    ),
    "erased": attr(
        None, "JSON pointers to the fields a mask policy removed.", multivalued=True
    ),
    "masked": attr(
        None, "JSON pointers to the fields a mask policy replaced.", multivalued=True
    ),
    "error": any_json("The error the evaluation raised, as OPA writes it in JSON."),
    "requested_by": attr(None, "The address of the client that asked."),
    "timestamp": attr("datetime", "When OPA made the decision."),
    "metrics": attr("OpaObject", "The query's metrics, by name.", inlined=True),
    "req_id": attr(
        "integer",
        "The number OPA gave the HTTP request, which its request and response logs "
        "also carry.",
        minimum_value=0,
    ),
    "rule_labels": attr(
        "OpaObject",
        "The merged `labels` annotations of each rule the evaluation used.",
        multivalued=True,
        inlined=True,
        inlined_as_list=True,
    ),
    "request_context": attr(
        "OpaRequestContext",
        "The parts of the HTTP request the configuration asks OPA to log.",
        inlined=True,
    ),
    "custom": attr(
        "OpaObject",
        "Fields the server or a plugin adds, such as `request_metadata`, which holds the "
        "top-level keys of a Data API request body other than `input`.",
        inlined=True,
    ),
}


def build_decision_log() -> dict:
    schema = header(
        "decision_log",
        "OPA decision log event",
        "The decision log event OPA's decision logger uploads to a decision log service, "
        "one per decision, in a JSON array. It renders the Go struct logs.EventV1 key for "
        "key.",
        f"{BLOB}{LOGS_GO}",
        ["common"],
    )
    event = go_class(
        LOGS_GO,
        "EventV1",
        EVENT_KEYS,
        tree_root=True,
        description="A decision OPA made: the query or path, the input and result, the "
        "bundles and the instance behind it, and when and for whom it was made.",
    )
    bundle = go_class(
        LOGS_GO,
        "BundleInfoV1",
        {"revision": attr(None, "The bundle's revision when OPA made the decision.")},
        description="A bundle whose policy made a decision.",
    )
    bundle["attributes"] = {
        "name": attr(None, "The bundle's name.", key=True),
        **bundle["attributes"],
    }
    schema["classes"] = {
        "OpaDecisionLogEvent": event,
        "OpaDecisionBundle": bundle,
        "OpaRequestContext": go_class(
            LOGS_GO,
            "RequestContext",
            {
                "http": attr(
                    "OpaHttpRequestContext",
                    "The logged parts of the HTTP request.",
                    inlined=True,
                )
            },
            description="The parts of the request that a decision log event logs.",
        ),
        "OpaHttpRequestContext": go_class(
            LOGS_GO,
            "HTTPRequestContext",
            {
                "headers": attr(
                    "OpaStringListMap",
                    "The headers the configuration names, each with its values.",
                    inlined=True,
                )
            },
            description="The logged parts of an HTTP request.",
        ),
    }
    return schema


# ---------------------------------------------------------------- status


STATUS_KEYS = {
    "labels": attr(
        "OpaLabels",
        "The labels of the OPA instance that sends the report.",
        inlined=True,
    ),
    "bundle": attr(
        "OpaBundleStatus",
        "The status of the one bundle of the legacy `bundle` configuration.",
        inlined=True,
        deprecated="OPA marks the key deprecated and writes `bundles` instead.",
    ),
    "bundles": attr(
        "OpaBundleStatus",
        "The status of each bundle OPA downloads, by name.",
        multivalued=True,
        inlined=True,
    ),
    "discovery": attr(
        "OpaBundleStatus", "The status of the discovery bundle.", inlined=True
    ),
    "decision_logs": attr(
        "OpaDecisionLogStatus", "The status of the decision log uploads.", inlined=True
    ),
    "metrics": attr(
        "OpaObject",
        "The instance's metrics, under the name of their provider, such as `prometheus`.",
        inlined=True,
    ),
    "plugins": attr(
        "OpaPluginStatus",
        "The state of each plugin, by name.",
        multivalued=True,
        inlined=True,
    ),
}

BUNDLE_STATUS_KEYS = {
    "name": attr(None, "The bundle's name.", key=True),
    "active_revision": attr(None, "The revision of the bundle OPA last activated."),
    "last_successful_activation": attr(
        "datetime", "When OPA last activated the bundle."
    ),
    "type": attr("OpaBundleType", "The bundle's type."),
    "size": attr("integer", "The bundle's size in bytes."),
    "last_successful_download": attr(
        "datetime", "When OPA last downloaded the bundle."
    ),
    "last_successful_request": attr(
        "datetime", "When a request for the bundle last succeeded."
    ),
    "last_request": attr("datetime", "When OPA last asked for the bundle."),
    "code": attr(None, "The error code, when the last download or activation failed."),
    "message": attr(None, "What went wrong, in words."),
    "errors": attr(
        "OpaObject",
        "The parse and compile errors of the last activation.",
        multivalued=True,
        inlined=True,
        inlined_as_list=True,
    ),
    "metrics": attr(
        "OpaObject", "The metrics of the last download and activation.", inlined=True
    ),
    "http_code": attr(
        "integer", "The HTTP status code of a download the server refused."
    ),
}

LOG_STATUS_KEYS = {
    "code": attr(None, "The error code, when the last upload failed."),
    "message": attr(None, "What went wrong, in words."),
    "http_code": attr(
        "integer", "The HTTP status code of an upload the server refused."
    ),
    "metrics": attr("OpaObject", "The decision logger's metrics.", inlined=True),
}

PLUGIN_STATUS_KEYS = {
    "state": attr("OpaPluginState", "The plugin's state."),
    "message": attr(None, "More about the state, in words."),
}


PLUGIN_STATES = {
    "NOT_READY": "Not in an error state, but not yet ready for normal operation, as at "
    "start-up.",
    "OK": "Working normally.",
    "ERROR": "In an error state, and not to be taken as working.",
    "WARN": "Working, but degraded or in a state a person may need to fix.",
}

BUNDLE_TYPES = {
    "snapshot": "A whole bundle, whose files replace what OPA held under its roots.",
    "delta": "A delta bundle, whose JSON Patch operations change the data OPA holds.",
}


def build_status_report() -> dict:
    schema = header(
        "status_report",
        "OPA status report",
        "The status report OPA's status plugin sends to a status service: the state of "
        "the instance's bundles, decision log uploads and plugins. It renders the Go "
        "struct status.UpdateRequestV1 and the structs it holds key for key.",
        f"{BLOB}{STATUS_GO}",
        ["common"],
    )
    bundle_status = go_class(
        BUNDLE_STATUS_GO,
        "Status",
        BUNDLE_STATUS_KEYS,
        description="The status of a bundle: its active revision, when OPA last asked "
        "for, downloaded and activated it, and the errors of the last attempt.",
        comments=[
            "OPA writes Go's zero time, 0001-01-01T00:00:00Z, for a time that has not "
            "come yet, such as the last activation of a bundle that never activated."
        ],
    )
    plugin_status = go_class(
        PLUGINS_GO, "Status", PLUGIN_STATUS_KEYS, description="The state of a plugin."
    )
    plugin_status["attributes"] = {
        "name": attr(None, "The plugin's name.", key=True),
        **plugin_status["attributes"],
    }
    schema["classes"] = {
        "OpaStatusReport": go_class(
            STATUS_GO,
            "UpdateRequestV1",
            STATUS_KEYS,
            tree_root=True,
            description="A report on an OPA instance: the state of its bundles, its "
            "decision log uploads and its plugins, and its metrics.",
        ),
        "OpaBundleStatus": bundle_status,
        "OpaDecisionLogStatus": go_class(
            LOGS_STATUS_GO,
            "Status",
            LOG_STATUS_KEYS,
            description="The status of the decision log uploads.",
        ),
        "OpaPluginStatus": plugin_status,
    }
    schema["enums"] = {
        "OpaPluginState": go_enum(
            PLUGINS_GO,
            r'^\s+State\w+\s+State\s*=\s*"([^"]+)"',
            PLUGIN_STATES,
            "The states a plugin reports.",
        ),
        "OpaBundleType": go_enum(
            BUNDLE_GO,
            r'^\s+\w+BundleType\s*=\s*"([^"]+)"',
            BUNDLE_TYPES,
            "The types of bundle.",
        ),
    }
    return schema


def build_umbrella() -> dict:
    schema = header(
        "opa",
        "Open Policy Agent (OPA)",
        "A LinkML model of eight of the JSON formats Open Policy Agent defines: the IR plan, the "
        "bundle manifest, the authorization policy input, the capabilities document, the "
        "built-in function metadata, the version index, the decision log event and the status "
        "report. "
        "Each module renders one format and keeps OPA's keys, so the schema checks a document "
        "OPA writes as it is, with no key renamed. The lokf adapt copy renames seven keys "
        "LOKF defines with another meaning.",
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
    "decision_log": build_decision_log,
    "status_report": build_status_report,
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
    "id": "schema:identifier",
}


# OPA's keys that LOKF defines with another meaning. Each is a top-level slot in common
# with an IRI of this schema's, which a class takes through `slots` and `slot_usage`:
# OPA's documents keep the key, and `lokf adapt` renames the slot in its copy and keeps
# the IRI. An attribute would keep its name in the copy, and a composite's JSON-LD
# context would read it as LOKF's.
PROMOTED = {
    "body": "The body of an HTTP request.",
    "revision": "A bundle's revision, a string the bundle's author chooses.",
    "source": "What a plan statement reads: a local, or an operand.",
    "target": "The local a plan statement writes its result to.",
    "timestamp": "When OPA made a decision.",
    "type": "The kind of an object: of a Rego type, a plan statement, an operand or a "
    "bundle, or a type written as OPA prints types.",
    "version": "A version: an implementation's, a Wasm ABI's major number or a file's "
    "Rego version.",
}


def promote_lokf_keys(schema: dict) -> None:
    for cls in (schema.get("classes") or {}).values():
        attrs = cls.get("attributes") or {}
        for key in [k for k in attrs if k in PROMOTED]:
            cls.setdefault("slots", []).append(key)
            cls.setdefault("slot_usage", {})[key] = attrs.pop(key)
        if "attributes" in cls and not attrs:
            del cls["attributes"]


def share_lokf_iris(schema: dict) -> None:
    for cls in (schema.get("classes") or {}).values():
        for key, slot in (cls.get("attributes") or {}).items():
            if key in SHARED_IRIS and "alias" not in slot:
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
        promote_lokf_keys(schema)
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
