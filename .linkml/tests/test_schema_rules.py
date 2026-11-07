"""Compares the adapt copy's names and slot IRIs with LOKF's and the neighbours' copies'."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
TREE = ROOT.parent

# What a host may import beside this schema's adapt copy: LOKF's schema, pinned
# by the sidecar, and the adapt copies other lmodel repositories release. Each
# neighbour is the schema asset of a release, downloaded and checked against
# the release's .sha256 and its build-provenance attestation, and pinned here
# by that checksum.
COPY = TREE / ".lokf" / "schema" / "opa.yaml"
LOKF = TREE / ".lokf" / "schema" / "lokf.yaml"
NEIGHBOURS = {
    # lmodel/ai-governance-framework v0.1.1, schema-v0.1.1-ai-governance-framework.yaml
    "ai-governance-framework.yaml": "5c853b7ffe526a8610c1b98a152e3321fb8db11a63007c3419cfb18a0e5d948d",
    # lmodel/attack v0.1.1, schema-v0.1.1-attack.yaml
    "attack.yaml": "c2e436b0d8ab0e60a8d6557b3ba32894e0b0d23b866f1e0c0d608a97e9f5f08e",
    # lmodel/calm v0.1.1, schema-v0.1.1-calm.yaml
    "calm.yaml": "79e1d30f9765efdf698b98f54a3621c4701a6a74782b0f038292addccf9682a4",
    # lmodel/capec v0.1.0, schema-v0.1.0-capec.yaml
    "capec.yaml": "613164c0520384919de7d353ff87debb4e82938cec861158d151b41edd506d46",
    # lmodel/cis-controls v0.2.1, schema-v0.2.1-cis-controls.yaml
    "cis-controls.yaml": "fbb325b4e55860381293b98f3be9c5b37e12903d3d88228d0e15a761dc80dc98",
    # lmodel/collections v0.2.0, schema-v0.2.0-collections.yaml
    "collections.yaml": "d750bfbd5be7ddfe40ce26760c76fa7859cbff45cb960913427f0585639dfeb0",
    # lmodel/cve v0.1.0, schema-v0.1.0-cve.yaml
    "cve.yaml": "33e6086a81ac8e4cdc1e6143598cfcc961cbc1864ad9268773da9e863c652a73",
    # lmodel/cwe v0.1.0, schema-v0.1.0-cwe.yaml
    "cwe.yaml": "1b2bb4c1beb089f031adc8861572b98ddf0b42f0ed3c6e5c3bfbc0f767b032cd",
    # lmodel/d3fend v0.1.0, schema-v0.1.0-d3fend.yaml
    "d3fend.yaml": "517a5c8a35b916c1efe4e288151d241d2f350fef38aaec218c4ba7ebea986d08",
    # lmodel/datatype v0.1.0, schema-v0.1.0-datatype.yaml
    "datatype.yaml": "52fe21c1cd4675b851a26947b69ae9a3b5b68ead592711b23a6552866ec6f933",
    # lmodel/dpv v0.1.0, schema-v0.1.0-dpv.yaml
    "dpv.yaml": "388ca72d90615903c6d57b6d0856e71fcf77a3b07a318cf2b2bee0224930b362",
    # lmodel/fix-orchestra v0.1.0, schema-v0.1.0-fix-orchestra.yaml
    "fix-orchestra.yaml": "68574443d6a144f1e9c4f453fea67ad421bf05186cdce972c45e1ac00111f4a8",
    # lmodel/fix-protocol v0.1.0, schema-v0.1.0-fix-protocol.yaml
    "fix-protocol.yaml": "a2e7c62dbf856298b9c93c8d6eb93365690f768b0f0b00dbf17ad14384a76d02",
    # lmodel/fix-sbe v0.1.0, schema-v0.1.0-fix-sbe.yaml
    "fix-sbe.yaml": "894cc3948e8283ab09f96a27ad8cbacbd19dcd9a7d8ae46acb9f3c166d53a353",
    # lmodel/fixp v0.1.0, schema-v0.1.0-fixp.yaml
    "fixp.yaml": "d047c64cafa23b19ae55986fc5a6d79ad8e3bb660526b115ba17c65027b21f7a",
    # lmodel/gist v0.7.1, schema-v0.7.1-gist.yaml
    "gist.yaml": "f7283f1c1df4aa6b6e2803e0645c2b1cb2eab37815642a6616d8034feb26d94d",
    # lmodel/github-actions v0.5.0, schema-v0.5.0-github-actions.yaml
    "github-actions.yaml": "375794f7343936ae8c555e8c060c2790346661e7d81fa84d15a761fd5a329969",
    # lmodel/in-toto v0.3.0, schema-v0.3.0-in-toto.yaml
    "in-toto.yaml": "b1d15be557adfbcd538ab75ec9d43f558027d4bcbd150d72d370e83c9602f25b",
    # lmodel/iso22989 v0.1.0, schema-v0.1.0-iso22989.yaml
    "iso22989.yaml": "6df8cd85c1ecf049a961bec2449ddff9043b2bae6ec0ba6ce1491cf52411e1d3",
    # lmodel/iso27001 v0.1.0, schema-v0.1.0-iso27001.yaml
    "iso27001.yaml": "f5ca519043cd994c41f286f84ebc2ea510121bd2129d83c017f73a3d24ee2fe1",
    # lmodel/iso29100 v0.1.0, schema-v0.1.0-iso29100.yaml
    "iso29100.yaml": "2b773c6c71a7bf72779fc92e9974f3c2b02c414fdc36c2185c4cb99f54f40bd2",
    # lmodel/iso42001 v0.1.0, schema-v0.1.0-iso42001.yaml
    "iso42001.yaml": "1ddebd365a181e2bee5d6c9d837e92924b5788eaa82cd8034fa50e9b7d537088",
    # lmodel/kev-catalog v0.1.1, schema-v0.1.1-kev-catalog.yaml
    "kev-catalog.yaml": "76bdff7d02cc34ac6a14314692e316b005649a34f442eaf54c2846b1dac5396c",
    # lmodel/nist-ai-100-1 v0.1.0, schema-v0.1.0-nist-ai-100-1.yaml
    "nist-ai-100-1.yaml": "a9498259b8ff781fa3c24e668f5258146fe1fc4cd6e08c2aac394cb63b76a3c9",
    # lmodel/nist-ai-600-1 v0.1.0, schema-v0.1.0-nist-ai-600-1.yaml
    "nist-ai-600-1.yaml": "4fffc03c0db437256b45ffa6814c54053ffeae06a933b4d4550f94c9ff0494f4",
    # lmodel/nist-ai-rmf v0.1.0, schema-v0.1.0-nist-ai-rmf.yaml
    "nist-ai-rmf.yaml": "752e6091936a877fb33495ead3d867b98bc4225b6125bc3337ec169bb493684f",
    # lmodel/nist-csf-v2 v0.2.0, schema-v0.2.0-nist-csf-v2.yaml
    "nist-csf-v2.yaml": "f5819af21a3dbd4bd758987f166831df35aab9942a650156f6873d10d01a0dcc",
    # lmodel/nist-nvd v0.1.0, schema-v0.1.0-nist-nvd.yaml
    "nist-nvd.yaml": "69dc8a9b34cc6646cf44515c121c8924c4e07232a9699e31065fb8930ed8be40",
    # lmodel/nist-sp-800-171 v0.1.0, schema-v0.1.0-nist-sp-800-171.yaml
    "nist-sp-800-171.yaml": "d204efa6653692da665f8604a8fb8bf445f04b37f41460a5ce2853a014b2982f",
    # lmodel/nist-sp-800-218 v0.1.1, schema-v0.1.1-nist-sp-800-218.yaml
    "nist-sp-800-218.yaml": "479824cdd95e52226a35ff3a471b7ce93239635ccd5db7ac72a8143cdd1d8495",
    # lmodel/nist-sp-800-53 v0.1.0, schema-v0.1.0-nist-sp-800-53.yaml
    "nist-sp-800-53.yaml": "d32a989b5b855281cb45d707bf59cf52b125f05a09c54930e2b4d45c174c0d99",
    # lmodel/ocsf v0.1.0, schema-v0.1.0-ocsf.yaml
    "ocsf.yaml": "b4e033eff09dc3684142308dd70d98926f30a853eb8906f0ad79f6cf1839167d",
    # lmodel/oscal v0.1.2, schema-v0.1.2-oscal.yaml
    "oscal.yaml": "4eb56d7d1106463ed0a2255a29af14b8d619741acc29863d1e86eb3f8923c710",
    # lmodel/slsa v0.10.0, schema-v0.10.0-slsa.yaml
    "slsa.yaml": "9eeb68decc918565886794fe4eb6e32e1fee0620688cc699961c227242a2f4c2",
    # lmodel/spdx v0.1.1, schema-v0.1.1-spdx.yaml
    "spdx.yaml": "3411cf5d19b1955f0362988c542984e4c817417c7b7b7892647aba1adf1ddd4a",
    # lmodel/stix v0.1.0, schema-v0.1.0-stix.yaml
    "stix.yaml": "3837d097c0cd48e0d2a98d118003c099d1290333f5b973aee85a7017bae344c9",
    # lmodel/uco v0.3.0, schema-v0.3.0-uco.yaml
    "uco.yaml": "78bc3a266fa463ba380da7290adcbdfb1b8e1b7cef1ceb992bf8b1bed9b7b758",
    # lmodel/void v0.1.0, schema-v0.1.0-void.yaml
    "void.yaml": "8c21583f49b860e38cc2ee4312a9ef5242300989915bda6fa7a2dd1d0b252051",
}
NEIGHBOUR_DIR = ROOT / "tests" / "neighbours"
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# Keys the copy shares with a neighbour. LinkML keeps one namespace, and the
# JSON-LD context gives each key one IRI across a composite, whether it is a
# slot or an attribute on either side, so a shared key projects under one
# vocabulary's IRI. Each key below is OPA's own, so a new overlap fails the test.
SHARED_WITH_NEIGHBOURS = {name: set() for name in NEIGHBOURS} | {
    "ai-governance-framework.yaml": {"label"},
    "attack.yaml": {"key", "labels", "path", "result", "size", "value"},
    "calm.yaml": {"metadata", "value"},
    "cve.yaml": {"metrics", "repo", "state", "value"},
    "d3fend.yaml": {"available", "blocks", "deprecated", "label"},
    "datatype.yaml": {"value"},
    "dpv.yaml": {"value"},
    "in-toto.yaml": {"annotations", "value"},
    "nist-nvd.yaml": {"deprecated", "id", "metrics", "repo", "value"},
    "ocsf.yaml": {
        "args",
        "categories",
        "code",
        "error",
        "file",
        "files",
        "labels",
        "location",
        "message",
        "metadata",
        "metrics",
        "module",
        "path",
        "query",
        "relation",
        "size",
        "state",
        "value",
    },
    "oscal.yaml": {"custom", "label", "metadata", "method", "params", "state", "value"},
    "slsa.yaml": {"annotations", "value"},
    "spdx.yaml": {"key", "value"},
    "stix.yaml": {"key", "labels", "path", "result", "size", "value"},
    "uco.yaml": {
        "categories",
        "error",
        "key",
        "labels",
        "location",
        "object",
        "path",
        "query",
        "result",
        "size",
        "state",
        "strings",
        "value",
    },
    "void.yaml": {"label"},
}

# The classes `just lokf-adapt` re-roots on Concept. The README lists them for the
# plugins' Known LOKF types setting. None has a subclass.
ROOTS = {"OpaBuiltin", "OpaCapabilities", "OpaManifest", "OpaPolicy"}
KNOWN_TYPES = ROOTS

MAPPING_KEYS = (
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)


def _names(path):
    """Each kind of element a schema file declares, and every slot and
    attribute key with the IRI it expands to. A slot's key is its alias where it
    has one, with a hyphen read as an underscore, as the JSON-LD context and
    JSON Schema generators write it."""
    doc = yaml.safe_load(path.read_text())
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            key = ((slot or {}).get("alias") or name).replace("-", "_")
            slots.setdefault(key, set()).add(expand(uri))
    return elements, slots


def _mappings(node):
    """Every mapping value anywhere in a parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in MAPPING_KEYS:
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item)


def test_neighbours_are_the_released_assets():
    """Each neighbour copy is byte for byte the asset its release published."""
    assert {p.name for p in NEIGHBOUR_DIR.iterdir()} == set(NEIGHBOURS)
    for name, sha256 in NEIGHBOURS.items():
        digest = hashlib.sha256((NEIGHBOUR_DIR / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and a slot
    name the two share carries LOKF's IRI. OPA's keys that LOKF defines with
    another meaning (body, revision, source, target, timestamp, type and
    version) are top-level slots in the source, which the copy renames with the
    prefix."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(LOKF)
    for kind in ELEMENT_KINDS:
        assert not elements[kind] & their_elements[kind], kind
    for name in slots.keys() & their_slots.keys():
        assert slots[name] == their_slots[name], name
    keys = ("body", "revision", "source", "target", "timestamp", "type", "version")
    for key in keys:
        assert f"openpolicyagent_{key}" in slots, key


def test_names_apart_from_neighbours():
    """A class, enum, type or subset name is the copy's alone, and the only
    keys it shares with a neighbour are the listed ones."""
    elements, slots = _names(COPY)
    for name in NEIGHBOURS:
        their_elements, their_slots = _names(NEIGHBOUR_DIR / name)
        for kind in ELEMENT_KINDS:
            assert not elements[kind] & their_elements[kind], (name, kind)
        assert slots.keys() & their_slots.keys() == SHARED_WITH_NEIGHBOURS[name], name


def test_copy_roots_the_concept_classes():
    """The copy re-roots exactly the listed classes on Concept and imports nothing
    but the LinkML types and LOKF."""
    doc = yaml.safe_load(COPY.read_text())
    rooted = {
        name for name, cls in doc["classes"].items() if cls.get("is_a") == "Concept"
    }
    assert rooted == ROOTS
    assert doc["imports"] == ["linkml:types", "lokf"]
    concrete = {
        name
        for name, cls in doc["classes"].items()
        if not cls.get("abstract") and (name in ROOTS or cls.get("is_a") in ROOTS)
    }
    assert concrete == KNOWN_TYPES


def test_the_readme_lists_the_known_types():
    """README.md lists the classes for the plugins' setting."""
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert ", ".join(sorted(KNOWN_TYPES)) in text


def test_mappings_use_a_bound_prefix():
    """Every mapping in the copy is a CURIE whose prefix the copy binds. A full
    address that no prefix covers makes every `lokf convert --schema` over the
    copy warn that it has no namespace."""
    doc = yaml.safe_load(COPY.read_text())
    prefixes = doc.get("prefixes") or {}
    mappings = list(_mappings(doc))
    assert mappings
    for mapping in mappings:
        prefix, sep, _ = mapping.partition(":")
        assert sep and prefix in prefixes, mapping


def test_every_mapping_names_a_definition_in_opas_files():
    """The copy maps classes only to the definition in OPA's JSON Schema they render,
    and each resolves in OPA's file in this tree."""
    import json

    files = {
        "opa_plan": "v1/ir/plan.schema.json",
        "opa_manifest": "v1/bundle/manifest.schema.json",
    }
    doc = yaml.safe_load(COPY.read_text())
    for mapping in _mappings(doc):
        prefix, _, name = mapping.partition(":")
        published = json.loads((TREE / files[prefix]).read_text(encoding="utf-8"))
        assert doc["prefixes"][prefix] == published["$id"] + "#/$defs/"
        assert name in published["$defs"], mapping
