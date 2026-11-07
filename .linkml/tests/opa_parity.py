"""Verdicts of the schema and of OPA's own JSON Schemas on one document.

The schema's verdict comes from the JSON Schema LinkML generates from it, with each
range over an abstract class admitting the class's subclasses, as linkml-validate
builds it. OPA's verdict comes from the JSON Schema OPA publishes for the format.
"""

import json
from functools import lru_cache
from pathlib import Path

import jsonschema
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

ROOT = Path(__file__).parent.parent
TREE = ROOT.parent
SCHEMA = ROOT / "src" / "opa" / "schema" / "opa.yaml"

# OPA's JSON Schemas, by the mapping prefix the schema gives each.
PUBLISHED = {
    "opa_plan": "v1/ir/plan.schema.json",
    "opa_manifest": "v1/bundle/manifest.schema.json",
}
AUTHZ = "v1/schemas/authorizationPolicy.json"


@lru_cache(maxsize=1)
def generated() -> dict:
    gen = JsonSchemaGenerator(
        str(SCHEMA), mergeimports=True, include_range_class_descendants=True
    )
    return json.loads(gen.serialize())


@lru_cache(maxsize=1)
def classes() -> dict:
    """Each class of the merged schema, as the YAML of its module gives it."""
    found = {}
    for path in sorted(SCHEMA.parent.glob("*.yaml")):
        found |= yaml.safe_load(path.read_text(encoding="utf-8")).get("classes") or {}
    return found


def subclasses(name: str) -> list[str]:
    """The concrete classes under an abstract one."""
    found = []
    for child, cls in sorted(classes().items()):
        if cls.get("is_a") == name:
            found += subclasses(child) if cls.get("abstract") else [child]
    return found


@lru_cache(maxsize=None)
def published(rel: str) -> dict:
    return json.loads((TREE / rel).read_text(encoding="utf-8"))


@lru_cache(maxsize=None)
def _validator(kind: str, target: str):
    if kind == "generated":
        doc = generated()
        schema = {"$schema": doc["$schema"], "$defs": doc["$defs"]}
        if classes()[target].get("abstract"):
            # An abstract class admits its subclasses, as a range over it does.
            schema["anyOf"] = [
                {"$ref": f"#/$defs/{name}"} for name in subclasses(target)
            ]
        else:
            schema["$ref"] = f"#/$defs/{target}"
    else:
        rel, _, name = target.partition("#")
        doc = published(rel)
        schema = dict(doc)
        if name:
            schema.pop("$id", None)
            schema["$ref"] = f"#/$defs/{name}"
    return jsonschema.validators.validator_for(schema)(schema)


def verdict(kind: str, target: str, data) -> bool:
    """Whether the schema (`generated`, a class name) or OPA (`published`, a file and
    an optional `#definition`) accepts the document."""
    return _validator(kind, target).is_valid(data)


def errors(kind: str, target: str, data) -> list[str]:
    return [e.message for e in _validator(kind, target).iter_errors(data)]
