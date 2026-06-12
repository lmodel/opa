# Auto generated from opa.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-06-12T23:26:43
# Schema: opa
#
# id: https://w3id.org/lmodel/opa
# description: Umbrella LinkML schema for Open Policy Agent (OPA) and the Rego policy language. Imports per-source submodules generated from upstream OPA artifacts (capabilities, built-in metadata, version index, sample authorization input, bundle manifest, and IR plan).
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.11.0"
version = "0.1.0"

# Namespaces
D3FEND = CurieNamespace('d3fend', 'https://w3id.org/lmodel/d3fend/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DPV = CurieNamespace('dpv', 'https://w3id.org/lmodel/dpv/')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OPENPOLICYAGENT = CurieNamespace('openpolicyagent', 'https://w3id.org/lmodel/opa/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SLSA = CurieNamespace('slsa', 'https://w3id.org/lmodel/slsa/')
DEFAULT_ = OPENPOLICYAGENT


# Types

# Class references
class BuiltinName(extended_str):
    pass


class BuiltinCategoryGroupName(extended_str):
    pass


class BuiltinMetadataName(extended_str):
    pass


class ElementVersionName(extended_str):
    pass


class FileRegoVersionPath(extended_str):
    pass


Any = Any

@dataclass(repr=False)
class Capabilities(YAMLRoot):
    """
    Top-level capabilities document published by an OPA build. Lists every built-in function the runtime supports
    along with Wasm ABI compatibility, future keywords and feature flags.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Capabilities"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Capabilities"
    class_name: ClassVar[str] = "Capabilities"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Capabilities

    builtins: Optional[Union[dict[Union[str, BuiltinName], Union[dict, "Builtin"]], list[Union[dict, "Builtin"]]]] = empty_dict()
    future_keywords: Optional[Union[Union[str, "FutureKeyword"], list[Union[str, "FutureKeyword"]]]] = empty_list()
    wasm_abi_versions: Optional[Union[Union[dict, "WasmABIVersion"], list[Union[dict, "WasmABIVersion"]]]] = empty_list()
    features: Optional[Union[Union[str, "FeatureName"], list[Union[str, "FeatureName"]]]] = empty_list()
    allow_net: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="builtins", slot_type=Builtin, key_name="name", keyed=True)

        if not isinstance(self.future_keywords, list):
            self.future_keywords = [self.future_keywords] if self.future_keywords is not None else []
        self.future_keywords = [v if isinstance(v, FutureKeyword) else FutureKeyword(v) for v in self.future_keywords]

        self._normalize_inlined_as_list(slot_name="wasm_abi_versions", slot_type=WasmABIVersion, key_name="version", keyed=False)

        if not isinstance(self.features, list):
            self.features = [self.features] if self.features is not None else []
        self.features = [v if isinstance(v, FeatureName) else FeatureName(v) for v in self.features]

        if not isinstance(self.allow_net, list):
            self.allow_net = [self.allow_net] if self.allow_net is not None else []
        self.allow_net = [v if isinstance(v, str) else str(v) for v in self.allow_net]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Builtin(YAMLRoot):
    """
    A Rego built-in function exposed by the OPA runtime.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Builtin"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Builtin"
    class_name: ClassVar[str] = "Builtin"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Builtin

    name: Union[str, BuiltinName] = None
    decl: Union[dict, "BuiltinDecl"] = None
    infix: Optional[str] = None
    deprecated: Optional[Union[bool, Bool]] = None
    nondeterministic: Optional[Union[bool, Bool]] = None
    relation: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BuiltinName):
            self.name = BuiltinName(self.name)

        if self._is_empty(self.decl):
            self.MissingRequiredField("decl")
        if not isinstance(self.decl, BuiltinDecl):
            self.decl = BuiltinDecl(**as_dict(self.decl))

        if self.infix is not None and not isinstance(self.infix, str):
            self.infix = str(self.infix)

        if self.deprecated is not None and not isinstance(self.deprecated, Bool):
            self.deprecated = Bool(self.deprecated)

        if self.nondeterministic is not None and not isinstance(self.nondeterministic, Bool):
            self.nondeterministic = Bool(self.nondeterministic)

        if self.relation is not None and not isinstance(self.relation, Bool):
            self.relation = Bool(self.relation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuiltinDecl(YAMLRoot):
    """
    Type declaration of a built-in: function signature and return type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["BuiltinDecl"]
    class_class_curie: ClassVar[str] = "openpolicyagent:BuiltinDecl"
    class_name: ClassVar[str] = "BuiltinDecl"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.BuiltinDecl

    type: str = None
    args: Optional[Union[Union[dict, "TypeDecl"], list[Union[dict, "TypeDecl"]]]] = empty_list()
    result: Optional[Union[dict, "TypeDecl"]] = None
    variadic: Optional[Union[dict, "TypeDecl"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.args, list):
            self.args = [self.args] if self.args is not None else []
        self.args = [v if isinstance(v, TypeDecl) else TypeDecl(**as_dict(v)) for v in self.args]

        if self.result is not None and not isinstance(self.result, TypeDecl):
            self.result = TypeDecl(**as_dict(self.result))

        if self.variadic is not None and not isinstance(self.variadic, TypeDecl):
            self.variadic = TypeDecl(**as_dict(self.variadic))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TypeDecl(YAMLRoot):
    """
    Recursive type expression used throughout Capabilities declarations.

    All slots are optional because TypeDecl doubles as the structural envelope
    for the various heterogeneous shapes the source JSON uses:
    * ``string|number|boolean|null|function`` -- atomic; only ``type`` is set.
    * ``any`` -- ``of`` is a list of alternative TypeDecls.
    * ``set`` -- ``of`` holds the (single) element TypeDecl.
    * ``array`` -- ``dynamic`` is the homogeneous element TypeDecl, or
    ``static`` is an ordered list describing a fixed-length tuple.
    * ``object`` -- ``static`` lists named property pairs (TypeDecls with
    ``key`` and ``value`` populated); ``dynamic`` is a TypeDecl whose
    ``key``/``value`` describe additional property typing.
    * Inside an ``object``'s ``dynamic`` value, the TypeDecl has only
    ``key`` and ``value`` populated -- ``type`` is absent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["TypeDecl"]
    class_class_curie: ClassVar[str] = "openpolicyagent:TypeDecl"
    class_name: ClassVar[str] = "TypeDecl"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.TypeDecl

    type: Optional[Union[str, "BuiltinTypeKind"]] = None
    of: Optional[Union[Union[dict, "TypeDecl"], list[Union[dict, "TypeDecl"]]]] = empty_list()
    dynamic: Optional[Union[dict, "TypeDecl"]] = None
    static: Optional[Union[Union[dict, "TypeDecl"], list[Union[dict, "TypeDecl"]]]] = empty_list()
    key: Optional[Union[dict, Any]] = None
    value: Optional[Union[dict, "TypeDecl"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type is not None and not isinstance(self.type, BuiltinTypeKind):
            self.type = BuiltinTypeKind(self.type)

        if not isinstance(self.of, list):
            self.of = [self.of] if self.of is not None else []
        self.of = [v if isinstance(v, TypeDecl) else TypeDecl(**as_dict(v)) for v in self.of]

        if self.dynamic is not None and not isinstance(self.dynamic, TypeDecl):
            self.dynamic = TypeDecl(**as_dict(self.dynamic))

        if not isinstance(self.static, list):
            self.static = [self.static] if self.static is not None else []
        self.static = [v if isinstance(v, TypeDecl) else TypeDecl(**as_dict(v)) for v in self.static]

        if self.value is not None and not isinstance(self.value, TypeDecl):
            self.value = TypeDecl(**as_dict(self.value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WasmABIVersion(YAMLRoot):
    """
    A supported Wasm ABI version pair.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["WasmABIVersion"]
    class_class_curie: ClassVar[str] = "openpolicyagent:WasmABIVersion"
    class_name: ClassVar[str] = "WasmABIVersion"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.WasmABIVersion

    version: int = None
    minor_version: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, int):
            self.version = int(self.version)

        if self._is_empty(self.minor_version):
            self.MissingRequiredField("minor_version")
        if not isinstance(self.minor_version, int):
            self.minor_version = int(self.minor_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuiltinMetadataCatalog(YAMLRoot):
    """
    Wrapper class for the contents of ``builtin_metadata.json``. The source document is a flat map keyed by built-in
    name plus a ``_categories`` map; the generator script reshapes it so ``categories`` and ``builtins`` are explicit,
    inlined-as-dict slots on this wrapper.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["BuiltinMetadataCatalog"]
    class_class_curie: ClassVar[str] = "openpolicyagent:BuiltinMetadataCatalog"
    class_name: ClassVar[str] = "BuiltinMetadataCatalog"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.BuiltinMetadataCatalog

    categories: Optional[Union[dict[Union[str, BuiltinCategoryGroupName], Union[dict, "BuiltinCategoryGroup"]], list[Union[dict, "BuiltinCategoryGroup"]]]] = empty_dict()
    builtins: Optional[Union[dict[Union[str, BuiltinMetadataName], Union[dict, "BuiltinMetadata"]], list[Union[dict, "BuiltinMetadata"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="categories", slot_type=BuiltinCategoryGroup, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="builtins", slot_type=BuiltinMetadata, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuiltinCategoryGroup(YAMLRoot):
    """
    Membership of built-ins in a documentation category.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["BuiltinCategoryGroup"]
    class_class_curie: ClassVar[str] = "openpolicyagent:BuiltinCategoryGroup"
    class_name: ClassVar[str] = "BuiltinCategoryGroup"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.BuiltinCategoryGroup

    name: Union[str, BuiltinCategoryGroupName] = None
    builtins: Union[str, list[str]] = None
    category: Optional[Union[str, "BuiltinCategory"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BuiltinCategoryGroupName):
            self.name = BuiltinCategoryGroupName(self.name)

        if self._is_empty(self.builtins):
            self.MissingRequiredField("builtins")
        if not isinstance(self.builtins, list):
            self.builtins = [self.builtins] if self.builtins is not None else []
        self.builtins = [v if isinstance(v, str) else str(v) for v in self.builtins]

        if self.category is not None and not isinstance(self.category, BuiltinCategory):
            self.category = BuiltinCategory(self.category)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuiltinMetadata(YAMLRoot):
    """
    Human-readable metadata for a single Rego built-in function.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["BuiltinMetadata"]
    class_class_curie: ClassVar[str] = "openpolicyagent:BuiltinMetadata"
    class_name: ClassVar[str] = "BuiltinMetadata"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.BuiltinMetadata

    name: Union[str, BuiltinMetadataName] = None
    description: Optional[str] = None
    introduced: Optional[str] = None
    available: Optional[Union[str, list[str]]] = empty_list()
    wasm: Optional[Union[bool, Bool]] = None
    infix: Optional[str] = None
    deprecated: Optional[Union[bool, Bool]] = None
    relation: Optional[Union[bool, Bool]] = None
    args: Optional[Union[Union[dict, "BuiltinArg"], list[Union[dict, "BuiltinArg"]]]] = empty_list()
    result: Optional[Union[dict, "BuiltinResult"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BuiltinMetadataName):
            self.name = BuiltinMetadataName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.introduced is not None and not isinstance(self.introduced, str):
            self.introduced = str(self.introduced)

        if not isinstance(self.available, list):
            self.available = [self.available] if self.available is not None else []
        self.available = [v if isinstance(v, str) else str(v) for v in self.available]

        if self.wasm is not None and not isinstance(self.wasm, Bool):
            self.wasm = Bool(self.wasm)

        if self.infix is not None and not isinstance(self.infix, str):
            self.infix = str(self.infix)

        if self.deprecated is not None and not isinstance(self.deprecated, Bool):
            self.deprecated = Bool(self.deprecated)

        if self.relation is not None and not isinstance(self.relation, Bool):
            self.relation = Bool(self.relation)

        if not isinstance(self.args, list):
            self.args = [self.args] if self.args is not None else []
        self.args = [v if isinstance(v, BuiltinArg) else BuiltinArg(**as_dict(v)) for v in self.args]

        if self.result is not None and not isinstance(self.result, BuiltinResult):
            self.result = BuiltinResult(**as_dict(self.result))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuiltinArg(YAMLRoot):
    """
    Documentation for one positional argument of a built-in.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["BuiltinArg"]
    class_class_curie: ClassVar[str] = "openpolicyagent:BuiltinArg"
    class_name: ClassVar[str] = "BuiltinArg"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.BuiltinArg

    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuiltinResult(YAMLRoot):
    """
    Documentation for the value returned by a built-in.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["BuiltinResult"]
    class_class_curie: ClassVar[str] = "openpolicyagent:BuiltinResult"
    class_name: ClassVar[str] = "BuiltinResult"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.BuiltinResult

    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VersionIndex(YAMLRoot):
    """
    Mapping from language-element names to the OPA semantic version that first introduced them. Grouped into
    built-ins, future-keywords, and features.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["VersionIndex"]
    class_class_curie: ClassVar[str] = "openpolicyagent:VersionIndex"
    class_name: ClassVar[str] = "VersionIndex"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.VersionIndex

    builtins: Optional[Union[dict[Union[str, ElementVersionName], Union[dict, "ElementVersion"]], list[Union[dict, "ElementVersion"]]]] = empty_dict()
    features: Optional[Union[dict[Union[str, ElementVersionName], Union[dict, "ElementVersion"]], list[Union[dict, "ElementVersion"]]]] = empty_dict()
    keywords: Optional[Union[dict[Union[str, ElementVersionName], Union[dict, "ElementVersion"]], list[Union[dict, "ElementVersion"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="builtins", slot_type=ElementVersion, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="features", slot_type=ElementVersion, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="keywords", slot_type=ElementVersion, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElementVersion(YAMLRoot):
    """
    Semantic version triple identifying when an element was introduced.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["ElementVersion"]
    class_class_curie: ClassVar[str] = "openpolicyagent:ElementVersion"
    class_name: ClassVar[str] = "ElementVersion"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.ElementVersion

    name: Union[str, ElementVersionName] = None
    major: int = None
    minor: int = None
    patch: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ElementVersionName):
            self.name = ElementVersionName(self.name)

        if self._is_empty(self.major):
            self.MissingRequiredField("major")
        if not isinstance(self.major, int):
            self.major = int(self.major)

        if self._is_empty(self.minor):
            self.MissingRequiredField("minor")
        if not isinstance(self.minor, int):
            self.minor = int(self.minor)

        if self._is_empty(self.patch):
            self.MissingRequiredField("patch")
        if not isinstance(self.patch, int):
            self.patch = int(self.patch)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuthorizationInput(YAMLRoot):
    """
    Input document the example HTTP API Authorization policy receives. Mirrors the OPA-provided JSON Schema at
    ``v1/schemas/authorizationPolicy.json``.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["AuthorizationInput"]
    class_class_curie: ClassVar[str] = "openpolicyagent:AuthorizationInput"
    class_name: ClassVar[str] = "AuthorizationInput"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.AuthorizationInput

    identity: str = None
    client_certificates: Union[Union[dict, Any], list[Union[dict, Any]]] = None
    method: str = None
    path: Union[str, list[str]] = None
    params: Union[dict, Any] = None
    headers: Union[dict, Any] = None
    body: Union[dict, Any] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identity):
            self.MissingRequiredField("identity")
        if not isinstance(self.identity, str):
            self.identity = str(self.identity)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.path):
            self.MissingRequiredField("path")
        if not isinstance(self.path, list):
            self.path = [self.path] if self.path is not None else []
        self.path = [v if isinstance(v, str) else str(v) for v in self.path]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Manifest(YAMLRoot):
    """
    ``Manifest`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Manifest"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Manifest"
    class_name: ClassVar[str] = "Manifest"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Manifest

    revision: str = None
    file_rego_versions: Optional[Union[dict[Union[str, FileRegoVersionPath], Union[dict, "FileRegoVersion"]], list[Union[dict, "FileRegoVersion"]]]] = empty_dict()
    metadata: Optional[Union[dict, Any]] = None
    rego_version: Optional[int] = None
    roots: Optional[Union[str, list[str]]] = empty_list()
    wasm: Optional[Union[Union[dict, "WasmResolver"], list[Union[dict, "WasmResolver"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.revision):
            self.MissingRequiredField("revision")
        if not isinstance(self.revision, str):
            self.revision = str(self.revision)

        self._normalize_inlined_as_list(slot_name="file_rego_versions", slot_type=FileRegoVersion, key_name="path", keyed=True)

        if self.rego_version is not None and not isinstance(self.rego_version, int):
            self.rego_version = int(self.rego_version)

        if not isinstance(self.roots, list):
            self.roots = [self.roots] if self.roots is not None else []
        self.roots = [v if isinstance(v, str) else str(v) for v in self.roots]

        if not isinstance(self.wasm, list):
            self.wasm = [self.wasm] if self.wasm is not None else []
        self.wasm = [v if isinstance(v, WasmResolver) else WasmResolver(**as_dict(v)) for v in self.wasm]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WasmResolver(YAMLRoot):
    """
    ``WasmResolver`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["WasmResolver"]
    class_class_curie: ClassVar[str] = "openpolicyagent:WasmResolver"
    class_name: ClassVar[str] = "WasmResolver"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.WasmResolver

    annotations: Optional[Union[Union[dict, Any], list[Union[dict, Any]]]] = empty_list()
    entrypoint: Optional[str] = None
    module: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.entrypoint is not None and not isinstance(self.entrypoint, str):
            self.entrypoint = str(self.entrypoint)

        if self.module is not None and not isinstance(self.module, str):
            self.module = str(self.module)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FileRegoVersion(YAMLRoot):
    """
    Typed override record for ``Manifest.file_rego_versions``. Provides stronger validation than a free-form map while
    keeping the same semantics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["FileRegoVersion"]
    class_class_curie: ClassVar[str] = "openpolicyagent:FileRegoVersion"
    class_name: ClassVar[str] = "FileRegoVersion"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.FileRegoVersion

    path: Union[str, FileRegoVersionPath] = None
    version: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.path):
            self.MissingRequiredField("path")
        if not isinstance(self.path, FileRegoVersionPath):
            self.path = FileRegoVersionPath(self.path)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, int):
            self.version = int(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ArrayAppendStmt(YAMLRoot):
    """
    ``ArrayAppendStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["ArrayAppendStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:ArrayAppendStmt"
    class_name: ClassVar[str] = "ArrayAppendStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.ArrayAppendStmt

    col: int = None
    file: int = None
    row: int = None
    array: int = None
    value: Union[dict, "Operand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.array):
            self.MissingRequiredField("array")
        if not isinstance(self.array, int):
            self.array = int(self.array)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Operand):
            self.value = Operand(**as_dict(self.value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssignIntStmt(YAMLRoot):
    """
    ``AssignIntStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["AssignIntStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:AssignIntStmt"
    class_name: ClassVar[str] = "AssignIntStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.AssignIntStmt

    col: int = None
    file: int = None
    row: int = None
    target: int = None
    value: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssignVarOnceStmt(YAMLRoot):
    """
    ``AssignVarOnceStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["AssignVarOnceStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:AssignVarOnceStmt"
    class_name: ClassVar[str] = "AssignVarOnceStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.AssignVarOnceStmt

    col: int = None
    file: int = None
    row: int = None
    source: Union[dict, "Operand"] = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, Operand):
            self.source = Operand(**as_dict(self.source))

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssignVarStmt(YAMLRoot):
    """
    ``AssignVarStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["AssignVarStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:AssignVarStmt"
    class_name: ClassVar[str] = "AssignVarStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.AssignVarStmt

    col: int = None
    file: int = None
    row: int = None
    source: Union[dict, "Operand"] = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, Operand):
            self.source = Operand(**as_dict(self.source))

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Block(YAMLRoot):
    """
    ``Block`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Block"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Block"
    class_name: ClassVar[str] = "Block"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Block

    stmts: Union[Union[dict, "Stmt"], list[Union[dict, "Stmt"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.stmts):
            self.MissingRequiredField("stmts")
        self._normalize_inlined_as_list(slot_name="stmts", slot_type=Stmt, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BlockStmt(YAMLRoot):
    """
    ``BlockStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["BlockStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:BlockStmt"
    class_name: ClassVar[str] = "BlockStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.BlockStmt

    col: int = None
    file: int = None
    row: int = None
    blocks: Union[Union[dict, Block], list[Union[dict, Block]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.blocks):
            self.MissingRequiredField("blocks")
        if not isinstance(self.blocks, list):
            self.blocks = [self.blocks] if self.blocks is not None else []
        self.blocks = [v if isinstance(v, Block) else Block(**as_dict(v)) for v in self.blocks]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BreakStmt(YAMLRoot):
    """
    ``BreakStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["BreakStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:BreakStmt"
    class_name: ClassVar[str] = "BreakStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.BreakStmt

    col: int = None
    file: int = None
    row: int = None
    index: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BuiltinFunc(YAMLRoot):
    """
    ``BuiltinFunc`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["BuiltinFunc"]
    class_class_curie: ClassVar[str] = "openpolicyagent:BuiltinFunc"
    class_name: ClassVar[str] = "BuiltinFunc"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.BuiltinFunc

    decl: Union[dict, Any] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CallDynamicStmt(YAMLRoot):
    """
    ``CallDynamicStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["CallDynamicStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:CallDynamicStmt"
    class_name: ClassVar[str] = "CallDynamicStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.CallDynamicStmt

    col: int = None
    file: int = None
    row: int = None
    args: Union[int, list[int]] = None
    path: Union[Union[dict, "Operand"], list[Union[dict, "Operand"]]] = None
    result: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.args):
            self.MissingRequiredField("args")
        if not isinstance(self.args, list):
            self.args = [self.args] if self.args is not None else []
        self.args = [v if isinstance(v, int) else int(v) for v in self.args]

        if self._is_empty(self.path):
            self.MissingRequiredField("path")
        self._normalize_inlined_as_list(slot_name="path", slot_type=Operand, key_name="type", keyed=False)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, int):
            self.result = int(self.result)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CallStmt(YAMLRoot):
    """
    ``CallStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["CallStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:CallStmt"
    class_name: ClassVar[str] = "CallStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.CallStmt

    col: int = None
    file: int = None
    row: int = None
    args: Union[Union[dict, "Operand"], list[Union[dict, "Operand"]]] = None
    func: str = None
    result: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.args):
            self.MissingRequiredField("args")
        self._normalize_inlined_as_list(slot_name="args", slot_type=Operand, key_name="type", keyed=False)

        if self._is_empty(self.func):
            self.MissingRequiredField("func")
        if not isinstance(self.func, str):
            self.func = str(self.func)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, int):
            self.result = int(self.result)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DotStmt(YAMLRoot):
    """
    ``DotStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["DotStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:DotStmt"
    class_name: ClassVar[str] = "DotStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.DotStmt

    col: int = None
    file: int = None
    row: int = None
    key: Union[dict, "Operand"] = None
    source: Union[dict, "Operand"] = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, Operand):
            self.key = Operand(**as_dict(self.key))

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, Operand):
            self.source = Operand(**as_dict(self.source))

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EqualStmt(YAMLRoot):
    """
    ``EqualStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["EqualStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:EqualStmt"
    class_name: ClassVar[str] = "EqualStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.EqualStmt

    col: int = None
    file: int = None
    row: int = None
    a: Union[dict, "Operand"] = None
    b: Union[dict, "Operand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.a):
            self.MissingRequiredField("a")
        if not isinstance(self.a, Operand):
            self.a = Operand(**as_dict(self.a))

        if self._is_empty(self.b):
            self.MissingRequiredField("b")
        if not isinstance(self.b, Operand):
            self.b = Operand(**as_dict(self.b))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Func(YAMLRoot):
    """
    ``Func`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Func"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Func"
    class_name: ClassVar[str] = "Func"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Func

    blocks: Union[Union[dict, Block], list[Union[dict, Block]]] = None
    name: str = None
    params: Union[int, list[int]] = None
    return_value: int = None
    path: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.blocks):
            self.MissingRequiredField("blocks")
        if not isinstance(self.blocks, list):
            self.blocks = [self.blocks] if self.blocks is not None else []
        self.blocks = [v if isinstance(v, Block) else Block(**as_dict(v)) for v in self.blocks]

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, list):
            self.params = [self.params] if self.params is not None else []
        self.params = [v if isinstance(v, int) else int(v) for v in self.params]

        if self._is_empty(self.return_value):
            self.MissingRequiredField("return_value")
        if not isinstance(self.return_value, int):
            self.return_value = int(self.return_value)

        if not isinstance(self.path, list):
            self.path = [self.path] if self.path is not None else []
        self.path = [v if isinstance(v, str) else str(v) for v in self.path]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Funcs(YAMLRoot):
    """
    ``Funcs`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Funcs"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Funcs"
    class_name: ClassVar[str] = "Funcs"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Funcs

    funcs: Union[Union[dict, Func], list[Union[dict, Func]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.funcs):
            self.MissingRequiredField("funcs")
        self._normalize_inlined_as_list(slot_name="funcs", slot_type=Func, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsArrayStmt(YAMLRoot):
    """
    ``IsArrayStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["IsArrayStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:IsArrayStmt"
    class_name: ClassVar[str] = "IsArrayStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.IsArrayStmt

    col: int = None
    file: int = None
    row: int = None
    source: Union[dict, "Operand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, Operand):
            self.source = Operand(**as_dict(self.source))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsDefinedStmt(YAMLRoot):
    """
    ``IsDefinedStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["IsDefinedStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:IsDefinedStmt"
    class_name: ClassVar[str] = "IsDefinedStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.IsDefinedStmt

    col: int = None
    file: int = None
    row: int = None
    source: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, int):
            self.source = int(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsObjectStmt(YAMLRoot):
    """
    ``IsObjectStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["IsObjectStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:IsObjectStmt"
    class_name: ClassVar[str] = "IsObjectStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.IsObjectStmt

    col: int = None
    file: int = None
    row: int = None
    source: Union[dict, "Operand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, Operand):
            self.source = Operand(**as_dict(self.source))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsSetStmt(YAMLRoot):
    """
    ``IsSetStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["IsSetStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:IsSetStmt"
    class_name: ClassVar[str] = "IsSetStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.IsSetStmt

    col: int = None
    file: int = None
    row: int = None
    source: Union[dict, "Operand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, Operand):
            self.source = Operand(**as_dict(self.source))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IsUndefinedStmt(YAMLRoot):
    """
    ``IsUndefinedStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["IsUndefinedStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:IsUndefinedStmt"
    class_name: ClassVar[str] = "IsUndefinedStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.IsUndefinedStmt

    col: int = None
    file: int = None
    row: int = None
    source: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, int):
            self.source = int(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LenStmt(YAMLRoot):
    """
    ``LenStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["LenStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:LenStmt"
    class_name: ClassVar[str] = "LenStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.LenStmt

    col: int = None
    file: int = None
    row: int = None
    source: Union[dict, "Operand"] = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, Operand):
            self.source = Operand(**as_dict(self.source))

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MakeArrayStmt(YAMLRoot):
    """
    ``MakeArrayStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["MakeArrayStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:MakeArrayStmt"
    class_name: ClassVar[str] = "MakeArrayStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.MakeArrayStmt

    col: int = None
    file: int = None
    row: int = None
    capacity: int = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.capacity):
            self.MissingRequiredField("capacity")
        if not isinstance(self.capacity, int):
            self.capacity = int(self.capacity)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MakeNullStmt(YAMLRoot):
    """
    ``MakeNullStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["MakeNullStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:MakeNullStmt"
    class_name: ClassVar[str] = "MakeNullStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.MakeNullStmt

    col: int = None
    file: int = None
    row: int = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MakeNumberIntStmt(YAMLRoot):
    """
    ``MakeNumberIntStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["MakeNumberIntStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:MakeNumberIntStmt"
    class_name: ClassVar[str] = "MakeNumberIntStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.MakeNumberIntStmt

    col: int = None
    file: int = None
    row: int = None
    target: int = None
    value: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MakeNumberRefStmt(YAMLRoot):
    """
    ``MakeNumberRefStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["MakeNumberRefStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:MakeNumberRefStmt"
    class_name: ClassVar[str] = "MakeNumberRefStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.MakeNumberRefStmt

    col: int = None
    file: int = None
    row: int = None
    index: int = None
    target: int = None
    Index: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        if self.Index is not None and not isinstance(self.Index, int):
            self.Index = int(self.Index)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MakeObjectStmt(YAMLRoot):
    """
    ``MakeObjectStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["MakeObjectStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:MakeObjectStmt"
    class_name: ClassVar[str] = "MakeObjectStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.MakeObjectStmt

    col: int = None
    file: int = None
    row: int = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MakeSetStmt(YAMLRoot):
    """
    ``MakeSetStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["MakeSetStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:MakeSetStmt"
    class_name: ClassVar[str] = "MakeSetStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.MakeSetStmt

    col: int = None
    file: int = None
    row: int = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NopStmt(YAMLRoot):
    """
    ``NopStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["NopStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:NopStmt"
    class_name: ClassVar[str] = "NopStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.NopStmt

    col: int = None
    file: int = None
    row: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotEqualStmt(YAMLRoot):
    """
    ``NotEqualStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["NotEqualStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:NotEqualStmt"
    class_name: ClassVar[str] = "NotEqualStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.NotEqualStmt

    col: int = None
    file: int = None
    row: int = None
    a: Union[dict, "Operand"] = None
    b: Union[dict, "Operand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.a):
            self.MissingRequiredField("a")
        if not isinstance(self.a, Operand):
            self.a = Operand(**as_dict(self.a))

        if self._is_empty(self.b):
            self.MissingRequiredField("b")
        if not isinstance(self.b, Operand):
            self.b = Operand(**as_dict(self.b))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotStmt(YAMLRoot):
    """
    ``NotStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["NotStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:NotStmt"
    class_name: ClassVar[str] = "NotStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.NotStmt

    col: int = None
    file: int = None
    row: int = None
    block: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.block):
            self.MissingRequiredField("block")
        if not isinstance(self.block, str):
            self.block = str(self.block)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObjectInsertOnceStmt(YAMLRoot):
    """
    ``ObjectInsertOnceStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["ObjectInsertOnceStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:ObjectInsertOnceStmt"
    class_name: ClassVar[str] = "ObjectInsertOnceStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.ObjectInsertOnceStmt

    col: int = None
    file: int = None
    row: int = None
    key: Union[dict, "Operand"] = None
    object: int = None
    value: Union[dict, "Operand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, Operand):
            self.key = Operand(**as_dict(self.key))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, int):
            self.object = int(self.object)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Operand):
            self.value = Operand(**as_dict(self.value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObjectInsertStmt(YAMLRoot):
    """
    ``ObjectInsertStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["ObjectInsertStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:ObjectInsertStmt"
    class_name: ClassVar[str] = "ObjectInsertStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.ObjectInsertStmt

    col: int = None
    file: int = None
    row: int = None
    key: Union[dict, "Operand"] = None
    object: int = None
    value: Union[dict, "Operand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, Operand):
            self.key = Operand(**as_dict(self.key))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, int):
            self.object = int(self.object)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Operand):
            self.value = Operand(**as_dict(self.value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObjectMergeStmt(YAMLRoot):
    """
    ``ObjectMergeStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["ObjectMergeStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:ObjectMergeStmt"
    class_name: ClassVar[str] = "ObjectMergeStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.ObjectMergeStmt

    col: int = None
    file: int = None
    row: int = None
    a: int = None
    b: int = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.a):
            self.MissingRequiredField("a")
        if not isinstance(self.a, int):
            self.a = int(self.a)

        if self._is_empty(self.b):
            self.MissingRequiredField("b")
        if not isinstance(self.b, int):
            self.b = int(self.b)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Plan(YAMLRoot):
    """
    ``Plan`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Plan"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Plan"
    class_name: ClassVar[str] = "Plan"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Plan

    blocks: Union[Union[dict, Block], list[Union[dict, Block]]] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.blocks):
            self.MissingRequiredField("blocks")
        if not isinstance(self.blocks, list):
            self.blocks = [self.blocks] if self.blocks is not None else []
        self.blocks = [v if isinstance(v, Block) else Block(**as_dict(v)) for v in self.blocks]

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Plans(YAMLRoot):
    """
    ``Plans`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Plans"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Plans"
    class_name: ClassVar[str] = "Plans"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Plans

    plans: Union[Union[dict, Plan], list[Union[dict, Plan]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.plans):
            self.MissingRequiredField("plans")
        self._normalize_inlined_as_list(slot_name="plans", slot_type=Plan, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Policy(YAMLRoot):
    """
    ``Policy`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Policy"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Policy"
    class_name: ClassVar[str] = "Policy"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Policy

    funcs: Optional[Union[dict, Funcs]] = None
    plans: Optional[Union[dict, Plans]] = None
    static: Optional[Union[dict, "Static"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.funcs is not None and not isinstance(self.funcs, Funcs):
            self.funcs = Funcs(**as_dict(self.funcs))

        if self.plans is not None and not isinstance(self.plans, Plans):
            self.plans = Plans(**as_dict(self.plans))

        if self.static is not None and not isinstance(self.static, Static):
            self.static = Static(**as_dict(self.static))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResetLocalStmt(YAMLRoot):
    """
    ``ResetLocalStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["ResetLocalStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:ResetLocalStmt"
    class_name: ClassVar[str] = "ResetLocalStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.ResetLocalStmt

    col: int = None
    file: int = None
    row: int = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResultSetAddStmt(YAMLRoot):
    """
    ``ResultSetAddStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["ResultSetAddStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:ResultSetAddStmt"
    class_name: ClassVar[str] = "ResultSetAddStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.ResultSetAddStmt

    col: int = None
    file: int = None
    row: int = None
    value: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReturnLocalStmt(YAMLRoot):
    """
    ``ReturnLocalStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["ReturnLocalStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:ReturnLocalStmt"
    class_name: ClassVar[str] = "ReturnLocalStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.ReturnLocalStmt

    col: int = None
    file: int = None
    row: int = None
    source: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, int):
            self.source = int(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScanStmt(YAMLRoot):
    """
    ``ScanStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["ScanStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:ScanStmt"
    class_name: ClassVar[str] = "ScanStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.ScanStmt

    col: int = None
    file: int = None
    row: int = None
    block: str = None
    key: int = None
    source: int = None
    value: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.block):
            self.MissingRequiredField("block")
        if not isinstance(self.block, str):
            self.block = str(self.block)

        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, int):
            self.key = int(self.key)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, int):
            self.source = int(self.source)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SetAddStmt(YAMLRoot):
    """
    ``SetAddStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["SetAddStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:SetAddStmt"
    class_name: ClassVar[str] = "SetAddStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.SetAddStmt

    col: int = None
    file: int = None
    row: int = None
    set: int = None
    value: Union[dict, "Operand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.set):
            self.MissingRequiredField("set")
        if not isinstance(self.set, int):
            self.set = int(self.set)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Operand):
            self.value = Operand(**as_dict(self.value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Static(YAMLRoot):
    """
    ``Static`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Static"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Static"
    class_name: ClassVar[str] = "Static"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Static

    builtin_funcs: Optional[Union[Union[dict, BuiltinFunc], list[Union[dict, BuiltinFunc]]]] = empty_list()
    files: Optional[Union[Union[dict, "StringConst"], list[Union[dict, "StringConst"]]]] = empty_list()
    strings: Optional[Union[Union[dict, "StringConst"], list[Union[dict, "StringConst"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="builtin_funcs", slot_type=BuiltinFunc, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="files", slot_type=StringConst, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="strings", slot_type=StringConst, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Stmt(YAMLRoot):
    """
    Tagged-wrapper class for the ``Stmt`` discriminated union from
    the upstream JSON Schema.

    The ``type`` slot carries the discriminator tag and the
    ``stmt`` slot carries the typed payload. Because the
    payload class varies by tag, ``stmt`` is typed as
    ``Any`` with an ``any_of`` union over the known payload classes;
    consumers select the concrete class using the table below.

    * ``ArrayAppendStmt`` -- payload class ``ArrayAppendStmt``
    * ``AssignIntStmt`` -- payload class ``AssignIntStmt``
    * ``AssignVarOnceStmt`` -- payload class ``AssignVarOnceStmt``
    * ``AssignVarStmt`` -- payload class ``AssignVarStmt``
    * ``BlockStmt`` -- payload class ``BlockStmt``
    * ``BreakStmt`` -- payload class ``BreakStmt``
    * ``CallDynamicStmt`` -- payload class ``CallDynamicStmt``
    * ``CallStmt`` -- payload class ``CallStmt``
    * ``DotStmt`` -- payload class ``DotStmt``
    * ``EqualStmt`` -- payload class ``EqualStmt``
    * ``IsArrayStmt`` -- payload class ``IsArrayStmt``
    * ``IsDefinedStmt`` -- payload class ``IsDefinedStmt``
    * ``IsObjectStmt`` -- payload class ``IsObjectStmt``
    * ``IsSetStmt`` -- payload class ``IsSetStmt``
    * ``IsUndefinedStmt`` -- payload class ``IsUndefinedStmt``
    * ``LenStmt`` -- payload class ``LenStmt``
    * ``MakeArrayStmt`` -- payload class ``MakeArrayStmt``
    * ``MakeNullStmt`` -- payload class ``MakeNullStmt``
    * ``MakeNumberIntStmt`` -- payload class ``MakeNumberIntStmt``
    * ``MakeNumberRefStmt`` -- payload class ``MakeNumberRefStmt``
    * ``MakeObjectStmt`` -- payload class ``MakeObjectStmt``
    * ``MakeSetStmt`` -- payload class ``MakeSetStmt``
    * ``NopStmt`` -- payload class ``NopStmt``
    * ``NotEqualStmt`` -- payload class ``NotEqualStmt``
    * ``NotStmt`` -- payload class ``NotStmt``
    * ``ObjectInsertOnceStmt`` -- payload class ``ObjectInsertOnceStmt``
    * ``ObjectInsertStmt`` -- payload class ``ObjectInsertStmt``
    * ``ObjectMergeStmt`` -- payload class ``ObjectMergeStmt``
    * ``ResetLocalStmt`` -- payload class ``ResetLocalStmt``
    * ``ResultSetAddStmt`` -- payload class ``ResultSetAddStmt``
    * ``ReturnLocalStmt`` -- payload class ``ReturnLocalStmt``
    * ``ScanStmt`` -- payload class ``ScanStmt``
    * ``SetAddStmt`` -- payload class ``SetAddStmt``
    * ``WithStmt`` -- payload class ``WithStmt``
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Stmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Stmt"
    class_name: ClassVar[str] = "Stmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Stmt

    type: Union[str, "StmtTag"] = None
    stmt: Union[dict, Any] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, StmtTag):
            self.type = StmtTag(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StringConst(YAMLRoot):
    """
    ``StringConst`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["StringConst"]
    class_class_curie: ClassVar[str] = "openpolicyagent:StringConst"
    class_name: ClassVar[str] = "StringConst"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.StringConst

    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Val(YAMLRoot):
    """
    Tagged-wrapper class for the ``Val`` discriminated union from
    the upstream JSON Schema.

    The ``type`` slot carries the discriminator tag and the
    ``value`` slot carries the typed payload. Because the
    payload class varies by tag, ``value`` is typed as
    ``Any`` with an ``any_of`` union over the known payload classes;
    consumers select the concrete class using the table below.

    * ``bool`` -- payload class ``boolean``
    * ``local`` -- payload class ``integer``
    * ``string_index`` -- payload class ``integer``
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Val"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Val"
    class_name: ClassVar[str] = "Val"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Val

    type: Union[str, "ValTag"] = None
    value: Union[dict, Any] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, ValTag):
            self.type = ValTag(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WithStmt(YAMLRoot):
    """
    ``WithStmt`` definition from upstream JSON Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["WithStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:WithStmt"
    class_name: ClassVar[str] = "WithStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.WithStmt

    col: int = None
    file: int = None
    row: int = None
    block: str = None
    local: int = None
    path: Union[int, list[int]] = None
    value: Union[dict, "Operand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.block):
            self.MissingRequiredField("block")
        if not isinstance(self.block, str):
            self.block = str(self.block)

        if self._is_empty(self.local):
            self.MissingRequiredField("local")
        if not isinstance(self.local, int):
            self.local = int(self.local)

        if self._is_empty(self.path):
            self.MissingRequiredField("path")
        if not isinstance(self.path, list):
            self.path = [self.path] if self.path is not None else []
        self.path = [v if isinstance(v, int) else int(v) for v in self.path]

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Operand):
            self.value = Operand(**as_dict(self.value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Operand(Val):
    """
    Alias for ``Val`` (single-``$ref`` def in upstream JSON Schema).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["Operand"]
    class_class_curie: ClassVar[str] = "openpolicyagent:Operand"
    class_name: ClassVar[str] = "Operand"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.Operand

    type: Union[str, "ValTag"] = None
    value: Union[dict, Any] = None

# Enumerations
class BuiltinTypeKind(EnumDefinitionImpl):
    """
    Kinds of value that a TypeDecl can describe.
    """
    string = PermissibleValue(text="string")
    number = PermissibleValue(text="number")
    boolean = PermissibleValue(text="boolean")
    null = PermissibleValue(text="null")
    any = PermissibleValue(text="any")
    array = PermissibleValue(text="array")
    set = PermissibleValue(text="set")
    object = PermissibleValue(text="object")
    function = PermissibleValue(text="function")

    _defn = EnumDefinition(
        name="BuiltinTypeKind",
        description="Kinds of value that a TypeDecl can describe.",
    )

class FeatureName(EnumDefinitionImpl):
    """
    Optional features advertised by the OPA build. The permissible values below are seeded from the upstream
    capabilities.json snapshot at generation time; future releases may introduce new flags.
    """
    keywords_in_refs = PermissibleValue(
        text="keywords_in_refs",
        meaning=OPENPOLICYAGENT["feature/keywords_in_refs"])
    rego_v1 = PermissibleValue(
        text="rego_v1",
        meaning=OPENPOLICYAGENT["feature/rego_v1"])
    template_strings = PermissibleValue(
        text="template_strings",
        meaning=OPENPOLICYAGENT["feature/template_strings"])

    _defn = EnumDefinition(
        name="FeatureName",
        description="""Optional features advertised by the OPA build. The permissible values below are seeded from the upstream capabilities.json snapshot at generation time; future releases may introduce new flags.""",
    )

class FutureKeyword(EnumDefinitionImpl):
    """
    Identifiers reserved for upcoming Rego releases.
    """
    _defn = EnumDefinition(
        name="FutureKeyword",
        description="Identifiers reserved for upcoming Rego releases.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not",
            PermissibleValue(
                text="not",
                meaning=OPENPOLICYAGENT["future_keyword/not"]))

class BuiltinCategory(EnumDefinitionImpl):
    """
    Documentation category a built-in belongs to. Permissible values are seeded from
    ``builtin_metadata.json._categories`` at generation time. Enum symbols follow LinkML's snake_case convention; each
    permissible value carries the upstream label (e.g. ``providers.aws``) in both its description and its ``meaning``
    mapping.
    """
    aggregates = PermissibleValue(
        text="aggregates",
        meaning=OPENPOLICYAGENT["category/aggregates"])
    array = PermissibleValue(
        text="array",
        meaning=OPENPOLICYAGENT["category/array"])
    bits = PermissibleValue(
        text="bits",
        meaning=OPENPOLICYAGENT["category/bits"])
    comparison = PermissibleValue(
        text="comparison",
        meaning=OPENPOLICYAGENT["category/comparison"])
    conversions = PermissibleValue(
        text="conversions",
        meaning=OPENPOLICYAGENT["category/conversions"])
    crypto = PermissibleValue(
        text="crypto",
        meaning=OPENPOLICYAGENT["category/crypto"])
    encoding = PermissibleValue(
        text="encoding",
        meaning=OPENPOLICYAGENT["category/encoding"])
    glob = PermissibleValue(
        text="glob",
        meaning=OPENPOLICYAGENT["category/glob"])
    graph = PermissibleValue(
        text="graph",
        meaning=OPENPOLICYAGENT["category/graph"])
    graphql = PermissibleValue(
        text="graphql",
        meaning=OPENPOLICYAGENT["category/graphql"])
    http = PermissibleValue(
        text="http",
        meaning=OPENPOLICYAGENT["category/http"])
    internal = PermissibleValue(
        text="internal",
        meaning=OPENPOLICYAGENT["category/internal"])
    net = PermissibleValue(
        text="net",
        meaning=OPENPOLICYAGENT["category/net"])
    numbers = PermissibleValue(
        text="numbers",
        meaning=OPENPOLICYAGENT["category/numbers"])
    object = PermissibleValue(
        text="object",
        meaning=OPENPOLICYAGENT["category/object"])
    opa = PermissibleValue(
        text="opa",
        meaning=OPENPOLICYAGENT["category/opa"])
    providers_aws = PermissibleValue(
        text="providers_aws",
        description="providers.aws",
        meaning=OPENPOLICYAGENT["category/providers.aws"])
    regex = PermissibleValue(
        text="regex",
        meaning=OPENPOLICYAGENT["category/regex"])
    rego = PermissibleValue(
        text="rego",
        meaning=OPENPOLICYAGENT["category/rego"])
    semver = PermissibleValue(
        text="semver",
        meaning=OPENPOLICYAGENT["category/semver"])
    sets = PermissibleValue(
        text="sets",
        meaning=OPENPOLICYAGENT["category/sets"])
    strings = PermissibleValue(
        text="strings",
        meaning=OPENPOLICYAGENT["category/strings"])
    time = PermissibleValue(
        text="time",
        meaning=OPENPOLICYAGENT["category/time"])
    tokens = PermissibleValue(
        text="tokens",
        meaning=OPENPOLICYAGENT["category/tokens"])
    tokensign = PermissibleValue(
        text="tokensign",
        meaning=OPENPOLICYAGENT["category/tokensign"])
    tracing = PermissibleValue(
        text="tracing",
        meaning=OPENPOLICYAGENT["category/tracing"])
    types = PermissibleValue(
        text="types",
        meaning=OPENPOLICYAGENT["category/types"])
    units = PermissibleValue(
        text="units",
        meaning=OPENPOLICYAGENT["category/units"])
    uri = PermissibleValue(
        text="uri",
        meaning=OPENPOLICYAGENT["category/uri"])
    uuid = PermissibleValue(
        text="uuid",
        meaning=OPENPOLICYAGENT["category/uuid"])

    _defn = EnumDefinition(
        name="BuiltinCategory",
        description="""Documentation category a built-in belongs to. Permissible values are seeded from ``builtin_metadata.json._categories`` at generation time. Enum symbols follow LinkML's snake_case convention; each permissible value carries the upstream label (e.g. ``providers.aws``) in both its description and its ``meaning`` mapping.""",
    )

class StmtTag(EnumDefinitionImpl):
    """
    Permissible discriminator tags for the ``Stmt`` union.
    """
    ArrayAppendStmt = PermissibleValue(text="ArrayAppendStmt")
    AssignIntStmt = PermissibleValue(text="AssignIntStmt")
    AssignVarOnceStmt = PermissibleValue(text="AssignVarOnceStmt")
    AssignVarStmt = PermissibleValue(text="AssignVarStmt")
    BlockStmt = PermissibleValue(text="BlockStmt")
    BreakStmt = PermissibleValue(text="BreakStmt")
    CallDynamicStmt = PermissibleValue(text="CallDynamicStmt")
    CallStmt = PermissibleValue(text="CallStmt")
    DotStmt = PermissibleValue(text="DotStmt")
    EqualStmt = PermissibleValue(text="EqualStmt")
    IsArrayStmt = PermissibleValue(text="IsArrayStmt")
    IsDefinedStmt = PermissibleValue(text="IsDefinedStmt")
    IsObjectStmt = PermissibleValue(text="IsObjectStmt")
    IsSetStmt = PermissibleValue(text="IsSetStmt")
    IsUndefinedStmt = PermissibleValue(text="IsUndefinedStmt")
    LenStmt = PermissibleValue(text="LenStmt")
    MakeArrayStmt = PermissibleValue(text="MakeArrayStmt")
    MakeNullStmt = PermissibleValue(text="MakeNullStmt")
    MakeNumberIntStmt = PermissibleValue(text="MakeNumberIntStmt")
    MakeNumberRefStmt = PermissibleValue(text="MakeNumberRefStmt")
    MakeObjectStmt = PermissibleValue(text="MakeObjectStmt")
    MakeSetStmt = PermissibleValue(text="MakeSetStmt")
    NopStmt = PermissibleValue(text="NopStmt")
    NotEqualStmt = PermissibleValue(text="NotEqualStmt")
    NotStmt = PermissibleValue(text="NotStmt")
    ObjectInsertOnceStmt = PermissibleValue(text="ObjectInsertOnceStmt")
    ObjectInsertStmt = PermissibleValue(text="ObjectInsertStmt")
    ObjectMergeStmt = PermissibleValue(text="ObjectMergeStmt")
    ResetLocalStmt = PermissibleValue(text="ResetLocalStmt")
    ResultSetAddStmt = PermissibleValue(text="ResultSetAddStmt")
    ReturnLocalStmt = PermissibleValue(text="ReturnLocalStmt")
    ScanStmt = PermissibleValue(text="ScanStmt")
    SetAddStmt = PermissibleValue(text="SetAddStmt")
    WithStmt = PermissibleValue(text="WithStmt")

    _defn = EnumDefinition(
        name="StmtTag",
        description="Permissible discriminator tags for the ``Stmt`` union.",
    )

class ValTag(EnumDefinitionImpl):
    """
    Permissible discriminator tags for the ``Val`` union.
    """
    bool = PermissibleValue(text="bool")
    local = PermissibleValue(text="local")
    string_index = PermissibleValue(text="string_index")

    _defn = EnumDefinition(
        name="ValTag",
        description="Permissible discriminator tags for the ``Val`` union.",
    )

# Slots
class slots:
    pass

slots.capabilities__builtins = Slot(uri=OPENPOLICYAGENT.builtins, name="capabilities__builtins", curie=OPENPOLICYAGENT.curie('builtins'),
                   model_uri=OPENPOLICYAGENT.capabilities__builtins, domain=None, range=Optional[Union[dict[Union[str, BuiltinName], Union[dict, Builtin]], list[Union[dict, Builtin]]]])

slots.capabilities__future_keywords = Slot(uri=OPENPOLICYAGENT.future_keywords, name="capabilities__future_keywords", curie=OPENPOLICYAGENT.curie('future_keywords'),
                   model_uri=OPENPOLICYAGENT.capabilities__future_keywords, domain=None, range=Optional[Union[Union[str, "FutureKeyword"], list[Union[str, "FutureKeyword"]]]])

slots.capabilities__wasm_abi_versions = Slot(uri=OPENPOLICYAGENT.wasm_abi_versions, name="capabilities__wasm_abi_versions", curie=OPENPOLICYAGENT.curie('wasm_abi_versions'),
                   model_uri=OPENPOLICYAGENT.capabilities__wasm_abi_versions, domain=None, range=Optional[Union[Union[dict, WasmABIVersion], list[Union[dict, WasmABIVersion]]]])

slots.capabilities__features = Slot(uri=OPENPOLICYAGENT.features, name="capabilities__features", curie=OPENPOLICYAGENT.curie('features'),
                   model_uri=OPENPOLICYAGENT.capabilities__features, domain=None, range=Optional[Union[Union[str, "FeatureName"], list[Union[str, "FeatureName"]]]])

slots.capabilities__allow_net = Slot(uri=OPENPOLICYAGENT.allow_net, name="capabilities__allow_net", curie=OPENPOLICYAGENT.curie('allow_net'),
                   model_uri=OPENPOLICYAGENT.capabilities__allow_net, domain=None, range=Optional[Union[str, list[str]]])

slots.builtin__name = Slot(uri=OPENPOLICYAGENT.name, name="builtin__name", curie=OPENPOLICYAGENT.curie('name'),
                   model_uri=OPENPOLICYAGENT.builtin__name, domain=None, range=URIRef)

slots.builtin__decl = Slot(uri=OPENPOLICYAGENT.decl, name="builtin__decl", curie=OPENPOLICYAGENT.curie('decl'),
                   model_uri=OPENPOLICYAGENT.builtin__decl, domain=None, range=Union[dict, BuiltinDecl])

slots.builtin__infix = Slot(uri=OPENPOLICYAGENT.infix, name="builtin__infix", curie=OPENPOLICYAGENT.curie('infix'),
                   model_uri=OPENPOLICYAGENT.builtin__infix, domain=None, range=Optional[str])

slots.builtin__deprecated = Slot(uri=OPENPOLICYAGENT.deprecated, name="builtin__deprecated", curie=OPENPOLICYAGENT.curie('deprecated'),
                   model_uri=OPENPOLICYAGENT.builtin__deprecated, domain=None, range=Optional[Union[bool, Bool]])

slots.builtin__nondeterministic = Slot(uri=OPENPOLICYAGENT.nondeterministic, name="builtin__nondeterministic", curie=OPENPOLICYAGENT.curie('nondeterministic'),
                   model_uri=OPENPOLICYAGENT.builtin__nondeterministic, domain=None, range=Optional[Union[bool, Bool]])

slots.builtin__relation = Slot(uri=OPENPOLICYAGENT.relation, name="builtin__relation", curie=OPENPOLICYAGENT.curie('relation'),
                   model_uri=OPENPOLICYAGENT.builtin__relation, domain=None, range=Optional[Union[bool, Bool]])

slots.builtinDecl__type = Slot(uri=OPENPOLICYAGENT.type, name="builtinDecl__type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.builtinDecl__type, domain=None, range=str)

slots.builtinDecl__args = Slot(uri=OPENPOLICYAGENT.args, name="builtinDecl__args", curie=OPENPOLICYAGENT.curie('args'),
                   model_uri=OPENPOLICYAGENT.builtinDecl__args, domain=None, range=Optional[Union[Union[dict, TypeDecl], list[Union[dict, TypeDecl]]]])

slots.builtinDecl__result = Slot(uri=OPENPOLICYAGENT.result, name="builtinDecl__result", curie=OPENPOLICYAGENT.curie('result'),
                   model_uri=OPENPOLICYAGENT.builtinDecl__result, domain=None, range=Optional[Union[dict, TypeDecl]])

slots.builtinDecl__variadic = Slot(uri=OPENPOLICYAGENT.variadic, name="builtinDecl__variadic", curie=OPENPOLICYAGENT.curie('variadic'),
                   model_uri=OPENPOLICYAGENT.builtinDecl__variadic, domain=None, range=Optional[Union[dict, TypeDecl]])

slots.typeDecl__type = Slot(uri=OPENPOLICYAGENT.type, name="typeDecl__type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.typeDecl__type, domain=None, range=Optional[Union[str, "BuiltinTypeKind"]])

slots.typeDecl__of = Slot(uri=OPENPOLICYAGENT.of, name="typeDecl__of", curie=OPENPOLICYAGENT.curie('of'),
                   model_uri=OPENPOLICYAGENT.typeDecl__of, domain=None, range=Optional[Union[Union[dict, TypeDecl], list[Union[dict, TypeDecl]]]])

slots.typeDecl__dynamic = Slot(uri=OPENPOLICYAGENT.dynamic, name="typeDecl__dynamic", curie=OPENPOLICYAGENT.curie('dynamic'),
                   model_uri=OPENPOLICYAGENT.typeDecl__dynamic, domain=None, range=Optional[Union[dict, TypeDecl]])

slots.typeDecl__static = Slot(uri=OPENPOLICYAGENT.static, name="typeDecl__static", curie=OPENPOLICYAGENT.curie('static'),
                   model_uri=OPENPOLICYAGENT.typeDecl__static, domain=None, range=Optional[Union[Union[dict, TypeDecl], list[Union[dict, TypeDecl]]]])

slots.typeDecl__key = Slot(uri=OPENPOLICYAGENT.key, name="typeDecl__key", curie=OPENPOLICYAGENT.curie('key'),
                   model_uri=OPENPOLICYAGENT.typeDecl__key, domain=None, range=Optional[Union[dict, Any]])

slots.typeDecl__value = Slot(uri=OPENPOLICYAGENT.value, name="typeDecl__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.typeDecl__value, domain=None, range=Optional[Union[dict, TypeDecl]])

slots.wasmABIVersion__version = Slot(uri=OPENPOLICYAGENT.version, name="wasmABIVersion__version", curie=OPENPOLICYAGENT.curie('version'),
                   model_uri=OPENPOLICYAGENT.wasmABIVersion__version, domain=None, range=int)

slots.wasmABIVersion__minor_version = Slot(uri=OPENPOLICYAGENT.minor_version, name="wasmABIVersion__minor_version", curie=OPENPOLICYAGENT.curie('minor_version'),
                   model_uri=OPENPOLICYAGENT.wasmABIVersion__minor_version, domain=None, range=int)

slots.builtinMetadataCatalog__categories = Slot(uri=OPENPOLICYAGENT.categories, name="builtinMetadataCatalog__categories", curie=OPENPOLICYAGENT.curie('categories'),
                   model_uri=OPENPOLICYAGENT.builtinMetadataCatalog__categories, domain=None, range=Optional[Union[dict[Union[str, BuiltinCategoryGroupName], Union[dict, BuiltinCategoryGroup]], list[Union[dict, BuiltinCategoryGroup]]]])

slots.builtinMetadataCatalog__builtins = Slot(uri=OPENPOLICYAGENT.builtins, name="builtinMetadataCatalog__builtins", curie=OPENPOLICYAGENT.curie('builtins'),
                   model_uri=OPENPOLICYAGENT.builtinMetadataCatalog__builtins, domain=None, range=Optional[Union[dict[Union[str, BuiltinMetadataName], Union[dict, BuiltinMetadata]], list[Union[dict, BuiltinMetadata]]]])

slots.builtinCategoryGroup__name = Slot(uri=OPENPOLICYAGENT.name, name="builtinCategoryGroup__name", curie=OPENPOLICYAGENT.curie('name'),
                   model_uri=OPENPOLICYAGENT.builtinCategoryGroup__name, domain=None, range=URIRef)

slots.builtinCategoryGroup__category = Slot(uri=OPENPOLICYAGENT.category, name="builtinCategoryGroup__category", curie=OPENPOLICYAGENT.curie('category'),
                   model_uri=OPENPOLICYAGENT.builtinCategoryGroup__category, domain=None, range=Optional[Union[str, "BuiltinCategory"]])

slots.builtinCategoryGroup__builtins = Slot(uri=OPENPOLICYAGENT.builtins, name="builtinCategoryGroup__builtins", curie=OPENPOLICYAGENT.curie('builtins'),
                   model_uri=OPENPOLICYAGENT.builtinCategoryGroup__builtins, domain=None, range=Union[str, list[str]])

slots.builtinMetadata__name = Slot(uri=OPENPOLICYAGENT.name, name="builtinMetadata__name", curie=OPENPOLICYAGENT.curie('name'),
                   model_uri=OPENPOLICYAGENT.builtinMetadata__name, domain=None, range=URIRef)

slots.builtinMetadata__description = Slot(uri=SCHEMA.description, name="builtinMetadata__description", curie=SCHEMA.curie('description'),
                   model_uri=OPENPOLICYAGENT.builtinMetadata__description, domain=None, range=Optional[str])

slots.builtinMetadata__introduced = Slot(uri=OPENPOLICYAGENT.introduced, name="builtinMetadata__introduced", curie=OPENPOLICYAGENT.curie('introduced'),
                   model_uri=OPENPOLICYAGENT.builtinMetadata__introduced, domain=None, range=Optional[str])

slots.builtinMetadata__available = Slot(uri=OPENPOLICYAGENT.available, name="builtinMetadata__available", curie=OPENPOLICYAGENT.curie('available'),
                   model_uri=OPENPOLICYAGENT.builtinMetadata__available, domain=None, range=Optional[Union[str, list[str]]])

slots.builtinMetadata__wasm = Slot(uri=OPENPOLICYAGENT.wasm, name="builtinMetadata__wasm", curie=OPENPOLICYAGENT.curie('wasm'),
                   model_uri=OPENPOLICYAGENT.builtinMetadata__wasm, domain=None, range=Optional[Union[bool, Bool]])

slots.builtinMetadata__infix = Slot(uri=OPENPOLICYAGENT.infix, name="builtinMetadata__infix", curie=OPENPOLICYAGENT.curie('infix'),
                   model_uri=OPENPOLICYAGENT.builtinMetadata__infix, domain=None, range=Optional[str])

slots.builtinMetadata__deprecated = Slot(uri=OPENPOLICYAGENT.deprecated, name="builtinMetadata__deprecated", curie=OPENPOLICYAGENT.curie('deprecated'),
                   model_uri=OPENPOLICYAGENT.builtinMetadata__deprecated, domain=None, range=Optional[Union[bool, Bool]])

slots.builtinMetadata__relation = Slot(uri=OPENPOLICYAGENT.relation, name="builtinMetadata__relation", curie=OPENPOLICYAGENT.curie('relation'),
                   model_uri=OPENPOLICYAGENT.builtinMetadata__relation, domain=None, range=Optional[Union[bool, Bool]])

slots.builtinMetadata__args = Slot(uri=OPENPOLICYAGENT.args, name="builtinMetadata__args", curie=OPENPOLICYAGENT.curie('args'),
                   model_uri=OPENPOLICYAGENT.builtinMetadata__args, domain=None, range=Optional[Union[Union[dict, BuiltinArg], list[Union[dict, BuiltinArg]]]])

slots.builtinMetadata__result = Slot(uri=OPENPOLICYAGENT.result, name="builtinMetadata__result", curie=OPENPOLICYAGENT.curie('result'),
                   model_uri=OPENPOLICYAGENT.builtinMetadata__result, domain=None, range=Optional[Union[dict, BuiltinResult]])

slots.builtinArg__name = Slot(uri=RDFS.label, name="builtinArg__name", curie=RDFS.curie('label'),
                   model_uri=OPENPOLICYAGENT.builtinArg__name, domain=None, range=Optional[str])

slots.builtinArg__description = Slot(uri=SCHEMA.description, name="builtinArg__description", curie=SCHEMA.curie('description'),
                   model_uri=OPENPOLICYAGENT.builtinArg__description, domain=None, range=Optional[str])

slots.builtinArg__type = Slot(uri=OPENPOLICYAGENT.type, name="builtinArg__type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.builtinArg__type, domain=None, range=Optional[str])

slots.builtinResult__name = Slot(uri=RDFS.label, name="builtinResult__name", curie=RDFS.curie('label'),
                   model_uri=OPENPOLICYAGENT.builtinResult__name, domain=None, range=Optional[str])

slots.builtinResult__description = Slot(uri=SCHEMA.description, name="builtinResult__description", curie=SCHEMA.curie('description'),
                   model_uri=OPENPOLICYAGENT.builtinResult__description, domain=None, range=Optional[str])

slots.builtinResult__type = Slot(uri=OPENPOLICYAGENT.type, name="builtinResult__type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.builtinResult__type, domain=None, range=Optional[str])

slots.versionIndex__builtins = Slot(uri=OPENPOLICYAGENT.builtins, name="versionIndex__builtins", curie=OPENPOLICYAGENT.curie('builtins'),
                   model_uri=OPENPOLICYAGENT.versionIndex__builtins, domain=None, range=Optional[Union[dict[Union[str, ElementVersionName], Union[dict, ElementVersion]], list[Union[dict, ElementVersion]]]])

slots.versionIndex__features = Slot(uri=OPENPOLICYAGENT.features, name="versionIndex__features", curie=OPENPOLICYAGENT.curie('features'),
                   model_uri=OPENPOLICYAGENT.versionIndex__features, domain=None, range=Optional[Union[dict[Union[str, ElementVersionName], Union[dict, ElementVersion]], list[Union[dict, ElementVersion]]]])

slots.versionIndex__keywords = Slot(uri=OPENPOLICYAGENT.keywords, name="versionIndex__keywords", curie=OPENPOLICYAGENT.curie('keywords'),
                   model_uri=OPENPOLICYAGENT.versionIndex__keywords, domain=None, range=Optional[Union[dict[Union[str, ElementVersionName], Union[dict, ElementVersion]], list[Union[dict, ElementVersion]]]])

slots.elementVersion__name = Slot(uri=OPENPOLICYAGENT.name, name="elementVersion__name", curie=OPENPOLICYAGENT.curie('name'),
                   model_uri=OPENPOLICYAGENT.elementVersion__name, domain=None, range=URIRef)

slots.elementVersion__major = Slot(uri=OPENPOLICYAGENT.major, name="elementVersion__major", curie=OPENPOLICYAGENT.curie('major'),
                   model_uri=OPENPOLICYAGENT.elementVersion__major, domain=None, range=int)

slots.elementVersion__minor = Slot(uri=OPENPOLICYAGENT.minor, name="elementVersion__minor", curie=OPENPOLICYAGENT.curie('minor'),
                   model_uri=OPENPOLICYAGENT.elementVersion__minor, domain=None, range=int)

slots.elementVersion__patch = Slot(uri=OPENPOLICYAGENT.patch, name="elementVersion__patch", curie=OPENPOLICYAGENT.curie('patch'),
                   model_uri=OPENPOLICYAGENT.elementVersion__patch, domain=None, range=int)

slots.authorizationInput__identity = Slot(uri=OPENPOLICYAGENT.identity, name="authorizationInput__identity", curie=OPENPOLICYAGENT.curie('identity'),
                   model_uri=OPENPOLICYAGENT.authorizationInput__identity, domain=None, range=str)

slots.authorizationInput__client_certificates = Slot(uri=OPENPOLICYAGENT.client_certificates, name="authorizationInput__client_certificates", curie=OPENPOLICYAGENT.curie('client_certificates'),
                   model_uri=OPENPOLICYAGENT.authorizationInput__client_certificates, domain=None, range=Union[Union[dict, Any], list[Union[dict, Any]]])

slots.authorizationInput__method = Slot(uri=OPENPOLICYAGENT.method, name="authorizationInput__method", curie=OPENPOLICYAGENT.curie('method'),
                   model_uri=OPENPOLICYAGENT.authorizationInput__method, domain=None, range=str)

slots.authorizationInput__path = Slot(uri=OPENPOLICYAGENT.path, name="authorizationInput__path", curie=OPENPOLICYAGENT.curie('path'),
                   model_uri=OPENPOLICYAGENT.authorizationInput__path, domain=None, range=Union[str, list[str]])

slots.authorizationInput__params = Slot(uri=OPENPOLICYAGENT.params, name="authorizationInput__params", curie=OPENPOLICYAGENT.curie('params'),
                   model_uri=OPENPOLICYAGENT.authorizationInput__params, domain=None, range=Union[dict, Any])

slots.authorizationInput__headers = Slot(uri=OPENPOLICYAGENT.headers, name="authorizationInput__headers", curie=OPENPOLICYAGENT.curie('headers'),
                   model_uri=OPENPOLICYAGENT.authorizationInput__headers, domain=None, range=Union[dict, Any])

slots.authorizationInput__body = Slot(uri=OPENPOLICYAGENT.body, name="authorizationInput__body", curie=OPENPOLICYAGENT.curie('body'),
                   model_uri=OPENPOLICYAGENT.authorizationInput__body, domain=None, range=Union[dict, Any])

slots.manifest__file_rego_versions = Slot(uri=OPENPOLICYAGENT.file_rego_versions, name="manifest__file_rego_versions", curie=OPENPOLICYAGENT.curie('file_rego_versions'),
                   model_uri=OPENPOLICYAGENT.manifest__file_rego_versions, domain=None, range=Optional[Union[dict[Union[str, FileRegoVersionPath], Union[dict, FileRegoVersion]], list[Union[dict, FileRegoVersion]]]])

slots.manifest__metadata = Slot(uri=OPENPOLICYAGENT.metadata, name="manifest__metadata", curie=OPENPOLICYAGENT.curie('metadata'),
                   model_uri=OPENPOLICYAGENT.manifest__metadata, domain=None, range=Optional[Union[dict, Any]])

slots.manifest__rego_version = Slot(uri=OPENPOLICYAGENT.rego_version, name="manifest__rego_version", curie=OPENPOLICYAGENT.curie('rego_version'),
                   model_uri=OPENPOLICYAGENT.manifest__rego_version, domain=None, range=Optional[int])

slots.manifest__revision = Slot(uri=OPENPOLICYAGENT.revision, name="manifest__revision", curie=OPENPOLICYAGENT.curie('revision'),
                   model_uri=OPENPOLICYAGENT.manifest__revision, domain=None, range=str)

slots.manifest__roots = Slot(uri=OPENPOLICYAGENT.roots, name="manifest__roots", curie=OPENPOLICYAGENT.curie('roots'),
                   model_uri=OPENPOLICYAGENT.manifest__roots, domain=None, range=Optional[Union[str, list[str]]])

slots.manifest__wasm = Slot(uri=OPENPOLICYAGENT.wasm, name="manifest__wasm", curie=OPENPOLICYAGENT.curie('wasm'),
                   model_uri=OPENPOLICYAGENT.manifest__wasm, domain=None, range=Optional[Union[Union[dict, WasmResolver], list[Union[dict, WasmResolver]]]])

slots.wasmResolver__annotations = Slot(uri=OPENPOLICYAGENT.annotations, name="wasmResolver__annotations", curie=OPENPOLICYAGENT.curie('annotations'),
                   model_uri=OPENPOLICYAGENT.wasmResolver__annotations, domain=None, range=Optional[Union[Union[dict, Any], list[Union[dict, Any]]]])

slots.wasmResolver__entrypoint = Slot(uri=OPENPOLICYAGENT.entrypoint, name="wasmResolver__entrypoint", curie=OPENPOLICYAGENT.curie('entrypoint'),
                   model_uri=OPENPOLICYAGENT.wasmResolver__entrypoint, domain=None, range=Optional[str])

slots.wasmResolver__module = Slot(uri=OPENPOLICYAGENT.module, name="wasmResolver__module", curie=OPENPOLICYAGENT.curie('module'),
                   model_uri=OPENPOLICYAGENT.wasmResolver__module, domain=None, range=Optional[str])

slots.fileRegoVersion__path = Slot(uri=OPENPOLICYAGENT.path, name="fileRegoVersion__path", curie=OPENPOLICYAGENT.curie('path'),
                   model_uri=OPENPOLICYAGENT.fileRegoVersion__path, domain=None, range=URIRef)

slots.fileRegoVersion__version = Slot(uri=OPENPOLICYAGENT.version, name="fileRegoVersion__version", curie=OPENPOLICYAGENT.curie('version'),
                   model_uri=OPENPOLICYAGENT.fileRegoVersion__version, domain=None, range=int)

slots.arrayAppendStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="arrayAppendStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.arrayAppendStmt__col, domain=None, range=int)

slots.arrayAppendStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="arrayAppendStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.arrayAppendStmt__file, domain=None, range=int)

slots.arrayAppendStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="arrayAppendStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.arrayAppendStmt__row, domain=None, range=int)

slots.arrayAppendStmt__array = Slot(uri=OPENPOLICYAGENT.array, name="arrayAppendStmt__array", curie=OPENPOLICYAGENT.curie('array'),
                   model_uri=OPENPOLICYAGENT.arrayAppendStmt__array, domain=None, range=int)

slots.arrayAppendStmt__value = Slot(uri=OPENPOLICYAGENT.value, name="arrayAppendStmt__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.arrayAppendStmt__value, domain=None, range=Union[dict, Operand])

slots.assignIntStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="assignIntStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.assignIntStmt__col, domain=None, range=int)

slots.assignIntStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="assignIntStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.assignIntStmt__file, domain=None, range=int)

slots.assignIntStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="assignIntStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.assignIntStmt__row, domain=None, range=int)

slots.assignIntStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="assignIntStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.assignIntStmt__target, domain=None, range=int)

slots.assignIntStmt__value = Slot(uri=OPENPOLICYAGENT.value, name="assignIntStmt__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.assignIntStmt__value, domain=None, range=int)

slots.assignVarOnceStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="assignVarOnceStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.assignVarOnceStmt__col, domain=None, range=int)

slots.assignVarOnceStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="assignVarOnceStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.assignVarOnceStmt__file, domain=None, range=int)

slots.assignVarOnceStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="assignVarOnceStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.assignVarOnceStmt__row, domain=None, range=int)

slots.assignVarOnceStmt__source = Slot(uri=OPENPOLICYAGENT.source, name="assignVarOnceStmt__source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.assignVarOnceStmt__source, domain=None, range=Union[dict, Operand])

slots.assignVarOnceStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="assignVarOnceStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.assignVarOnceStmt__target, domain=None, range=int)

slots.assignVarStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="assignVarStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.assignVarStmt__col, domain=None, range=int)

slots.assignVarStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="assignVarStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.assignVarStmt__file, domain=None, range=int)

slots.assignVarStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="assignVarStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.assignVarStmt__row, domain=None, range=int)

slots.assignVarStmt__source = Slot(uri=OPENPOLICYAGENT.source, name="assignVarStmt__source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.assignVarStmt__source, domain=None, range=Union[dict, Operand])

slots.assignVarStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="assignVarStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.assignVarStmt__target, domain=None, range=int)

slots.block__stmts = Slot(uri=OPENPOLICYAGENT.stmts, name="block__stmts", curie=OPENPOLICYAGENT.curie('stmts'),
                   model_uri=OPENPOLICYAGENT.block__stmts, domain=None, range=Union[Union[dict, Stmt], list[Union[dict, Stmt]]])

slots.blockStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="blockStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.blockStmt__col, domain=None, range=int)

slots.blockStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="blockStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.blockStmt__file, domain=None, range=int)

slots.blockStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="blockStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.blockStmt__row, domain=None, range=int)

slots.blockStmt__blocks = Slot(uri=OPENPOLICYAGENT.blocks, name="blockStmt__blocks", curie=OPENPOLICYAGENT.curie('blocks'),
                   model_uri=OPENPOLICYAGENT.blockStmt__blocks, domain=None, range=Union[Union[dict, Block], list[Union[dict, Block]]])

slots.breakStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="breakStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.breakStmt__col, domain=None, range=int)

slots.breakStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="breakStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.breakStmt__file, domain=None, range=int)

slots.breakStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="breakStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.breakStmt__row, domain=None, range=int)

slots.breakStmt__index = Slot(uri=OPENPOLICYAGENT.index, name="breakStmt__index", curie=OPENPOLICYAGENT.curie('index'),
                   model_uri=OPENPOLICYAGENT.breakStmt__index, domain=None, range=int)

slots.builtinFunc__decl = Slot(uri=OPENPOLICYAGENT.decl, name="builtinFunc__decl", curie=OPENPOLICYAGENT.curie('decl'),
                   model_uri=OPENPOLICYAGENT.builtinFunc__decl, domain=None, range=Union[dict, Any])

slots.builtinFunc__name = Slot(uri=RDFS.label, name="builtinFunc__name", curie=RDFS.curie('label'),
                   model_uri=OPENPOLICYAGENT.builtinFunc__name, domain=None, range=str)

slots.callDynamicStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="callDynamicStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.callDynamicStmt__col, domain=None, range=int)

slots.callDynamicStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="callDynamicStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.callDynamicStmt__file, domain=None, range=int)

slots.callDynamicStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="callDynamicStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.callDynamicStmt__row, domain=None, range=int)

slots.callDynamicStmt__args = Slot(uri=OPENPOLICYAGENT.args, name="callDynamicStmt__args", curie=OPENPOLICYAGENT.curie('args'),
                   model_uri=OPENPOLICYAGENT.callDynamicStmt__args, domain=None, range=Union[int, list[int]])

slots.callDynamicStmt__path = Slot(uri=OPENPOLICYAGENT.path, name="callDynamicStmt__path", curie=OPENPOLICYAGENT.curie('path'),
                   model_uri=OPENPOLICYAGENT.callDynamicStmt__path, domain=None, range=Union[Union[dict, Operand], list[Union[dict, Operand]]])

slots.callDynamicStmt__result = Slot(uri=OPENPOLICYAGENT.result, name="callDynamicStmt__result", curie=OPENPOLICYAGENT.curie('result'),
                   model_uri=OPENPOLICYAGENT.callDynamicStmt__result, domain=None, range=int)

slots.callStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="callStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.callStmt__col, domain=None, range=int)

slots.callStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="callStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.callStmt__file, domain=None, range=int)

slots.callStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="callStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.callStmt__row, domain=None, range=int)

slots.callStmt__args = Slot(uri=OPENPOLICYAGENT.args, name="callStmt__args", curie=OPENPOLICYAGENT.curie('args'),
                   model_uri=OPENPOLICYAGENT.callStmt__args, domain=None, range=Union[Union[dict, Operand], list[Union[dict, Operand]]])

slots.callStmt__func = Slot(uri=OPENPOLICYAGENT.func, name="callStmt__func", curie=OPENPOLICYAGENT.curie('func'),
                   model_uri=OPENPOLICYAGENT.callStmt__func, domain=None, range=str)

slots.callStmt__result = Slot(uri=OPENPOLICYAGENT.result, name="callStmt__result", curie=OPENPOLICYAGENT.curie('result'),
                   model_uri=OPENPOLICYAGENT.callStmt__result, domain=None, range=int)

slots.dotStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="dotStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.dotStmt__col, domain=None, range=int)

slots.dotStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="dotStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.dotStmt__file, domain=None, range=int)

slots.dotStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="dotStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.dotStmt__row, domain=None, range=int)

slots.dotStmt__key = Slot(uri=OPENPOLICYAGENT.key, name="dotStmt__key", curie=OPENPOLICYAGENT.curie('key'),
                   model_uri=OPENPOLICYAGENT.dotStmt__key, domain=None, range=Union[dict, Operand])

slots.dotStmt__source = Slot(uri=OPENPOLICYAGENT.source, name="dotStmt__source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.dotStmt__source, domain=None, range=Union[dict, Operand])

slots.dotStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="dotStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.dotStmt__target, domain=None, range=int)

slots.equalStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="equalStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.equalStmt__col, domain=None, range=int)

slots.equalStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="equalStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.equalStmt__file, domain=None, range=int)

slots.equalStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="equalStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.equalStmt__row, domain=None, range=int)

slots.equalStmt__a = Slot(uri=OPENPOLICYAGENT.a, name="equalStmt__a", curie=OPENPOLICYAGENT.curie('a'),
                   model_uri=OPENPOLICYAGENT.equalStmt__a, domain=None, range=Union[dict, Operand])

slots.equalStmt__b = Slot(uri=OPENPOLICYAGENT.b, name="equalStmt__b", curie=OPENPOLICYAGENT.curie('b'),
                   model_uri=OPENPOLICYAGENT.equalStmt__b, domain=None, range=Union[dict, Operand])

slots.func__blocks = Slot(uri=OPENPOLICYAGENT.blocks, name="func__blocks", curie=OPENPOLICYAGENT.curie('blocks'),
                   model_uri=OPENPOLICYAGENT.func__blocks, domain=None, range=Union[Union[dict, Block], list[Union[dict, Block]]])

slots.func__name = Slot(uri=RDFS.label, name="func__name", curie=RDFS.curie('label'),
                   model_uri=OPENPOLICYAGENT.func__name, domain=None, range=str)

slots.func__params = Slot(uri=OPENPOLICYAGENT.params, name="func__params", curie=OPENPOLICYAGENT.curie('params'),
                   model_uri=OPENPOLICYAGENT.func__params, domain=None, range=Union[int, list[int]])

slots.func__path = Slot(uri=OPENPOLICYAGENT.path, name="func__path", curie=OPENPOLICYAGENT.curie('path'),
                   model_uri=OPENPOLICYAGENT.func__path, domain=None, range=Optional[Union[str, list[str]]])

slots.func__return_value = Slot(uri=OPENPOLICYAGENT.return_value, name="func__return_value", curie=OPENPOLICYAGENT.curie('return_value'),
                   model_uri=OPENPOLICYAGENT.func__return_value, domain=None, range=int)

slots.funcs__funcs = Slot(uri=OPENPOLICYAGENT.funcs, name="funcs__funcs", curie=OPENPOLICYAGENT.curie('funcs'),
                   model_uri=OPENPOLICYAGENT.funcs__funcs, domain=None, range=Union[Union[dict, Func], list[Union[dict, Func]]])

slots.isArrayStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="isArrayStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.isArrayStmt__col, domain=None, range=int)

slots.isArrayStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="isArrayStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.isArrayStmt__file, domain=None, range=int)

slots.isArrayStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="isArrayStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.isArrayStmt__row, domain=None, range=int)

slots.isArrayStmt__source = Slot(uri=OPENPOLICYAGENT.source, name="isArrayStmt__source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.isArrayStmt__source, domain=None, range=Union[dict, Operand])

slots.isDefinedStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="isDefinedStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.isDefinedStmt__col, domain=None, range=int)

slots.isDefinedStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="isDefinedStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.isDefinedStmt__file, domain=None, range=int)

slots.isDefinedStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="isDefinedStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.isDefinedStmt__row, domain=None, range=int)

slots.isDefinedStmt__source = Slot(uri=OPENPOLICYAGENT.source, name="isDefinedStmt__source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.isDefinedStmt__source, domain=None, range=int)

slots.isObjectStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="isObjectStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.isObjectStmt__col, domain=None, range=int)

slots.isObjectStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="isObjectStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.isObjectStmt__file, domain=None, range=int)

slots.isObjectStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="isObjectStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.isObjectStmt__row, domain=None, range=int)

slots.isObjectStmt__source = Slot(uri=OPENPOLICYAGENT.source, name="isObjectStmt__source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.isObjectStmt__source, domain=None, range=Union[dict, Operand])

slots.isSetStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="isSetStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.isSetStmt__col, domain=None, range=int)

slots.isSetStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="isSetStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.isSetStmt__file, domain=None, range=int)

slots.isSetStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="isSetStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.isSetStmt__row, domain=None, range=int)

slots.isSetStmt__source = Slot(uri=OPENPOLICYAGENT.source, name="isSetStmt__source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.isSetStmt__source, domain=None, range=Union[dict, Operand])

slots.isUndefinedStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="isUndefinedStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.isUndefinedStmt__col, domain=None, range=int)

slots.isUndefinedStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="isUndefinedStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.isUndefinedStmt__file, domain=None, range=int)

slots.isUndefinedStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="isUndefinedStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.isUndefinedStmt__row, domain=None, range=int)

slots.isUndefinedStmt__source = Slot(uri=OPENPOLICYAGENT.source, name="isUndefinedStmt__source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.isUndefinedStmt__source, domain=None, range=int)

slots.lenStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="lenStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.lenStmt__col, domain=None, range=int)

slots.lenStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="lenStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.lenStmt__file, domain=None, range=int)

slots.lenStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="lenStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.lenStmt__row, domain=None, range=int)

slots.lenStmt__source = Slot(uri=OPENPOLICYAGENT.source, name="lenStmt__source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.lenStmt__source, domain=None, range=Union[dict, Operand])

slots.lenStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="lenStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.lenStmt__target, domain=None, range=int)

slots.makeArrayStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="makeArrayStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.makeArrayStmt__col, domain=None, range=int)

slots.makeArrayStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="makeArrayStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.makeArrayStmt__file, domain=None, range=int)

slots.makeArrayStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="makeArrayStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.makeArrayStmt__row, domain=None, range=int)

slots.makeArrayStmt__capacity = Slot(uri=OPENPOLICYAGENT.capacity, name="makeArrayStmt__capacity", curie=OPENPOLICYAGENT.curie('capacity'),
                   model_uri=OPENPOLICYAGENT.makeArrayStmt__capacity, domain=None, range=int)

slots.makeArrayStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="makeArrayStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.makeArrayStmt__target, domain=None, range=int)

slots.makeNullStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="makeNullStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.makeNullStmt__col, domain=None, range=int)

slots.makeNullStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="makeNullStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.makeNullStmt__file, domain=None, range=int)

slots.makeNullStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="makeNullStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.makeNullStmt__row, domain=None, range=int)

slots.makeNullStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="makeNullStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.makeNullStmt__target, domain=None, range=int)

slots.makeNumberIntStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="makeNumberIntStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.makeNumberIntStmt__col, domain=None, range=int)

slots.makeNumberIntStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="makeNumberIntStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.makeNumberIntStmt__file, domain=None, range=int)

slots.makeNumberIntStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="makeNumberIntStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.makeNumberIntStmt__row, domain=None, range=int)

slots.makeNumberIntStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="makeNumberIntStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.makeNumberIntStmt__target, domain=None, range=int)

slots.makeNumberIntStmt__value = Slot(uri=OPENPOLICYAGENT.value, name="makeNumberIntStmt__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.makeNumberIntStmt__value, domain=None, range=int)

slots.makeNumberRefStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="makeNumberRefStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.makeNumberRefStmt__col, domain=None, range=int)

slots.makeNumberRefStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="makeNumberRefStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.makeNumberRefStmt__file, domain=None, range=int)

slots.makeNumberRefStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="makeNumberRefStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.makeNumberRefStmt__row, domain=None, range=int)

slots.makeNumberRefStmt__index = Slot(uri=OPENPOLICYAGENT.index, name="makeNumberRefStmt__index", curie=OPENPOLICYAGENT.curie('index'),
                   model_uri=OPENPOLICYAGENT.makeNumberRefStmt__index, domain=None, range=int)

slots.makeNumberRefStmt__Index = Slot(uri=OPENPOLICYAGENT.Index, name="makeNumberRefStmt__Index", curie=OPENPOLICYAGENT.curie('Index'),
                   model_uri=OPENPOLICYAGENT.makeNumberRefStmt__Index, domain=None, range=Optional[int])

slots.makeNumberRefStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="makeNumberRefStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.makeNumberRefStmt__target, domain=None, range=int)

slots.makeObjectStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="makeObjectStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.makeObjectStmt__col, domain=None, range=int)

slots.makeObjectStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="makeObjectStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.makeObjectStmt__file, domain=None, range=int)

slots.makeObjectStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="makeObjectStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.makeObjectStmt__row, domain=None, range=int)

slots.makeObjectStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="makeObjectStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.makeObjectStmt__target, domain=None, range=int)

slots.makeSetStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="makeSetStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.makeSetStmt__col, domain=None, range=int)

slots.makeSetStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="makeSetStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.makeSetStmt__file, domain=None, range=int)

slots.makeSetStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="makeSetStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.makeSetStmt__row, domain=None, range=int)

slots.makeSetStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="makeSetStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.makeSetStmt__target, domain=None, range=int)

slots.nopStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="nopStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.nopStmt__col, domain=None, range=int)

slots.nopStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="nopStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.nopStmt__file, domain=None, range=int)

slots.nopStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="nopStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.nopStmt__row, domain=None, range=int)

slots.notEqualStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="notEqualStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.notEqualStmt__col, domain=None, range=int)

slots.notEqualStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="notEqualStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.notEqualStmt__file, domain=None, range=int)

slots.notEqualStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="notEqualStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.notEqualStmt__row, domain=None, range=int)

slots.notEqualStmt__a = Slot(uri=OPENPOLICYAGENT.a, name="notEqualStmt__a", curie=OPENPOLICYAGENT.curie('a'),
                   model_uri=OPENPOLICYAGENT.notEqualStmt__a, domain=None, range=Union[dict, Operand])

slots.notEqualStmt__b = Slot(uri=OPENPOLICYAGENT.b, name="notEqualStmt__b", curie=OPENPOLICYAGENT.curie('b'),
                   model_uri=OPENPOLICYAGENT.notEqualStmt__b, domain=None, range=Union[dict, Operand])

slots.notStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="notStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.notStmt__col, domain=None, range=int)

slots.notStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="notStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.notStmt__file, domain=None, range=int)

slots.notStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="notStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.notStmt__row, domain=None, range=int)

slots.notStmt__block = Slot(uri=OPENPOLICYAGENT.block, name="notStmt__block", curie=OPENPOLICYAGENT.curie('block'),
                   model_uri=OPENPOLICYAGENT.notStmt__block, domain=None, range=str)

slots.objectInsertOnceStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="objectInsertOnceStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.objectInsertOnceStmt__col, domain=None, range=int)

slots.objectInsertOnceStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="objectInsertOnceStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.objectInsertOnceStmt__file, domain=None, range=int)

slots.objectInsertOnceStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="objectInsertOnceStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.objectInsertOnceStmt__row, domain=None, range=int)

slots.objectInsertOnceStmt__key = Slot(uri=OPENPOLICYAGENT.key, name="objectInsertOnceStmt__key", curie=OPENPOLICYAGENT.curie('key'),
                   model_uri=OPENPOLICYAGENT.objectInsertOnceStmt__key, domain=None, range=Union[dict, Operand])

slots.objectInsertOnceStmt__object = Slot(uri=OPENPOLICYAGENT.object, name="objectInsertOnceStmt__object", curie=OPENPOLICYAGENT.curie('object'),
                   model_uri=OPENPOLICYAGENT.objectInsertOnceStmt__object, domain=None, range=int)

slots.objectInsertOnceStmt__value = Slot(uri=OPENPOLICYAGENT.value, name="objectInsertOnceStmt__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.objectInsertOnceStmt__value, domain=None, range=Union[dict, Operand])

slots.objectInsertStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="objectInsertStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.objectInsertStmt__col, domain=None, range=int)

slots.objectInsertStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="objectInsertStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.objectInsertStmt__file, domain=None, range=int)

slots.objectInsertStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="objectInsertStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.objectInsertStmt__row, domain=None, range=int)

slots.objectInsertStmt__key = Slot(uri=OPENPOLICYAGENT.key, name="objectInsertStmt__key", curie=OPENPOLICYAGENT.curie('key'),
                   model_uri=OPENPOLICYAGENT.objectInsertStmt__key, domain=None, range=Union[dict, Operand])

slots.objectInsertStmt__object = Slot(uri=OPENPOLICYAGENT.object, name="objectInsertStmt__object", curie=OPENPOLICYAGENT.curie('object'),
                   model_uri=OPENPOLICYAGENT.objectInsertStmt__object, domain=None, range=int)

slots.objectInsertStmt__value = Slot(uri=OPENPOLICYAGENT.value, name="objectInsertStmt__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.objectInsertStmt__value, domain=None, range=Union[dict, Operand])

slots.objectMergeStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="objectMergeStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.objectMergeStmt__col, domain=None, range=int)

slots.objectMergeStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="objectMergeStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.objectMergeStmt__file, domain=None, range=int)

slots.objectMergeStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="objectMergeStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.objectMergeStmt__row, domain=None, range=int)

slots.objectMergeStmt__a = Slot(uri=OPENPOLICYAGENT.a, name="objectMergeStmt__a", curie=OPENPOLICYAGENT.curie('a'),
                   model_uri=OPENPOLICYAGENT.objectMergeStmt__a, domain=None, range=int)

slots.objectMergeStmt__b = Slot(uri=OPENPOLICYAGENT.b, name="objectMergeStmt__b", curie=OPENPOLICYAGENT.curie('b'),
                   model_uri=OPENPOLICYAGENT.objectMergeStmt__b, domain=None, range=int)

slots.objectMergeStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="objectMergeStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.objectMergeStmt__target, domain=None, range=int)

slots.plan__blocks = Slot(uri=OPENPOLICYAGENT.blocks, name="plan__blocks", curie=OPENPOLICYAGENT.curie('blocks'),
                   model_uri=OPENPOLICYAGENT.plan__blocks, domain=None, range=Union[Union[dict, Block], list[Union[dict, Block]]])

slots.plan__name = Slot(uri=RDFS.label, name="plan__name", curie=RDFS.curie('label'),
                   model_uri=OPENPOLICYAGENT.plan__name, domain=None, range=str)

slots.plans__plans = Slot(uri=OPENPOLICYAGENT.plans, name="plans__plans", curie=OPENPOLICYAGENT.curie('plans'),
                   model_uri=OPENPOLICYAGENT.plans__plans, domain=None, range=Union[Union[dict, Plan], list[Union[dict, Plan]]])

slots.policy__funcs = Slot(uri=OPENPOLICYAGENT.funcs, name="policy__funcs", curie=OPENPOLICYAGENT.curie('funcs'),
                   model_uri=OPENPOLICYAGENT.policy__funcs, domain=None, range=Optional[Union[dict, Funcs]])

slots.policy__plans = Slot(uri=OPENPOLICYAGENT.plans, name="policy__plans", curie=OPENPOLICYAGENT.curie('plans'),
                   model_uri=OPENPOLICYAGENT.policy__plans, domain=None, range=Optional[Union[dict, Plans]])

slots.policy__static = Slot(uri=OPENPOLICYAGENT.static, name="policy__static", curie=OPENPOLICYAGENT.curie('static'),
                   model_uri=OPENPOLICYAGENT.policy__static, domain=None, range=Optional[Union[dict, Static]])

slots.resetLocalStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="resetLocalStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.resetLocalStmt__col, domain=None, range=int)

slots.resetLocalStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="resetLocalStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.resetLocalStmt__file, domain=None, range=int)

slots.resetLocalStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="resetLocalStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.resetLocalStmt__row, domain=None, range=int)

slots.resetLocalStmt__target = Slot(uri=OPENPOLICYAGENT.target, name="resetLocalStmt__target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.resetLocalStmt__target, domain=None, range=int)

slots.resultSetAddStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="resultSetAddStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.resultSetAddStmt__col, domain=None, range=int)

slots.resultSetAddStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="resultSetAddStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.resultSetAddStmt__file, domain=None, range=int)

slots.resultSetAddStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="resultSetAddStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.resultSetAddStmt__row, domain=None, range=int)

slots.resultSetAddStmt__value = Slot(uri=OPENPOLICYAGENT.value, name="resultSetAddStmt__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.resultSetAddStmt__value, domain=None, range=int)

slots.returnLocalStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="returnLocalStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.returnLocalStmt__col, domain=None, range=int)

slots.returnLocalStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="returnLocalStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.returnLocalStmt__file, domain=None, range=int)

slots.returnLocalStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="returnLocalStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.returnLocalStmt__row, domain=None, range=int)

slots.returnLocalStmt__source = Slot(uri=OPENPOLICYAGENT.source, name="returnLocalStmt__source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.returnLocalStmt__source, domain=None, range=int)

slots.scanStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="scanStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.scanStmt__col, domain=None, range=int)

slots.scanStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="scanStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.scanStmt__file, domain=None, range=int)

slots.scanStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="scanStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.scanStmt__row, domain=None, range=int)

slots.scanStmt__block = Slot(uri=OPENPOLICYAGENT.block, name="scanStmt__block", curie=OPENPOLICYAGENT.curie('block'),
                   model_uri=OPENPOLICYAGENT.scanStmt__block, domain=None, range=str)

slots.scanStmt__key = Slot(uri=OPENPOLICYAGENT.key, name="scanStmt__key", curie=OPENPOLICYAGENT.curie('key'),
                   model_uri=OPENPOLICYAGENT.scanStmt__key, domain=None, range=int)

slots.scanStmt__source = Slot(uri=OPENPOLICYAGENT.source, name="scanStmt__source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.scanStmt__source, domain=None, range=int)

slots.scanStmt__value = Slot(uri=OPENPOLICYAGENT.value, name="scanStmt__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.scanStmt__value, domain=None, range=int)

slots.setAddStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="setAddStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.setAddStmt__col, domain=None, range=int)

slots.setAddStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="setAddStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.setAddStmt__file, domain=None, range=int)

slots.setAddStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="setAddStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.setAddStmt__row, domain=None, range=int)

slots.setAddStmt__set = Slot(uri=OPENPOLICYAGENT.set, name="setAddStmt__set", curie=OPENPOLICYAGENT.curie('set'),
                   model_uri=OPENPOLICYAGENT.setAddStmt__set, domain=None, range=int)

slots.setAddStmt__value = Slot(uri=OPENPOLICYAGENT.value, name="setAddStmt__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.setAddStmt__value, domain=None, range=Union[dict, Operand])

slots.static__builtin_funcs = Slot(uri=OPENPOLICYAGENT.builtin_funcs, name="static__builtin_funcs", curie=OPENPOLICYAGENT.curie('builtin_funcs'),
                   model_uri=OPENPOLICYAGENT.static__builtin_funcs, domain=None, range=Optional[Union[Union[dict, BuiltinFunc], list[Union[dict, BuiltinFunc]]]])

slots.static__files = Slot(uri=OPENPOLICYAGENT.files, name="static__files", curie=OPENPOLICYAGENT.curie('files'),
                   model_uri=OPENPOLICYAGENT.static__files, domain=None, range=Optional[Union[Union[dict, StringConst], list[Union[dict, StringConst]]]])

slots.static__strings = Slot(uri=OPENPOLICYAGENT.strings, name="static__strings", curie=OPENPOLICYAGENT.curie('strings'),
                   model_uri=OPENPOLICYAGENT.static__strings, domain=None, range=Optional[Union[Union[dict, StringConst], list[Union[dict, StringConst]]]])

slots.stmt__type = Slot(uri=OPENPOLICYAGENT.type, name="stmt__type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.stmt__type, domain=None, range=Union[str, "StmtTag"])

slots.stmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="stmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.stmt__stmt, domain=None, range=Union[dict, Any])

slots.stringConst__value = Slot(uri=OPENPOLICYAGENT.value, name="stringConst__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.stringConst__value, domain=None, range=str)

slots.val__type = Slot(uri=OPENPOLICYAGENT.type, name="val__type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.val__type, domain=None, range=Union[str, "ValTag"])

slots.val__value = Slot(uri=OPENPOLICYAGENT.value, name="val__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.val__value, domain=None, range=Union[dict, Any])

slots.withStmt__col = Slot(uri=OPENPOLICYAGENT.col, name="withStmt__col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.withStmt__col, domain=None, range=int)

slots.withStmt__file = Slot(uri=OPENPOLICYAGENT.file, name="withStmt__file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.withStmt__file, domain=None, range=int)

slots.withStmt__row = Slot(uri=OPENPOLICYAGENT.row, name="withStmt__row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.withStmt__row, domain=None, range=int)

slots.withStmt__block = Slot(uri=OPENPOLICYAGENT.block, name="withStmt__block", curie=OPENPOLICYAGENT.curie('block'),
                   model_uri=OPENPOLICYAGENT.withStmt__block, domain=None, range=str)

slots.withStmt__local = Slot(uri=OPENPOLICYAGENT.local, name="withStmt__local", curie=OPENPOLICYAGENT.curie('local'),
                   model_uri=OPENPOLICYAGENT.withStmt__local, domain=None, range=int)

slots.withStmt__path = Slot(uri=OPENPOLICYAGENT.path, name="withStmt__path", curie=OPENPOLICYAGENT.curie('path'),
                   model_uri=OPENPOLICYAGENT.withStmt__path, domain=None, range=Union[int, list[int]])

slots.withStmt__value = Slot(uri=OPENPOLICYAGENT.value, name="withStmt__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.withStmt__value, domain=None, range=Union[dict, Operand])
