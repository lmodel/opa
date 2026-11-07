# Auto generated from opa.yaml by pythongen.py version: 0.0.1
# Schema: opa
#
# id: https://w3id.org/lmodel/opa
# description: A LinkML model of the JSON formats Open Policy Agent defines: the IR plan, the bundle manifest, the authorization policy input, the capabilities document, the built-in function metadata and the version index. Each module renders one format, and keeps OPA's keys, so a document OPA writes validates against this schema unchanged. The lokf adapt copy renames six keys LOKF defines with another meaning.
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

metamodel_version = "1.12.0"
version = "1.22.2"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OPA_MANIFEST = CurieNamespace('opa_manifest', 'https://openpolicyagent.org/schemas/bundle/v1/manifest.schema.json#/$defs/')
OPA_PLAN = CurieNamespace('opa_plan', 'https://openpolicyagent.org/schemas/ir/v1/plan.schema.json#/$defs/')
OPENPOLICYAGENT = CurieNamespace('openpolicyagent', 'https://w3id.org/lmodel/opa/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = OPENPOLICYAGENT


# Types

# Class references
class OpaBuiltinCategoryName(extended_str):
    pass


class OpaImplementationSupportImplementation(extended_str):
    pass


class OpaVersionEntryName(extended_str):
    pass


class OpaFileRegoVersionPath(extended_str):
    pass


class OpaObject(YAMLRoot):
    """
    A JSON object whose keys OPA leaves open.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaObject"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaObject"
    class_name: ClassVar[str] = "OpaObject"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaObject


OpaValue = Any

class OpaStringListMap(YAMLRoot):
    """
    An object whose every value is a list of strings, as Go writes HTTP headers and query parameters.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaStringListMap"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaStringListMap"
    class_name: ClassVar[str] = "OpaStringListMap"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaStringListMap


@dataclass(repr=False)
class OpaType(YAMLRoot):
    """
    A Rego type, as OPA's types package writes it in JSON. A named type is an argument or result of a built-in
    function, with a name and a description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaType"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaType"
    class_name: ClassVar[str] = "OpaType"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaType

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaAnyType(OpaType):
    """
    A union of the types it lists in `of`, or any value when it lists none.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaAnyType"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaAnyType"
    class_name: ClassVar[str] = "OpaAnyType"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaAnyType

    type: str = None
    of: Optional[Union[Union[dict, OpaType], list[Union[dict, OpaType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.of, list):
            self.of = [self.of] if self.of is not None else []
        self.of = [v if isinstance(v, OpaType) else OpaType(**as_dict(v)) for v in self.of]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaArrayType(OpaType):
    """
    An array, with a type per position in `static` and one for the rest in `dynamic`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaArrayType"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaArrayType"
    class_name: ClassVar[str] = "OpaArrayType"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaArrayType

    type: str = None
    static: Optional[Union[Union[dict, OpaType], list[Union[dict, OpaType]]]] = empty_list()
    dynamic: Optional[Union[dict, OpaType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.static, list):
            self.static = [self.static] if self.static is not None else []
        self.static = [v if isinstance(v, OpaType) else OpaType(**as_dict(v)) for v in self.static]

        if self.dynamic is not None and not isinstance(self.dynamic, OpaType):
            self.dynamic = OpaType(**as_dict(self.dynamic))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBooleanType(OpaType):
    """
    A boolean.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBooleanType"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBooleanType"
    class_name: ClassVar[str] = "OpaBooleanType"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBooleanType

    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaFunctionType(OpaType):
    """
    A function, with its arguments, its result and a variadic argument type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaFunctionType"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaFunctionType"
    class_name: ClassVar[str] = "OpaFunctionType"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaFunctionType

    type: str = None
    args: Optional[Union[Union[dict, OpaType], list[Union[dict, OpaType]]]] = empty_list()
    result: Optional[Union[dict, OpaType]] = None
    variadic: Optional[Union[dict, OpaType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.args, list):
            self.args = [self.args] if self.args is not None else []
        self.args = [v if isinstance(v, OpaType) else OpaType(**as_dict(v)) for v in self.args]

        if self.result is not None and not isinstance(self.result, OpaType):
            self.result = OpaType(**as_dict(self.result))

        if self.variadic is not None and not isinstance(self.variadic, OpaType):
            self.variadic = OpaType(**as_dict(self.variadic))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaNullType(OpaType):
    """
    The null value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaNullType"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaNullType"
    class_name: ClassVar[str] = "OpaNullType"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaNullType

    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaNumberType(OpaType):
    """
    A number.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaNumberType"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaNumberType"
    class_name: ClassVar[str] = "OpaNumberType"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaNumberType

    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaObjectType(OpaType):
    """
    An object, with typed known keys in `static` and a key and value type for the rest in `dynamic`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaObjectType"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaObjectType"
    class_name: ClassVar[str] = "OpaObjectType"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaObjectType

    type: str = None
    static: Optional[Union[Union[dict, "OpaStaticProperty"], list[Union[dict, "OpaStaticProperty"]]]] = empty_list()
    dynamic: Optional[Union[dict, "OpaDynamicProperty"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.static, list):
            self.static = [self.static] if self.static is not None else []
        self.static = [v if isinstance(v, OpaStaticProperty) else OpaStaticProperty(**as_dict(v)) for v in self.static]

        if self.dynamic is not None and not isinstance(self.dynamic, OpaDynamicProperty):
            self.dynamic = OpaDynamicProperty(**as_dict(self.dynamic))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaSetType(OpaType):
    """
    A set, whose members have the type in `of`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaSetType"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaSetType"
    class_name: ClassVar[str] = "OpaSetType"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaSetType

    type: str = None
    of: Optional[Union[dict, OpaType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.of is not None and not isinstance(self.of, OpaType):
            self.of = OpaType(**as_dict(self.of))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaStringType(OpaType):
    """
    A string.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaStringType"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaStringType"
    class_name: ClassVar[str] = "OpaStringType"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaStringType

    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaStaticProperty(YAMLRoot):
    """
    A known key of an object type and the type of its value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaStaticProperty"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaStaticProperty"
    class_name: ClassVar[str] = "OpaStaticProperty"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaStaticProperty

    key: Union[dict, OpaValue] = None
    value: Union[dict, OpaType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, (OpaValue,)):
            value = self.key
            for _coerce in (lambda: OpaValue(),):
                try:
                    self.key = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types OpaValue could be constructed from {value!r} for slot key")

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, OpaType):
            self.value = OpaType(**as_dict(self.value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaDynamicProperty(YAMLRoot):
    """
    The key type and value type that an object type gives its other keys.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaDynamicProperty"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaDynamicProperty"
    class_name: ClassVar[str] = "OpaDynamicProperty"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaDynamicProperty

    key: Union[dict, OpaType] = None
    value: Union[dict, OpaType] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, OpaType):
            self.key = OpaType(**as_dict(self.key))

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, OpaType):
            self.value = OpaType(**as_dict(self.value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaCapabilities(YAMLRoot):
    """
    What an OPA version supports, which a policy can be checked against.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaCapabilities"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaCapabilities"
    class_name: ClassVar[str] = "OpaCapabilities"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaCapabilities

    builtins: Optional[Union[Union[dict, "OpaBuiltin"], list[Union[dict, "OpaBuiltin"]]]] = empty_list()
    future_keywords: Optional[Union[Union[str, "OpaFutureKeyword"], list[Union[str, "OpaFutureKeyword"]]]] = empty_list()
    wasm_abi_versions: Optional[Union[Union[dict, "OpaWasmAbiVersion"], list[Union[dict, "OpaWasmAbiVersion"]]]] = empty_list()
    features: Optional[Union[Union[str, "OpaFeature"], list[Union[str, "OpaFeature"]]]] = empty_list()
    allow_net: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="builtins", slot_type=OpaBuiltin, key_name="name", keyed=False)

        if not isinstance(self.future_keywords, list):
            self.future_keywords = [self.future_keywords] if self.future_keywords is not None else []
        self.future_keywords = [v if isinstance(v, OpaFutureKeyword) else OpaFutureKeyword(v) for v in self.future_keywords]

        self._normalize_inlined_as_list(slot_name="wasm_abi_versions", slot_type=OpaWasmAbiVersion, key_name="version", keyed=False)

        if not isinstance(self.features, list):
            self.features = [self.features] if self.features is not None else []
        self.features = [v if isinstance(v, OpaFeature) else OpaFeature(v) for v in self.features]

        if not isinstance(self.allow_net, list):
            self.allow_net = [self.allow_net] if self.allow_net is not None else []
        self.allow_net = [v if isinstance(v, str) else str(v) for v in self.allow_net]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBuiltin(YAMLRoot):
    """
    A built-in function and its type declaration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBuiltin"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBuiltin"
    class_name: ClassVar[str] = "OpaBuiltin"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBuiltin

    name: str = None
    decl: Union[dict, OpaFunctionType] = None
    description: Optional[str] = None
    categories: Optional[Union[str, list[str]]] = empty_list()
    infix: Optional[str] = None
    relation: Optional[Union[bool, Bool]] = None
    deprecated: Optional[Union[bool, Bool]] = None
    nondeterministic: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.decl):
            self.MissingRequiredField("decl")
        if not isinstance(self.decl, OpaFunctionType):
            self.decl = OpaFunctionType(**as_dict(self.decl))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, str) else str(v) for v in self.categories]

        if self.infix is not None and not isinstance(self.infix, str):
            self.infix = str(self.infix)

        if self.relation is not None and not isinstance(self.relation, Bool):
            self.relation = Bool(self.relation)

        if self.deprecated is not None and not isinstance(self.deprecated, Bool):
            self.deprecated = Bool(self.deprecated)

        if self.nondeterministic is not None and not isinstance(self.nondeterministic, Bool):
            self.nondeterministic = Bool(self.nondeterministic)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaWasmAbiVersion(YAMLRoot):
    """
    A Wasm ABI version, as a major and a minor number.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaWasmAbiVersion"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaWasmAbiVersion"
    class_name: ClassVar[str] = "OpaWasmAbiVersion"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaWasmAbiVersion

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
class OpaBuiltinMetadataCatalog(YAMLRoot):
    """
    The catalogue: two keys that start with an underscore, and one key per built-in function, whose value describes it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBuiltinMetadataCatalog"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBuiltinMetadataCatalog"
    class_name: ClassVar[str] = "OpaBuiltinMetadataCatalog"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBuiltinMetadataCatalog

    _categories: Union[dict[Union[str, OpaBuiltinCategoryName], Union[dict, "OpaBuiltinCategory"]], list[Union[dict, "OpaBuiltinCategory"]]] = empty_dict()
    _implementations: Union[Union[dict, "OpaImplementation"], list[Union[dict, "OpaImplementation"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self._categories):
            self.MissingRequiredField("_categories")
        self._normalize_inlined_as_dict(slot_name="_categories", slot_type=OpaBuiltinCategory, key_name="name", keyed=True)

        if self._is_empty(self._implementations):
            self.MissingRequiredField("_implementations")
        self._normalize_inlined_as_list(slot_name="_implementations", slot_type=OpaImplementation, key_name="version", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBuiltinCategory(YAMLRoot):
    """
    A category of built-in functions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBuiltinCategory"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBuiltinCategory"
    class_name: ClassVar[str] = "OpaBuiltinCategory"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBuiltinCategory

    name: Union[str, OpaBuiltinCategoryName] = None
    builtins: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, OpaBuiltinCategoryName):
            self.name = OpaBuiltinCategoryName(self.name)

        if self._is_empty(self.builtins):
            self.MissingRequiredField("builtins")
        if not isinstance(self.builtins, list):
            self.builtins = [self.builtins] if self.builtins is not None else []
        self.builtins = [v if isinstance(v, str) else str(v) for v in self.builtins]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaImplementation(YAMLRoot):
    """
    An implementation of Rego besides OPA.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaImplementation"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaImplementation"
    class_name: ClassVar[str] = "OpaImplementation"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaImplementation

    version: str = None
    id: str = None
    label: str = None
    repo: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self._is_empty(self.repo):
            self.MissingRequiredField("repo")
        if not isinstance(self.repo, str):
            self.repo = str(self.repo)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBuiltinMetadata(YAMLRoot):
    """
    What the catalogue says about one built-in function.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBuiltinMetadata"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBuiltinMetadata"
    class_name: ClassVar[str] = "OpaBuiltinMetadata"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBuiltinMetadata

    introduced: str = None
    available: Union[str, list[str]] = None
    wasm: Union[bool, Bool] = None
    args: Union[Union[dict, "OpaBuiltinArgument"], list[Union[dict, "OpaBuiltinArgument"]]] = None
    result: Union[dict, "OpaBuiltinResult"] = None
    implementations: Union[dict[Union[str, OpaImplementationSupportImplementation], Union[dict, "OpaImplementationSupport"]], list[Union[dict, "OpaImplementationSupport"]]] = empty_dict()
    description: Optional[str] = None
    infix: Optional[str] = None
    relation: Optional[Union[bool, Bool]] = None
    deprecated: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.introduced):
            self.MissingRequiredField("introduced")
        if not isinstance(self.introduced, str):
            self.introduced = str(self.introduced)

        if self._is_empty(self.available):
            self.MissingRequiredField("available")
        if not isinstance(self.available, list):
            self.available = [self.available] if self.available is not None else []
        self.available = [v if isinstance(v, str) else str(v) for v in self.available]

        if self._is_empty(self.wasm):
            self.MissingRequiredField("wasm")
        if not isinstance(self.wasm, Bool):
            self.wasm = Bool(self.wasm)

        if self._is_empty(self.args):
            self.MissingRequiredField("args")
        self._normalize_inlined_as_list(slot_name="args", slot_type=OpaBuiltinArgument, key_name="type", keyed=False)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, OpaBuiltinResult):
            self.result = OpaBuiltinResult(**as_dict(self.result))

        if self._is_empty(self.implementations):
            self.MissingRequiredField("implementations")
        self._normalize_inlined_as_dict(slot_name="implementations", slot_type=OpaImplementationSupport, key_name="implementation", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.infix is not None and not isinstance(self.infix, str):
            self.infix = str(self.infix)

        if self.relation is not None and not isinstance(self.relation, Bool):
            self.relation = Bool(self.relation)

        if self.deprecated is not None and not isinstance(self.deprecated, Bool):
            self.deprecated = Bool(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBuiltinArgument(YAMLRoot):
    """
    An argument of a built-in function.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBuiltinArgument"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBuiltinArgument"
    class_name: ClassVar[str] = "OpaBuiltinArgument"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBuiltinArgument

    type: str = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBuiltinResult(YAMLRoot):
    """
    The result of a built-in function. Some functions declare none.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBuiltinResult"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBuiltinResult"
    class_name: ClassVar[str] = "OpaBuiltinResult"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBuiltinResult

    type: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaImplementationSupport(YAMLRoot):
    """
    An implementation that supports a function, and the version that added it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaImplementationSupport"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaImplementationSupport"
    class_name: ClassVar[str] = "OpaImplementationSupport"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaImplementationSupport

    implementation: Union[str, OpaImplementationSupportImplementation] = None
    version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.implementation):
            self.MissingRequiredField("implementation")
        if not isinstance(self.implementation, OpaImplementationSupportImplementation):
            self.implementation = OpaImplementationSupportImplementation(self.implementation)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaVersionIndex(YAMLRoot):
    """
    The version index.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaVersionIndex"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaVersionIndex"
    class_name: ClassVar[str] = "OpaVersionIndex"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaVersionIndex

    builtins: Union[dict[Union[str, OpaVersionEntryName], Union[dict, "OpaVersionEntry"]], list[Union[dict, "OpaVersionEntry"]]] = empty_dict()
    features: Union[dict[Union[str, OpaVersionEntryName], Union[dict, "OpaVersionEntry"]], list[Union[dict, "OpaVersionEntry"]]] = empty_dict()
    keywords: Union[dict[Union[str, OpaVersionEntryName], Union[dict, "OpaVersionEntry"]], list[Union[dict, "OpaVersionEntry"]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.builtins):
            self.MissingRequiredField("builtins")
        self._normalize_inlined_as_dict(slot_name="builtins", slot_type=OpaVersionEntry, key_name="name", keyed=True)

        if self._is_empty(self.features):
            self.MissingRequiredField("features")
        self._normalize_inlined_as_dict(slot_name="features", slot_type=OpaVersionEntry, key_name="name", keyed=True)

        if self._is_empty(self.keywords):
            self.MissingRequiredField("keywords")
        self._normalize_inlined_as_dict(slot_name="keywords", slot_type=OpaVersionEntry, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaVersionEntry(YAMLRoot):
    """
    A built-in function, feature or keyword, and the OPA version that introduced it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaVersionEntry"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaVersionEntry"
    class_name: ClassVar[str] = "OpaVersionEntry"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaVersionEntry

    name: Union[str, OpaVersionEntryName] = None
    Major: int = None
    Minor: int = None
    Patch: int = None
    PreRelease: Optional[str] = None
    Metadata: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, OpaVersionEntryName):
            self.name = OpaVersionEntryName(self.name)

        if self._is_empty(self.Major):
            self.MissingRequiredField("Major")
        if not isinstance(self.Major, int):
            self.Major = int(self.Major)

        if self._is_empty(self.Minor):
            self.MissingRequiredField("Minor")
        if not isinstance(self.Minor, int):
            self.Minor = int(self.Minor)

        if self._is_empty(self.Patch):
            self.MissingRequiredField("Patch")
        if not isinstance(self.Patch, int):
            self.Patch = int(self.Patch)

        if self.PreRelease is not None and not isinstance(self.PreRelease, str):
            self.PreRelease = str(self.PreRelease)

        if self.Metadata is not None and not isinstance(self.Metadata, str):
            self.Metadata = str(self.Metadata)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaAuthorizationInput(YAMLRoot):
    """
    The OPA Authorization Policy Input document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaAuthorizationInput"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaAuthorizationInput"
    class_name: ClassVar[str] = "OpaAuthorizationInput"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaAuthorizationInput

    method: str = None
    path: Union[str, list[str]] = None
    params: Union[dict, OpaStringListMap] = None
    headers: Union[dict, OpaStringListMap] = None
    body: Optional[Union[dict, OpaValue]] = None
    identity: Optional[str] = None
    client_certificates: Optional[Union[Union[dict, OpaObject], list[Union[dict, OpaObject]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.path):
            self.MissingRequiredField("path")
        if not isinstance(self.path, list):
            self.path = [self.path] if self.path is not None else []
        self.path = [v if isinstance(v, str) else str(v) for v in self.path]

        if self._is_empty(self.params):
            self.MissingRequiredField("params")
        if not isinstance(self.params, OpaStringListMap):
            self.params = OpaStringListMap()

        if self._is_empty(self.headers):
            self.MissingRequiredField("headers")
        if not isinstance(self.headers, OpaStringListMap):
            self.headers = OpaStringListMap()

        if self.body is not None and not isinstance(self.body, (OpaValue,)):
            value = self.body
            for _coerce in (lambda: OpaValue(),):
                try:
                    self.body = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types OpaValue could be constructed from {value!r} for slot body")

        if self.identity is not None and not isinstance(self.identity, str):
            self.identity = str(self.identity)

        if not isinstance(self.client_certificates, list):
            self.client_certificates = [self.client_certificates] if self.client_certificates is not None else []
        self.client_certificates = [v if isinstance(v, OpaObject) else OpaObject(**as_dict(v)) for v in self.client_certificates]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaManifest(YAMLRoot):
    """
    A bundle manifest. OPA's schema leaves the manifest open to other keys.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaManifest"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaManifest"
    class_name: ClassVar[str] = "OpaManifest"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaManifest

    revision: str = None
    file_rego_versions: Optional[Union[dict[Union[str, OpaFileRegoVersionPath], Union[dict, "OpaFileRegoVersion"]], list[Union[dict, "OpaFileRegoVersion"]]]] = empty_dict()
    metadata: Optional[Union[dict, OpaObject]] = None
    rego_version: Optional[int] = None
    roots: Optional[Union[str, list[str]]] = empty_list()
    wasm: Optional[Union[Union[dict, "OpaWasmResolver"], list[Union[dict, "OpaWasmResolver"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.revision):
            self.MissingRequiredField("revision")
        if not isinstance(self.revision, str):
            self.revision = str(self.revision)

        self._normalize_inlined_as_dict(slot_name="file_rego_versions", slot_type=OpaFileRegoVersion, key_name="path", keyed=True)

        if self.metadata is not None and not isinstance(self.metadata, OpaObject):
            self.metadata = OpaObject()

        if self.rego_version is not None and not isinstance(self.rego_version, int):
            self.rego_version = int(self.rego_version)

        if not isinstance(self.roots, list):
            self.roots = [self.roots] if self.roots is not None else []
        self.roots = [v if isinstance(v, str) else str(v) for v in self.roots]

        if not isinstance(self.wasm, list):
            self.wasm = [self.wasm] if self.wasm is not None else []
        self.wasm = [v if isinstance(v, OpaWasmResolver) else OpaWasmResolver(**as_dict(v)) for v in self.wasm]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaWasmResolver(YAMLRoot):
    """
    A Wasm module in a bundle, and the entrypoint it resolves.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaWasmResolver"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaWasmResolver"
    class_name: ClassVar[str] = "OpaWasmResolver"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaWasmResolver

    annotations: Optional[Union[Union[dict, OpaObject], list[Union[dict, OpaObject]]]] = empty_list()
    entrypoint: Optional[str] = None
    module: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.annotations, list):
            self.annotations = [self.annotations] if self.annotations is not None else []
        self.annotations = [v if isinstance(v, OpaObject) else OpaObject(**as_dict(v)) for v in self.annotations]

        if self.entrypoint is not None and not isinstance(self.entrypoint, str):
            self.entrypoint = str(self.entrypoint)

        if self.module is not None and not isinstance(self.module, str):
            self.module = str(self.module)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaFileRegoVersion(YAMLRoot):
    """
    The Rego version of one file in the bundle.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaFileRegoVersion"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaFileRegoVersion"
    class_name: ClassVar[str] = "OpaFileRegoVersion"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaFileRegoVersion

    path: Union[str, OpaFileRegoVersionPath] = None
    version: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.path):
            self.MissingRequiredField("path")
        if not isinstance(self.path, OpaFileRegoVersionPath):
            self.path = OpaFileRegoVersionPath(self.path)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, int):
            self.version = int(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaPolicy(YAMLRoot):
    """
    Policy represents a planned policy query.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaPolicy"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaPolicy"
    class_name: ClassVar[str] = "OpaPolicy"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaPolicy

    funcs: Optional[Union[dict, "OpaFuncs"]] = None
    plans: Optional[Union[dict, "OpaPlans"]] = None
    static: Optional[Union[dict, "OpaStatic"]] = None
    unplanned_rules: Optional[Union[Union[dict, "OpaUnplannedRule"], list[Union[dict, "OpaUnplannedRule"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.funcs is not None and not isinstance(self.funcs, OpaFuncs):
            self.funcs = OpaFuncs(**as_dict(self.funcs))

        if self.plans is not None and not isinstance(self.plans, OpaPlans):
            self.plans = OpaPlans(**as_dict(self.plans))

        if self.static is not None and not isinstance(self.static, OpaStatic):
            self.static = OpaStatic(**as_dict(self.static))

        self._normalize_inlined_as_list(slot_name="unplanned_rules", slot_type=OpaUnplannedRule, key_name="path", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaStatic(YAMLRoot):
    """
    Static represents a static data segment that is indexed into by the policy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaStatic"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaStatic"
    class_name: ClassVar[str] = "OpaStatic"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaStatic

    builtin_funcs: Optional[Union[Union[dict, "OpaBuiltinFunc"], list[Union[dict, "OpaBuiltinFunc"]]]] = empty_list()
    files: Optional[Union[Union[dict, "OpaStringConst"], list[Union[dict, "OpaStringConst"]]]] = empty_list()
    strings: Optional[Union[Union[dict, "OpaStringConst"], list[Union[dict, "OpaStringConst"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="builtin_funcs", slot_type=OpaBuiltinFunc, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="files", slot_type=OpaStringConst, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="strings", slot_type=OpaStringConst, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaStringConst(YAMLRoot):
    """
    StringConst represents a string value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaStringConst"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaStringConst"
    class_name: ClassVar[str] = "OpaStringConst"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaStringConst

    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBuiltinFunc(YAMLRoot):
    """
    BuiltinFunc represents a built-in function that may be required by the policy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBuiltinFunc"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBuiltinFunc"
    class_name: ClassVar[str] = "OpaBuiltinFunc"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBuiltinFunc

    name: str = None
    decl: Optional[Union[dict, OpaFunctionType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.decl is not None and not isinstance(self.decl, OpaFunctionType):
            self.decl = OpaFunctionType(**as_dict(self.decl))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaPlans(YAMLRoot):
    """
    Plans represents a collection of named query plans to expose in the policy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaPlans"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaPlans"
    class_name: ClassVar[str] = "OpaPlans"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaPlans

    plans: Optional[Union[Union[dict, "OpaPlan"], list[Union[dict, "OpaPlan"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="plans", slot_type=OpaPlan, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaPlan(YAMLRoot):
    """
    Plan represents an ordered series of blocks to execute. Plan execution stops when a return statement is reached.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaPlan"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaPlan"
    class_name: ClassVar[str] = "OpaPlan"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaPlan

    name: str = None
    blocks: Optional[Union[Union[dict, "OpaBlock"], list[Union[dict, "OpaBlock"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.blocks, list):
            self.blocks = [self.blocks] if self.blocks is not None else []
        self.blocks = [v if isinstance(v, OpaBlock) else OpaBlock(**as_dict(v)) for v in self.blocks]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaFuncs(YAMLRoot):
    """
    Funcs represents a collection of planned functions to include in the policy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaFuncs"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaFuncs"
    class_name: ClassVar[str] = "OpaFuncs"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaFuncs

    funcs: Optional[Union[Union[dict, "OpaFunc"], list[Union[dict, "OpaFunc"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="funcs", slot_type=OpaFunc, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaFunc(YAMLRoot):
    """
    Func represents a named plan (function) that can be invoked. Functions accept one or more parameters and return a
    value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaFunc"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaFunc"
    class_name: ClassVar[str] = "OpaFunc"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaFunc

    name: str = None
    return_: int = None
    blocks: Optional[Union[Union[dict, "OpaBlock"], list[Union[dict, "OpaBlock"]]]] = empty_list()
    params: Optional[Union[int, list[int]]] = empty_list()
    path: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.return_):
            self.MissingRequiredField("return_")
        if not isinstance(self.return_, int):
            self.return_ = int(self.return_)

        if not isinstance(self.blocks, list):
            self.blocks = [self.blocks] if self.blocks is not None else []
        self.blocks = [v if isinstance(v, OpaBlock) else OpaBlock(**as_dict(v)) for v in self.blocks]

        if not isinstance(self.params, list):
            self.params = [self.params] if self.params is not None else []
        self.params = [v if isinstance(v, int) else int(v) for v in self.params]

        if not isinstance(self.path, list):
            self.path = [self.path] if self.path is not None else []
        self.path = [v if isinstance(v, str) else str(v) for v in self.path]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBlock(YAMLRoot):
    """
    Block represents an ordered sequence of statements to execute. Blocks are executed until a return statement is
    encountered, a statement is undefined, or there are no more statements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBlock"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBlock"
    class_name: ClassVar[str] = "OpaBlock"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBlock

    stmts: Union[Union[dict, "OpaStmt"], list[Union[dict, "OpaStmt"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.stmts):
            self.MissingRequiredField("stmts")
        if not isinstance(self.stmts, list):
            self.stmts = [self.stmts] if self.stmts is not None else []
        self.stmts = [v if isinstance(v, OpaStmt) else OpaStmt(**as_dict(v)) for v in self.stmts]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaUnplannedRule(YAMLRoot):
    """
    UnplannedRule represents a rule that was parsed but not included in the plan because it is not reachable from the
    entrypoint. This is used for coverage reporting, to distinguish rules that were never planned from rules that were
    planned but never executed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaUnplannedRule"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaUnplannedRule"
    class_name: ClassVar[str] = "OpaUnplannedRule"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaUnplannedRule

    path: str = None
    location: Optional[Union[dict, "OpaLocation"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.path):
            self.MissingRequiredField("path")
        if not isinstance(self.path, str):
            self.path = str(self.path)

        if self.location is not None and not isinstance(self.location, OpaLocation):
            self.location = OpaLocation(**as_dict(self.location))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaLocation(YAMLRoot):
    """
    Location records the filen index, and the row and column inside that file that a statement can be connected to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaLocation"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaLocation"
    class_name: ClassVar[str] = "OpaLocation"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaLocation

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.end_col):
            self.MissingRequiredField("end_col")
        if not isinstance(self.end_col, int):
            self.end_col = int(self.end_col)

        if self._is_empty(self.end_row):
            self.MissingRequiredField("end_row")
        if not isinstance(self.end_row, int):
            self.end_row = int(self.end_row)

        super().__post_init__(**kwargs)


class OpaStmt(YAMLRoot):
    """
    Stmt represents an operation (e.g., comparison, loop, dot, etc.) to execute. OPA writes each statement as its kind
    in `type` and its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaStmt"
    class_name: ClassVar[str] = "OpaStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaStmt


@dataclass(repr=False)
class OpaStmtBody(YAMLRoot):
    """
    The fields of a statement. Every kind carries the location of its source text.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaStmtBody"
    class_name: ClassVar[str] = "OpaStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file):
            self.MissingRequiredField("file")
        if not isinstance(self.file, int):
            self.file = int(self.file)

        if self._is_empty(self.col):
            self.MissingRequiredField("col")
        if not isinstance(self.col, int):
            self.col = int(self.col)

        if self._is_empty(self.row):
            self.MissingRequiredField("row")
        if not isinstance(self.row, int):
            self.row = int(self.row)

        if self._is_empty(self.end_col):
            self.MissingRequiredField("end_col")
        if not isinstance(self.end_col, int):
            self.end_col = int(self.end_col)

        if self._is_empty(self.end_row):
            self.MissingRequiredField("end_row")
        if not isinstance(self.end_row, int):
            self.end_row = int(self.end_row)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaArrayAppendStmt(OpaStmt):
    """
    A statement of kind ArrayAppendStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaArrayAppendStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaArrayAppendStmt"
    class_name: ClassVar[str] = "OpaArrayAppendStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaArrayAppendStmt

    type: str = None
    stmt: Union[dict, "OpaArrayAppendStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaArrayAppendStmtBody):
            self.stmt = OpaArrayAppendStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaArrayAppendStmtBody(OpaStmtBody):
    """
    ArrayAppendStmt represents a dynamic append operation of a value onto an array.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaArrayAppendStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaArrayAppendStmtBody"
    class_name: ClassVar[str] = "OpaArrayAppendStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaArrayAppendStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    array: int = None
    value: Union[dict, "OpaOperand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.array):
            self.MissingRequiredField("array")
        if not isinstance(self.array, int):
            self.array = int(self.array)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, OpaOperand):
            self.value = OpaOperand()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaAssignIntStmt(OpaStmt):
    """
    A statement of kind AssignIntStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaAssignIntStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaAssignIntStmt"
    class_name: ClassVar[str] = "OpaAssignIntStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaAssignIntStmt

    type: str = None
    stmt: Union[dict, "OpaAssignIntStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaAssignIntStmtBody):
            self.stmt = OpaAssignIntStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaAssignIntStmtBody(OpaStmtBody):
    """
    AssignIntStmt represents an assignment of an integer value to a local variable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaAssignIntStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaAssignIntStmtBody"
    class_name: ClassVar[str] = "OpaAssignIntStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaAssignIntStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    target: int = None
    value: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
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
class OpaAssignVarOnceStmt(OpaStmt):
    """
    A statement of kind AssignVarOnceStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaAssignVarOnceStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaAssignVarOnceStmt"
    class_name: ClassVar[str] = "OpaAssignVarOnceStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaAssignVarOnceStmt

    type: str = None
    stmt: Union[dict, "OpaAssignVarOnceStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaAssignVarOnceStmtBody):
            self.stmt = OpaAssignVarOnceStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaAssignVarOnceStmtBody(OpaStmtBody):
    """
    AssignVarOnceStmt represents an assignment of one local variable to another. If the target is defined, execution
    aborts with a conflict error.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaAssignVarOnceStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaAssignVarOnceStmtBody"
    class_name: ClassVar[str] = "OpaAssignVarOnceStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaAssignVarOnceStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    source: Union[dict, "OpaOperand"] = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, OpaOperand):
            self.source = OpaOperand()

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaAssignVarStmt(OpaStmt):
    """
    A statement of kind AssignVarStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaAssignVarStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaAssignVarStmt"
    class_name: ClassVar[str] = "OpaAssignVarStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaAssignVarStmt

    type: str = None
    stmt: Union[dict, "OpaAssignVarStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaAssignVarStmtBody):
            self.stmt = OpaAssignVarStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaAssignVarStmtBody(OpaStmtBody):
    """
    AssignVarStmt represents an assignment of one local variable to another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaAssignVarStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaAssignVarStmtBody"
    class_name: ClassVar[str] = "OpaAssignVarStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaAssignVarStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    source: Union[dict, "OpaOperand"] = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, OpaOperand):
            self.source = OpaOperand()

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBlockStmt(OpaStmt):
    """
    A statement of kind BlockStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBlockStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBlockStmt"
    class_name: ClassVar[str] = "OpaBlockStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBlockStmt

    type: str = None
    stmt: Union[dict, "OpaBlockStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaBlockStmtBody):
            self.stmt = OpaBlockStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBlockStmtBody(OpaStmtBody):
    """
    BlockStmt represents a nested block. Nested blocks and break statements can be used to short-circuit execution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBlockStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBlockStmtBody"
    class_name: ClassVar[str] = "OpaBlockStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBlockStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    blocks: Optional[Union[Union[dict, OpaBlock], list[Union[dict, OpaBlock]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.blocks, list):
            self.blocks = [self.blocks] if self.blocks is not None else []
        self.blocks = [v if isinstance(v, OpaBlock) else OpaBlock(**as_dict(v)) for v in self.blocks]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBreakStmt(OpaStmt):
    """
    A statement of kind BreakStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBreakStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBreakStmt"
    class_name: ClassVar[str] = "OpaBreakStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBreakStmt

    type: str = None
    stmt: Union[dict, "OpaBreakStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaBreakStmtBody):
            self.stmt = OpaBreakStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaBreakStmtBody(OpaStmtBody):
    """
    BreakStmt represents a jump out of the current block. The index specifies how many blocks to jump starting from
    zero (the current block).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBreakStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBreakStmtBody"
    class_name: ClassVar[str] = "OpaBreakStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBreakStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    index: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaCallDynamicStmt(OpaStmt):
    """
    A statement of kind CallDynamicStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaCallDynamicStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaCallDynamicStmt"
    class_name: ClassVar[str] = "OpaCallDynamicStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaCallDynamicStmt

    type: str = None
    stmt: Union[dict, "OpaCallDynamicStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaCallDynamicStmtBody):
            self.stmt = OpaCallDynamicStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaCallDynamicStmtBody(OpaStmtBody):
    """
    CallDynamicStmt represents an indirect (data) function call. The result should be stored in the result local.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaCallDynamicStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaCallDynamicStmtBody"
    class_name: ClassVar[str] = "OpaCallDynamicStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaCallDynamicStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    result: int = None
    args: Optional[Union[int, list[int]]] = empty_list()
    path: Optional[Union[Union[dict, "OpaOperand"], list[Union[dict, "OpaOperand"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, int):
            self.result = int(self.result)

        if not isinstance(self.args, list):
            self.args = [self.args] if self.args is not None else []
        self.args = [v if isinstance(v, int) else int(v) for v in self.args]

        if not isinstance(self.path, list):
            self.path = [self.path] if self.path is not None else []
        self.path = [v if isinstance(v, OpaOperand) else OpaOperand(**as_dict(v)) for v in self.path]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaCallStmt(OpaStmt):
    """
    A statement of kind CallStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaCallStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaCallStmt"
    class_name: ClassVar[str] = "OpaCallStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaCallStmt

    type: str = None
    stmt: Union[dict, "OpaCallStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaCallStmtBody):
            self.stmt = OpaCallStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaCallStmtBody(OpaStmtBody):
    """
    CallStmt represents a named function call. The result should be stored in the result local.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaCallStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaCallStmtBody"
    class_name: ClassVar[str] = "OpaCallStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaCallStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    func: str = None
    result: int = None
    args: Optional[Union[Union[dict, "OpaOperand"], list[Union[dict, "OpaOperand"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.func):
            self.MissingRequiredField("func")
        if not isinstance(self.func, str):
            self.func = str(self.func)

        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, int):
            self.result = int(self.result)

        if not isinstance(self.args, list):
            self.args = [self.args] if self.args is not None else []
        self.args = [v if isinstance(v, OpaOperand) else OpaOperand(**as_dict(v)) for v in self.args]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaDotStmt(OpaStmt):
    """
    A statement of kind DotStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaDotStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaDotStmt"
    class_name: ClassVar[str] = "OpaDotStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaDotStmt

    type: str = None
    stmt: Union[dict, "OpaDotStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaDotStmtBody):
            self.stmt = OpaDotStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaDotStmtBody(OpaStmtBody):
    """
    DotStmt represents a lookup operation on a value (e.g., array, object, etc.) The source of a DotStmt may be a
    scalar value in which case the statement will be undefined.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaDotStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaDotStmtBody"
    class_name: ClassVar[str] = "OpaDotStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaDotStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    source: Union[dict, "OpaOperand"] = None
    target: int = None
    key: Union[dict, "OpaOperand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, OpaOperand):
            self.source = OpaOperand()

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, OpaOperand):
            self.key = OpaOperand()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaEqualStmt(OpaStmt):
    """
    A statement of kind EqualStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaEqualStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaEqualStmt"
    class_name: ClassVar[str] = "OpaEqualStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaEqualStmt

    type: str = None
    stmt: Union[dict, "OpaEqualStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaEqualStmtBody):
            self.stmt = OpaEqualStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaEqualStmtBody(OpaStmtBody):
    """
    EqualStmt represents an value-equality check of two local variables.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaEqualStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaEqualStmtBody"
    class_name: ClassVar[str] = "OpaEqualStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaEqualStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    a: Union[dict, "OpaOperand"] = None
    b: Union[dict, "OpaOperand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.a):
            self.MissingRequiredField("a")
        if not isinstance(self.a, OpaOperand):
            self.a = OpaOperand()

        if self._is_empty(self.b):
            self.MissingRequiredField("b")
        if not isinstance(self.b, OpaOperand):
            self.b = OpaOperand()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaIsArrayStmt(OpaStmt):
    """
    A statement of kind IsArrayStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaIsArrayStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaIsArrayStmt"
    class_name: ClassVar[str] = "OpaIsArrayStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaIsArrayStmt

    type: str = None
    stmt: Union[dict, "OpaIsArrayStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaIsArrayStmtBody):
            self.stmt = OpaIsArrayStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaIsArrayStmtBody(OpaStmtBody):
    """
    IsArrayStmt represents a dynamic type check on a local variable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaIsArrayStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaIsArrayStmtBody"
    class_name: ClassVar[str] = "OpaIsArrayStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaIsArrayStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    source: Union[dict, "OpaOperand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, OpaOperand):
            self.source = OpaOperand()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaIsDefinedStmt(OpaStmt):
    """
    A statement of kind IsDefinedStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaIsDefinedStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaIsDefinedStmt"
    class_name: ClassVar[str] = "OpaIsDefinedStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaIsDefinedStmt

    type: str = None
    stmt: Union[dict, "OpaIsDefinedStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaIsDefinedStmtBody):
            self.stmt = OpaIsDefinedStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaIsDefinedStmtBody(OpaStmtBody):
    """
    IsDefinedStmt represents a check of whether a local variable is defined.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaIsDefinedStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaIsDefinedStmtBody"
    class_name: ClassVar[str] = "OpaIsDefinedStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaIsDefinedStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    source: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, int):
            self.source = int(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaIsObjectStmt(OpaStmt):
    """
    A statement of kind IsObjectStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaIsObjectStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaIsObjectStmt"
    class_name: ClassVar[str] = "OpaIsObjectStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaIsObjectStmt

    type: str = None
    stmt: Union[dict, "OpaIsObjectStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaIsObjectStmtBody):
            self.stmt = OpaIsObjectStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaIsObjectStmtBody(OpaStmtBody):
    """
    IsObjectStmt represents a dynamic type check on a local variable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaIsObjectStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaIsObjectStmtBody"
    class_name: ClassVar[str] = "OpaIsObjectStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaIsObjectStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    source: Union[dict, "OpaOperand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, OpaOperand):
            self.source = OpaOperand()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaIsSetStmt(OpaStmt):
    """
    A statement of kind IsSetStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaIsSetStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaIsSetStmt"
    class_name: ClassVar[str] = "OpaIsSetStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaIsSetStmt

    type: str = None
    stmt: Union[dict, "OpaIsSetStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaIsSetStmtBody):
            self.stmt = OpaIsSetStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaIsSetStmtBody(OpaStmtBody):
    """
    IsSetStmt represents a dynamic type check on a local variable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaIsSetStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaIsSetStmtBody"
    class_name: ClassVar[str] = "OpaIsSetStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaIsSetStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    source: Union[dict, "OpaOperand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, OpaOperand):
            self.source = OpaOperand()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaIsUndefinedStmt(OpaStmt):
    """
    A statement of kind IsUndefinedStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaIsUndefinedStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaIsUndefinedStmt"
    class_name: ClassVar[str] = "OpaIsUndefinedStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaIsUndefinedStmt

    type: str = None
    stmt: Union[dict, "OpaIsUndefinedStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaIsUndefinedStmtBody):
            self.stmt = OpaIsUndefinedStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaIsUndefinedStmtBody(OpaStmtBody):
    """
    IsUndefinedStmt represents a check of whether local variable is undefined.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaIsUndefinedStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaIsUndefinedStmtBody"
    class_name: ClassVar[str] = "OpaIsUndefinedStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaIsUndefinedStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    source: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, int):
            self.source = int(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaLenStmt(OpaStmt):
    """
    A statement of kind LenStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaLenStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaLenStmt"
    class_name: ClassVar[str] = "OpaLenStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaLenStmt

    type: str = None
    stmt: Union[dict, "OpaLenStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaLenStmtBody):
            self.stmt = OpaLenStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaLenStmtBody(OpaStmtBody):
    """
    LenStmt represents a length() operation on a local variable. The result is stored in the target local variable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaLenStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaLenStmtBody"
    class_name: ClassVar[str] = "OpaLenStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaLenStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    source: Union[dict, "OpaOperand"] = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, OpaOperand):
            self.source = OpaOperand()

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaMakeArrayStmt(OpaStmt):
    """
    A statement of kind MakeArrayStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeArrayStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeArrayStmt"
    class_name: ClassVar[str] = "OpaMakeArrayStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeArrayStmt

    type: str = None
    stmt: Union[dict, "OpaMakeArrayStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaMakeArrayStmtBody):
            self.stmt = OpaMakeArrayStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaMakeArrayStmtBody(OpaStmtBody):
    """
    MakeArrayStmt constructs a local variable that refers to an array value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeArrayStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeArrayStmtBody"
    class_name: ClassVar[str] = "OpaMakeArrayStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeArrayStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    target: int = None
    capacity: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        if self._is_empty(self.capacity):
            self.MissingRequiredField("capacity")
        if not isinstance(self.capacity, int):
            self.capacity = int(self.capacity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaMakeNullStmt(OpaStmt):
    """
    A statement of kind MakeNullStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeNullStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeNullStmt"
    class_name: ClassVar[str] = "OpaMakeNullStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeNullStmt

    type: str = None
    stmt: Union[dict, "OpaMakeNullStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaMakeNullStmtBody):
            self.stmt = OpaMakeNullStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaMakeNullStmtBody(OpaStmtBody):
    """
    MakeNullStmt constructs a local variable that refers to a null value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeNullStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeNullStmtBody"
    class_name: ClassVar[str] = "OpaMakeNullStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeNullStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaMakeNumberIntStmt(OpaStmt):
    """
    A statement of kind MakeNumberIntStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeNumberIntStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeNumberIntStmt"
    class_name: ClassVar[str] = "OpaMakeNumberIntStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeNumberIntStmt

    type: str = None
    stmt: Union[dict, "OpaMakeNumberIntStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaMakeNumberIntStmtBody):
            self.stmt = OpaMakeNumberIntStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaMakeNumberIntStmtBody(OpaStmtBody):
    """
    MakeNumberIntStmt constructs a local variable that refers to an integer value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeNumberIntStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeNumberIntStmtBody"
    class_name: ClassVar[str] = "OpaMakeNumberIntStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeNumberIntStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    target: int = None
    value: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
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
class OpaMakeNumberRefStmt(OpaStmt):
    """
    A statement of kind MakeNumberRefStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeNumberRefStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeNumberRefStmt"
    class_name: ClassVar[str] = "OpaMakeNumberRefStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeNumberRefStmt

    type: str = None
    stmt: Union[dict, "OpaMakeNumberRefStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaMakeNumberRefStmtBody):
            self.stmt = OpaMakeNumberRefStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaMakeNumberRefStmtBody(OpaStmtBody):
    """
    MakeNumberRefStmt constructs a local variable that refers to a number stored as a string.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeNumberRefStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeNumberRefStmtBody"
    class_name: ClassVar[str] = "OpaMakeNumberRefStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeNumberRefStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    target: int = None
    index: int = None
    Index: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        if self.Index is not None and not isinstance(self.Index, int):
            self.Index = int(self.Index)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaMakeObjectStmt(OpaStmt):
    """
    A statement of kind MakeObjectStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeObjectStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeObjectStmt"
    class_name: ClassVar[str] = "OpaMakeObjectStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeObjectStmt

    type: str = None
    stmt: Union[dict, "OpaMakeObjectStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaMakeObjectStmtBody):
            self.stmt = OpaMakeObjectStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaMakeObjectStmtBody(OpaStmtBody):
    """
    MakeObjectStmt constructs a local variable that refers to an object value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeObjectStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeObjectStmtBody"
    class_name: ClassVar[str] = "OpaMakeObjectStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeObjectStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaMakeSetStmt(OpaStmt):
    """
    A statement of kind MakeSetStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeSetStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeSetStmt"
    class_name: ClassVar[str] = "OpaMakeSetStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeSetStmt

    type: str = None
    stmt: Union[dict, "OpaMakeSetStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaMakeSetStmtBody):
            self.stmt = OpaMakeSetStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaMakeSetStmtBody(OpaStmtBody):
    """
    MakeSetStmt constructs a local variable that refers to a set value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaMakeSetStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaMakeSetStmtBody"
    class_name: ClassVar[str] = "OpaMakeSetStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaMakeSetStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaNopStmt(OpaStmt):
    """
    A statement of kind NopStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaNopStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaNopStmt"
    class_name: ClassVar[str] = "OpaNopStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaNopStmt

    type: str = None
    stmt: Union[dict, "OpaNopStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaNopStmtBody):
            self.stmt = OpaNopStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaNopStmtBody(OpaStmtBody):
    """
    NopStmt adds a nop instruction. Useful during development and debugging only.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaNopStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaNopStmtBody"
    class_name: ClassVar[str] = "OpaNopStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaNopStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None

@dataclass(repr=False)
class OpaNotEqualStmt(OpaStmt):
    """
    A statement of kind NotEqualStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaNotEqualStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaNotEqualStmt"
    class_name: ClassVar[str] = "OpaNotEqualStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaNotEqualStmt

    type: str = None
    stmt: Union[dict, "OpaNotEqualStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaNotEqualStmtBody):
            self.stmt = OpaNotEqualStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaNotEqualStmtBody(OpaStmtBody):
    """
    NotEqualStmt represents a != check of two local variables.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaNotEqualStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaNotEqualStmtBody"
    class_name: ClassVar[str] = "OpaNotEqualStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaNotEqualStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    a: Union[dict, "OpaOperand"] = None
    b: Union[dict, "OpaOperand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.a):
            self.MissingRequiredField("a")
        if not isinstance(self.a, OpaOperand):
            self.a = OpaOperand()

        if self._is_empty(self.b):
            self.MissingRequiredField("b")
        if not isinstance(self.b, OpaOperand):
            self.b = OpaOperand()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaNotStmt(OpaStmt):
    """
    A statement of kind NotStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaNotStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaNotStmt"
    class_name: ClassVar[str] = "OpaNotStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaNotStmt

    type: str = None
    stmt: Union[dict, "OpaNotStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaNotStmtBody):
            self.stmt = OpaNotStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaNotStmtBody(OpaStmtBody):
    """
    NotStmt represents a negated statement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaNotStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaNotStmtBody"
    class_name: ClassVar[str] = "OpaNotStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaNotStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    block: Optional[Union[dict, OpaBlock]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.block is not None and not isinstance(self.block, OpaBlock):
            self.block = OpaBlock(**as_dict(self.block))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaObjectInsertOnceStmt(OpaStmt):
    """
    A statement of kind ObjectInsertOnceStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaObjectInsertOnceStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaObjectInsertOnceStmt"
    class_name: ClassVar[str] = "OpaObjectInsertOnceStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaObjectInsertOnceStmt

    type: str = None
    stmt: Union[dict, "OpaObjectInsertOnceStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaObjectInsertOnceStmtBody):
            self.stmt = OpaObjectInsertOnceStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaObjectInsertOnceStmtBody(OpaStmtBody):
    """
    ObjectInsertOnceStmt represents a dynamic insert operation of a key/value pair into an object. If the key already
    exists and the value differs, execution aborts with a conflict error.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaObjectInsertOnceStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaObjectInsertOnceStmtBody"
    class_name: ClassVar[str] = "OpaObjectInsertOnceStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaObjectInsertOnceStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    key: Union[dict, "OpaOperand"] = None
    object: int = None
    value: Union[dict, "OpaOperand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, OpaOperand):
            self.key = OpaOperand()

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, int):
            self.object = int(self.object)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, OpaOperand):
            self.value = OpaOperand()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaObjectInsertStmt(OpaStmt):
    """
    A statement of kind ObjectInsertStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaObjectInsertStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaObjectInsertStmt"
    class_name: ClassVar[str] = "OpaObjectInsertStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaObjectInsertStmt

    type: str = None
    stmt: Union[dict, "OpaObjectInsertStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaObjectInsertStmtBody):
            self.stmt = OpaObjectInsertStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaObjectInsertStmtBody(OpaStmtBody):
    """
    ObjectInsertStmt represents a dynamic insert operation of a key/value pair into an object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaObjectInsertStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaObjectInsertStmtBody"
    class_name: ClassVar[str] = "OpaObjectInsertStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaObjectInsertStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    key: Union[dict, "OpaOperand"] = None
    object: int = None
    value: Union[dict, "OpaOperand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, OpaOperand):
            self.key = OpaOperand()

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, int):
            self.object = int(self.object)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, OpaOperand):
            self.value = OpaOperand()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaObjectMergeStmt(OpaStmt):
    """
    A statement of kind ObjectMergeStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaObjectMergeStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaObjectMergeStmt"
    class_name: ClassVar[str] = "OpaObjectMergeStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaObjectMergeStmt

    type: str = None
    stmt: Union[dict, "OpaObjectMergeStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaObjectMergeStmtBody):
            self.stmt = OpaObjectMergeStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaObjectMergeStmtBody(OpaStmtBody):
    """
    ObjectMergeStmt performs a recursive merge of two object values. If either of the locals refer to non-object
    values this operation will abort with a conflict error.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaObjectMergeStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaObjectMergeStmtBody"
    class_name: ClassVar[str] = "OpaObjectMergeStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaObjectMergeStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    target: int = None
    a: int = None
    b: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        if self._is_empty(self.a):
            self.MissingRequiredField("a")
        if not isinstance(self.a, int):
            self.a = int(self.a)

        if self._is_empty(self.b):
            self.MissingRequiredField("b")
        if not isinstance(self.b, int):
            self.b = int(self.b)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaResetLocalStmt(OpaStmt):
    """
    A statement of kind ResetLocalStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaResetLocalStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaResetLocalStmt"
    class_name: ClassVar[str] = "OpaResetLocalStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaResetLocalStmt

    type: str = None
    stmt: Union[dict, "OpaResetLocalStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaResetLocalStmtBody):
            self.stmt = OpaResetLocalStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaResetLocalStmtBody(OpaStmtBody):
    """
    ResetLocalStmt resets a local variable to 0.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaResetLocalStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaResetLocalStmtBody"
    class_name: ClassVar[str] = "OpaResetLocalStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaResetLocalStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    target: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, int):
            self.target = int(self.target)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaResultSetAddStmt(OpaStmt):
    """
    A statement of kind ResultSetAddStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaResultSetAddStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaResultSetAddStmt"
    class_name: ClassVar[str] = "OpaResultSetAddStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaResultSetAddStmt

    type: str = None
    stmt: Union[dict, "OpaResultSetAddStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaResultSetAddStmtBody):
            self.stmt = OpaResultSetAddStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaResultSetAddStmtBody(OpaStmtBody):
    """
    ResultSetAddStmt adds a value into the result set returned by the query plan.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaResultSetAddStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaResultSetAddStmtBody"
    class_name: ClassVar[str] = "OpaResultSetAddStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaResultSetAddStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    value: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaReturnLocalStmt(OpaStmt):
    """
    A statement of kind ReturnLocalStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaReturnLocalStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaReturnLocalStmt"
    class_name: ClassVar[str] = "OpaReturnLocalStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaReturnLocalStmt

    type: str = None
    stmt: Union[dict, "OpaReturnLocalStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaReturnLocalStmtBody):
            self.stmt = OpaReturnLocalStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaReturnLocalStmtBody(OpaStmtBody):
    """
    ReturnLocalStmt represents a return statement that yields a local value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaReturnLocalStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaReturnLocalStmtBody"
    class_name: ClassVar[str] = "OpaReturnLocalStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaReturnLocalStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    source: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, int):
            self.source = int(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaScanStmt(OpaStmt):
    """
    A statement of kind ScanStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaScanStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaScanStmt"
    class_name: ClassVar[str] = "OpaScanStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaScanStmt

    type: str = None
    stmt: Union[dict, "OpaScanStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaScanStmtBody):
            self.stmt = OpaScanStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaScanStmtBody(OpaStmtBody):
    """
    ScanStmt represents a linear scan over a composite value. The source may be a scalar in which case the block will
    never execute.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaScanStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaScanStmtBody"
    class_name: ClassVar[str] = "OpaScanStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaScanStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    source: int = None
    key: int = None
    value: int = None
    block: Optional[Union[dict, OpaBlock]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, int):
            self.source = int(self.source)

        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, int):
            self.key = int(self.key)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        if self.block is not None and not isinstance(self.block, OpaBlock):
            self.block = OpaBlock(**as_dict(self.block))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaSetAddStmt(OpaStmt):
    """
    A statement of kind SetAddStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaSetAddStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaSetAddStmt"
    class_name: ClassVar[str] = "OpaSetAddStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaSetAddStmt

    type: str = None
    stmt: Union[dict, "OpaSetAddStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaSetAddStmtBody):
            self.stmt = OpaSetAddStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaSetAddStmtBody(OpaStmtBody):
    """
    SetAddStmt represents a dynamic add operation of an element into a set.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaSetAddStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaSetAddStmtBody"
    class_name: ClassVar[str] = "OpaSetAddStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaSetAddStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    set: int = None
    value: Union[dict, "OpaOperand"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.set):
            self.MissingRequiredField("set")
        if not isinstance(self.set, int):
            self.set = int(self.set)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, OpaOperand):
            self.value = OpaOperand()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaWithStmt(OpaStmt):
    """
    A statement of kind WithStmt, with its fields in `stmt`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaWithStmt"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaWithStmt"
    class_name: ClassVar[str] = "OpaWithStmt"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaWithStmt

    type: str = None
    stmt: Union[dict, "OpaWithStmtBody"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.stmt):
            self.MissingRequiredField("stmt")
        if not isinstance(self.stmt, OpaWithStmtBody):
            self.stmt = OpaWithStmtBody(**as_dict(self.stmt))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaWithStmtBody(OpaStmtBody):
    """
    WithStmt replaces the Local or a portion of the document referred to by the Local with the Value and executes the
    contained block. If the Path is non-empty, the Value is upserted into the Local.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaWithStmtBody"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaWithStmtBody"
    class_name: ClassVar[str] = "OpaWithStmtBody"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaWithStmtBody

    file: int = None
    col: int = None
    row: int = None
    end_col: int = None
    end_row: int = None
    local: int = None
    value: Union[dict, "OpaOperand"] = None
    block: Optional[Union[dict, OpaBlock]] = None
    path: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.local):
            self.MissingRequiredField("local")
        if not isinstance(self.local, int):
            self.local = int(self.local)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, OpaOperand):
            self.value = OpaOperand()

        if self.block is not None and not isinstance(self.block, OpaBlock):
            self.block = OpaBlock(**as_dict(self.block))

        if not isinstance(self.path, list):
            self.path = [self.path] if self.path is not None else []
        self.path = [v if isinstance(v, int) else int(v) for v in self.path]

        super().__post_init__(**kwargs)


class OpaOperand(YAMLRoot):
    """
    Operand represents a value that a statement operates on. OPA writes it as its kind in `type` and the value in
    `value`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaOperand"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaOperand"
    class_name: ClassVar[str] = "OpaOperand"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaOperand


@dataclass(repr=False)
class OpaBoolOperand(OpaOperand):
    """
    Bool represents a constant boolean.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaBoolOperand"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaBoolOperand"
    class_name: ClassVar[str] = "OpaBoolOperand"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaBoolOperand

    type: str = None
    value: Union[bool, Bool] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Bool):
            self.value = Bool(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaLocalOperand(OpaOperand):
    """
    A local variable, by its number.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaLocalOperand"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaLocalOperand"
    class_name: ClassVar[str] = "OpaLocalOperand"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaLocalOperand

    type: str = None
    value: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpaStringIndexOperand(OpaOperand):
    """
    StringIndex represents the index into the plan's list of constant strings of a constant string.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENPOLICYAGENT["OpaStringIndexOperand"]
    class_class_curie: ClassVar[str] = "openpolicyagent:OpaStringIndexOperand"
    class_name: ClassVar[str] = "OpaStringIndexOperand"
    class_model_uri: ClassVar[URIRef] = OPENPOLICYAGENT.OpaStringIndexOperand

    type: str = None
    value: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


# Enumerations
class OpaFutureKeyword(EnumDefinitionImpl):
    """
    The future keywords the capabilities files OPA includes name.
    """
    contains = PermissibleValue(text="contains")
    every = PermissibleValue(text="every")

    _defn = EnumDefinition(
        name="OpaFutureKeyword",
        description="The future keywords the capabilities files OPA includes name.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "and",
            PermissibleValue(text="and"))
        setattr(cls, "if",
            PermissibleValue(text="if"))
        setattr(cls, "in",
            PermissibleValue(text="in"))
        setattr(cls, "not",
            PermissibleValue(text="not"))
        setattr(cls, "or",
            PermissibleValue(text="or"))

class OpaFeature(EnumDefinitionImpl):
    """
    The language features the capabilities files OPA includes name.
    """
    keywords_in_refs = PermissibleValue(text="keywords_in_refs")
    rego_v1 = PermissibleValue(text="rego_v1")
    rego_v1_import = PermissibleValue(text="rego_v1_import")
    rego_v2 = PermissibleValue(text="rego_v2")
    rego_v2_import = PermissibleValue(text="rego_v2_import")
    rule_head_ref_string_prefixes = PermissibleValue(text="rule_head_ref_string_prefixes")
    rule_head_refs = PermissibleValue(text="rule_head_refs")
    template_strings = PermissibleValue(text="template_strings")

    _defn = EnumDefinition(
        name="OpaFeature",
        description="The language features the capabilities files OPA includes name.",
    )

# Slots
class slots:
    pass

slots.body = Slot(uri=OPENPOLICYAGENT.body, name="body", curie=OPENPOLICYAGENT.curie('body'),
                   model_uri=OPENPOLICYAGENT.body, domain=None, range=Optional[str])

slots.revision = Slot(uri=OPENPOLICYAGENT.revision, name="revision", curie=OPENPOLICYAGENT.curie('revision'),
                   model_uri=OPENPOLICYAGENT.revision, domain=None, range=Optional[str])

slots.source = Slot(uri=OPENPOLICYAGENT.source, name="source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.source, domain=None, range=Optional[str])

slots.target = Slot(uri=OPENPOLICYAGENT.target, name="target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.target, domain=None, range=Optional[str])

slots.type = Slot(uri=OPENPOLICYAGENT.type, name="type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.type, domain=None, range=Optional[str])

slots.version = Slot(uri=OPENPOLICYAGENT.version, name="version", curie=OPENPOLICYAGENT.curie('version'),
                   model_uri=OPENPOLICYAGENT.version, domain=None, range=Optional[str])

slots.file = Slot(uri=OPENPOLICYAGENT.file, name="file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.file, domain=None, range=Optional[int])

slots.col = Slot(uri=OPENPOLICYAGENT.col, name="col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.col, domain=None, range=Optional[int])

slots.row = Slot(uri=OPENPOLICYAGENT.row, name="row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.row, domain=None, range=Optional[int])

slots.end_col = Slot(uri=OPENPOLICYAGENT.end_col, name="end_col", curie=OPENPOLICYAGENT.curie('end_col'),
                   model_uri=OPENPOLICYAGENT.end_col, domain=None, range=Optional[int])

slots.end_row = Slot(uri=OPENPOLICYAGENT.end_row, name="end_row", curie=OPENPOLICYAGENT.curie('end_row'),
                   model_uri=OPENPOLICYAGENT.end_row, domain=None, range=Optional[int])

slots.opaType__name = Slot(uri=SCHEMA.name, name="opaType__name", curie=SCHEMA.curie('name'),
                   model_uri=OPENPOLICYAGENT.opaType__name, domain=None, range=Optional[str])

slots.opaType__description = Slot(uri=SCHEMA.description, name="opaType__description", curie=SCHEMA.curie('description'),
                   model_uri=OPENPOLICYAGENT.opaType__description, domain=None, range=Optional[str])

slots.opaAnyType__of = Slot(uri=OPENPOLICYAGENT.of, name="opaAnyType__of", curie=OPENPOLICYAGENT.curie('of'),
                   model_uri=OPENPOLICYAGENT.opaAnyType__of, domain=None, range=Optional[Union[Union[dict, OpaType], list[Union[dict, OpaType]]]])

slots.opaArrayType__static = Slot(uri=OPENPOLICYAGENT.static, name="opaArrayType__static", curie=OPENPOLICYAGENT.curie('static'),
                   model_uri=OPENPOLICYAGENT.opaArrayType__static, domain=None, range=Optional[Union[Union[dict, OpaType], list[Union[dict, OpaType]]]])

slots.opaArrayType__dynamic = Slot(uri=OPENPOLICYAGENT.dynamic, name="opaArrayType__dynamic", curie=OPENPOLICYAGENT.curie('dynamic'),
                   model_uri=OPENPOLICYAGENT.opaArrayType__dynamic, domain=None, range=Optional[Union[dict, OpaType]])

slots.opaFunctionType__args = Slot(uri=OPENPOLICYAGENT.args, name="opaFunctionType__args", curie=OPENPOLICYAGENT.curie('args'),
                   model_uri=OPENPOLICYAGENT.opaFunctionType__args, domain=None, range=Optional[Union[Union[dict, OpaType], list[Union[dict, OpaType]]]])

slots.opaFunctionType__result = Slot(uri=OPENPOLICYAGENT.result, name="opaFunctionType__result", curie=OPENPOLICYAGENT.curie('result'),
                   model_uri=OPENPOLICYAGENT.opaFunctionType__result, domain=None, range=Optional[Union[dict, OpaType]])

slots.opaFunctionType__variadic = Slot(uri=OPENPOLICYAGENT.variadic, name="opaFunctionType__variadic", curie=OPENPOLICYAGENT.curie('variadic'),
                   model_uri=OPENPOLICYAGENT.opaFunctionType__variadic, domain=None, range=Optional[Union[dict, OpaType]])

slots.opaObjectType__static = Slot(uri=OPENPOLICYAGENT.static, name="opaObjectType__static", curie=OPENPOLICYAGENT.curie('static'),
                   model_uri=OPENPOLICYAGENT.opaObjectType__static, domain=None, range=Optional[Union[Union[dict, OpaStaticProperty], list[Union[dict, OpaStaticProperty]]]])

slots.opaObjectType__dynamic = Slot(uri=OPENPOLICYAGENT.dynamic, name="opaObjectType__dynamic", curie=OPENPOLICYAGENT.curie('dynamic'),
                   model_uri=OPENPOLICYAGENT.opaObjectType__dynamic, domain=None, range=Optional[Union[dict, OpaDynamicProperty]])

slots.opaSetType__of = Slot(uri=OPENPOLICYAGENT.of, name="opaSetType__of", curie=OPENPOLICYAGENT.curie('of'),
                   model_uri=OPENPOLICYAGENT.opaSetType__of, domain=None, range=Optional[Union[dict, OpaType]])

slots.opaStaticProperty__key = Slot(uri=OPENPOLICYAGENT.key, name="opaStaticProperty__key", curie=OPENPOLICYAGENT.curie('key'),
                   model_uri=OPENPOLICYAGENT.opaStaticProperty__key, domain=None, range=Union[dict, OpaValue])

slots.opaStaticProperty__value = Slot(uri=OPENPOLICYAGENT.value, name="opaStaticProperty__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaStaticProperty__value, domain=None, range=Union[dict, OpaType])

slots.opaDynamicProperty__key = Slot(uri=OPENPOLICYAGENT.key, name="opaDynamicProperty__key", curie=OPENPOLICYAGENT.curie('key'),
                   model_uri=OPENPOLICYAGENT.opaDynamicProperty__key, domain=None, range=Union[dict, OpaType])

slots.opaDynamicProperty__value = Slot(uri=OPENPOLICYAGENT.value, name="opaDynamicProperty__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaDynamicProperty__value, domain=None, range=Union[dict, OpaType])

slots.opaCapabilities__builtins = Slot(uri=OPENPOLICYAGENT.builtins, name="opaCapabilities__builtins", curie=OPENPOLICYAGENT.curie('builtins'),
                   model_uri=OPENPOLICYAGENT.opaCapabilities__builtins, domain=None, range=Optional[Union[Union[dict, OpaBuiltin], list[Union[dict, OpaBuiltin]]]])

slots.opaCapabilities__future_keywords = Slot(uri=OPENPOLICYAGENT.future_keywords, name="opaCapabilities__future_keywords", curie=OPENPOLICYAGENT.curie('future_keywords'),
                   model_uri=OPENPOLICYAGENT.opaCapabilities__future_keywords, domain=None, range=Optional[Union[Union[str, "OpaFutureKeyword"], list[Union[str, "OpaFutureKeyword"]]]])

slots.opaCapabilities__wasm_abi_versions = Slot(uri=OPENPOLICYAGENT.wasm_abi_versions, name="opaCapabilities__wasm_abi_versions", curie=OPENPOLICYAGENT.curie('wasm_abi_versions'),
                   model_uri=OPENPOLICYAGENT.opaCapabilities__wasm_abi_versions, domain=None, range=Optional[Union[Union[dict, OpaWasmAbiVersion], list[Union[dict, OpaWasmAbiVersion]]]])

slots.opaCapabilities__features = Slot(uri=OPENPOLICYAGENT.features, name="opaCapabilities__features", curie=OPENPOLICYAGENT.curie('features'),
                   model_uri=OPENPOLICYAGENT.opaCapabilities__features, domain=None, range=Optional[Union[Union[str, "OpaFeature"], list[Union[str, "OpaFeature"]]]])

slots.opaCapabilities__allow_net = Slot(uri=OPENPOLICYAGENT.allow_net, name="opaCapabilities__allow_net", curie=OPENPOLICYAGENT.curie('allow_net'),
                   model_uri=OPENPOLICYAGENT.opaCapabilities__allow_net, domain=None, range=Optional[Union[str, list[str]]])

slots.opaBuiltin__name = Slot(uri=SCHEMA.name, name="opaBuiltin__name", curie=SCHEMA.curie('name'),
                   model_uri=OPENPOLICYAGENT.opaBuiltin__name, domain=None, range=str)

slots.opaBuiltin__description = Slot(uri=SCHEMA.description, name="opaBuiltin__description", curie=SCHEMA.curie('description'),
                   model_uri=OPENPOLICYAGENT.opaBuiltin__description, domain=None, range=Optional[str])

slots.opaBuiltin__categories = Slot(uri=OPENPOLICYAGENT.categories, name="opaBuiltin__categories", curie=OPENPOLICYAGENT.curie('categories'),
                   model_uri=OPENPOLICYAGENT.opaBuiltin__categories, domain=None, range=Optional[Union[str, list[str]]])

slots.opaBuiltin__decl = Slot(uri=OPENPOLICYAGENT.decl, name="opaBuiltin__decl", curie=OPENPOLICYAGENT.curie('decl'),
                   model_uri=OPENPOLICYAGENT.opaBuiltin__decl, domain=None, range=Union[dict, OpaFunctionType])

slots.opaBuiltin__infix = Slot(uri=OPENPOLICYAGENT.infix, name="opaBuiltin__infix", curie=OPENPOLICYAGENT.curie('infix'),
                   model_uri=OPENPOLICYAGENT.opaBuiltin__infix, domain=None, range=Optional[str])

slots.opaBuiltin__relation = Slot(uri=OPENPOLICYAGENT.relation, name="opaBuiltin__relation", curie=OPENPOLICYAGENT.curie('relation'),
                   model_uri=OPENPOLICYAGENT.opaBuiltin__relation, domain=None, range=Optional[Union[bool, Bool]])

slots.opaBuiltin__deprecated = Slot(uri=OPENPOLICYAGENT.deprecated, name="opaBuiltin__deprecated", curie=OPENPOLICYAGENT.curie('deprecated'),
                   model_uri=OPENPOLICYAGENT.opaBuiltin__deprecated, domain=None, range=Optional[Union[bool, Bool]])

slots.opaBuiltin__nondeterministic = Slot(uri=OPENPOLICYAGENT.nondeterministic, name="opaBuiltin__nondeterministic", curie=OPENPOLICYAGENT.curie('nondeterministic'),
                   model_uri=OPENPOLICYAGENT.opaBuiltin__nondeterministic, domain=None, range=Optional[Union[bool, Bool]])

slots.opaWasmAbiVersion__minor_version = Slot(uri=OPENPOLICYAGENT.minor_version, name="opaWasmAbiVersion__minor_version", curie=OPENPOLICYAGENT.curie('minor_version'),
                   model_uri=OPENPOLICYAGENT.opaWasmAbiVersion__minor_version, domain=None, range=int)

slots.opaBuiltinMetadataCatalog__categories = Slot(uri=OPENPOLICYAGENT._categories, name="opaBuiltinMetadataCatalog__categories", curie=OPENPOLICYAGENT.curie('_categories'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadataCatalog__categories, domain=None, range=Union[dict[Union[str, OpaBuiltinCategoryName], Union[dict, OpaBuiltinCategory]], list[Union[dict, OpaBuiltinCategory]]])

slots.opaBuiltinMetadataCatalog__implementations = Slot(uri=OPENPOLICYAGENT._implementations, name="opaBuiltinMetadataCatalog__implementations", curie=OPENPOLICYAGENT.curie('_implementations'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadataCatalog__implementations, domain=None, range=Union[Union[dict, OpaImplementation], list[Union[dict, OpaImplementation]]])

slots.opaBuiltinCategory__name = Slot(uri=SCHEMA.name, name="opaBuiltinCategory__name", curie=SCHEMA.curie('name'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinCategory__name, domain=None, range=URIRef)

slots.opaBuiltinCategory__builtins = Slot(uri=OPENPOLICYAGENT.builtins, name="opaBuiltinCategory__builtins", curie=OPENPOLICYAGENT.curie('builtins'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinCategory__builtins, domain=None, range=Union[str, list[str]])

slots.opaImplementation__id = Slot(uri=SCHEMA.identifier, name="opaImplementation__id", curie=SCHEMA.curie('identifier'),
                   model_uri=OPENPOLICYAGENT.opaImplementation__id, domain=None, range=str)

slots.opaImplementation__label = Slot(uri=OPENPOLICYAGENT.label, name="opaImplementation__label", curie=OPENPOLICYAGENT.curie('label'),
                   model_uri=OPENPOLICYAGENT.opaImplementation__label, domain=None, range=str)

slots.opaImplementation__repo = Slot(uri=OPENPOLICYAGENT.repo, name="opaImplementation__repo", curie=OPENPOLICYAGENT.curie('repo'),
                   model_uri=OPENPOLICYAGENT.opaImplementation__repo, domain=None, range=str)

slots.opaBuiltinMetadata__description = Slot(uri=SCHEMA.description, name="opaBuiltinMetadata__description", curie=SCHEMA.curie('description'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadata__description, domain=None, range=Optional[str])

slots.opaBuiltinMetadata__introduced = Slot(uri=OPENPOLICYAGENT.introduced, name="opaBuiltinMetadata__introduced", curie=OPENPOLICYAGENT.curie('introduced'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadata__introduced, domain=None, range=str)

slots.opaBuiltinMetadata__available = Slot(uri=OPENPOLICYAGENT.available, name="opaBuiltinMetadata__available", curie=OPENPOLICYAGENT.curie('available'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadata__available, domain=None, range=Union[str, list[str]])

slots.opaBuiltinMetadata__wasm = Slot(uri=OPENPOLICYAGENT.wasm, name="opaBuiltinMetadata__wasm", curie=OPENPOLICYAGENT.curie('wasm'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadata__wasm, domain=None, range=Union[bool, Bool])

slots.opaBuiltinMetadata__args = Slot(uri=OPENPOLICYAGENT.args, name="opaBuiltinMetadata__args", curie=OPENPOLICYAGENT.curie('args'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadata__args, domain=None, range=Union[Union[dict, OpaBuiltinArgument], list[Union[dict, OpaBuiltinArgument]]])

slots.opaBuiltinMetadata__result = Slot(uri=OPENPOLICYAGENT.result, name="opaBuiltinMetadata__result", curie=OPENPOLICYAGENT.curie('result'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadata__result, domain=None, range=Union[dict, OpaBuiltinResult])

slots.opaBuiltinMetadata__implementations = Slot(uri=OPENPOLICYAGENT.implementations, name="opaBuiltinMetadata__implementations", curie=OPENPOLICYAGENT.curie('implementations'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadata__implementations, domain=None, range=Union[dict[Union[str, OpaImplementationSupportImplementation], Union[dict, OpaImplementationSupport]], list[Union[dict, OpaImplementationSupport]]])

slots.opaBuiltinMetadata__infix = Slot(uri=OPENPOLICYAGENT.infix, name="opaBuiltinMetadata__infix", curie=OPENPOLICYAGENT.curie('infix'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadata__infix, domain=None, range=Optional[str])

slots.opaBuiltinMetadata__relation = Slot(uri=OPENPOLICYAGENT.relation, name="opaBuiltinMetadata__relation", curie=OPENPOLICYAGENT.curie('relation'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadata__relation, domain=None, range=Optional[Union[bool, Bool]])

slots.opaBuiltinMetadata__deprecated = Slot(uri=OPENPOLICYAGENT.deprecated, name="opaBuiltinMetadata__deprecated", curie=OPENPOLICYAGENT.curie('deprecated'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinMetadata__deprecated, domain=None, range=Optional[Union[bool, Bool]])

slots.opaBuiltinArgument__name = Slot(uri=SCHEMA.name, name="opaBuiltinArgument__name", curie=SCHEMA.curie('name'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinArgument__name, domain=None, range=Optional[str])

slots.opaBuiltinArgument__description = Slot(uri=SCHEMA.description, name="opaBuiltinArgument__description", curie=SCHEMA.curie('description'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinArgument__description, domain=None, range=Optional[str])

slots.opaBuiltinResult__name = Slot(uri=SCHEMA.name, name="opaBuiltinResult__name", curie=SCHEMA.curie('name'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinResult__name, domain=None, range=Optional[str])

slots.opaBuiltinResult__description = Slot(uri=SCHEMA.description, name="opaBuiltinResult__description", curie=SCHEMA.curie('description'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinResult__description, domain=None, range=Optional[str])

slots.opaImplementationSupport__implementation = Slot(uri=OPENPOLICYAGENT.implementation, name="opaImplementationSupport__implementation", curie=OPENPOLICYAGENT.curie('implementation'),
                   model_uri=OPENPOLICYAGENT.opaImplementationSupport__implementation, domain=None, range=URIRef)

slots.opaVersionIndex__builtins = Slot(uri=OPENPOLICYAGENT.builtins, name="opaVersionIndex__builtins", curie=OPENPOLICYAGENT.curie('builtins'),
                   model_uri=OPENPOLICYAGENT.opaVersionIndex__builtins, domain=None, range=Union[dict[Union[str, OpaVersionEntryName], Union[dict, OpaVersionEntry]], list[Union[dict, OpaVersionEntry]]])

slots.opaVersionIndex__features = Slot(uri=OPENPOLICYAGENT.features, name="opaVersionIndex__features", curie=OPENPOLICYAGENT.curie('features'),
                   model_uri=OPENPOLICYAGENT.opaVersionIndex__features, domain=None, range=Union[dict[Union[str, OpaVersionEntryName], Union[dict, OpaVersionEntry]], list[Union[dict, OpaVersionEntry]]])

slots.opaVersionIndex__keywords = Slot(uri=OPENPOLICYAGENT.keywords, name="opaVersionIndex__keywords", curie=OPENPOLICYAGENT.curie('keywords'),
                   model_uri=OPENPOLICYAGENT.opaVersionIndex__keywords, domain=None, range=Union[dict[Union[str, OpaVersionEntryName], Union[dict, OpaVersionEntry]], list[Union[dict, OpaVersionEntry]]])

slots.opaVersionEntry__name = Slot(uri=SCHEMA.name, name="opaVersionEntry__name", curie=SCHEMA.curie('name'),
                   model_uri=OPENPOLICYAGENT.opaVersionEntry__name, domain=None, range=URIRef)

slots.opaVersionEntry__major = Slot(uri=OPENPOLICYAGENT.Major, name="opaVersionEntry__major", curie=OPENPOLICYAGENT.curie('Major'),
                   model_uri=OPENPOLICYAGENT.opaVersionEntry__major, domain=None, range=int)

slots.opaVersionEntry__minor = Slot(uri=OPENPOLICYAGENT.Minor, name="opaVersionEntry__minor", curie=OPENPOLICYAGENT.curie('Minor'),
                   model_uri=OPENPOLICYAGENT.opaVersionEntry__minor, domain=None, range=int)

slots.opaVersionEntry__patch = Slot(uri=OPENPOLICYAGENT.Patch, name="opaVersionEntry__patch", curie=OPENPOLICYAGENT.curie('Patch'),
                   model_uri=OPENPOLICYAGENT.opaVersionEntry__patch, domain=None, range=int)

slots.opaVersionEntry__pre_release = Slot(uri=OPENPOLICYAGENT.PreRelease, name="opaVersionEntry__pre_release", curie=OPENPOLICYAGENT.curie('PreRelease'),
                   model_uri=OPENPOLICYAGENT.opaVersionEntry__pre_release, domain=None, range=Optional[str])

slots.opaVersionEntry__metadata = Slot(uri=OPENPOLICYAGENT.Metadata, name="opaVersionEntry__metadata", curie=OPENPOLICYAGENT.curie('Metadata'),
                   model_uri=OPENPOLICYAGENT.opaVersionEntry__metadata, domain=None, range=Optional[str])

slots.opaAuthorizationInput__identity = Slot(uri=OPENPOLICYAGENT.identity, name="opaAuthorizationInput__identity", curie=OPENPOLICYAGENT.curie('identity'),
                   model_uri=OPENPOLICYAGENT.opaAuthorizationInput__identity, domain=None, range=Optional[str])

slots.opaAuthorizationInput__client_certificates = Slot(uri=OPENPOLICYAGENT.client_certificates, name="opaAuthorizationInput__client_certificates", curie=OPENPOLICYAGENT.curie('client_certificates'),
                   model_uri=OPENPOLICYAGENT.opaAuthorizationInput__client_certificates, domain=None, range=Optional[Union[Union[dict, OpaObject], list[Union[dict, OpaObject]]]])

slots.opaAuthorizationInput__method = Slot(uri=OPENPOLICYAGENT.method, name="opaAuthorizationInput__method", curie=OPENPOLICYAGENT.curie('method'),
                   model_uri=OPENPOLICYAGENT.opaAuthorizationInput__method, domain=None, range=str)

slots.opaAuthorizationInput__path = Slot(uri=OPENPOLICYAGENT.path, name="opaAuthorizationInput__path", curie=OPENPOLICYAGENT.curie('path'),
                   model_uri=OPENPOLICYAGENT.opaAuthorizationInput__path, domain=None, range=Union[str, list[str]])

slots.opaAuthorizationInput__params = Slot(uri=OPENPOLICYAGENT.params, name="opaAuthorizationInput__params", curie=OPENPOLICYAGENT.curie('params'),
                   model_uri=OPENPOLICYAGENT.opaAuthorizationInput__params, domain=None, range=Union[dict, OpaStringListMap])

slots.opaAuthorizationInput__headers = Slot(uri=OPENPOLICYAGENT.headers, name="opaAuthorizationInput__headers", curie=OPENPOLICYAGENT.curie('headers'),
                   model_uri=OPENPOLICYAGENT.opaAuthorizationInput__headers, domain=None, range=Union[dict, OpaStringListMap])

slots.opaManifest__file_rego_versions = Slot(uri=OPENPOLICYAGENT.file_rego_versions, name="opaManifest__file_rego_versions", curie=OPENPOLICYAGENT.curie('file_rego_versions'),
                   model_uri=OPENPOLICYAGENT.opaManifest__file_rego_versions, domain=None, range=Optional[Union[dict[Union[str, OpaFileRegoVersionPath], Union[dict, OpaFileRegoVersion]], list[Union[dict, OpaFileRegoVersion]]]])

slots.opaManifest__metadata = Slot(uri=OPENPOLICYAGENT.metadata, name="opaManifest__metadata", curie=OPENPOLICYAGENT.curie('metadata'),
                   model_uri=OPENPOLICYAGENT.opaManifest__metadata, domain=None, range=Optional[Union[dict, OpaObject]])

slots.opaManifest__rego_version = Slot(uri=OPENPOLICYAGENT.rego_version, name="opaManifest__rego_version", curie=OPENPOLICYAGENT.curie('rego_version'),
                   model_uri=OPENPOLICYAGENT.opaManifest__rego_version, domain=None, range=Optional[int])

slots.opaManifest__roots = Slot(uri=OPENPOLICYAGENT.roots, name="opaManifest__roots", curie=OPENPOLICYAGENT.curie('roots'),
                   model_uri=OPENPOLICYAGENT.opaManifest__roots, domain=None, range=Optional[Union[str, list[str]]])

slots.opaManifest__wasm = Slot(uri=OPENPOLICYAGENT.wasm, name="opaManifest__wasm", curie=OPENPOLICYAGENT.curie('wasm'),
                   model_uri=OPENPOLICYAGENT.opaManifest__wasm, domain=None, range=Optional[Union[Union[dict, OpaWasmResolver], list[Union[dict, OpaWasmResolver]]]])

slots.opaWasmResolver__annotations = Slot(uri=OPENPOLICYAGENT.annotations, name="opaWasmResolver__annotations", curie=OPENPOLICYAGENT.curie('annotations'),
                   model_uri=OPENPOLICYAGENT.opaWasmResolver__annotations, domain=None, range=Optional[Union[Union[dict, OpaObject], list[Union[dict, OpaObject]]]])

slots.opaWasmResolver__entrypoint = Slot(uri=OPENPOLICYAGENT.entrypoint, name="opaWasmResolver__entrypoint", curie=OPENPOLICYAGENT.curie('entrypoint'),
                   model_uri=OPENPOLICYAGENT.opaWasmResolver__entrypoint, domain=None, range=Optional[str])

slots.opaWasmResolver__module = Slot(uri=OPENPOLICYAGENT.module, name="opaWasmResolver__module", curie=OPENPOLICYAGENT.curie('module'),
                   model_uri=OPENPOLICYAGENT.opaWasmResolver__module, domain=None, range=Optional[str])

slots.opaFileRegoVersion__path = Slot(uri=OPENPOLICYAGENT.path, name="opaFileRegoVersion__path", curie=OPENPOLICYAGENT.curie('path'),
                   model_uri=OPENPOLICYAGENT.opaFileRegoVersion__path, domain=None, range=URIRef)

slots.opaPolicy__funcs = Slot(uri=OPENPOLICYAGENT.funcs, name="opaPolicy__funcs", curie=OPENPOLICYAGENT.curie('funcs'),
                   model_uri=OPENPOLICYAGENT.opaPolicy__funcs, domain=None, range=Optional[Union[dict, OpaFuncs]])

slots.opaPolicy__plans = Slot(uri=OPENPOLICYAGENT.plans, name="opaPolicy__plans", curie=OPENPOLICYAGENT.curie('plans'),
                   model_uri=OPENPOLICYAGENT.opaPolicy__plans, domain=None, range=Optional[Union[dict, OpaPlans]])

slots.opaPolicy__static = Slot(uri=OPENPOLICYAGENT.static, name="opaPolicy__static", curie=OPENPOLICYAGENT.curie('static'),
                   model_uri=OPENPOLICYAGENT.opaPolicy__static, domain=None, range=Optional[Union[dict, OpaStatic]])

slots.opaPolicy__unplanned_rules = Slot(uri=OPENPOLICYAGENT.unplanned_rules, name="opaPolicy__unplanned_rules", curie=OPENPOLICYAGENT.curie('unplanned_rules'),
                   model_uri=OPENPOLICYAGENT.opaPolicy__unplanned_rules, domain=None, range=Optional[Union[Union[dict, OpaUnplannedRule], list[Union[dict, OpaUnplannedRule]]]])

slots.opaStatic__builtin_funcs = Slot(uri=OPENPOLICYAGENT.builtin_funcs, name="opaStatic__builtin_funcs", curie=OPENPOLICYAGENT.curie('builtin_funcs'),
                   model_uri=OPENPOLICYAGENT.opaStatic__builtin_funcs, domain=None, range=Optional[Union[Union[dict, OpaBuiltinFunc], list[Union[dict, OpaBuiltinFunc]]]])

slots.opaStatic__files = Slot(uri=OPENPOLICYAGENT.files, name="opaStatic__files", curie=OPENPOLICYAGENT.curie('files'),
                   model_uri=OPENPOLICYAGENT.opaStatic__files, domain=None, range=Optional[Union[Union[dict, OpaStringConst], list[Union[dict, OpaStringConst]]]])

slots.opaStatic__strings = Slot(uri=OPENPOLICYAGENT.strings, name="opaStatic__strings", curie=OPENPOLICYAGENT.curie('strings'),
                   model_uri=OPENPOLICYAGENT.opaStatic__strings, domain=None, range=Optional[Union[Union[dict, OpaStringConst], list[Union[dict, OpaStringConst]]]])

slots.opaStringConst__value = Slot(uri=OPENPOLICYAGENT.value, name="opaStringConst__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaStringConst__value, domain=None, range=str)

slots.opaBuiltinFunc__decl = Slot(uri=OPENPOLICYAGENT.decl, name="opaBuiltinFunc__decl", curie=OPENPOLICYAGENT.curie('decl'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinFunc__decl, domain=None, range=Optional[Union[dict, OpaFunctionType]])

slots.opaBuiltinFunc__name = Slot(uri=SCHEMA.name, name="opaBuiltinFunc__name", curie=SCHEMA.curie('name'),
                   model_uri=OPENPOLICYAGENT.opaBuiltinFunc__name, domain=None, range=str)

slots.opaPlans__plans = Slot(uri=OPENPOLICYAGENT.plans, name="opaPlans__plans", curie=OPENPOLICYAGENT.curie('plans'),
                   model_uri=OPENPOLICYAGENT.opaPlans__plans, domain=None, range=Optional[Union[Union[dict, OpaPlan], list[Union[dict, OpaPlan]]]])

slots.opaPlan__blocks = Slot(uri=OPENPOLICYAGENT.blocks, name="opaPlan__blocks", curie=OPENPOLICYAGENT.curie('blocks'),
                   model_uri=OPENPOLICYAGENT.opaPlan__blocks, domain=None, range=Optional[Union[Union[dict, OpaBlock], list[Union[dict, OpaBlock]]]])

slots.opaPlan__name = Slot(uri=SCHEMA.name, name="opaPlan__name", curie=SCHEMA.curie('name'),
                   model_uri=OPENPOLICYAGENT.opaPlan__name, domain=None, range=str)

slots.opaFuncs__funcs = Slot(uri=OPENPOLICYAGENT.funcs, name="opaFuncs__funcs", curie=OPENPOLICYAGENT.curie('funcs'),
                   model_uri=OPENPOLICYAGENT.opaFuncs__funcs, domain=None, range=Optional[Union[Union[dict, OpaFunc], list[Union[dict, OpaFunc]]]])

slots.opaFunc__blocks = Slot(uri=OPENPOLICYAGENT.blocks, name="opaFunc__blocks", curie=OPENPOLICYAGENT.curie('blocks'),
                   model_uri=OPENPOLICYAGENT.opaFunc__blocks, domain=None, range=Optional[Union[Union[dict, OpaBlock], list[Union[dict, OpaBlock]]]])

slots.opaFunc__name = Slot(uri=SCHEMA.name, name="opaFunc__name", curie=SCHEMA.curie('name'),
                   model_uri=OPENPOLICYAGENT.opaFunc__name, domain=None, range=str)

slots.opaFunc__params = Slot(uri=OPENPOLICYAGENT.params, name="opaFunc__params", curie=OPENPOLICYAGENT.curie('params'),
                   model_uri=OPENPOLICYAGENT.opaFunc__params, domain=None, range=Optional[Union[int, list[int]]])

slots.opaFunc__path = Slot(uri=OPENPOLICYAGENT.path, name="opaFunc__path", curie=OPENPOLICYAGENT.curie('path'),
                   model_uri=OPENPOLICYAGENT.opaFunc__path, domain=None, range=Optional[Union[str, list[str]]])

slots.opaFunc__return_local = Slot(uri=OPENPOLICYAGENT['return'], name="opaFunc__return_local", curie=OPENPOLICYAGENT.curie('return'),
                   model_uri=OPENPOLICYAGENT.opaFunc__return_local, domain=None, range=int)

slots.opaBlock__stmts = Slot(uri=OPENPOLICYAGENT.stmts, name="opaBlock__stmts", curie=OPENPOLICYAGENT.curie('stmts'),
                   model_uri=OPENPOLICYAGENT.opaBlock__stmts, domain=None, range=Union[Union[dict, OpaStmt], list[Union[dict, OpaStmt]]])

slots.opaUnplannedRule__location = Slot(uri=OPENPOLICYAGENT.location, name="opaUnplannedRule__location", curie=OPENPOLICYAGENT.curie('location'),
                   model_uri=OPENPOLICYAGENT.opaUnplannedRule__location, domain=None, range=Optional[Union[dict, OpaLocation]])

slots.opaUnplannedRule__path = Slot(uri=OPENPOLICYAGENT.path, name="opaUnplannedRule__path", curie=OPENPOLICYAGENT.curie('path'),
                   model_uri=OPENPOLICYAGENT.opaUnplannedRule__path, domain=None, range=str)

slots.opaArrayAppendStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaArrayAppendStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaArrayAppendStmt__stmt, domain=None, range=Union[dict, OpaArrayAppendStmtBody])

slots.opaArrayAppendStmtBody__array = Slot(uri=OPENPOLICYAGENT.array, name="opaArrayAppendStmtBody__array", curie=OPENPOLICYAGENT.curie('array'),
                   model_uri=OPENPOLICYAGENT.opaArrayAppendStmtBody__array, domain=None, range=int)

slots.opaArrayAppendStmtBody__value = Slot(uri=OPENPOLICYAGENT.value, name="opaArrayAppendStmtBody__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaArrayAppendStmtBody__value, domain=None, range=Union[dict, OpaOperand])

slots.opaAssignIntStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaAssignIntStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaAssignIntStmt__stmt, domain=None, range=Union[dict, OpaAssignIntStmtBody])

slots.opaAssignIntStmtBody__value = Slot(uri=OPENPOLICYAGENT.value, name="opaAssignIntStmtBody__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaAssignIntStmtBody__value, domain=None, range=int)

slots.opaAssignVarOnceStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaAssignVarOnceStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaAssignVarOnceStmt__stmt, domain=None, range=Union[dict, OpaAssignVarOnceStmtBody])

slots.opaAssignVarStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaAssignVarStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaAssignVarStmt__stmt, domain=None, range=Union[dict, OpaAssignVarStmtBody])

slots.opaBlockStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaBlockStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaBlockStmt__stmt, domain=None, range=Union[dict, OpaBlockStmtBody])

slots.opaBlockStmtBody__blocks = Slot(uri=OPENPOLICYAGENT.blocks, name="opaBlockStmtBody__blocks", curie=OPENPOLICYAGENT.curie('blocks'),
                   model_uri=OPENPOLICYAGENT.opaBlockStmtBody__blocks, domain=None, range=Optional[Union[Union[dict, OpaBlock], list[Union[dict, OpaBlock]]]])

slots.opaBreakStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaBreakStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaBreakStmt__stmt, domain=None, range=Union[dict, OpaBreakStmtBody])

slots.opaBreakStmtBody__index = Slot(uri=OPENPOLICYAGENT.index, name="opaBreakStmtBody__index", curie=OPENPOLICYAGENT.curie('index'),
                   model_uri=OPENPOLICYAGENT.opaBreakStmtBody__index, domain=None, range=int)

slots.opaCallDynamicStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaCallDynamicStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaCallDynamicStmt__stmt, domain=None, range=Union[dict, OpaCallDynamicStmtBody])

slots.opaCallDynamicStmtBody__args = Slot(uri=OPENPOLICYAGENT.args, name="opaCallDynamicStmtBody__args", curie=OPENPOLICYAGENT.curie('args'),
                   model_uri=OPENPOLICYAGENT.opaCallDynamicStmtBody__args, domain=None, range=Optional[Union[int, list[int]]])

slots.opaCallDynamicStmtBody__path = Slot(uri=OPENPOLICYAGENT.path, name="opaCallDynamicStmtBody__path", curie=OPENPOLICYAGENT.curie('path'),
                   model_uri=OPENPOLICYAGENT.opaCallDynamicStmtBody__path, domain=None, range=Optional[Union[Union[dict, OpaOperand], list[Union[dict, OpaOperand]]]])

slots.opaCallDynamicStmtBody__result = Slot(uri=OPENPOLICYAGENT.result, name="opaCallDynamicStmtBody__result", curie=OPENPOLICYAGENT.curie('result'),
                   model_uri=OPENPOLICYAGENT.opaCallDynamicStmtBody__result, domain=None, range=int)

slots.opaCallStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaCallStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaCallStmt__stmt, domain=None, range=Union[dict, OpaCallStmtBody])

slots.opaCallStmtBody__args = Slot(uri=OPENPOLICYAGENT.args, name="opaCallStmtBody__args", curie=OPENPOLICYAGENT.curie('args'),
                   model_uri=OPENPOLICYAGENT.opaCallStmtBody__args, domain=None, range=Optional[Union[Union[dict, OpaOperand], list[Union[dict, OpaOperand]]]])

slots.opaCallStmtBody__func = Slot(uri=OPENPOLICYAGENT.func, name="opaCallStmtBody__func", curie=OPENPOLICYAGENT.curie('func'),
                   model_uri=OPENPOLICYAGENT.opaCallStmtBody__func, domain=None, range=str)

slots.opaCallStmtBody__result = Slot(uri=OPENPOLICYAGENT.result, name="opaCallStmtBody__result", curie=OPENPOLICYAGENT.curie('result'),
                   model_uri=OPENPOLICYAGENT.opaCallStmtBody__result, domain=None, range=int)

slots.opaDotStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaDotStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaDotStmt__stmt, domain=None, range=Union[dict, OpaDotStmtBody])

slots.opaDotStmtBody__key = Slot(uri=OPENPOLICYAGENT.key, name="opaDotStmtBody__key", curie=OPENPOLICYAGENT.curie('key'),
                   model_uri=OPENPOLICYAGENT.opaDotStmtBody__key, domain=None, range=Union[dict, OpaOperand])

slots.opaEqualStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaEqualStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaEqualStmt__stmt, domain=None, range=Union[dict, OpaEqualStmtBody])

slots.opaEqualStmtBody__operand_a = Slot(uri=OPENPOLICYAGENT.a, name="opaEqualStmtBody__operand_a", curie=OPENPOLICYAGENT.curie('a'),
                   model_uri=OPENPOLICYAGENT.opaEqualStmtBody__operand_a, domain=None, range=Union[dict, OpaOperand])

slots.opaEqualStmtBody__operand_b = Slot(uri=OPENPOLICYAGENT.b, name="opaEqualStmtBody__operand_b", curie=OPENPOLICYAGENT.curie('b'),
                   model_uri=OPENPOLICYAGENT.opaEqualStmtBody__operand_b, domain=None, range=Union[dict, OpaOperand])

slots.opaIsArrayStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaIsArrayStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaIsArrayStmt__stmt, domain=None, range=Union[dict, OpaIsArrayStmtBody])

slots.opaIsDefinedStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaIsDefinedStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaIsDefinedStmt__stmt, domain=None, range=Union[dict, OpaIsDefinedStmtBody])

slots.opaIsObjectStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaIsObjectStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaIsObjectStmt__stmt, domain=None, range=Union[dict, OpaIsObjectStmtBody])

slots.opaIsSetStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaIsSetStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaIsSetStmt__stmt, domain=None, range=Union[dict, OpaIsSetStmtBody])

slots.opaIsUndefinedStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaIsUndefinedStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaIsUndefinedStmt__stmt, domain=None, range=Union[dict, OpaIsUndefinedStmtBody])

slots.opaLenStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaLenStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaLenStmt__stmt, domain=None, range=Union[dict, OpaLenStmtBody])

slots.opaMakeArrayStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaMakeArrayStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaMakeArrayStmt__stmt, domain=None, range=Union[dict, OpaMakeArrayStmtBody])

slots.opaMakeArrayStmtBody__capacity = Slot(uri=OPENPOLICYAGENT.capacity, name="opaMakeArrayStmtBody__capacity", curie=OPENPOLICYAGENT.curie('capacity'),
                   model_uri=OPENPOLICYAGENT.opaMakeArrayStmtBody__capacity, domain=None, range=int)

slots.opaMakeNullStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaMakeNullStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaMakeNullStmt__stmt, domain=None, range=Union[dict, OpaMakeNullStmtBody])

slots.opaMakeNumberIntStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaMakeNumberIntStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaMakeNumberIntStmt__stmt, domain=None, range=Union[dict, OpaMakeNumberIntStmtBody])

slots.opaMakeNumberIntStmtBody__value = Slot(uri=OPENPOLICYAGENT.value, name="opaMakeNumberIntStmtBody__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaMakeNumberIntStmtBody__value, domain=None, range=int)

slots.opaMakeNumberRefStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaMakeNumberRefStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaMakeNumberRefStmt__stmt, domain=None, range=Union[dict, OpaMakeNumberRefStmtBody])

slots.opaMakeNumberRefStmtBody__index = Slot(uri=OPENPOLICYAGENT.index, name="opaMakeNumberRefStmtBody__index", curie=OPENPOLICYAGENT.curie('index'),
                   model_uri=OPENPOLICYAGENT.opaMakeNumberRefStmtBody__index, domain=None, range=int)

slots.opaMakeNumberRefStmtBody__index_legacy = Slot(uri=OPENPOLICYAGENT.Index, name="opaMakeNumberRefStmtBody__index_legacy", curie=OPENPOLICYAGENT.curie('Index'),
                   model_uri=OPENPOLICYAGENT.opaMakeNumberRefStmtBody__index_legacy, domain=None, range=Optional[int])

slots.opaMakeObjectStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaMakeObjectStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaMakeObjectStmt__stmt, domain=None, range=Union[dict, OpaMakeObjectStmtBody])

slots.opaMakeSetStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaMakeSetStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaMakeSetStmt__stmt, domain=None, range=Union[dict, OpaMakeSetStmtBody])

slots.opaNopStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaNopStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaNopStmt__stmt, domain=None, range=Union[dict, OpaNopStmtBody])

slots.opaNotEqualStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaNotEqualStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaNotEqualStmt__stmt, domain=None, range=Union[dict, OpaNotEqualStmtBody])

slots.opaNotEqualStmtBody__operand_a = Slot(uri=OPENPOLICYAGENT.a, name="opaNotEqualStmtBody__operand_a", curie=OPENPOLICYAGENT.curie('a'),
                   model_uri=OPENPOLICYAGENT.opaNotEqualStmtBody__operand_a, domain=None, range=Union[dict, OpaOperand])

slots.opaNotEqualStmtBody__operand_b = Slot(uri=OPENPOLICYAGENT.b, name="opaNotEqualStmtBody__operand_b", curie=OPENPOLICYAGENT.curie('b'),
                   model_uri=OPENPOLICYAGENT.opaNotEqualStmtBody__operand_b, domain=None, range=Union[dict, OpaOperand])

slots.opaNotStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaNotStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaNotStmt__stmt, domain=None, range=Union[dict, OpaNotStmtBody])

slots.opaNotStmtBody__block = Slot(uri=OPENPOLICYAGENT.block, name="opaNotStmtBody__block", curie=OPENPOLICYAGENT.curie('block'),
                   model_uri=OPENPOLICYAGENT.opaNotStmtBody__block, domain=None, range=Optional[Union[dict, OpaBlock]])

slots.opaObjectInsertOnceStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaObjectInsertOnceStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaObjectInsertOnceStmt__stmt, domain=None, range=Union[dict, OpaObjectInsertOnceStmtBody])

slots.opaObjectInsertOnceStmtBody__key = Slot(uri=OPENPOLICYAGENT.key, name="opaObjectInsertOnceStmtBody__key", curie=OPENPOLICYAGENT.curie('key'),
                   model_uri=OPENPOLICYAGENT.opaObjectInsertOnceStmtBody__key, domain=None, range=Union[dict, OpaOperand])

slots.opaObjectInsertOnceStmtBody__object = Slot(uri=OPENPOLICYAGENT.object, name="opaObjectInsertOnceStmtBody__object", curie=OPENPOLICYAGENT.curie('object'),
                   model_uri=OPENPOLICYAGENT.opaObjectInsertOnceStmtBody__object, domain=None, range=int)

slots.opaObjectInsertOnceStmtBody__value = Slot(uri=OPENPOLICYAGENT.value, name="opaObjectInsertOnceStmtBody__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaObjectInsertOnceStmtBody__value, domain=None, range=Union[dict, OpaOperand])

slots.opaObjectInsertStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaObjectInsertStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaObjectInsertStmt__stmt, domain=None, range=Union[dict, OpaObjectInsertStmtBody])

slots.opaObjectInsertStmtBody__key = Slot(uri=OPENPOLICYAGENT.key, name="opaObjectInsertStmtBody__key", curie=OPENPOLICYAGENT.curie('key'),
                   model_uri=OPENPOLICYAGENT.opaObjectInsertStmtBody__key, domain=None, range=Union[dict, OpaOperand])

slots.opaObjectInsertStmtBody__object = Slot(uri=OPENPOLICYAGENT.object, name="opaObjectInsertStmtBody__object", curie=OPENPOLICYAGENT.curie('object'),
                   model_uri=OPENPOLICYAGENT.opaObjectInsertStmtBody__object, domain=None, range=int)

slots.opaObjectInsertStmtBody__value = Slot(uri=OPENPOLICYAGENT.value, name="opaObjectInsertStmtBody__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaObjectInsertStmtBody__value, domain=None, range=Union[dict, OpaOperand])

slots.opaObjectMergeStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaObjectMergeStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaObjectMergeStmt__stmt, domain=None, range=Union[dict, OpaObjectMergeStmtBody])

slots.opaObjectMergeStmtBody__operand_a = Slot(uri=OPENPOLICYAGENT.a, name="opaObjectMergeStmtBody__operand_a", curie=OPENPOLICYAGENT.curie('a'),
                   model_uri=OPENPOLICYAGENT.opaObjectMergeStmtBody__operand_a, domain=None, range=int)

slots.opaObjectMergeStmtBody__operand_b = Slot(uri=OPENPOLICYAGENT.b, name="opaObjectMergeStmtBody__operand_b", curie=OPENPOLICYAGENT.curie('b'),
                   model_uri=OPENPOLICYAGENT.opaObjectMergeStmtBody__operand_b, domain=None, range=int)

slots.opaResetLocalStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaResetLocalStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaResetLocalStmt__stmt, domain=None, range=Union[dict, OpaResetLocalStmtBody])

slots.opaResultSetAddStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaResultSetAddStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaResultSetAddStmt__stmt, domain=None, range=Union[dict, OpaResultSetAddStmtBody])

slots.opaResultSetAddStmtBody__value = Slot(uri=OPENPOLICYAGENT.value, name="opaResultSetAddStmtBody__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaResultSetAddStmtBody__value, domain=None, range=int)

slots.opaReturnLocalStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaReturnLocalStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaReturnLocalStmt__stmt, domain=None, range=Union[dict, OpaReturnLocalStmtBody])

slots.opaScanStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaScanStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaScanStmt__stmt, domain=None, range=Union[dict, OpaScanStmtBody])

slots.opaScanStmtBody__block = Slot(uri=OPENPOLICYAGENT.block, name="opaScanStmtBody__block", curie=OPENPOLICYAGENT.curie('block'),
                   model_uri=OPENPOLICYAGENT.opaScanStmtBody__block, domain=None, range=Optional[Union[dict, OpaBlock]])

slots.opaScanStmtBody__key = Slot(uri=OPENPOLICYAGENT.key, name="opaScanStmtBody__key", curie=OPENPOLICYAGENT.curie('key'),
                   model_uri=OPENPOLICYAGENT.opaScanStmtBody__key, domain=None, range=int)

slots.opaScanStmtBody__value = Slot(uri=OPENPOLICYAGENT.value, name="opaScanStmtBody__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaScanStmtBody__value, domain=None, range=int)

slots.opaSetAddStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaSetAddStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaSetAddStmt__stmt, domain=None, range=Union[dict, OpaSetAddStmtBody])

slots.opaSetAddStmtBody__set = Slot(uri=OPENPOLICYAGENT.set, name="opaSetAddStmtBody__set", curie=OPENPOLICYAGENT.curie('set'),
                   model_uri=OPENPOLICYAGENT.opaSetAddStmtBody__set, domain=None, range=int)

slots.opaSetAddStmtBody__value = Slot(uri=OPENPOLICYAGENT.value, name="opaSetAddStmtBody__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaSetAddStmtBody__value, domain=None, range=Union[dict, OpaOperand])

slots.opaWithStmt__stmt = Slot(uri=OPENPOLICYAGENT.stmt, name="opaWithStmt__stmt", curie=OPENPOLICYAGENT.curie('stmt'),
                   model_uri=OPENPOLICYAGENT.opaWithStmt__stmt, domain=None, range=Union[dict, OpaWithStmtBody])

slots.opaWithStmtBody__block = Slot(uri=OPENPOLICYAGENT.block, name="opaWithStmtBody__block", curie=OPENPOLICYAGENT.curie('block'),
                   model_uri=OPENPOLICYAGENT.opaWithStmtBody__block, domain=None, range=Optional[Union[dict, OpaBlock]])

slots.opaWithStmtBody__local = Slot(uri=OPENPOLICYAGENT.local, name="opaWithStmtBody__local", curie=OPENPOLICYAGENT.curie('local'),
                   model_uri=OPENPOLICYAGENT.opaWithStmtBody__local, domain=None, range=int)

slots.opaWithStmtBody__path = Slot(uri=OPENPOLICYAGENT.path, name="opaWithStmtBody__path", curie=OPENPOLICYAGENT.curie('path'),
                   model_uri=OPENPOLICYAGENT.opaWithStmtBody__path, domain=None, range=Optional[Union[int, list[int]]])

slots.opaWithStmtBody__value = Slot(uri=OPENPOLICYAGENT.value, name="opaWithStmtBody__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaWithStmtBody__value, domain=None, range=Union[dict, OpaOperand])

slots.opaBoolOperand__value = Slot(uri=OPENPOLICYAGENT.value, name="opaBoolOperand__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaBoolOperand__value, domain=None, range=Union[bool, Bool])

slots.opaLocalOperand__value = Slot(uri=OPENPOLICYAGENT.value, name="opaLocalOperand__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaLocalOperand__value, domain=None, range=int)

slots.opaStringIndexOperand__value = Slot(uri=OPENPOLICYAGENT.value, name="opaStringIndexOperand__value", curie=OPENPOLICYAGENT.curie('value'),
                   model_uri=OPENPOLICYAGENT.opaStringIndexOperand__value, domain=None, range=int)

slots.OpaAnyType_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaAnyType_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaAnyType_type, domain=OpaAnyType, range=str)

slots.OpaArrayType_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaArrayType_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaArrayType_type, domain=OpaArrayType, range=str)

slots.OpaBooleanType_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaBooleanType_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaBooleanType_type, domain=OpaBooleanType, range=str)

slots.OpaFunctionType_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaFunctionType_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaFunctionType_type, domain=OpaFunctionType, range=str)

slots.OpaNullType_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaNullType_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaNullType_type, domain=OpaNullType, range=str)

slots.OpaNumberType_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaNumberType_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaNumberType_type, domain=OpaNumberType, range=str)

slots.OpaObjectType_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaObjectType_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaObjectType_type, domain=OpaObjectType, range=str)

slots.OpaSetType_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaSetType_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaSetType_type, domain=OpaSetType, range=str)

slots.OpaStringType_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaStringType_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaStringType_type, domain=OpaStringType, range=str)

slots.OpaWasmAbiVersion_version = Slot(uri=OPENPOLICYAGENT.version, name="OpaWasmAbiVersion_version", curie=OPENPOLICYAGENT.curie('version'),
                   model_uri=OPENPOLICYAGENT.OpaWasmAbiVersion_version, domain=OpaWasmAbiVersion, range=int)

slots.OpaImplementation_version = Slot(uri=OPENPOLICYAGENT.version, name="OpaImplementation_version", curie=OPENPOLICYAGENT.curie('version'),
                   model_uri=OPENPOLICYAGENT.OpaImplementation_version, domain=OpaImplementation, range=str)

slots.OpaBuiltinArgument_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaBuiltinArgument_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaBuiltinArgument_type, domain=OpaBuiltinArgument, range=str)

slots.OpaBuiltinResult_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaBuiltinResult_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaBuiltinResult_type, domain=OpaBuiltinResult, range=Optional[str])

slots.OpaImplementationSupport_version = Slot(uri=OPENPOLICYAGENT.version, name="OpaImplementationSupport_version", curie=OPENPOLICYAGENT.curie('version'),
                   model_uri=OPENPOLICYAGENT.OpaImplementationSupport_version, domain=OpaImplementationSupport, range=Optional[str])

slots.OpaAuthorizationInput_body = Slot(uri=OPENPOLICYAGENT.body, name="OpaAuthorizationInput_body", curie=OPENPOLICYAGENT.curie('body'),
                   model_uri=OPENPOLICYAGENT.OpaAuthorizationInput_body, domain=OpaAuthorizationInput, range=Optional[Union[dict, OpaValue]])

slots.OpaManifest_revision = Slot(uri=OPENPOLICYAGENT.revision, name="OpaManifest_revision", curie=OPENPOLICYAGENT.curie('revision'),
                   model_uri=OPENPOLICYAGENT.OpaManifest_revision, domain=OpaManifest, range=str)

slots.OpaFileRegoVersion_version = Slot(uri=OPENPOLICYAGENT.version, name="OpaFileRegoVersion_version", curie=OPENPOLICYAGENT.curie('version'),
                   model_uri=OPENPOLICYAGENT.OpaFileRegoVersion_version, domain=OpaFileRegoVersion, range=int)

slots.OpaLocation_file = Slot(uri=OPENPOLICYAGENT.file, name="OpaLocation_file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.OpaLocation_file, domain=OpaLocation, range=int)

slots.OpaLocation_col = Slot(uri=OPENPOLICYAGENT.col, name="OpaLocation_col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.OpaLocation_col, domain=OpaLocation, range=int)

slots.OpaLocation_row = Slot(uri=OPENPOLICYAGENT.row, name="OpaLocation_row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.OpaLocation_row, domain=OpaLocation, range=int)

slots.OpaLocation_end_col = Slot(uri=OPENPOLICYAGENT.end_col, name="OpaLocation_end_col", curie=OPENPOLICYAGENT.curie('end_col'),
                   model_uri=OPENPOLICYAGENT.OpaLocation_end_col, domain=OpaLocation, range=int)

slots.OpaLocation_end_row = Slot(uri=OPENPOLICYAGENT.end_row, name="OpaLocation_end_row", curie=OPENPOLICYAGENT.curie('end_row'),
                   model_uri=OPENPOLICYAGENT.OpaLocation_end_row, domain=OpaLocation, range=int)

slots.OpaStmtBody_file = Slot(uri=OPENPOLICYAGENT.file, name="OpaStmtBody_file", curie=OPENPOLICYAGENT.curie('file'),
                   model_uri=OPENPOLICYAGENT.OpaStmtBody_file, domain=OpaStmtBody, range=int)

slots.OpaStmtBody_col = Slot(uri=OPENPOLICYAGENT.col, name="OpaStmtBody_col", curie=OPENPOLICYAGENT.curie('col'),
                   model_uri=OPENPOLICYAGENT.OpaStmtBody_col, domain=OpaStmtBody, range=int)

slots.OpaStmtBody_row = Slot(uri=OPENPOLICYAGENT.row, name="OpaStmtBody_row", curie=OPENPOLICYAGENT.curie('row'),
                   model_uri=OPENPOLICYAGENT.OpaStmtBody_row, domain=OpaStmtBody, range=int)

slots.OpaStmtBody_end_col = Slot(uri=OPENPOLICYAGENT.end_col, name="OpaStmtBody_end_col", curie=OPENPOLICYAGENT.curie('end_col'),
                   model_uri=OPENPOLICYAGENT.OpaStmtBody_end_col, domain=OpaStmtBody, range=int)

slots.OpaStmtBody_end_row = Slot(uri=OPENPOLICYAGENT.end_row, name="OpaStmtBody_end_row", curie=OPENPOLICYAGENT.curie('end_row'),
                   model_uri=OPENPOLICYAGENT.OpaStmtBody_end_row, domain=OpaStmtBody, range=int)

slots.OpaArrayAppendStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaArrayAppendStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaArrayAppendStmt_type, domain=OpaArrayAppendStmt, range=str)

slots.OpaAssignIntStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaAssignIntStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaAssignIntStmt_type, domain=OpaAssignIntStmt, range=str)

slots.OpaAssignIntStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaAssignIntStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaAssignIntStmtBody_target, domain=OpaAssignIntStmtBody, range=int)

slots.OpaAssignVarOnceStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaAssignVarOnceStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaAssignVarOnceStmt_type, domain=OpaAssignVarOnceStmt, range=str)

slots.OpaAssignVarOnceStmtBody_source = Slot(uri=OPENPOLICYAGENT.source, name="OpaAssignVarOnceStmtBody_source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.OpaAssignVarOnceStmtBody_source, domain=OpaAssignVarOnceStmtBody, range=Union[dict, "OpaOperand"])

slots.OpaAssignVarOnceStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaAssignVarOnceStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaAssignVarOnceStmtBody_target, domain=OpaAssignVarOnceStmtBody, range=int)

slots.OpaAssignVarStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaAssignVarStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaAssignVarStmt_type, domain=OpaAssignVarStmt, range=str)

slots.OpaAssignVarStmtBody_source = Slot(uri=OPENPOLICYAGENT.source, name="OpaAssignVarStmtBody_source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.OpaAssignVarStmtBody_source, domain=OpaAssignVarStmtBody, range=Union[dict, "OpaOperand"])

slots.OpaAssignVarStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaAssignVarStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaAssignVarStmtBody_target, domain=OpaAssignVarStmtBody, range=int)

slots.OpaBlockStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaBlockStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaBlockStmt_type, domain=OpaBlockStmt, range=str)

slots.OpaBreakStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaBreakStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaBreakStmt_type, domain=OpaBreakStmt, range=str)

slots.OpaCallDynamicStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaCallDynamicStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaCallDynamicStmt_type, domain=OpaCallDynamicStmt, range=str)

slots.OpaCallStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaCallStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaCallStmt_type, domain=OpaCallStmt, range=str)

slots.OpaDotStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaDotStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaDotStmt_type, domain=OpaDotStmt, range=str)

slots.OpaDotStmtBody_source = Slot(uri=OPENPOLICYAGENT.source, name="OpaDotStmtBody_source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.OpaDotStmtBody_source, domain=OpaDotStmtBody, range=Union[dict, "OpaOperand"])

slots.OpaDotStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaDotStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaDotStmtBody_target, domain=OpaDotStmtBody, range=int)

slots.OpaEqualStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaEqualStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaEqualStmt_type, domain=OpaEqualStmt, range=str)

slots.OpaIsArrayStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaIsArrayStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaIsArrayStmt_type, domain=OpaIsArrayStmt, range=str)

slots.OpaIsArrayStmtBody_source = Slot(uri=OPENPOLICYAGENT.source, name="OpaIsArrayStmtBody_source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.OpaIsArrayStmtBody_source, domain=OpaIsArrayStmtBody, range=Union[dict, "OpaOperand"])

slots.OpaIsDefinedStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaIsDefinedStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaIsDefinedStmt_type, domain=OpaIsDefinedStmt, range=str)

slots.OpaIsDefinedStmtBody_source = Slot(uri=OPENPOLICYAGENT.source, name="OpaIsDefinedStmtBody_source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.OpaIsDefinedStmtBody_source, domain=OpaIsDefinedStmtBody, range=int)

slots.OpaIsObjectStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaIsObjectStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaIsObjectStmt_type, domain=OpaIsObjectStmt, range=str)

slots.OpaIsObjectStmtBody_source = Slot(uri=OPENPOLICYAGENT.source, name="OpaIsObjectStmtBody_source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.OpaIsObjectStmtBody_source, domain=OpaIsObjectStmtBody, range=Union[dict, "OpaOperand"])

slots.OpaIsSetStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaIsSetStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaIsSetStmt_type, domain=OpaIsSetStmt, range=str)

slots.OpaIsSetStmtBody_source = Slot(uri=OPENPOLICYAGENT.source, name="OpaIsSetStmtBody_source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.OpaIsSetStmtBody_source, domain=OpaIsSetStmtBody, range=Union[dict, "OpaOperand"])

slots.OpaIsUndefinedStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaIsUndefinedStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaIsUndefinedStmt_type, domain=OpaIsUndefinedStmt, range=str)

slots.OpaIsUndefinedStmtBody_source = Slot(uri=OPENPOLICYAGENT.source, name="OpaIsUndefinedStmtBody_source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.OpaIsUndefinedStmtBody_source, domain=OpaIsUndefinedStmtBody, range=int)

slots.OpaLenStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaLenStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaLenStmt_type, domain=OpaLenStmt, range=str)

slots.OpaLenStmtBody_source = Slot(uri=OPENPOLICYAGENT.source, name="OpaLenStmtBody_source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.OpaLenStmtBody_source, domain=OpaLenStmtBody, range=Union[dict, "OpaOperand"])

slots.OpaLenStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaLenStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaLenStmtBody_target, domain=OpaLenStmtBody, range=int)

slots.OpaMakeArrayStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaMakeArrayStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaMakeArrayStmt_type, domain=OpaMakeArrayStmt, range=str)

slots.OpaMakeArrayStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaMakeArrayStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaMakeArrayStmtBody_target, domain=OpaMakeArrayStmtBody, range=int)

slots.OpaMakeNullStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaMakeNullStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaMakeNullStmt_type, domain=OpaMakeNullStmt, range=str)

slots.OpaMakeNullStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaMakeNullStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaMakeNullStmtBody_target, domain=OpaMakeNullStmtBody, range=int)

slots.OpaMakeNumberIntStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaMakeNumberIntStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaMakeNumberIntStmt_type, domain=OpaMakeNumberIntStmt, range=str)

slots.OpaMakeNumberIntStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaMakeNumberIntStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaMakeNumberIntStmtBody_target, domain=OpaMakeNumberIntStmtBody, range=int)

slots.OpaMakeNumberRefStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaMakeNumberRefStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaMakeNumberRefStmt_type, domain=OpaMakeNumberRefStmt, range=str)

slots.OpaMakeNumberRefStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaMakeNumberRefStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaMakeNumberRefStmtBody_target, domain=OpaMakeNumberRefStmtBody, range=int)

slots.OpaMakeObjectStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaMakeObjectStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaMakeObjectStmt_type, domain=OpaMakeObjectStmt, range=str)

slots.OpaMakeObjectStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaMakeObjectStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaMakeObjectStmtBody_target, domain=OpaMakeObjectStmtBody, range=int)

slots.OpaMakeSetStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaMakeSetStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaMakeSetStmt_type, domain=OpaMakeSetStmt, range=str)

slots.OpaMakeSetStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaMakeSetStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaMakeSetStmtBody_target, domain=OpaMakeSetStmtBody, range=int)

slots.OpaNopStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaNopStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaNopStmt_type, domain=OpaNopStmt, range=str)

slots.OpaNotEqualStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaNotEqualStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaNotEqualStmt_type, domain=OpaNotEqualStmt, range=str)

slots.OpaNotStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaNotStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaNotStmt_type, domain=OpaNotStmt, range=str)

slots.OpaObjectInsertOnceStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaObjectInsertOnceStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaObjectInsertOnceStmt_type, domain=OpaObjectInsertOnceStmt, range=str)

slots.OpaObjectInsertStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaObjectInsertStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaObjectInsertStmt_type, domain=OpaObjectInsertStmt, range=str)

slots.OpaObjectMergeStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaObjectMergeStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaObjectMergeStmt_type, domain=OpaObjectMergeStmt, range=str)

slots.OpaObjectMergeStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaObjectMergeStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaObjectMergeStmtBody_target, domain=OpaObjectMergeStmtBody, range=int)

slots.OpaResetLocalStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaResetLocalStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaResetLocalStmt_type, domain=OpaResetLocalStmt, range=str)

slots.OpaResetLocalStmtBody_target = Slot(uri=OPENPOLICYAGENT.target, name="OpaResetLocalStmtBody_target", curie=OPENPOLICYAGENT.curie('target'),
                   model_uri=OPENPOLICYAGENT.OpaResetLocalStmtBody_target, domain=OpaResetLocalStmtBody, range=int)

slots.OpaResultSetAddStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaResultSetAddStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaResultSetAddStmt_type, domain=OpaResultSetAddStmt, range=str)

slots.OpaReturnLocalStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaReturnLocalStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaReturnLocalStmt_type, domain=OpaReturnLocalStmt, range=str)

slots.OpaReturnLocalStmtBody_source = Slot(uri=OPENPOLICYAGENT.source, name="OpaReturnLocalStmtBody_source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.OpaReturnLocalStmtBody_source, domain=OpaReturnLocalStmtBody, range=int)

slots.OpaScanStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaScanStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaScanStmt_type, domain=OpaScanStmt, range=str)

slots.OpaScanStmtBody_source = Slot(uri=OPENPOLICYAGENT.source, name="OpaScanStmtBody_source", curie=OPENPOLICYAGENT.curie('source'),
                   model_uri=OPENPOLICYAGENT.OpaScanStmtBody_source, domain=OpaScanStmtBody, range=int)

slots.OpaSetAddStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaSetAddStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaSetAddStmt_type, domain=OpaSetAddStmt, range=str)

slots.OpaWithStmt_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaWithStmt_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaWithStmt_type, domain=OpaWithStmt, range=str)

slots.OpaBoolOperand_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaBoolOperand_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaBoolOperand_type, domain=OpaBoolOperand, range=str)

slots.OpaLocalOperand_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaLocalOperand_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaLocalOperand_type, domain=OpaLocalOperand, range=str)

slots.OpaStringIndexOperand_type = Slot(uri=OPENPOLICYAGENT.type, name="OpaStringIndexOperand_type", curie=OPENPOLICYAGENT.curie('type'),
                   model_uri=OPENPOLICYAGENT.OpaStringIndexOperand_type, domain=OpaStringIndexOperand, range=str)
