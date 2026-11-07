from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "1.22.2"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'upstream_commit': {'tag': 'upstream_commit',
                                         'value': '482d9e368c2ddfed67ced59259fa6a247bb5f1e5'},
                     'upstream_license': {'tag': 'upstream_license',
                                          'value': 'Apache-2.0'},
                     'upstream_release_date': {'tag': 'upstream_release_date',
                                               'value': '2026-11-05'},
                     'upstream_tag': {'tag': 'upstream_tag', 'value': 'v1.22.2'}},
     'default_prefix': 'openpolicyagent',
     'default_range': 'string',
     'description': 'A LinkML model of the JSON formats Open Policy Agent defines: '
                    'the IR plan, the bundle manifest, the authorization policy '
                    'input, the capabilities document, the built-in function '
                    'metadata and the version index. Each module renders one '
                    "format, and keeps OPA's keys, so a document OPA writes "
                    'validates here unchanged.',
     'id': 'https://w3id.org/lmodel/opa',
     'imports': ['linkml:types',
                 'common',
                 'capabilities',
                 'builtin_metadata',
                 'version_index',
                 'authorization_input',
                 'bundle_manifest',
                 'ir_plan'],
     'keywords': ['policy as code', 'Open Policy Agent', 'Rego', 'CNCF'],
     'license': 'Apache-2.0',
     'name': 'opa',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'openpolicyagent': {'prefix_prefix': 'openpolicyagent',
                                      'prefix_reference': 'https://w3id.org/lmodel/opa/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://lmodel.github.io/opa',
                  'https://www.openpolicyagent.org/docs'],
     'source': 'https://github.com/open-policy-agent/opa/tree/482d9e368c2ddfed67ced59259fa6a247bb5f1e5',
     'source_file': 'src/opa/schema/opa.yaml',
     'title': 'Open Policy Agent (OPA)'} )

class OpaFutureKeyword(str, Enum):
    """
    The future keywords the shipped capabilities files name.
    """
    and_ = "and"
    contains = "contains"
    every = "every"
    if_ = "if"
    in_ = "in"
    not_ = "not"
    or_ = "or"


class OpaFeature(str, Enum):
    """
    The language features the shipped capabilities files name.
    """
    keywords_in_refs = "keywords_in_refs"
    rego_v1 = "rego_v1"
    rego_v1_import = "rego_v1_import"
    rego_v2 = "rego_v2"
    rego_v2_import = "rego_v2_import"
    rule_head_ref_string_prefixes = "rule_head_ref_string_prefixes"
    rule_head_refs = "rule_head_refs"
    template_strings = "template_strings"



class OpaObject(ConfiguredBaseModel):
    """
    A JSON object whose keys OPA leaves open.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/opa/common'})

    pass


class OpaType(ConfiguredBaseModel):
    """
    A Rego type, as OPA's types package writes it in JSON. A named type is an argument or result of a built-in function, with a name and a description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/lmodel/opa/common'})

    name: Optional[str] = Field(default=None, description="""The argument's or result's name, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the argument or result holds, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })


class OpaAnyType(OpaType):
    """
    A union of the types it lists in `of`, or any value when it lists none.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/common'})

    type: Literal["any"] = Field(default=..., description="""The kind of type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'any'} })
    of: Optional[list[OpaType]] = Field(default=None, description="""The types the union admits.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType', 'OpaSetType']} })
    name: Optional[str] = Field(default=None, description="""The argument's or result's name, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the argument or result holds, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })


class OpaArrayType(OpaType):
    """
    An array, with a type per position in `static` and one for the rest in `dynamic`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/common'})

    type: Literal["array"] = Field(default=..., description="""The kind of type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'array'} })
    static: Optional[list[OpaType]] = Field(default=None, description="""The type of each element by position.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayType', 'OpaObjectType', 'OpaPolicy']} })
    dynamic: Optional[OpaType] = Field(default=None, description="""The type of the elements after the static ones.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayType', 'OpaObjectType']} })
    name: Optional[str] = Field(default=None, description="""The argument's or result's name, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the argument or result holds, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })


class OpaBooleanType(OpaType):
    """
    A boolean.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/common'})

    type: Literal["boolean"] = Field(default=..., description="""The kind of type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'boolean'} })
    name: Optional[str] = Field(default=None, description="""The argument's or result's name, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the argument or result holds, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })


class OpaFunctionType(OpaType):
    """
    A function, with its arguments, its result and a variadic argument type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/common'})

    type: Literal["function"] = Field(default=..., description="""The kind of type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'function'} })
    args: Optional[list[OpaType]] = Field(default=None, description="""The argument types, in order.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaFunctionType',
                       'OpaBuiltinMetadata',
                       'OpaCallDynamicStmtBody',
                       'OpaCallStmtBody']} })
    result: Optional[OpaType] = Field(default=None, description="""The result type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaFunctionType',
                       'OpaBuiltinMetadata',
                       'OpaCallDynamicStmtBody',
                       'OpaCallStmtBody']} })
    variadic: Optional[OpaType] = Field(default=None, description="""The type of any further arguments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaFunctionType']} })
    name: Optional[str] = Field(default=None, description="""The argument's or result's name, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the argument or result holds, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })


class OpaNullType(OpaType):
    """
    The null value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/common'})

    type: Literal["null"] = Field(default=..., description="""The kind of type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'null'} })
    name: Optional[str] = Field(default=None, description="""The argument's or result's name, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the argument or result holds, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })


class OpaNumberType(OpaType):
    """
    A number.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/common'})

    type: Literal["number"] = Field(default=..., description="""The kind of type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'number'} })
    name: Optional[str] = Field(default=None, description="""The argument's or result's name, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the argument or result holds, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })


class OpaObjectType(OpaType):
    """
    An object, with typed known keys in `static` and a key and value type for the rest in `dynamic`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/common'})

    type: Literal["object"] = Field(default=..., description="""The kind of type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'object'} })
    static: Optional[list[OpaStaticProperty]] = Field(default=None, description="""The known keys and the types of their values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayType', 'OpaObjectType', 'OpaPolicy']} })
    dynamic: Optional[OpaDynamicProperty] = Field(default=None, description="""The key type and value type of the other keys.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayType', 'OpaObjectType']} })
    name: Optional[str] = Field(default=None, description="""The argument's or result's name, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the argument or result holds, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })


class OpaSetType(OpaType):
    """
    A set, whose members have the type in `of`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/common'})

    type: Literal["set"] = Field(default=..., description="""The kind of type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'set'} })
    of: Optional[OpaType] = Field(default=None, description="""The type of the set's members.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType', 'OpaSetType']} })
    name: Optional[str] = Field(default=None, description="""The argument's or result's name, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the argument or result holds, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })


class OpaStringType(OpaType):
    """
    A string.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/common'})

    type: Literal["string"] = Field(default=..., description="""The kind of type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'string'} })
    name: Optional[str] = Field(default=None, description="""The argument's or result's name, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the argument or result holds, on a named type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })


class OpaStaticProperty(ConfiguredBaseModel):
    """
    A known key of an object type and the type of its value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/common'})

    key: Any = Field(default=..., description="""The key, as a JSON value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaDotStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaScanStmtBody']} })
    value: OpaType = Field(default=..., description="""The type of the key's value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })


class OpaDynamicProperty(ConfiguredBaseModel):
    """
    The key type and value type that an object type gives its other keys.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/common'})

    key: OpaType = Field(default=..., description="""The type of the keys.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaDotStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaScanStmtBody']} })
    value: OpaType = Field(default=..., description="""The type of the values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })


class OpaCapabilities(ConfiguredBaseModel):
    """
    What an OPA version supports, which a policy can be checked against.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/capabilities', 'tree_root': True})

    builtins: Optional[list[OpaBuiltin]] = Field(default=None, description="""The built-in functions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaCapabilities', 'OpaBuiltinCategory', 'OpaVersionIndex']} })
    future_keywords: Optional[list[OpaFutureKeyword]] = Field(default=None, description="""The keywords a policy may import from future.keywords.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaCapabilities']} })
    wasm_abi_versions: Optional[list[OpaWasmAbiVersion]] = Field(default=None, description="""The Wasm ABI versions supported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaCapabilities']} })
    features: Optional[list[OpaFeature]] = Field(default=None, description="""The language features supported.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaCapabilities', 'OpaVersionIndex']} })
    allow_net: Optional[list[str]] = Field(default=None, description="""The hosts OPA may connect to, as host names or IP addresses. OPA reaches any host when the key is absent, and none when the list is empty.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaCapabilities']} })


class OpaBuiltin(ConfiguredBaseModel):
    """
    A built-in function and its type declaration.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/capabilities'})

    name: str = Field(default=..., description="""The function's name, such as `array.concat`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the function does.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })
    categories: Optional[list[str]] = Field(default=None, description="""The categories the function belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltin', 'OpaBuiltinMetadataCatalog']} })
    decl: OpaFunctionType = Field(default=..., description="""The function's type declaration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltin', 'OpaBuiltinFunc']} })
    infix: Optional[str] = Field(default=None, description="""The infix operator that calls the function, such as `+`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltin', 'OpaBuiltinMetadata']} })
    relation: Optional[bool] = Field(default=None, description="""Whether the function acts as a relation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltin', 'OpaBuiltinMetadata']} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether the function is deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltin', 'OpaBuiltinMetadata']} })
    nondeterministic: Optional[bool] = Field(default=None, description="""Whether the function may return different results for the same arguments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltin']} })


class OpaWasmAbiVersion(ConfiguredBaseModel):
    """
    A Wasm ABI version, as a major and a minor number.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/capabilities'})

    version: int = Field(default=..., description="""The major version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaWasmAbiVersion',
                       'OpaImplementation',
                       'OpaImplementationSupport',
                       'OpaFileRegoVersion']} })
    minor_version: int = Field(default=..., description="""The minor version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaWasmAbiVersion']} })


class OpaBuiltinMetadataCatalog(ConfiguredBaseModel):
    """
    The catalogue: two keys that start with an underscore, and one key per built-in function, whose value describes it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'range_expression': {'range': 'OpaBuiltinMetadata'}},
         'from_schema': 'https://w3id.org/lmodel/opa/builtin_metadata',
         'tree_root': True})

    categories: Optional[dict[str, Union[str, OpaBuiltinCategory]]] = Field(default=None, alias="_categories", description="""The categories, each with the names of its functions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltin', 'OpaBuiltinMetadataCatalog']} })
    implementations: Optional[list[OpaImplementation]] = Field(default=None, alias="_implementations", description="""The implementations of Rego besides OPA that the catalogue tracks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltinMetadataCatalog', 'OpaBuiltinMetadata']} })


class OpaBuiltinCategory(ConfiguredBaseModel):
    """
    A category of built-in functions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/builtin_metadata'})

    name: str = Field(default=..., description="""The category's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    builtins: list[str] = Field(default=..., description="""The names of the category's functions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaCapabilities', 'OpaBuiltinCategory', 'OpaVersionIndex']} })


class OpaImplementation(ConfiguredBaseModel):
    """
    An implementation of Rego besides OPA.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/builtin_metadata'})

    id: str = Field(default=..., description="""The implementation's key in each function's `implementations`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaImplementation'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""The implementation's display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaImplementation']} })
    repo: str = Field(default=..., description="""The implementation's GitHub repository, as owner/name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaImplementation']} })
    version: str = Field(default=..., description="""The implementation's version the catalogue reflects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaWasmAbiVersion',
                       'OpaImplementation',
                       'OpaImplementationSupport',
                       'OpaFileRegoVersion'],
         'slot_uri': 'schema:version'} })


class OpaBuiltinMetadata(ConfiguredBaseModel):
    """
    What the catalogue says about one built-in function.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/builtin_metadata'})

    description: Optional[str] = Field(default=None, description="""What the function does.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })
    introduced: str = Field(default=..., description="""The OPA version that added the function.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltinMetadata']} })
    available: list[str] = Field(default=..., description="""The OPA versions that have the function, and `edge`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltinMetadata']} })
    wasm: bool = Field(default=..., description="""Whether OPA's Wasm target implements the function.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltinMetadata', 'OpaManifest']} })
    args: list[OpaBuiltinArgument] = Field(default=..., description="""The arguments, in order.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaFunctionType',
                       'OpaBuiltinMetadata',
                       'OpaCallDynamicStmtBody',
                       'OpaCallStmtBody']} })
    result: OpaBuiltinResult = Field(default=..., description="""The result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaFunctionType',
                       'OpaBuiltinMetadata',
                       'OpaCallDynamicStmtBody',
                       'OpaCallStmtBody']} })
    implementations: dict[str, Union[str, OpaImplementationSupport]] = Field(default=..., description="""The other implementations that support the function, with the version that added it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltinMetadataCatalog', 'OpaBuiltinMetadata']} })
    infix: Optional[str] = Field(default=None, description="""The infix operator that calls the function.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltin', 'OpaBuiltinMetadata']} })
    relation: Optional[bool] = Field(default=None, description="""Whether the function acts as a relation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltin', 'OpaBuiltinMetadata']} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether the function is deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltin', 'OpaBuiltinMetadata']} })


class OpaBuiltinArgument(ConfiguredBaseModel):
    """
    An argument of a built-in function.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/builtin_metadata'})

    name: Optional[str] = Field(default=None, description="""The argument's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the argument holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })
    type: str = Field(default=..., description="""The argument's type, written as OPA prints types, such as `array[string]`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })


class OpaBuiltinResult(ConfiguredBaseModel):
    """
    The result of a built-in function. Some functions declare none.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/builtin_metadata'})

    name: Optional[str] = Field(default=None, description="""The result's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the result holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinMetadata',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult'],
         'slot_uri': 'schema:description'} })
    type: Optional[str] = Field(default=None, description="""The result's type, written as OPA prints types.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })


class OpaImplementationSupport(ConfiguredBaseModel):
    """
    An implementation that supports a function, and the version that added it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/builtin_metadata'})

    implementation: str = Field(default=..., description="""The implementation's id.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaImplementationSupport']} })
    version: str = Field(default=..., description="""The implementation's version that added the function.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaWasmAbiVersion',
                       'OpaImplementation',
                       'OpaImplementationSupport',
                       'OpaFileRegoVersion'],
         'slot_uri': 'schema:version'} })


class OpaVersionIndex(ConfiguredBaseModel):
    """
    The version index.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/version_index', 'tree_root': True})

    builtins: dict[str, OpaVersionEntry] = Field(default=..., description="""The builtins, keyed by name, each with the version that introduced it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaCapabilities', 'OpaBuiltinCategory', 'OpaVersionIndex']} })
    features: dict[str, OpaVersionEntry] = Field(default=..., description="""The features, keyed by name, each with the version that introduced it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaCapabilities', 'OpaVersionIndex']} })
    keywords: dict[str, OpaVersionEntry] = Field(default=..., description="""The keywords, keyed by name, each with the version that introduced it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaVersionIndex']} })


class OpaVersionEntry(ConfiguredBaseModel):
    """
    A built-in function, feature or keyword, and the OPA version that introduced it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/version_index'})

    name: str = Field(default=..., description="""The name of the function, feature or keyword.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    Major: int = Field(default=..., description="""The major version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaVersionEntry']} })
    Minor: int = Field(default=..., description="""The minor version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaVersionEntry']} })
    Patch: int = Field(default=..., description="""The patch version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaVersionEntry']} })
    PreRelease: Optional[str] = Field(default=None, description="""The pre-release label, such as `rc2`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaVersionEntry']} })


class OpaAuthorizationInput(ConfiguredBaseModel):
    """
    The OPA Authorization Policy Input document.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/opa/authorization_input',
         'tree_root': True})

    identity: str = Field(default=..., description="""The bearer token or client certificate subject that identifies the caller.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput']} })
    client_certificates: list[OpaObject] = Field(default=..., description="""The client's TLS certificates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput']} })
    method: str = Field(default=..., description="""The HTTP method of the request.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput']} })
    path: list[str] = Field(default=..., description="""The request path, one segment per element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput',
                       'OpaFileRegoVersion',
                       'OpaFunc',
                       'OpaUnplannedRule',
                       'OpaCallDynamicStmtBody',
                       'OpaWithStmtBody']} })
    params: OpaObject = Field(default=..., description="""The query parameters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput', 'OpaFunc']} })
    headers: OpaObject = Field(default=..., description="""The request headers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput']} })
    body: OpaObject = Field(default=..., description="""The request body.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput']} })


class OpaManifest(ConfiguredBaseModel):
    """
    A bundle manifest. OPA's schema leaves the manifest open to other keys.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_manifest:Manifest'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/opa/bundle_manifest',
         'tree_root': True})

    file_rego_versions: Optional[dict[str, Union[int, OpaFileRegoVersion]]] = Field(default=None, description="""Rego versions for single files, which override `rego_version`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaManifest']} })
    metadata: Optional[OpaObject] = Field(default=None, description="""Metadata the bundle's author adds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaManifest']} })
    rego_version: Optional[int] = Field(default=None, description="""The Rego version of the bundle's files: 0 for v0, 1 for v1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaManifest']} })
    revision: str = Field(default=..., description="""The bundle's revision, a string the bundle's author chooses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaManifest']} })
    roots: Optional[list[str]] = Field(default=None, description="""The paths in the data tree the bundle owns. A bundle without the key owns the whole tree.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaManifest']} })
    wasm: Optional[list[OpaWasmResolver]] = Field(default=None, description="""The Wasm modules the bundle holds, and the entrypoints they resolve.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltinMetadata', 'OpaManifest']} })


class OpaWasmResolver(ConfiguredBaseModel):
    """
    A Wasm module in a bundle, and the entrypoint it resolves.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_manifest:WasmResolver'],
         'from_schema': 'https://w3id.org/lmodel/opa/bundle_manifest'})

    annotations: Optional[list[OpaObject]] = Field(default=None, description="""The entrypoint's Rego annotations. OPA's schema leaves their shape open.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaWasmResolver']} })
    entrypoint: Optional[str] = Field(default=None, description="""The entrypoint the module resolves.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaWasmResolver']} })
    module: Optional[str] = Field(default=None, description="""The module's path in the bundle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaWasmResolver']} })


class OpaFileRegoVersion(ConfiguredBaseModel):
    """
    The Rego version of one file in the bundle.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/bundle_manifest'})

    path: str = Field(default=..., description="""The file's path in the bundle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput',
                       'OpaFileRegoVersion',
                       'OpaFunc',
                       'OpaUnplannedRule',
                       'OpaCallDynamicStmtBody',
                       'OpaWithStmtBody']} })
    version: int = Field(default=..., description="""The file's Rego version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaWasmAbiVersion',
                       'OpaImplementation',
                       'OpaImplementationSupport',
                       'OpaFileRegoVersion']} })


class OpaPolicy(ConfiguredBaseModel):
    """
    Policy represents a planned policy query.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:Policy'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan',
         'tree_root': True})

    funcs: Optional[OpaFuncs] = Field(default=None, description="""The functions the plans call.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaPolicy', 'OpaFuncs']} })
    plans: Optional[OpaPlans] = Field(default=None, description="""The query plans the policy exposes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaPolicy', 'OpaPlans']} })
    static: Optional[OpaStatic] = Field(default=None, description="""The constants the plan indexes into.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayType', 'OpaObjectType', 'OpaPolicy']} })
    unplanned_rules: Optional[list[OpaUnplannedRule]] = Field(default=None, description="""The rules left out because no entrypoint reaches them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaPolicy']} })


class OpaStatic(ConfiguredBaseModel):
    """
    Static represents a static data segment that is indexed into by the policy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:Static'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    builtin_funcs: Optional[list[OpaBuiltinFunc]] = Field(default=None, description="""The built-in functions the plan calls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStatic']} })
    files: Optional[list[OpaStringConst]] = Field(default=None, description="""The names of the policy files, which a location refers to by position.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStatic']} })
    strings: Optional[list[OpaStringConst]] = Field(default=None, description="""The string constants, which a string index refers to by position.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStatic']} })


class OpaStringConst(ConfiguredBaseModel):
    """
    StringConst represents a string value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:StringConst'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    value: str = Field(default=..., description="""The string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })


class OpaBuiltinFunc(ConfiguredBaseModel):
    """
    BuiltinFunc represents a built-in function that may be required by the policy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:BuiltinFunc'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    decl: Optional[OpaFunctionType] = Field(default=None, description="""BuiltinFunc declaration; opaque in this schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBuiltin', 'OpaBuiltinFunc']} })
    name: str = Field(default=..., description="""The function's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })


class OpaPlans(ConfiguredBaseModel):
    """
    Plans represents a collection of named query plans to expose in the policy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:Plans'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    plans: Optional[list[OpaPlan]] = Field(default=None, description="""The plans.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaPolicy', 'OpaPlans']} })


class OpaPlan(ConfiguredBaseModel):
    """
    Plan represents an ordered series of blocks to execute. Plan execution stops when a return statement is reached.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:Plan'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    blocks: Optional[list[OpaBlock]] = Field(default=None, description="""The blocks, run in order.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaPlan', 'OpaFunc', 'OpaBlockStmtBody']} })
    name: str = Field(default=..., description="""The plan's name, which is its entrypoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })


class OpaFuncs(ConfiguredBaseModel):
    """
    Funcs represents a collection of planned functions to include in the policy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:Funcs'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    funcs: Optional[list[OpaFunc]] = Field(default=None, description="""The functions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaPolicy', 'OpaFuncs']} })


class OpaFunc(ConfiguredBaseModel):
    """
    Func represents a named plan (function) that can be invoked. Functions accept one or more parameters and return a value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:Func'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    blocks: Optional[list[OpaBlock]] = Field(default=None, description="""The blocks, run in order.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaPlan', 'OpaFunc', 'OpaBlockStmtBody']} })
    name: str = Field(default=..., description="""The function's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaType',
                       'OpaBuiltin',
                       'OpaBuiltinCategory',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaVersionEntry',
                       'OpaBuiltinFunc',
                       'OpaPlan',
                       'OpaFunc'],
         'slot_uri': 'schema:name'} })
    params: Optional[list[int]] = Field(default=None, description="""The locals that hold the parameters. The first two are the input and data documents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput', 'OpaFunc']} })
    path: Optional[list[str]] = Field(default=None, description="""Where the function sits in the data tree, when it has a path.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput',
                       'OpaFileRegoVersion',
                       'OpaFunc',
                       'OpaUnplannedRule',
                       'OpaCallDynamicStmtBody',
                       'OpaWithStmtBody']} })
    return_: int = Field(default=..., alias="return", description="""The local that holds the return value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaFunc']} })


class OpaBlock(ConfiguredBaseModel):
    """
    Block represents an ordered sequence of statements to execute. Blocks are executed until a return statement is encountered, a statement is undefined, or there are no more statements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:Block'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    stmts: list[OpaStmt] = Field(default=..., description="""The statements, run in order.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBlock']} })


class OpaUnplannedRule(ConfiguredBaseModel):
    """
    UnplannedRule represents a rule that was parsed but not included in the plan because it is not reachable from the entrypoint. This is used for coverage reporting, to distinguish rules that were never planned from rules that were planned but never executed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:UnplannedRule'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    location: Optional[OpaLocation] = Field(default=None, description="""Where the rule is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaUnplannedRule']} })
    path: str = Field(default=..., description="""The rule's path.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput',
                       'OpaFileRegoVersion',
                       'OpaFunc',
                       'OpaUnplannedRule',
                       'OpaCallDynamicStmtBody',
                       'OpaWithStmtBody']} })


class OpaLocation(ConfiguredBaseModel):
    """
    Location records the filen index, and the row and column inside that file that a statement can be connected to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:Location'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan',
         'slot_usage': {'col': {'name': 'col', 'required': True},
                        'end_col': {'name': 'end_col', 'required': True},
                        'end_row': {'name': 'end_row', 'required': True},
                        'file': {'name': 'file', 'required': True},
                        'row': {'name': 'row', 'required': True}}})

    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaStmt(ConfiguredBaseModel):
    """
    Stmt represents an operation (e.g., comparison, loop, dot, etc.) to execute. OPA writes each statement as its kind in `type` and its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'exact_mappings': ['opa_plan:Stmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    pass


class OpaStmtBody(ConfiguredBaseModel):
    """
    The fields of a statement. Every kind carries the location of its source text.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan',
         'slot_usage': {'col': {'name': 'col', 'required': True},
                        'end_col': {'name': 'end_col', 'required': True},
                        'end_row': {'name': 'end_row', 'required': True},
                        'file': {'name': 'file', 'required': True},
                        'row': {'name': 'row', 'required': True}}})

    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaArrayAppendStmt(OpaStmt):
    """
    A statement of kind ArrayAppendStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["ArrayAppendStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'ArrayAppendStmt'} })
    stmt: OpaArrayAppendStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaArrayAppendStmtBody(OpaStmtBody):
    """
    ArrayAppendStmt represents a dynamic append operation of a value onto an array.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:ArrayAppendStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    array: int = Field(default=..., description="""The local that holds the array.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmtBody']} })
    value: OpaOperand = Field(default=..., description="""The value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaAssignIntStmt(OpaStmt):
    """
    A statement of kind AssignIntStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["AssignIntStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'AssignIntStmt'} })
    stmt: OpaAssignIntStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaAssignIntStmtBody(OpaStmtBody):
    """
    AssignIntStmt represents an assignment of an integer value to a local variable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:AssignIntStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    value: int = Field(default=..., description="""The value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaAssignVarOnceStmt(OpaStmt):
    """
    A statement of kind AssignVarOnceStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["AssignVarOnceStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'AssignVarOnceStmt'} })
    stmt: OpaAssignVarOnceStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaAssignVarOnceStmtBody(OpaStmtBody):
    """
    AssignVarOnceStmt represents an assignment of one local variable to another. If the target is defined, execution aborts with a conflict error.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:AssignVarOnceStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    source: OpaOperand = Field(default=..., description="""What the statement reads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaIsArrayStmtBody',
                       'OpaIsDefinedStmtBody',
                       'OpaIsObjectStmtBody',
                       'OpaIsSetStmtBody',
                       'OpaIsUndefinedStmtBody',
                       'OpaLenStmtBody',
                       'OpaReturnLocalStmtBody',
                       'OpaScanStmtBody']} })
    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaAssignVarStmt(OpaStmt):
    """
    A statement of kind AssignVarStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["AssignVarStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'AssignVarStmt'} })
    stmt: OpaAssignVarStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaAssignVarStmtBody(OpaStmtBody):
    """
    AssignVarStmt represents an assignment of one local variable to another.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:AssignVarStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    source: OpaOperand = Field(default=..., description="""What the statement reads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaIsArrayStmtBody',
                       'OpaIsDefinedStmtBody',
                       'OpaIsObjectStmtBody',
                       'OpaIsSetStmtBody',
                       'OpaIsUndefinedStmtBody',
                       'OpaLenStmtBody',
                       'OpaReturnLocalStmtBody',
                       'OpaScanStmtBody']} })
    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaBlockStmt(OpaStmt):
    """
    A statement of kind BlockStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["BlockStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'BlockStmt'} })
    stmt: OpaBlockStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaBlockStmtBody(OpaStmtBody):
    """
    BlockStmt represents a nested block. Nested blocks and break statements can be used to short-circuit execution.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:BlockStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    blocks: Optional[list[OpaBlock]] = Field(default=None, description="""The blocks the statement runs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaPlan', 'OpaFunc', 'OpaBlockStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaBreakStmt(OpaStmt):
    """
    A statement of kind BreakStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["BreakStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'BreakStmt'} })
    stmt: OpaBreakStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaBreakStmtBody(OpaStmtBody):
    """
    BreakStmt represents a jump out of the current block. The index specifies how many blocks to jump starting from zero (the current block).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:BreakStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    index: int = Field(default=..., description="""How many enclosing blocks to leave, counting the current block as zero.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBreakStmtBody', 'OpaMakeNumberRefStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaCallDynamicStmt(OpaStmt):
    """
    A statement of kind CallDynamicStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["CallDynamicStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'CallDynamicStmt'} })
    stmt: OpaCallDynamicStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaCallDynamicStmtBody(OpaStmtBody):
    """
    CallDynamicStmt represents an indirect (data) function call. The result should be stored in the result local.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:CallDynamicStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    args: Optional[list[int]] = Field(default=None, description="""The locals passed as arguments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaFunctionType',
                       'OpaBuiltinMetadata',
                       'OpaCallDynamicStmtBody',
                       'OpaCallStmtBody']} })
    path: Optional[list[OpaOperand]] = Field(default=None, description="""The path of the function in the data tree, one operand per segment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput',
                       'OpaFileRegoVersion',
                       'OpaFunc',
                       'OpaUnplannedRule',
                       'OpaCallDynamicStmtBody',
                       'OpaWithStmtBody']} })
    result: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaFunctionType',
                       'OpaBuiltinMetadata',
                       'OpaCallDynamicStmtBody',
                       'OpaCallStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaCallStmt(OpaStmt):
    """
    A statement of kind CallStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["CallStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'CallStmt'} })
    stmt: OpaCallStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaCallStmtBody(OpaStmtBody):
    """
    CallStmt represents a named function call. The result should be stored in the result local.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:CallStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    args: Optional[list[OpaOperand]] = Field(default=None, description="""The arguments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaFunctionType',
                       'OpaBuiltinMetadata',
                       'OpaCallDynamicStmtBody',
                       'OpaCallStmtBody']} })
    func: str = Field(default=..., description="""The name of the function called.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaCallStmtBody']} })
    result: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaFunctionType',
                       'OpaBuiltinMetadata',
                       'OpaCallDynamicStmtBody',
                       'OpaCallStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaDotStmt(OpaStmt):
    """
    A statement of kind DotStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["DotStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'DotStmt'} })
    stmt: OpaDotStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaDotStmtBody(OpaStmtBody):
    """
    DotStmt represents a lookup operation on a value (e.g., array, object, etc.) The source of a DotStmt may be a scalar value in which case the statement will be undefined.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:DotStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    key: OpaOperand = Field(default=..., description="""The key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaDotStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaScanStmtBody']} })
    source: OpaOperand = Field(default=..., description="""What the statement reads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaIsArrayStmtBody',
                       'OpaIsDefinedStmtBody',
                       'OpaIsObjectStmtBody',
                       'OpaIsSetStmtBody',
                       'OpaIsUndefinedStmtBody',
                       'OpaLenStmtBody',
                       'OpaReturnLocalStmtBody',
                       'OpaScanStmtBody']} })
    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaEqualStmt(OpaStmt):
    """
    A statement of kind EqualStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["EqualStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'EqualStmt'} })
    stmt: OpaEqualStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaEqualStmtBody(OpaStmtBody):
    """
    EqualStmt represents an value-equality check of two local variables.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:EqualStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    a: OpaOperand = Field(default=..., description="""The first value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaEqualStmtBody',
                       'OpaNotEqualStmtBody',
                       'OpaObjectMergeStmtBody']} })
    b: OpaOperand = Field(default=..., description="""The second value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaEqualStmtBody',
                       'OpaNotEqualStmtBody',
                       'OpaObjectMergeStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaIsArrayStmt(OpaStmt):
    """
    A statement of kind IsArrayStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["IsArrayStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'IsArrayStmt'} })
    stmt: OpaIsArrayStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaIsArrayStmtBody(OpaStmtBody):
    """
    IsArrayStmt represents a dynamic type check on a local variable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:IsArrayStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    source: OpaOperand = Field(default=..., description="""What the statement reads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaIsArrayStmtBody',
                       'OpaIsDefinedStmtBody',
                       'OpaIsObjectStmtBody',
                       'OpaIsSetStmtBody',
                       'OpaIsUndefinedStmtBody',
                       'OpaLenStmtBody',
                       'OpaReturnLocalStmtBody',
                       'OpaScanStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaIsDefinedStmt(OpaStmt):
    """
    A statement of kind IsDefinedStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["IsDefinedStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'IsDefinedStmt'} })
    stmt: OpaIsDefinedStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaIsDefinedStmtBody(OpaStmtBody):
    """
    IsDefinedStmt represents a check of whether a local variable is defined.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:IsDefinedStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    source: int = Field(default=..., description="""The local checked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaIsArrayStmtBody',
                       'OpaIsDefinedStmtBody',
                       'OpaIsObjectStmtBody',
                       'OpaIsSetStmtBody',
                       'OpaIsUndefinedStmtBody',
                       'OpaLenStmtBody',
                       'OpaReturnLocalStmtBody',
                       'OpaScanStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaIsObjectStmt(OpaStmt):
    """
    A statement of kind IsObjectStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["IsObjectStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'IsObjectStmt'} })
    stmt: OpaIsObjectStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaIsObjectStmtBody(OpaStmtBody):
    """
    IsObjectStmt represents a dynamic type check on a local variable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:IsObjectStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    source: OpaOperand = Field(default=..., description="""What the statement reads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaIsArrayStmtBody',
                       'OpaIsDefinedStmtBody',
                       'OpaIsObjectStmtBody',
                       'OpaIsSetStmtBody',
                       'OpaIsUndefinedStmtBody',
                       'OpaLenStmtBody',
                       'OpaReturnLocalStmtBody',
                       'OpaScanStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaIsSetStmt(OpaStmt):
    """
    A statement of kind IsSetStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["IsSetStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'IsSetStmt'} })
    stmt: OpaIsSetStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaIsSetStmtBody(OpaStmtBody):
    """
    IsSetStmt represents a dynamic type check on a local variable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:IsSetStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    source: OpaOperand = Field(default=..., description="""What the statement reads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaIsArrayStmtBody',
                       'OpaIsDefinedStmtBody',
                       'OpaIsObjectStmtBody',
                       'OpaIsSetStmtBody',
                       'OpaIsUndefinedStmtBody',
                       'OpaLenStmtBody',
                       'OpaReturnLocalStmtBody',
                       'OpaScanStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaIsUndefinedStmt(OpaStmt):
    """
    A statement of kind IsUndefinedStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["IsUndefinedStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'IsUndefinedStmt'} })
    stmt: OpaIsUndefinedStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaIsUndefinedStmtBody(OpaStmtBody):
    """
    IsUndefinedStmt represents a check of whether local variable is undefined.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:IsUndefinedStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    source: int = Field(default=..., description="""The local checked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaIsArrayStmtBody',
                       'OpaIsDefinedStmtBody',
                       'OpaIsObjectStmtBody',
                       'OpaIsSetStmtBody',
                       'OpaIsUndefinedStmtBody',
                       'OpaLenStmtBody',
                       'OpaReturnLocalStmtBody',
                       'OpaScanStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaLenStmt(OpaStmt):
    """
    A statement of kind LenStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["LenStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'LenStmt'} })
    stmt: OpaLenStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaLenStmtBody(OpaStmtBody):
    """
    LenStmt represents a length() operation on a local variable. The result is stored in the target local variable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:LenStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    source: OpaOperand = Field(default=..., description="""What the statement reads.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaIsArrayStmtBody',
                       'OpaIsDefinedStmtBody',
                       'OpaIsObjectStmtBody',
                       'OpaIsSetStmtBody',
                       'OpaIsUndefinedStmtBody',
                       'OpaLenStmtBody',
                       'OpaReturnLocalStmtBody',
                       'OpaScanStmtBody']} })
    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaMakeArrayStmt(OpaStmt):
    """
    A statement of kind MakeArrayStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["MakeArrayStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'MakeArrayStmt'} })
    stmt: OpaMakeArrayStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaMakeArrayStmtBody(OpaStmtBody):
    """
    MakeArrayStmt constructs a local variable that refers to an array value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:MakeArrayStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    capacity: int = Field(default=..., description="""The capacity to allocate.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaMakeArrayStmtBody']} })
    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaMakeNullStmt(OpaStmt):
    """
    A statement of kind MakeNullStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["MakeNullStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'MakeNullStmt'} })
    stmt: OpaMakeNullStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaMakeNullStmtBody(OpaStmtBody):
    """
    MakeNullStmt constructs a local variable that refers to a null value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:MakeNullStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaMakeNumberIntStmt(OpaStmt):
    """
    A statement of kind MakeNumberIntStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["MakeNumberIntStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'MakeNumberIntStmt'} })
    stmt: OpaMakeNumberIntStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaMakeNumberIntStmtBody(OpaStmtBody):
    """
    MakeNumberIntStmt constructs a local variable that refers to an integer value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:MakeNumberIntStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    value: int = Field(default=..., description="""The value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaMakeNumberRefStmt(OpaStmt):
    """
    A statement of kind MakeNumberRefStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["MakeNumberRefStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'MakeNumberRefStmt'} })
    stmt: OpaMakeNumberRefStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaMakeNumberRefStmtBody(OpaStmtBody):
    """
    MakeNumberRefStmt constructs a local variable that refers to a number stored as a string.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:MakeNumberRefStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    index: int = Field(default=..., description="""Index, in the plan's static strings, of the number written as a string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaBreakStmtBody', 'OpaMakeNumberRefStmtBody']} })
    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    Index: Optional[int] = Field(default=None, description="""Deprecated alias for `index`. Both keys are emitted by current OPA versions for backwards compatibility; will be removed in a future major release. Read `index` instead.""", json_schema_extra = { "linkml_meta": {'deprecated': 'Deprecated alias for `index`. Both keys are emitted by current '
                       'OPA versions for backwards compatibility; will be removed in a '
                       'future major release. Read `index` instead.',
         'domain_of': ['OpaMakeNumberRefStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaMakeObjectStmt(OpaStmt):
    """
    A statement of kind MakeObjectStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["MakeObjectStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'MakeObjectStmt'} })
    stmt: OpaMakeObjectStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaMakeObjectStmtBody(OpaStmtBody):
    """
    MakeObjectStmt constructs a local variable that refers to an object value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:MakeObjectStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaMakeSetStmt(OpaStmt):
    """
    A statement of kind MakeSetStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["MakeSetStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'MakeSetStmt'} })
    stmt: OpaMakeSetStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaMakeSetStmtBody(OpaStmtBody):
    """
    MakeSetStmt constructs a local variable that refers to a set value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:MakeSetStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaNopStmt(OpaStmt):
    """
    A statement of kind NopStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["NopStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'NopStmt'} })
    stmt: OpaNopStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaNopStmtBody(OpaStmtBody):
    """
    NopStmt adds a nop instruction. Useful during development and debugging only.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:NopStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaNotEqualStmt(OpaStmt):
    """
    A statement of kind NotEqualStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["NotEqualStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'NotEqualStmt'} })
    stmt: OpaNotEqualStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaNotEqualStmtBody(OpaStmtBody):
    """
    NotEqualStmt represents a != check of two local variables.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:NotEqualStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    a: OpaOperand = Field(default=..., description="""The first value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaEqualStmtBody',
                       'OpaNotEqualStmtBody',
                       'OpaObjectMergeStmtBody']} })
    b: OpaOperand = Field(default=..., description="""The second value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaEqualStmtBody',
                       'OpaNotEqualStmtBody',
                       'OpaObjectMergeStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaNotStmt(OpaStmt):
    """
    A statement of kind NotStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["NotStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'NotStmt'} })
    stmt: OpaNotStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaNotStmtBody(OpaStmtBody):
    """
    NotStmt represents a negated statement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:NotStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    block: Optional[OpaBlock] = Field(default=None, description="""The block the statement runs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaNotStmtBody', 'OpaScanStmtBody', 'OpaWithStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaObjectInsertOnceStmt(OpaStmt):
    """
    A statement of kind ObjectInsertOnceStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["ObjectInsertOnceStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'ObjectInsertOnceStmt'} })
    stmt: OpaObjectInsertOnceStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaObjectInsertOnceStmtBody(OpaStmtBody):
    """
    ObjectInsertOnceStmt represents a dynamic insert operation of a key/value pair into an object. If the key already exists and the value differs, execution aborts with a conflict error.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:ObjectInsertOnceStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    key: OpaOperand = Field(default=..., description="""The key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaDotStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaScanStmtBody']} })
    object: int = Field(default=..., description="""The local that holds the object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaObjectInsertOnceStmtBody', 'OpaObjectInsertStmtBody']} })
    value: OpaOperand = Field(default=..., description="""The value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaObjectInsertStmt(OpaStmt):
    """
    A statement of kind ObjectInsertStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["ObjectInsertStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'ObjectInsertStmt'} })
    stmt: OpaObjectInsertStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaObjectInsertStmtBody(OpaStmtBody):
    """
    ObjectInsertStmt represents a dynamic insert operation of a key/value pair into an object.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:ObjectInsertStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    key: OpaOperand = Field(default=..., description="""The key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaDotStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaScanStmtBody']} })
    object: int = Field(default=..., description="""The local that holds the object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaObjectInsertOnceStmtBody', 'OpaObjectInsertStmtBody']} })
    value: OpaOperand = Field(default=..., description="""The value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaObjectMergeStmt(OpaStmt):
    """
    A statement of kind ObjectMergeStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["ObjectMergeStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'ObjectMergeStmt'} })
    stmt: OpaObjectMergeStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaObjectMergeStmtBody(OpaStmtBody):
    """
    ObjectMergeStmt performs a recursive merge of two object values. If either of the locals refer to non-object values this operation will abort with a conflict error.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:ObjectMergeStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    a: int = Field(default=..., description="""The local that holds the first object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaEqualStmtBody',
                       'OpaNotEqualStmtBody',
                       'OpaObjectMergeStmtBody']} })
    b: int = Field(default=..., description="""The local that holds the second object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaEqualStmtBody',
                       'OpaNotEqualStmtBody',
                       'OpaObjectMergeStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaResetLocalStmt(OpaStmt):
    """
    A statement of kind ResetLocalStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["ResetLocalStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'ResetLocalStmt'} })
    stmt: OpaResetLocalStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaResetLocalStmtBody(OpaStmtBody):
    """
    ResetLocalStmt resets a local variable to 0.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:ResetLocalStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    target: int = Field(default=..., description="""The local that receives the result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignIntStmtBody',
                       'OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaLenStmtBody',
                       'OpaMakeArrayStmtBody',
                       'OpaMakeNullStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaMakeNumberRefStmtBody',
                       'OpaMakeObjectStmtBody',
                       'OpaMakeSetStmtBody',
                       'OpaObjectMergeStmtBody',
                       'OpaResetLocalStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaResultSetAddStmt(OpaStmt):
    """
    A statement of kind ResultSetAddStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["ResultSetAddStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'ResultSetAddStmt'} })
    stmt: OpaResultSetAddStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaResultSetAddStmtBody(OpaStmtBody):
    """
    ResultSetAddStmt adds a value into the result set returned by the query plan.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:ResultSetAddStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    value: int = Field(default=..., description="""The local added to the result set.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaReturnLocalStmt(OpaStmt):
    """
    A statement of kind ReturnLocalStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["ReturnLocalStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'ReturnLocalStmt'} })
    stmt: OpaReturnLocalStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaReturnLocalStmtBody(OpaStmtBody):
    """
    ReturnLocalStmt represents a return statement that yields a local value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:ReturnLocalStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    source: int = Field(default=..., description="""The local returned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaIsArrayStmtBody',
                       'OpaIsDefinedStmtBody',
                       'OpaIsObjectStmtBody',
                       'OpaIsSetStmtBody',
                       'OpaIsUndefinedStmtBody',
                       'OpaLenStmtBody',
                       'OpaReturnLocalStmtBody',
                       'OpaScanStmtBody']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaScanStmt(OpaStmt):
    """
    A statement of kind ScanStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["ScanStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'ScanStmt'} })
    stmt: OpaScanStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaScanStmtBody(OpaStmtBody):
    """
    ScanStmt represents a linear scan over a composite value. The source may be a scalar in which case the block will never execute.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:ScanStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    block: Optional[OpaBlock] = Field(default=None, description="""The block run for each key and value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaNotStmtBody', 'OpaScanStmtBody', 'OpaWithStmtBody']} })
    key: int = Field(default=..., description="""The local that receives each key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaDotStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaScanStmtBody']} })
    source: int = Field(default=..., description="""The local whose value is scanned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAssignVarOnceStmtBody',
                       'OpaAssignVarStmtBody',
                       'OpaDotStmtBody',
                       'OpaIsArrayStmtBody',
                       'OpaIsDefinedStmtBody',
                       'OpaIsObjectStmtBody',
                       'OpaIsSetStmtBody',
                       'OpaIsUndefinedStmtBody',
                       'OpaLenStmtBody',
                       'OpaReturnLocalStmtBody',
                       'OpaScanStmtBody']} })
    value: int = Field(default=..., description="""The local that receives each value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaSetAddStmt(OpaStmt):
    """
    A statement of kind SetAddStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["SetAddStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'SetAddStmt'} })
    stmt: OpaSetAddStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaSetAddStmtBody(OpaStmtBody):
    """
    SetAddStmt represents a dynamic add operation of an element into a set.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:SetAddStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    set: int = Field(default=..., description="""The local that holds the set.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaSetAddStmtBody']} })
    value: OpaOperand = Field(default=..., description="""The value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaWithStmt(OpaStmt):
    """
    A statement of kind WithStmt, with its fields in `stmt`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["WithStmt"] = Field(default=..., description="""The kind of statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'WithStmt'} })
    stmt: OpaWithStmtBody = Field(default=..., description="""The statement's fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt']} })


class OpaWithStmtBody(OpaStmtBody):
    """
    WithStmt replaces the Local or a portion of the document referred to by the Local with the Value and executes the contained block. If the Path is non-empty, the Value is upserted into the Local.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['opa_plan:WithStmt'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    block: Optional[OpaBlock] = Field(default=None, description="""The block the statement runs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaNotStmtBody', 'OpaScanStmtBody', 'OpaWithStmtBody']} })
    local: int = Field(default=..., description="""The local whose value, or part of it, is replaced.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaWithStmtBody']} })
    path: Optional[list[int]] = Field(default=None, description="""The path within the local's value to replace, as indices of static strings. Empty replaces the whole value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAuthorizationInput',
                       'OpaFileRegoVersion',
                       'OpaFunc',
                       'OpaUnplannedRule',
                       'OpaCallDynamicStmtBody',
                       'OpaWithStmtBody']} })
    value: OpaOperand = Field(default=..., description="""The replacement value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })
    file: int = Field(default=..., description="""Index, in the plan's static files, of the policy file the statement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    col: int = Field(default=..., description="""Column where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    row: int = Field(default=..., description="""Line where the statement's source text starts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_col: int = Field(default=..., description="""Column where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })
    end_row: int = Field(default=..., description="""Line where the statement's source text ends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaLocation', 'OpaStmtBody']} })


class OpaOperand(ConfiguredBaseModel):
    """
    Operand represents a value that a statement operates on. OPA writes it as its kind in `type` and the value in `value`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'exact_mappings': ['opa_plan:Operand', 'opa_plan:Val'],
         'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    pass


class OpaBoolOperand(OpaOperand):
    """
    Bool represents a constant boolean.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["bool"] = Field(default=..., description="""The kind of operand.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'bool'} })
    value: bool = Field(default=..., description="""The operand's value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })


class OpaLocalOperand(OpaOperand):
    """
    A local variable, by its number.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["local"] = Field(default=..., description="""The kind of operand.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'local'} })
    value: int = Field(default=..., description="""The operand's value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })


class OpaStringIndexOperand(OpaOperand):
    """
    StringIndex represents the index into the plan's list of constant strings of a constant string.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/opa/ir_plan'})

    type: Literal["string_index"] = Field(default=..., description="""The kind of operand.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaAnyType',
                       'OpaArrayType',
                       'OpaBooleanType',
                       'OpaFunctionType',
                       'OpaNullType',
                       'OpaNumberType',
                       'OpaObjectType',
                       'OpaSetType',
                       'OpaStringType',
                       'OpaBuiltinArgument',
                       'OpaBuiltinResult',
                       'OpaArrayAppendStmt',
                       'OpaAssignIntStmt',
                       'OpaAssignVarOnceStmt',
                       'OpaAssignVarStmt',
                       'OpaBlockStmt',
                       'OpaBreakStmt',
                       'OpaCallDynamicStmt',
                       'OpaCallStmt',
                       'OpaDotStmt',
                       'OpaEqualStmt',
                       'OpaIsArrayStmt',
                       'OpaIsDefinedStmt',
                       'OpaIsObjectStmt',
                       'OpaIsSetStmt',
                       'OpaIsUndefinedStmt',
                       'OpaLenStmt',
                       'OpaMakeArrayStmt',
                       'OpaMakeNullStmt',
                       'OpaMakeNumberIntStmt',
                       'OpaMakeNumberRefStmt',
                       'OpaMakeObjectStmt',
                       'OpaMakeSetStmt',
                       'OpaNopStmt',
                       'OpaNotEqualStmt',
                       'OpaNotStmt',
                       'OpaObjectInsertOnceStmt',
                       'OpaObjectInsertStmt',
                       'OpaObjectMergeStmt',
                       'OpaResetLocalStmt',
                       'OpaResultSetAddStmt',
                       'OpaReturnLocalStmt',
                       'OpaScanStmt',
                       'OpaSetAddStmt',
                       'OpaWithStmt',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand'],
         'equals_string': 'string_index'} })
    value: int = Field(default=..., description="""The operand's value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OpaStaticProperty',
                       'OpaDynamicProperty',
                       'OpaStringConst',
                       'OpaArrayAppendStmtBody',
                       'OpaAssignIntStmtBody',
                       'OpaMakeNumberIntStmtBody',
                       'OpaObjectInsertOnceStmtBody',
                       'OpaObjectInsertStmtBody',
                       'OpaResultSetAddStmtBody',
                       'OpaScanStmtBody',
                       'OpaSetAddStmtBody',
                       'OpaWithStmtBody',
                       'OpaBoolOperand',
                       'OpaLocalOperand',
                       'OpaStringIndexOperand']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
OpaObject.model_rebuild()
OpaType.model_rebuild()
OpaAnyType.model_rebuild()
OpaArrayType.model_rebuild()
OpaBooleanType.model_rebuild()
OpaFunctionType.model_rebuild()
OpaNullType.model_rebuild()
OpaNumberType.model_rebuild()
OpaObjectType.model_rebuild()
OpaSetType.model_rebuild()
OpaStringType.model_rebuild()
OpaStaticProperty.model_rebuild()
OpaDynamicProperty.model_rebuild()
OpaCapabilities.model_rebuild()
OpaBuiltin.model_rebuild()
OpaWasmAbiVersion.model_rebuild()
OpaBuiltinMetadataCatalog.model_rebuild()
OpaBuiltinCategory.model_rebuild()
OpaImplementation.model_rebuild()
OpaBuiltinMetadata.model_rebuild()
OpaBuiltinArgument.model_rebuild()
OpaBuiltinResult.model_rebuild()
OpaImplementationSupport.model_rebuild()
OpaVersionIndex.model_rebuild()
OpaVersionEntry.model_rebuild()
OpaAuthorizationInput.model_rebuild()
OpaManifest.model_rebuild()
OpaWasmResolver.model_rebuild()
OpaFileRegoVersion.model_rebuild()
OpaPolicy.model_rebuild()
OpaStatic.model_rebuild()
OpaStringConst.model_rebuild()
OpaBuiltinFunc.model_rebuild()
OpaPlans.model_rebuild()
OpaPlan.model_rebuild()
OpaFuncs.model_rebuild()
OpaFunc.model_rebuild()
OpaBlock.model_rebuild()
OpaUnplannedRule.model_rebuild()
OpaLocation.model_rebuild()
OpaStmt.model_rebuild()
OpaStmtBody.model_rebuild()
OpaArrayAppendStmt.model_rebuild()
OpaArrayAppendStmtBody.model_rebuild()
OpaAssignIntStmt.model_rebuild()
OpaAssignIntStmtBody.model_rebuild()
OpaAssignVarOnceStmt.model_rebuild()
OpaAssignVarOnceStmtBody.model_rebuild()
OpaAssignVarStmt.model_rebuild()
OpaAssignVarStmtBody.model_rebuild()
OpaBlockStmt.model_rebuild()
OpaBlockStmtBody.model_rebuild()
OpaBreakStmt.model_rebuild()
OpaBreakStmtBody.model_rebuild()
OpaCallDynamicStmt.model_rebuild()
OpaCallDynamicStmtBody.model_rebuild()
OpaCallStmt.model_rebuild()
OpaCallStmtBody.model_rebuild()
OpaDotStmt.model_rebuild()
OpaDotStmtBody.model_rebuild()
OpaEqualStmt.model_rebuild()
OpaEqualStmtBody.model_rebuild()
OpaIsArrayStmt.model_rebuild()
OpaIsArrayStmtBody.model_rebuild()
OpaIsDefinedStmt.model_rebuild()
OpaIsDefinedStmtBody.model_rebuild()
OpaIsObjectStmt.model_rebuild()
OpaIsObjectStmtBody.model_rebuild()
OpaIsSetStmt.model_rebuild()
OpaIsSetStmtBody.model_rebuild()
OpaIsUndefinedStmt.model_rebuild()
OpaIsUndefinedStmtBody.model_rebuild()
OpaLenStmt.model_rebuild()
OpaLenStmtBody.model_rebuild()
OpaMakeArrayStmt.model_rebuild()
OpaMakeArrayStmtBody.model_rebuild()
OpaMakeNullStmt.model_rebuild()
OpaMakeNullStmtBody.model_rebuild()
OpaMakeNumberIntStmt.model_rebuild()
OpaMakeNumberIntStmtBody.model_rebuild()
OpaMakeNumberRefStmt.model_rebuild()
OpaMakeNumberRefStmtBody.model_rebuild()
OpaMakeObjectStmt.model_rebuild()
OpaMakeObjectStmtBody.model_rebuild()
OpaMakeSetStmt.model_rebuild()
OpaMakeSetStmtBody.model_rebuild()
OpaNopStmt.model_rebuild()
OpaNopStmtBody.model_rebuild()
OpaNotEqualStmt.model_rebuild()
OpaNotEqualStmtBody.model_rebuild()
OpaNotStmt.model_rebuild()
OpaNotStmtBody.model_rebuild()
OpaObjectInsertOnceStmt.model_rebuild()
OpaObjectInsertOnceStmtBody.model_rebuild()
OpaObjectInsertStmt.model_rebuild()
OpaObjectInsertStmtBody.model_rebuild()
OpaObjectMergeStmt.model_rebuild()
OpaObjectMergeStmtBody.model_rebuild()
OpaResetLocalStmt.model_rebuild()
OpaResetLocalStmtBody.model_rebuild()
OpaResultSetAddStmt.model_rebuild()
OpaResultSetAddStmtBody.model_rebuild()
OpaReturnLocalStmt.model_rebuild()
OpaReturnLocalStmtBody.model_rebuild()
OpaScanStmt.model_rebuild()
OpaScanStmtBody.model_rebuild()
OpaSetAddStmt.model_rebuild()
OpaSetAddStmtBody.model_rebuild()
OpaWithStmt.model_rebuild()
OpaWithStmtBody.model_rebuild()
OpaOperand.model_rebuild()
OpaBoolOperand.model_rebuild()
OpaLocalOperand.model_rebuild()
OpaStringIndexOperand.model_rebuild()
