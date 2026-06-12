export type BuiltinName = string;
export type BuiltinCategoryGroupName = string;
export type BuiltinMetadataName = string;
export type ElementVersionName = string;
export type FileRegoVersionPath = string;
/**
* Kinds of value that a TypeDecl can describe.
*/
export enum BuiltinTypeKind {
    
    string = "string",
    number = "number",
    boolean = "boolean",
    null = "null",
    any = "any",
    array = "array",
    set = "set",
    object = "object",
    function = "function",
};
/**
* Optional features advertised by the OPA build. The permissible values below are seeded from the upstream capabilities.json snapshot at generation time; future releases may introduce new flags.
*/
export enum FeatureName {
    
    keywords_in_refs = "keywords_in_refs",
    rego_v1 = "rego_v1",
    template_strings = "template_strings",
};
/**
* Identifiers reserved for upcoming Rego releases.
*/
export enum FutureKeyword {
    
    not = "not",
};
/**
* Documentation category a built-in belongs to. Permissible values are seeded from ``builtin_metadata.json._categories`` at generation time. Enum symbols follow LinkML's snake_case convention; each permissible value carries the upstream label (e.g. ``providers.aws``) in both its description and its ``meaning`` mapping.
*/
export enum BuiltinCategory {
    
    aggregates = "aggregates",
    array = "array",
    bits = "bits",
    comparison = "comparison",
    conversions = "conversions",
    crypto = "crypto",
    encoding = "encoding",
    glob = "glob",
    graph = "graph",
    graphql = "graphql",
    http = "http",
    internal = "internal",
    net = "net",
    numbers = "numbers",
    object = "object",
    opa = "opa",
    /** providers.aws */
    providers_aws = "providers_aws",
    regex = "regex",
    rego = "rego",
    semver = "semver",
    sets = "sets",
    strings = "strings",
    time = "time",
    tokens = "tokens",
    tokensign = "tokensign",
    tracing = "tracing",
    types = "types",
    units = "units",
    uri = "uri",
    uuid = "uuid",
};
/**
* Permissible discriminator tags for the ``Stmt`` union.
*/
export enum StmtTag {
    
    ArrayAppendStmt = "ArrayAppendStmt",
    AssignIntStmt = "AssignIntStmt",
    AssignVarOnceStmt = "AssignVarOnceStmt",
    AssignVarStmt = "AssignVarStmt",
    BlockStmt = "BlockStmt",
    BreakStmt = "BreakStmt",
    CallDynamicStmt = "CallDynamicStmt",
    CallStmt = "CallStmt",
    DotStmt = "DotStmt",
    EqualStmt = "EqualStmt",
    IsArrayStmt = "IsArrayStmt",
    IsDefinedStmt = "IsDefinedStmt",
    IsObjectStmt = "IsObjectStmt",
    IsSetStmt = "IsSetStmt",
    IsUndefinedStmt = "IsUndefinedStmt",
    LenStmt = "LenStmt",
    MakeArrayStmt = "MakeArrayStmt",
    MakeNullStmt = "MakeNullStmt",
    MakeNumberIntStmt = "MakeNumberIntStmt",
    MakeNumberRefStmt = "MakeNumberRefStmt",
    MakeObjectStmt = "MakeObjectStmt",
    MakeSetStmt = "MakeSetStmt",
    NopStmt = "NopStmt",
    NotEqualStmt = "NotEqualStmt",
    NotStmt = "NotStmt",
    ObjectInsertOnceStmt = "ObjectInsertOnceStmt",
    ObjectInsertStmt = "ObjectInsertStmt",
    ObjectMergeStmt = "ObjectMergeStmt",
    ResetLocalStmt = "ResetLocalStmt",
    ResultSetAddStmt = "ResultSetAddStmt",
    ReturnLocalStmt = "ReturnLocalStmt",
    ScanStmt = "ScanStmt",
    SetAddStmt = "SetAddStmt",
    WithStmt = "WithStmt",
};
/**
* Permissible discriminator tags for the ``Val`` union.
*/
export enum ValTag {
    
    bool = "bool",
    local = "local",
    string_index = "string_index",
};


/**
 * Free-form value placeholder (scalar, list, or object). Used to model source slots whose representation is heterogeneous or intentionally open (e.g. ``TypeDecl.key``, ``AuthorizationInput.body``).
 */
export interface Any {
}


/**
 * Top-level capabilities document published by an OPA build. Lists every built-in function the runtime supports along with Wasm ABI compatibility, future keywords and feature flags.
 */
export interface Capabilities {
    /** All built-in functions supported by this OPA build. */
    builtins?: Builtin[],
    /** Keywords reserved for future Rego releases. */
    future_keywords?: string,
    /** Wasm ABI versions the runtime can host. */
    wasm_abi_versions?: WasmABIVersion[],
    /** Optional language / runtime features enabled in this build. */
    features?: string,
    /** Network destinations the built-ins are allowed to contact. Absent or empty means unrestricted; an empty list means no network access. */
    allow_net?: string[],
}


/**
 * A Rego built-in function exposed by the OPA runtime.
 */
export interface Builtin {
    /** Built-in identifier (dotted path, e.g. ``array.concat``). */
    name: string,
    /** Type declaration: signature plus return type. */
    decl: BuiltinDecl,
    /** Optional infix operator symbol (e.g. ``&``, ``==``). */
    infix?: string,
    /** True when the built-in is scheduled for removal. */
    deprecated?: boolean,
    /** True when invocations may produce different results across runs. */
    nondeterministic?: boolean,
    /** True when the built-in is a relation (binds output variables). */
    relation?: boolean,
}


/**
 * Type declaration of a built-in: function signature and return type.
 */
export interface BuiltinDecl {
    /** Always the literal string ``function``. */
    type: string,
    /** Positional argument types in declaration order. */
    args?: TypeDecl[],
    /** Type of the result returned by the built-in. */
    result?: TypeDecl,
    /** When present, indicates the built-in accepts any number of trailing arguments of this type. */
    variadic?: TypeDecl,
}


/**
 * Recursive type expression used throughout Capabilities declarations.

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

 */
export interface TypeDecl {
    /** Discriminator: the kind of value this TypeDecl describes. */
    type?: string,
    /** Element type(s). For ``set`` it is the (single) element type; for ``any`` it is a union of alternative types. Always represented as a list -- the instance generator wraps source scalar values for shape uniformity. */
    of?: TypeDecl[],
    /** For ``array`` types this is the element TypeDecl; for ``object`` types it is a TypeDecl with ``key`` and ``value`` populated. */
    dynamic?: TypeDecl,
    /** Either named property pairs of an ``object`` TypeDecl (each entry has ``key`` and ``value`` populated) or positional tuple element TypeDecls of a fixed-length ``array`` TypeDecl. Same recursive TypeDecl shape. */
    static?: TypeDecl[],
    /** Key of an object's dynamic-property mapping or static-property entry. When the parent TypeDecl is an object's ``dynamic`` slot, this is itself a TypeDecl (e.g. ``{type: string}``); when the parent is an object's ``static`` entry, it is a string literal naming the property. */
    key?: Any,
    /** Value type of an object's dynamic property mapping or static property entry. Always a TypeDecl. */
    value?: TypeDecl,
}


/**
 * A supported Wasm ABI version pair.
 */
export interface WasmABIVersion {
    /** Major ABI version. */
    version: number,
    /** Minor ABI version. */
    minor_version: number,
}


/**
 * Wrapper class for the contents of ``builtin_metadata.json``. The source document is a flat map keyed by built-in name plus a ``_categories`` map; the generator script reshapes it so ``categories`` and ``builtins`` are explicit, inlined-as-dict slots on this wrapper.
 */
export interface BuiltinMetadataCatalog {
    /** Category name -> list of built-in names belonging to it. */
    categories?: {[index: BuiltinCategoryGroupName]: BuiltinCategoryGroup },
    /** All documented built-ins keyed by name. */
    builtins?: {[index: BuiltinMetadataName]: BuiltinMetadata },
}


/**
 * Membership of built-ins in a documentation category.
 */
export interface BuiltinCategoryGroup {
    /** Category identifier. Plain string (not the BuiltinCategory enum) so gen-python's identifier-slot machinery does not forward-reference the enum class. */
    name: string,
    /** Same value as ``name``, typed against the BuiltinCategory enum for downstream consumers. */
    category?: string,
    /** Names of the built-ins belonging to this category. */
    builtins: string[],
}


/**
 * Human-readable metadata for a single Rego built-in function.
 */
export interface BuiltinMetadata {
    /** Built-in identifier (dotted path). */
    name: string,
    /** Markdown description of the built-in. */
    description?: string,
    /** Earliest OPA release tag in which the built-in was available. */
    introduced?: string,
    /** Every OPA release tag in which the built-in is available. */
    available?: string[],
    /** True if the built-in is implemented for the Wasm target. */
    wasm?: boolean,
    /** Optional infix operator symbol. */
    infix?: string,
    /** True when the built-in is scheduled for removal. */
    deprecated?: boolean,
    /** True when the built-in is a relation. */
    relation?: boolean,
    /** Positional argument descriptors in declaration order. */
    args?: BuiltinArg[],
    /** Descriptor for the value returned by the built-in. */
    result?: BuiltinResult,
}


/**
 * Documentation for one positional argument of a built-in.
 */
export interface BuiltinArg {
    /** Argument identifier as documented (often single-letter). */
    name?: string,
    /** Markdown description of the argument. */
    description?: string,
    /** Compact textual form of the argument type (e.g. ``number``, ``set[any]``, ``any<string, number>``). */
    type?: string,
}


/**
 * Documentation for the value returned by a built-in.
 */
export interface BuiltinResult {
    /** Result identifier as documented. */
    name?: string,
    /** Markdown description of the result. */
    description?: string,
    /** Compact textual form of the result type. */
    type?: string,
}


/**
 * Mapping from language-element names to the OPA semantic version that first introduced them. Grouped into built-ins, future-keywords, and features.
 */
export interface VersionIndex {
    /** Built-in name -> introduction version. */
    builtins?: {[index: ElementVersionName]: ElementVersion },
    /** Feature flag -> introduction version. */
    features?: {[index: ElementVersionName]: ElementVersion },
    /** Future keyword -> introduction version. */
    keywords?: {[index: ElementVersionName]: ElementVersion },
}


/**
 * Semantic version triple identifying when an element was introduced.
 */
export interface ElementVersion {
    /** Name of the language element (built-in, keyword, or feature). */
    name: string,
    /** Major version number (source field ``Major``). */
    major: number,
    /** Minor version number (source field ``Minor``). */
    minor: number,
    /** Patch version number (source field ``Patch``). */
    patch: number,
}


/**
 * Input document the example HTTP API Authorization policy receives. Mirrors the OPA-provided JSON Schema at ``v1/schemas/authorizationPolicy.json``.
 */
export interface AuthorizationInput {
    /** Caller identity, typically extracted from an authentication token. */
    identity: string,
    /** Client certificates presented during the TLS handshake. The example schema leaves the item shape opaque (free-form objects). */
    client_certificates: Any[],
    /** HTTP method of the request being authorized (e.g. ``GET``, ``POST``). */
    method: string,
    /** Request URL path split on ``/`` and decoded into a list of path segments. */
    path: string[],
    /** Query-string parameters as a free-form object. */
    params: Any,
    /** Request headers as a free-form object (case insensitive in HTTP). */
    headers: Any,
    /** Decoded request body as a free-form object. */
    body: Any,
}


/**
 * ``Manifest`` definition from upstream JSON Schema.
 */
export interface Manifest {
    /** Per-file Rego language version overrides. Each record maps a bundle file path to ``version`` where ``0`` = Rego v0 and ``1`` = Rego v1. */
    file_rego_versions?: FileRegoVersion[],
    /** ``metadata`` field of ``Manifest`` (from upstream JSON Schema). */
    metadata?: Any,
    /** Rego language version pinned for files in this bundle. ``0`` = Rego v0 (legacy); ``1`` = Rego v1 (default since OPA 1.0). See ``v1/bundle/bundle.go`` for the canonical mapping. */
    rego_version?: number,
    /** ``revision`` field of ``Manifest`` (from upstream JSON Schema). */
    revision: string,
    /** ``roots`` field of ``Manifest`` (from upstream JSON Schema). */
    roots?: string[],
    /** ``wasm`` field of ``Manifest`` (from upstream JSON Schema). */
    wasm?: WasmResolver[],
}


/**
 * ``WasmResolver`` definition from upstream JSON Schema.
 */
export interface WasmResolver {
    /** ``annotations`` field of ``WasmResolver`` (from upstream JSON Schema). */
    annotations?: Any[],
    /** ``entrypoint`` field of ``WasmResolver`` (from upstream JSON Schema). */
    entrypoint?: string,
    /** ``module`` field of ``WasmResolver`` (from upstream JSON Schema). */
    module?: string,
}


/**
 * Typed override record for ``Manifest.file_rego_versions``. Provides stronger validation than a free-form map while keeping the same semantics.
 */
export interface FileRegoVersion {
    /** Bundle-relative file path receiving a Rego version override. */
    path: string,
    /** Rego version for this file: ``0`` (v0) or ``1`` (v1). */
    version: number,
}


/**
 * ``ArrayAppendStmt`` definition from upstream JSON Schema.
 */
export interface ArrayAppendStmt {
    /** ``col`` field of ``ArrayAppendStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``ArrayAppendStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``ArrayAppendStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``array`` field of ``ArrayAppendStmt`` (from upstream JSON Schema). */
    array: number,
    /** ``value`` field of ``ArrayAppendStmt`` (from upstream JSON Schema). */
    value: Operand,
}


/**
 * ``AssignIntStmt`` definition from upstream JSON Schema.
 */
export interface AssignIntStmt {
    /** ``col`` field of ``AssignIntStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``AssignIntStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``AssignIntStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``target`` field of ``AssignIntStmt`` (from upstream JSON Schema). */
    target: number,
    /** ``value`` field of ``AssignIntStmt`` (from upstream JSON Schema). */
    value: number,
}


/**
 * ``AssignVarOnceStmt`` definition from upstream JSON Schema.
 */
export interface AssignVarOnceStmt {
    /** ``col`` field of ``AssignVarOnceStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``AssignVarOnceStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``AssignVarOnceStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``source`` field of ``AssignVarOnceStmt`` (from upstream JSON Schema). */
    source: Operand,
    /** ``target`` field of ``AssignVarOnceStmt`` (from upstream JSON Schema). */
    target: number,
}


/**
 * ``AssignVarStmt`` definition from upstream JSON Schema.
 */
export interface AssignVarStmt {
    /** ``col`` field of ``AssignVarStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``AssignVarStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``AssignVarStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``source`` field of ``AssignVarStmt`` (from upstream JSON Schema). */
    source: Operand,
    /** ``target`` field of ``AssignVarStmt`` (from upstream JSON Schema). */
    target: number,
}


/**
 * ``Block`` definition from upstream JSON Schema.
 */
export interface Block {
    /** ``stmts`` field of ``Block`` (from upstream JSON Schema). */
    stmts: Stmt[],
}


/**
 * ``BlockStmt`` definition from upstream JSON Schema.
 */
export interface BlockStmt {
    /** ``col`` field of ``BlockStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``BlockStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``BlockStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``blocks`` field of ``BlockStmt`` (from upstream JSON Schema). */
    blocks: Block[],
}


/**
 * ``BreakStmt`` definition from upstream JSON Schema.
 */
export interface BreakStmt {
    /** ``col`` field of ``BreakStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``BreakStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``BreakStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``index`` field of ``BreakStmt`` (from upstream JSON Schema). */
    index: number,
}


/**
 * ``BuiltinFunc`` definition from upstream JSON Schema.
 */
export interface BuiltinFunc {
    /** BuiltinFunc declaration; opaque in this schema. */
    decl: Any,
    /** ``name`` field of ``BuiltinFunc`` (from upstream JSON Schema). */
    name: string,
}


/**
 * ``CallDynamicStmt`` definition from upstream JSON Schema.
 */
export interface CallDynamicStmt {
    /** ``col`` field of ``CallDynamicStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``CallDynamicStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``CallDynamicStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``args`` field of ``CallDynamicStmt`` (from upstream JSON Schema). */
    args: number[],
    /** ``path`` field of ``CallDynamicStmt`` (from upstream JSON Schema). */
    path: Operand[],
    /** ``result`` field of ``CallDynamicStmt`` (from upstream JSON Schema). */
    result: number,
}


/**
 * ``CallStmt`` definition from upstream JSON Schema.
 */
export interface CallStmt {
    /** ``col`` field of ``CallStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``CallStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``CallStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``args`` field of ``CallStmt`` (from upstream JSON Schema). */
    args: Operand[],
    /** ``func`` field of ``CallStmt`` (from upstream JSON Schema). */
    func: string,
    /** ``result`` field of ``CallStmt`` (from upstream JSON Schema). */
    result: number,
}


/**
 * ``DotStmt`` definition from upstream JSON Schema.
 */
export interface DotStmt {
    /** ``col`` field of ``DotStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``DotStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``DotStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``key`` field of ``DotStmt`` (from upstream JSON Schema). */
    key: Operand,
    /** ``source`` field of ``DotStmt`` (from upstream JSON Schema). */
    source: Operand,
    /** ``target`` field of ``DotStmt`` (from upstream JSON Schema). */
    target: number,
}


/**
 * ``EqualStmt`` definition from upstream JSON Schema.
 */
export interface EqualStmt {
    /** ``col`` field of ``EqualStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``EqualStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``EqualStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``a`` field of ``EqualStmt`` (from upstream JSON Schema). */
    a: Operand,
    /** ``b`` field of ``EqualStmt`` (from upstream JSON Schema). */
    b: Operand,
}


/**
 * ``Func`` definition from upstream JSON Schema.
 */
export interface Func {
    /** ``blocks`` field of ``Func`` (from upstream JSON Schema). */
    blocks: Block[],
    /** ``name`` field of ``Func`` (from upstream JSON Schema). */
    name: string,
    /** ``params`` field of ``Func`` (from upstream JSON Schema). */
    params: number[],
    /** ``path`` field of ``Func`` (from upstream JSON Schema). */
    path?: string[],
    /** ``return`` field of ``Func`` (from upstream JSON Schema). (Renamed from upstream wire-format key ``return`` to avoid the Python reserved word.) */
    return_value: number,
}


/**
 * ``Funcs`` definition from upstream JSON Schema.
 */
export interface Funcs {
    /** ``funcs`` field of ``Funcs`` (from upstream JSON Schema). */
    funcs: Func[],
}


/**
 * ``IsArrayStmt`` definition from upstream JSON Schema.
 */
export interface IsArrayStmt {
    /** ``col`` field of ``IsArrayStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``IsArrayStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``IsArrayStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``source`` field of ``IsArrayStmt`` (from upstream JSON Schema). */
    source: Operand,
}


/**
 * ``IsDefinedStmt`` definition from upstream JSON Schema.
 */
export interface IsDefinedStmt {
    /** ``col`` field of ``IsDefinedStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``IsDefinedStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``IsDefinedStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``source`` field of ``IsDefinedStmt`` (from upstream JSON Schema). */
    source: number,
}


/**
 * ``IsObjectStmt`` definition from upstream JSON Schema.
 */
export interface IsObjectStmt {
    /** ``col`` field of ``IsObjectStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``IsObjectStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``IsObjectStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``source`` field of ``IsObjectStmt`` (from upstream JSON Schema). */
    source: Operand,
}


/**
 * ``IsSetStmt`` definition from upstream JSON Schema.
 */
export interface IsSetStmt {
    /** ``col`` field of ``IsSetStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``IsSetStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``IsSetStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``source`` field of ``IsSetStmt`` (from upstream JSON Schema). */
    source: Operand,
}


/**
 * ``IsUndefinedStmt`` definition from upstream JSON Schema.
 */
export interface IsUndefinedStmt {
    /** ``col`` field of ``IsUndefinedStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``IsUndefinedStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``IsUndefinedStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``source`` field of ``IsUndefinedStmt`` (from upstream JSON Schema). */
    source: number,
}


/**
 * ``LenStmt`` definition from upstream JSON Schema.
 */
export interface LenStmt {
    /** ``col`` field of ``LenStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``LenStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``LenStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``source`` field of ``LenStmt`` (from upstream JSON Schema). */
    source: Operand,
    /** ``target`` field of ``LenStmt`` (from upstream JSON Schema). */
    target: number,
}


/**
 * ``MakeArrayStmt`` definition from upstream JSON Schema.
 */
export interface MakeArrayStmt {
    /** ``col`` field of ``MakeArrayStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``MakeArrayStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``MakeArrayStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``capacity`` field of ``MakeArrayStmt`` (from upstream JSON Schema). */
    capacity: number,
    /** ``target`` field of ``MakeArrayStmt`` (from upstream JSON Schema). */
    target: number,
}


/**
 * ``MakeNullStmt`` definition from upstream JSON Schema.
 */
export interface MakeNullStmt {
    /** ``col`` field of ``MakeNullStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``MakeNullStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``MakeNullStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``target`` field of ``MakeNullStmt`` (from upstream JSON Schema). */
    target: number,
}


/**
 * ``MakeNumberIntStmt`` definition from upstream JSON Schema.
 */
export interface MakeNumberIntStmt {
    /** ``col`` field of ``MakeNumberIntStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``MakeNumberIntStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``MakeNumberIntStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``target`` field of ``MakeNumberIntStmt`` (from upstream JSON Schema). */
    target: number,
    /** ``value`` field of ``MakeNumberIntStmt`` (from upstream JSON Schema). */
    value: number,
}


/**
 * ``MakeNumberRefStmt`` definition from upstream JSON Schema.
 */
export interface MakeNumberRefStmt {
    /** ``col`` field of ``MakeNumberRefStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``MakeNumberRefStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``MakeNumberRefStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``index`` field of ``MakeNumberRefStmt`` (from upstream JSON Schema). */
    index: number,
    /** Deprecated alias for `index`. Both keys are emitted by current OPA versions for backwards compatibility; will be removed in a future major release. Read `index` instead. */
    Index?: number,
    /** ``target`` field of ``MakeNumberRefStmt`` (from upstream JSON Schema). */
    target: number,
}


/**
 * ``MakeObjectStmt`` definition from upstream JSON Schema.
 */
export interface MakeObjectStmt {
    /** ``col`` field of ``MakeObjectStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``MakeObjectStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``MakeObjectStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``target`` field of ``MakeObjectStmt`` (from upstream JSON Schema). */
    target: number,
}


/**
 * ``MakeSetStmt`` definition from upstream JSON Schema.
 */
export interface MakeSetStmt {
    /** ``col`` field of ``MakeSetStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``MakeSetStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``MakeSetStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``target`` field of ``MakeSetStmt`` (from upstream JSON Schema). */
    target: number,
}


/**
 * ``NopStmt`` definition from upstream JSON Schema.
 */
export interface NopStmt {
    /** ``col`` field of ``NopStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``NopStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``NopStmt`` (from upstream JSON Schema). */
    row: number,
}


/**
 * ``NotEqualStmt`` definition from upstream JSON Schema.
 */
export interface NotEqualStmt {
    /** ``col`` field of ``NotEqualStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``NotEqualStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``NotEqualStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``a`` field of ``NotEqualStmt`` (from upstream JSON Schema). */
    a: Operand,
    /** ``b`` field of ``NotEqualStmt`` (from upstream JSON Schema). */
    b: Operand,
}


/**
 * ``NotStmt`` definition from upstream JSON Schema.
 */
export interface NotStmt {
    /** ``col`` field of ``NotStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``NotStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``NotStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``block`` field of ``NotStmt`` (from upstream JSON Schema). */
    block: string,
}


/**
 * ``ObjectInsertOnceStmt`` definition from upstream JSON Schema.
 */
export interface ObjectInsertOnceStmt {
    /** ``col`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``key`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema). */
    key: Operand,
    /** ``object`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema). */
    object: number,
    /** ``value`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema). */
    value: Operand,
}


/**
 * ``ObjectInsertStmt`` definition from upstream JSON Schema.
 */
export interface ObjectInsertStmt {
    /** ``col`` field of ``ObjectInsertStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``ObjectInsertStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``ObjectInsertStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``key`` field of ``ObjectInsertStmt`` (from upstream JSON Schema). */
    key: Operand,
    /** ``object`` field of ``ObjectInsertStmt`` (from upstream JSON Schema). */
    object: number,
    /** ``value`` field of ``ObjectInsertStmt`` (from upstream JSON Schema). */
    value: Operand,
}


/**
 * ``ObjectMergeStmt`` definition from upstream JSON Schema.
 */
export interface ObjectMergeStmt {
    /** ``col`` field of ``ObjectMergeStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``ObjectMergeStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``ObjectMergeStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``a`` field of ``ObjectMergeStmt`` (from upstream JSON Schema). */
    a: number,
    /** ``b`` field of ``ObjectMergeStmt`` (from upstream JSON Schema). */
    b: number,
    /** ``target`` field of ``ObjectMergeStmt`` (from upstream JSON Schema). */
    target: number,
}


/**
 * ``Plan`` definition from upstream JSON Schema.
 */
export interface Plan {
    /** ``blocks`` field of ``Plan`` (from upstream JSON Schema). */
    blocks: Block[],
    /** ``name`` field of ``Plan`` (from upstream JSON Schema). */
    name: string,
}


/**
 * ``Plans`` definition from upstream JSON Schema.
 */
export interface Plans {
    /** ``plans`` field of ``Plans`` (from upstream JSON Schema). */
    plans: Plan[],
}


/**
 * ``Policy`` definition from upstream JSON Schema.
 */
export interface Policy {
    /** ``funcs`` field of ``Policy`` (from upstream JSON Schema). */
    funcs?: Funcs,
    /** ``plans`` field of ``Policy`` (from upstream JSON Schema). */
    plans?: Plans,
    /** ``static`` field of ``Policy`` (from upstream JSON Schema). */
    static?: Static,
}


/**
 * ``ResetLocalStmt`` definition from upstream JSON Schema.
 */
export interface ResetLocalStmt {
    /** ``col`` field of ``ResetLocalStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``ResetLocalStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``ResetLocalStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``target`` field of ``ResetLocalStmt`` (from upstream JSON Schema). */
    target: number,
}


/**
 * ``ResultSetAddStmt`` definition from upstream JSON Schema.
 */
export interface ResultSetAddStmt {
    /** ``col`` field of ``ResultSetAddStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``ResultSetAddStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``ResultSetAddStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``value`` field of ``ResultSetAddStmt`` (from upstream JSON Schema). */
    value: number,
}


/**
 * ``ReturnLocalStmt`` definition from upstream JSON Schema.
 */
export interface ReturnLocalStmt {
    /** ``col`` field of ``ReturnLocalStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``ReturnLocalStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``ReturnLocalStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``source`` field of ``ReturnLocalStmt`` (from upstream JSON Schema). */
    source: number,
}


/**
 * ``ScanStmt`` definition from upstream JSON Schema.
 */
export interface ScanStmt {
    /** ``col`` field of ``ScanStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``ScanStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``ScanStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``block`` field of ``ScanStmt`` (from upstream JSON Schema). */
    block: string,
    /** ``key`` field of ``ScanStmt`` (from upstream JSON Schema). */
    key: number,
    /** ``source`` field of ``ScanStmt`` (from upstream JSON Schema). */
    source: number,
    /** ``value`` field of ``ScanStmt`` (from upstream JSON Schema). */
    value: number,
}


/**
 * ``SetAddStmt`` definition from upstream JSON Schema.
 */
export interface SetAddStmt {
    /** ``col`` field of ``SetAddStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``SetAddStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``SetAddStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``set`` field of ``SetAddStmt`` (from upstream JSON Schema). */
    set: number,
    /** ``value`` field of ``SetAddStmt`` (from upstream JSON Schema). */
    value: Operand,
}


/**
 * ``Static`` definition from upstream JSON Schema.
 */
export interface Static {
    /** ``builtin_funcs`` field of ``Static`` (from upstream JSON Schema). */
    builtin_funcs?: BuiltinFunc[],
    /** ``files`` field of ``Static`` (from upstream JSON Schema). */
    files?: StringConst[],
    /** ``strings`` field of ``Static`` (from upstream JSON Schema). */
    strings?: StringConst[],
}


/**
 * Tagged-wrapper class for the ``Stmt`` discriminated union from
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
 */
export interface Stmt {
    /** Discriminator tag identifying the Stmt variant. */
    type: string,
    /** Typed payload; concrete class is selected by ``type``. */
    stmt: Any,
}


/**
 * ``StringConst`` definition from upstream JSON Schema.
 */
export interface StringConst {
    /** ``value`` field of ``StringConst`` (from upstream JSON Schema). */
    value: string,
}


/**
 * Tagged-wrapper class for the ``Val`` discriminated union from
the upstream JSON Schema.

The ``type`` slot carries the discriminator tag and the
``value`` slot carries the typed payload. Because the
payload class varies by tag, ``value`` is typed as
``Any`` with an ``any_of`` union over the known payload classes;
consumers select the concrete class using the table below.

* ``bool`` -- payload class ``boolean``
* ``local`` -- payload class ``integer``
* ``string_index`` -- payload class ``integer``
 */
export interface Val {
    /** Discriminator tag identifying the Val variant. */
    type: string,
    /** Typed payload; concrete class is selected by ``type``. */
    value: Any,
}


/**
 * ``WithStmt`` definition from upstream JSON Schema.
 */
export interface WithStmt {
    /** ``col`` field of ``WithStmt`` (from upstream JSON Schema). */
    col: number,
    /** ``file`` field of ``WithStmt`` (from upstream JSON Schema). */
    file: number,
    /** ``row`` field of ``WithStmt`` (from upstream JSON Schema). */
    row: number,
    /** ``block`` field of ``WithStmt`` (from upstream JSON Schema). */
    block: string,
    /** ``local`` field of ``WithStmt`` (from upstream JSON Schema). */
    local: number,
    /** ``path`` field of ``WithStmt`` (from upstream JSON Schema). */
    path: number[],
    /** ``value`` field of ``WithStmt`` (from upstream JSON Schema). */
    value: Operand,
}


/**
 * Alias for ``Val`` (single-``$ref`` def in upstream JSON Schema).
 */
export interface Operand extends Val {
}



