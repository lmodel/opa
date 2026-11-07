export type OpaBuiltinCategoryName = string;
export type OpaImplementationSupportImplementation = string;
export type OpaVersionEntryName = string;
export type OpaFileRegoVersionPath = string;
export type OpaDecisionBundleName = string;
export type OpaBundleStatusName = string;
export type OpaPluginStatusName = string;
/**
* The future keywords the capabilities files OPA includes name.
*/
export enum OpaFutureKeyword {
    
    and = "and",
    contains = "contains",
    every = "every",
    if = "if",
    in = "in",
    not = "not",
    or = "or",
};
/**
* The language features the capabilities files OPA includes name.
*/
export enum OpaFeature {
    
    keywords_in_refs = "keywords_in_refs",
    rego_v1 = "rego_v1",
    rego_v1_import = "rego_v1_import",
    rego_v2 = "rego_v2",
    rego_v2_import = "rego_v2_import",
    rule_head_ref_string_prefixes = "rule_head_ref_string_prefixes",
    rule_head_refs = "rule_head_refs",
    template_strings = "template_strings",
};
/**
* The states a plugin reports.
*/
export enum OpaPluginState {
    
    /** Not in an error state, but not yet ready for normal operation, as at start-up. */
    NOT_READY = "NOT_READY",
    /** Working normally. */
    OK = "OK",
    /** In an error state, and not to be taken as working. */
    ERROR = "ERROR",
    /** Working, but degraded or in a state a person may need to fix. */
    WARN = "WARN",
};
/**
* The types of bundle.
*/
export enum OpaBundleType {
    
    /** A delta bundle, whose JSON Patch operations change the data OPA holds. */
    delta = "delta",
    /** A whole bundle, whose files replace what OPA held under its roots. */
    snapshot = "snapshot",
};


/**
 * A JSON object whose keys OPA leaves open.
 */
export interface OpaObject {
}


/**
 * Any JSON value.
 */
export interface OpaValue {
}


/**
 * Labels as text keys and text values, such as an OPA instance's `id` and `version`.
 */
export interface OpaLabels {
}


/**
 * An object whose every value is a list of strings, as Go writes HTTP headers and query parameters.
 */
export interface OpaStringListMap {
}


/**
 * A Rego type, as OPA's types package writes it in JSON. A named type is an argument or result of a built-in function, with a name and a description.
 */
export interface OpaType {
    /** The argument's or result's name, on a named type. */
    name?: string,
    /** What the argument or result holds, on a named type. */
    description?: string,
}


/**
 * A union of the types it lists in `of`, or any value when it lists none.
 */
export interface OpaAnyType extends OpaType {
    /** The kind of type. */
    type: string,
    /** The types the union admits. */
    of?: OpaType[],
}


/**
 * An array, with a type per position in `static` and one for the rest in `dynamic`.
 */
export interface OpaArrayType extends OpaType {
    /** The kind of type. */
    type: string,
    /** The type of each element by position. */
    static?: OpaType[],
    /** The type of the elements after the static ones. */
    dynamic?: OpaType,
}


/**
 * A boolean.
 */
export interface OpaBooleanType extends OpaType {
    /** The kind of type. */
    type: string,
}


/**
 * A function, with its arguments, its result and a variadic argument type.
 */
export interface OpaFunctionType extends OpaType {
    /** The kind of type. */
    type: string,
    /** The argument types, in order. */
    args?: OpaType[],
    /** The result type. */
    result?: OpaType,
    /** The type of any further arguments. */
    variadic?: OpaType,
}


/**
 * The null value.
 */
export interface OpaNullType extends OpaType {
    /** The kind of type. */
    type: string,
}


/**
 * A number.
 */
export interface OpaNumberType extends OpaType {
    /** The kind of type. */
    type: string,
}


/**
 * An object, with typed known keys in `static` and a key and value type for the rest in `dynamic`.
 */
export interface OpaObjectType extends OpaType {
    /** The kind of type. */
    type: string,
    /** The known keys and the types of their values. */
    static?: OpaStaticProperty[],
    /** The key type and value type of the other keys. */
    dynamic?: OpaDynamicProperty,
}


/**
 * A set, whose members have the type in `of`.
 */
export interface OpaSetType extends OpaType {
    /** The kind of type. */
    type: string,
    /** The type of the set's members. */
    of?: OpaType,
}


/**
 * A string.
 */
export interface OpaStringType extends OpaType {
    /** The kind of type. */
    type: string,
}


/**
 * A known key of an object type and the type of its value.
 */
export interface OpaStaticProperty {
    /** The key, as a JSON value. */
    key: OpaValue,
    /** The type of the key's value. */
    value: OpaType,
}


/**
 * The key type and value type that an object type gives its other keys.
 */
export interface OpaDynamicProperty {
    /** The type of the keys. */
    key: OpaType,
    /** The type of the values. */
    value: OpaType,
}


/**
 * What an OPA version supports, which a policy can be checked against.
 */
export interface OpaCapabilities {
    /** The built-in functions. */
    builtins?: OpaBuiltin[],
    /** The keywords a policy may import from future.keywords. */
    future_keywords?: string,
    /** The Wasm ABI versions supported. */
    wasm_abi_versions?: OpaWasmAbiVersion[],
    /** The language features supported. */
    features?: string,
    /** The hosts OPA may connect to, as host names or IP addresses. OPA reaches any host when the key is absent, and none when the list is empty. */
    allow_net?: string[],
}


/**
 * A built-in function and its type declaration.
 */
export interface OpaBuiltin {
    /** The function's name, such as `array.concat`. */
    name: string,
    /** What the function does. */
    description?: string,
    /** The categories the function belongs to. */
    categories?: string[],
    /** The function's type declaration. */
    decl: OpaFunctionType,
    /** The infix operator that calls the function, such as `+`. */
    infix?: string,
    /** Whether the function acts as a relation. */
    relation?: boolean,
    /** Whether the function is deprecated. */
    deprecated?: boolean,
    /** Whether the function may return different results for the same arguments. */
    nondeterministic?: boolean,
}


/**
 * A Wasm ABI version, as a major and a minor number.
 */
export interface OpaWasmAbiVersion {
    /** The major version. */
    version: number,
    /** The minor version. */
    minor_version: number,
}


/**
 * The catalogue: two keys that start with an underscore, and one key per built-in function, whose value describes it.
 */
export interface OpaBuiltinMetadataCatalog {
    /** The categories, each with the names of its functions. */
    _categories: {[index: OpaBuiltinCategoryName]: OpaBuiltinCategory },
    /** The implementations of Rego besides OPA that the catalogue tracks. */
    _implementations: OpaImplementation[],
}


/**
 * A category of built-in functions.
 */
export interface OpaBuiltinCategory {
    /** The category's name. */
    name: string,
    /** The names of the category's functions. */
    builtins: string[],
}


/**
 * An implementation of Rego besides OPA.
 */
export interface OpaImplementation {
    /** The implementation's version the catalogue reflects. */
    version: string,
    /** The implementation's key in each function's `implementations`. */
    id: string,
    /** The implementation's display name. */
    label: string,
    /** The implementation's GitHub repository, as owner/name. */
    repo: string,
}


/**
 * What the catalogue says about one built-in function.
 */
export interface OpaBuiltinMetadata {
    /** What the function does. */
    description?: string,
    /** The OPA version that added the function. */
    introduced: string,
    /** The OPA versions that have the function, and `edge`. */
    available: string[],
    /** Whether OPA's Wasm target implements the function. */
    wasm: boolean,
    /** The arguments, in order. */
    args: OpaBuiltinArgument[],
    /** The result. */
    result: OpaBuiltinResult,
    /** The other implementations that support the function, with the version that added it. */
    implementations: {[index: OpaImplementationSupportImplementation]: OpaImplementationSupport },
    /** The infix operator that calls the function. */
    infix?: string,
    /** Whether the function acts as a relation. */
    relation?: boolean,
    /** Whether the function is deprecated. */
    deprecated?: boolean,
}


/**
 * An argument of a built-in function.
 */
export interface OpaBuiltinArgument {
    /** The argument's type, written as OPA prints types, such as `array[string]`. */
    type: string,
    /** The argument's name. */
    name?: string,
    /** What the argument holds. */
    description?: string,
}


/**
 * The result of a built-in function. Some functions declare none.
 */
export interface OpaBuiltinResult {
    /** The result's type, written as OPA prints types. */
    type?: string,
    /** The result's name. */
    name?: string,
    /** What the result holds. */
    description?: string,
}


/**
 * An implementation that supports a function, and the version that added it.
 */
export interface OpaImplementationSupport {
    /** The implementation's version that added the function, or null for an implementation that publishes no version history. */
    version?: string,
    /** The implementation's id. */
    implementation: string,
}


/**
 * The version index.
 */
export interface OpaVersionIndex {
    /** The builtins, keyed by name, each with the version that introduced it. */
    builtins: {[index: OpaVersionEntryName]: OpaVersionEntry },
    /** The features, keyed by name, each with the version that introduced it. */
    features: {[index: OpaVersionEntryName]: OpaVersionEntry },
    /** The keywords, keyed by name, each with the version that introduced it. */
    keywords: {[index: OpaVersionEntryName]: OpaVersionEntry },
}


/**
 * A built-in function, feature or keyword, and the OPA version that introduced it.
 */
export interface OpaVersionEntry {
    /** The name of the function, feature or keyword. */
    name: string,
    /** The major version. */
    Major: number,
    /** The minor version. */
    Minor: number,
    /** The patch version. */
    Patch: number,
    /** The pre-release label, such as `rc2`. */
    PreRelease?: string,
    /** The build metadata, the part of a version after a plus sign. */
    Metadata?: string,
}


/**
 * The OPA Authorization Policy Input document.
 */
export interface OpaAuthorizationInput {
    /** The request body, parsed from JSON or YAML, for a POST to the default decision, v0/data, v1/data, v1/compile or v1/query. */
    body?: OpaValue,
    /** The caller's identity: the bearer token under --authentication=token, or the client certificate's subject under --authentication=tls. */
    identity?: string,
    /** The client's TLS certificates under --authentication=tls, each as Go writes an x509 certificate in JSON. */
    client_certificates?: OpaObject[],
    /** The HTTP method of the request, in upper case. */
    method: string,
    /** The request path, one segment per element. */
    path: string[],
    /** The query parameters, each with its list of values. */
    params: OpaStringListMap,
    /** The request headers, each with its list of values. */
    headers: OpaStringListMap,
}


/**
 * A bundle manifest. OPA's schema leaves the manifest open to other keys.
 */
export interface OpaManifest {
    /** The bundle's revision, a string the bundle's author chooses. */
    revision: string,
    /** Rego versions for single files, which override `rego_version`. */
    file_rego_versions?: {[index: OpaFileRegoVersionPath]: OpaFileRegoVersion },
    /** Metadata the bundle's author adds. */
    metadata?: OpaObject,
    /** The Rego version of the bundle's files: 0 for v0, 1 for v1. */
    rego_version?: number,
    /** The paths in the data tree the bundle owns. A bundle without the key owns the whole tree. */
    roots?: string[],
    /** The Wasm modules the bundle holds, and the entrypoints they resolve. */
    wasm?: OpaWasmResolver[],
}


/**
 * A Wasm module in a bundle, and the entrypoint it resolves.
 */
export interface OpaWasmResolver {
    /** The entrypoint's Rego annotations. OPA's schema leaves their shape open. */
    annotations?: OpaObject[],
    /** The entrypoint the module resolves. */
    entrypoint?: string,
    /** The module's path in the bundle. */
    module?: string,
}


/**
 * The Rego version of one file in the bundle.
 */
export interface OpaFileRegoVersion {
    /** The file's Rego version. */
    version: number,
    /** The file's path in the bundle. */
    path: string,
}


/**
 * Policy represents a planned policy query.
 */
export interface OpaPolicy {
    /** The functions the plans call. */
    funcs?: OpaFuncs,
    /** The query plans the policy exposes. */
    plans?: OpaPlans,
    /** The constants the plan indexes into. */
    static?: OpaStatic,
    /** The rules left out because no entrypoint reaches them. */
    unplanned_rules?: OpaUnplannedRule[],
}


/**
 * Static represents a static data segment that is indexed into by the policy.
 */
export interface OpaStatic {
    /** The built-in functions the plan calls. */
    builtin_funcs?: OpaBuiltinFunc[],
    /** The names of the policy files, which a location refers to by position. */
    files?: OpaStringConst[],
    /** The string constants, which a string index refers to by position. */
    strings?: OpaStringConst[],
}


/**
 * StringConst represents a string value.
 */
export interface OpaStringConst {
    /** The string. */
    value: string,
}


/**
 * BuiltinFunc represents a built-in function that may be required by the policy.
 */
export interface OpaBuiltinFunc {
    /** The function's type declaration. OPA's schema leaves it opaque; OPA writes a function type. */
    decl?: OpaFunctionType,
    /** The function's name. */
    name: string,
}


/**
 * Plans represents a collection of named query plans to expose in the policy.
 */
export interface OpaPlans {
    /** The plans. */
    plans?: OpaPlan[],
}


/**
 * Plan represents an ordered series of blocks to execute. Plan execution stops when a return statement is reached.
 */
export interface OpaPlan {
    /** The blocks, run in order. */
    blocks?: OpaBlock[],
    /** The plan's name, which is its entrypoint. */
    name: string,
}


/**
 * Funcs represents a collection of planned functions to include in the policy.
 */
export interface OpaFuncs {
    /** The functions. */
    funcs?: OpaFunc[],
}


/**
 * Func represents a named plan (function) that can be invoked. Functions accept one or more parameters and return a value.
 */
export interface OpaFunc {
    /** The blocks, run in order. */
    blocks?: OpaBlock[],
    /** The function's name. */
    name: string,
    /** The locals that hold the parameters. The first two are the input and data documents. */
    params?: number[],
    /** Where the function is in the data tree, when it has a path. */
    path?: string[],
    /** The local that holds the return value. */
    return: number,
}


/**
 * Block represents an ordered sequence of statements to execute. Blocks are executed until a return statement is encountered, a statement is undefined, or there are no more statements.
 */
export interface OpaBlock {
    /** The statements, run in order. */
    stmts: OpaStmt[],
}


/**
 * UnplannedRule represents a rule that was parsed but not included in the plan because it is not reachable from the entrypoint. This is used for coverage reporting, to distinguish rules that were never planned from rules that were planned but never executed.
 */
export interface OpaUnplannedRule {
    /** Where the rule is defined. */
    location?: OpaLocation,
    /** The rule's path. */
    path: string,
}


/**
 * Location records the filen index, and the row and column inside that file that a statement can be connected to.
 */
export interface OpaLocation {
    /** Index, in the plan's static files, of the policy file the statement comes from. */
    file: number,
    /** Column where the statement's source text starts. */
    col: number,
    /** Line where the statement's source text starts. */
    row: number,
    /** Column where the statement's source text ends. */
    end_col: number,
    /** Line where the statement's source text ends. */
    end_row: number,
}


/**
 * Stmt represents an operation (e.g., comparison, loop, dot, etc.) to execute. OPA writes each statement as its kind in `type` and its fields in `stmt`.
 */
export interface OpaStmt {
}


/**
 * The fields of a statement. Every kind carries the location of its source text.
 */
export interface OpaStmtBody {
    /** Index, in the plan's static files, of the policy file the statement comes from. */
    file: number,
    /** Column where the statement's source text starts. */
    col: number,
    /** Line where the statement's source text starts. */
    row: number,
    /** Column where the statement's source text ends. */
    end_col: number,
    /** Line where the statement's source text ends. */
    end_row: number,
}


/**
 * A statement of kind ArrayAppendStmt, with its fields in `stmt`.
 */
export interface OpaArrayAppendStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaArrayAppendStmtBody,
}


/**
 * ArrayAppendStmt represents a dynamic append operation of a value onto an array.
 */
export interface OpaArrayAppendStmtBody extends OpaStmtBody {
    /** The local that holds the array. */
    array: number,
    /** The value. */
    value: OpaOperand,
}


/**
 * A statement of kind AssignIntStmt, with its fields in `stmt`.
 */
export interface OpaAssignIntStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaAssignIntStmtBody,
}


/**
 * AssignIntStmt represents an assignment of an integer value to a local variable.
 */
export interface OpaAssignIntStmtBody extends OpaStmtBody {
    /** The local that receives the result. */
    target: number,
    /** The value. */
    value: number,
}


/**
 * A statement of kind AssignVarOnceStmt, with its fields in `stmt`.
 */
export interface OpaAssignVarOnceStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaAssignVarOnceStmtBody,
}


/**
 * AssignVarOnceStmt represents an assignment of one local variable to another. If the target is defined, execution aborts with a conflict error.
 */
export interface OpaAssignVarOnceStmtBody extends OpaStmtBody {
    /** What the statement reads. */
    source: OpaOperand,
    /** The local that receives the result. */
    target: number,
}


/**
 * A statement of kind AssignVarStmt, with its fields in `stmt`.
 */
export interface OpaAssignVarStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaAssignVarStmtBody,
}


/**
 * AssignVarStmt represents an assignment of one local variable to another.
 */
export interface OpaAssignVarStmtBody extends OpaStmtBody {
    /** What the statement reads. */
    source: OpaOperand,
    /** The local that receives the result. */
    target: number,
}


/**
 * A statement of kind BlockStmt, with its fields in `stmt`.
 */
export interface OpaBlockStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaBlockStmtBody,
}


/**
 * BlockStmt represents a nested block. Nested blocks and break statements can be used to short-circuit execution.
 */
export interface OpaBlockStmtBody extends OpaStmtBody {
    /** The blocks the statement runs. */
    blocks?: OpaBlock[],
}


/**
 * A statement of kind BreakStmt, with its fields in `stmt`.
 */
export interface OpaBreakStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaBreakStmtBody,
}


/**
 * BreakStmt represents a jump out of the current block. The index specifies how many blocks to jump starting from zero (the current block).
 */
export interface OpaBreakStmtBody extends OpaStmtBody {
    /** How many enclosing blocks to leave, counting the current block as zero. */
    index: number,
}


/**
 * A statement of kind CallDynamicStmt, with its fields in `stmt`.
 */
export interface OpaCallDynamicStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaCallDynamicStmtBody,
}


/**
 * CallDynamicStmt represents an indirect (data) function call. The result should be stored in the result local.
 */
export interface OpaCallDynamicStmtBody extends OpaStmtBody {
    /** The locals passed as arguments. */
    args?: number[],
    /** The path of the function in the data tree, one operand per segment. */
    path?: OpaOperand[],
    /** The local that receives the result. */
    result: number,
}


/**
 * A statement of kind CallStmt, with its fields in `stmt`.
 */
export interface OpaCallStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaCallStmtBody,
}


/**
 * CallStmt represents a named function call. The result should be stored in the result local.
 */
export interface OpaCallStmtBody extends OpaStmtBody {
    /** The arguments. */
    args?: OpaOperand[],
    /** The name of the function called. */
    func: string,
    /** The local that receives the result. */
    result: number,
}


/**
 * A statement of kind DotStmt, with its fields in `stmt`.
 */
export interface OpaDotStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaDotStmtBody,
}


/**
 * DotStmt represents a lookup operation on a value (e.g., array, object, etc.) The source of a DotStmt may be a scalar value in which case the statement will be undefined.
 */
export interface OpaDotStmtBody extends OpaStmtBody {
    /** What the statement reads. */
    source: OpaOperand,
    /** The local that receives the result. */
    target: number,
    /** The key. */
    key: OpaOperand,
}


/**
 * A statement of kind EqualStmt, with its fields in `stmt`.
 */
export interface OpaEqualStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaEqualStmtBody,
}


/**
 * EqualStmt represents an value-equality check of two local variables.
 */
export interface OpaEqualStmtBody extends OpaStmtBody {
    /** The first value. */
    a: OpaOperand,
    /** The second value. */
    b: OpaOperand,
}


/**
 * A statement of kind IsArrayStmt, with its fields in `stmt`.
 */
export interface OpaIsArrayStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaIsArrayStmtBody,
}


/**
 * IsArrayStmt represents a dynamic type check on a local variable.
 */
export interface OpaIsArrayStmtBody extends OpaStmtBody {
    /** What the statement reads. */
    source: OpaOperand,
}


/**
 * A statement of kind IsDefinedStmt, with its fields in `stmt`.
 */
export interface OpaIsDefinedStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaIsDefinedStmtBody,
}


/**
 * IsDefinedStmt represents a check of whether a local variable is defined.
 */
export interface OpaIsDefinedStmtBody extends OpaStmtBody {
    /** The local checked. */
    source: number,
}


/**
 * A statement of kind IsObjectStmt, with its fields in `stmt`.
 */
export interface OpaIsObjectStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaIsObjectStmtBody,
}


/**
 * IsObjectStmt represents a dynamic type check on a local variable.
 */
export interface OpaIsObjectStmtBody extends OpaStmtBody {
    /** What the statement reads. */
    source: OpaOperand,
}


/**
 * A statement of kind IsSetStmt, with its fields in `stmt`.
 */
export interface OpaIsSetStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaIsSetStmtBody,
}


/**
 * IsSetStmt represents a dynamic type check on a local variable.
 */
export interface OpaIsSetStmtBody extends OpaStmtBody {
    /** What the statement reads. */
    source: OpaOperand,
}


/**
 * A statement of kind IsUndefinedStmt, with its fields in `stmt`.
 */
export interface OpaIsUndefinedStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaIsUndefinedStmtBody,
}


/**
 * IsUndefinedStmt represents a check of whether local variable is undefined.
 */
export interface OpaIsUndefinedStmtBody extends OpaStmtBody {
    /** The local checked. */
    source: number,
}


/**
 * A statement of kind LenStmt, with its fields in `stmt`.
 */
export interface OpaLenStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaLenStmtBody,
}


/**
 * LenStmt represents a length() operation on a local variable. The result is stored in the target local variable.
 */
export interface OpaLenStmtBody extends OpaStmtBody {
    /** What the statement reads. */
    source: OpaOperand,
    /** The local that receives the result. */
    target: number,
}


/**
 * A statement of kind MakeArrayStmt, with its fields in `stmt`.
 */
export interface OpaMakeArrayStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaMakeArrayStmtBody,
}


/**
 * MakeArrayStmt constructs a local variable that refers to an array value.
 */
export interface OpaMakeArrayStmtBody extends OpaStmtBody {
    /** The local that receives the result. */
    target: number,
    /** The capacity to allocate. */
    capacity: number,
}


/**
 * A statement of kind MakeNullStmt, with its fields in `stmt`.
 */
export interface OpaMakeNullStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaMakeNullStmtBody,
}


/**
 * MakeNullStmt constructs a local variable that refers to a null value.
 */
export interface OpaMakeNullStmtBody extends OpaStmtBody {
    /** The local that receives the result. */
    target: number,
}


/**
 * A statement of kind MakeNumberIntStmt, with its fields in `stmt`.
 */
export interface OpaMakeNumberIntStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaMakeNumberIntStmtBody,
}


/**
 * MakeNumberIntStmt constructs a local variable that refers to an integer value.
 */
export interface OpaMakeNumberIntStmtBody extends OpaStmtBody {
    /** The local that receives the result. */
    target: number,
    /** The value. */
    value: number,
}


/**
 * A statement of kind MakeNumberRefStmt, with its fields in `stmt`.
 */
export interface OpaMakeNumberRefStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaMakeNumberRefStmtBody,
}


/**
 * MakeNumberRefStmt constructs a local variable that refers to a number stored as a string.
 */
export interface OpaMakeNumberRefStmtBody extends OpaStmtBody {
    /** The local that receives the result. */
    target: number,
    /** Index, in the plan's static strings, of the number written as a string. */
    index: number,
    /** Deprecated alias for `index`. Both keys are emitted by current OPA versions for backwards compatibility; will be removed in a future major release. Read `index` instead. */
    Index?: number,
}


/**
 * A statement of kind MakeObjectStmt, with its fields in `stmt`.
 */
export interface OpaMakeObjectStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaMakeObjectStmtBody,
}


/**
 * MakeObjectStmt constructs a local variable that refers to an object value.
 */
export interface OpaMakeObjectStmtBody extends OpaStmtBody {
    /** The local that receives the result. */
    target: number,
}


/**
 * A statement of kind MakeSetStmt, with its fields in `stmt`.
 */
export interface OpaMakeSetStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaMakeSetStmtBody,
}


/**
 * MakeSetStmt constructs a local variable that refers to a set value.
 */
export interface OpaMakeSetStmtBody extends OpaStmtBody {
    /** The local that receives the result. */
    target: number,
}


/**
 * A statement of kind NopStmt, with its fields in `stmt`.
 */
export interface OpaNopStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaNopStmtBody,
}


/**
 * NopStmt adds a nop instruction. Useful during development and debugging only.
 */
export interface OpaNopStmtBody extends OpaStmtBody {
}


/**
 * A statement of kind NotEqualStmt, with its fields in `stmt`.
 */
export interface OpaNotEqualStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaNotEqualStmtBody,
}


/**
 * NotEqualStmt represents a != check of two local variables.
 */
export interface OpaNotEqualStmtBody extends OpaStmtBody {
    /** The first value. */
    a: OpaOperand,
    /** The second value. */
    b: OpaOperand,
}


/**
 * A statement of kind NotStmt, with its fields in `stmt`.
 */
export interface OpaNotStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaNotStmtBody,
}


/**
 * NotStmt represents a negated statement.
 */
export interface OpaNotStmtBody extends OpaStmtBody {
    /** The block the statement runs. */
    block?: OpaBlock,
}


/**
 * A statement of kind ObjectInsertOnceStmt, with its fields in `stmt`.
 */
export interface OpaObjectInsertOnceStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaObjectInsertOnceStmtBody,
}


/**
 * ObjectInsertOnceStmt represents a dynamic insert operation of a key/value pair into an object. If the key already exists and the value differs, execution aborts with a conflict error.
 */
export interface OpaObjectInsertOnceStmtBody extends OpaStmtBody {
    /** The key. */
    key: OpaOperand,
    /** The local that holds the object. */
    object: number,
    /** The value. */
    value: OpaOperand,
}


/**
 * A statement of kind ObjectInsertStmt, with its fields in `stmt`.
 */
export interface OpaObjectInsertStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaObjectInsertStmtBody,
}


/**
 * ObjectInsertStmt represents a dynamic insert operation of a key/value pair into an object.
 */
export interface OpaObjectInsertStmtBody extends OpaStmtBody {
    /** The key. */
    key: OpaOperand,
    /** The local that holds the object. */
    object: number,
    /** The value. */
    value: OpaOperand,
}


/**
 * A statement of kind ObjectMergeStmt, with its fields in `stmt`.
 */
export interface OpaObjectMergeStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaObjectMergeStmtBody,
}


/**
 * ObjectMergeStmt performs a recursive merge of two object values. If either of the locals refer to non-object values this operation will abort with a conflict error.
 */
export interface OpaObjectMergeStmtBody extends OpaStmtBody {
    /** The local that receives the result. */
    target: number,
    /** The local that holds the first object. */
    a: number,
    /** The local that holds the second object. */
    b: number,
}


/**
 * A statement of kind ResetLocalStmt, with its fields in `stmt`.
 */
export interface OpaResetLocalStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaResetLocalStmtBody,
}


/**
 * ResetLocalStmt resets a local variable to 0.
 */
export interface OpaResetLocalStmtBody extends OpaStmtBody {
    /** The local that receives the result. */
    target: number,
}


/**
 * A statement of kind ResultSetAddStmt, with its fields in `stmt`.
 */
export interface OpaResultSetAddStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaResultSetAddStmtBody,
}


/**
 * ResultSetAddStmt adds a value into the result set returned by the query plan.
 */
export interface OpaResultSetAddStmtBody extends OpaStmtBody {
    /** The local added to the result set. */
    value: number,
}


/**
 * A statement of kind ReturnLocalStmt, with its fields in `stmt`.
 */
export interface OpaReturnLocalStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaReturnLocalStmtBody,
}


/**
 * ReturnLocalStmt represents a return statement that yields a local value.
 */
export interface OpaReturnLocalStmtBody extends OpaStmtBody {
    /** The local returned. */
    source: number,
}


/**
 * A statement of kind ScanStmt, with its fields in `stmt`.
 */
export interface OpaScanStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaScanStmtBody,
}


/**
 * ScanStmt represents a linear scan over a composite value. The source may be a scalar in which case the block will never execute.
 */
export interface OpaScanStmtBody extends OpaStmtBody {
    /** The local whose value is scanned. */
    source: number,
    /** The block run for each key and value. */
    block?: OpaBlock,
    /** The local that receives each key. */
    key: number,
    /** The local that receives each value. */
    value: number,
}


/**
 * A statement of kind SetAddStmt, with its fields in `stmt`.
 */
export interface OpaSetAddStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaSetAddStmtBody,
}


/**
 * SetAddStmt represents a dynamic add operation of an element into a set.
 */
export interface OpaSetAddStmtBody extends OpaStmtBody {
    /** The local that holds the set. */
    set: number,
    /** The value. */
    value: OpaOperand,
}


/**
 * A statement of kind WithStmt, with its fields in `stmt`.
 */
export interface OpaWithStmt extends OpaStmt {
    /** The kind of statement. */
    type: string,
    /** The statement's fields. */
    stmt: OpaWithStmtBody,
}


/**
 * WithStmt replaces the Local or a portion of the document referred to by the Local with the Value and executes the contained block. If the Path is non-empty, the Value is upserted into the Local.
 */
export interface OpaWithStmtBody extends OpaStmtBody {
    /** The block the statement runs. */
    block?: OpaBlock,
    /** The local whose value, or part of it, is replaced. */
    local: number,
    /** The path within the local's value to replace, as indices of static strings. Empty replaces the whole value. */
    path?: number[],
    /** The replacement value. */
    value: OpaOperand,
}


/**
 * Operand represents a value that a statement operates on. OPA writes it as its kind in `type` and the value in `value`.
 */
export interface OpaOperand {
}


/**
 * Bool represents a constant boolean.
 */
export interface OpaBoolOperand extends OpaOperand {
    /** The kind of operand. */
    type: string,
    /** The operand's value. */
    value: boolean,
}


/**
 * A local variable, by its number.
 */
export interface OpaLocalOperand extends OpaOperand {
    /** The kind of operand. */
    type: string,
    /** The operand's value. */
    value: number,
}


/**
 * StringIndex represents the index into the plan's list of constant strings of a constant string.
 */
export interface OpaStringIndexOperand extends OpaOperand {
    /** The kind of operand. */
    type: string,
    /** The operand's value. */
    value: number,
}


/**
 * A decision OPA made: the query or path, the input and result, the bundles and the instance behind it, and when and for whom it was made.
 */
export interface OpaDecisionLogEvent {
    /** The revision of the bundle that made the decision, under the legacy `bundle` configuration. */
    revision?: string,
    /** When OPA made the decision. */
    timestamp: string,
    /** The labels of the OPA instance that made the decision: its `id`, its `version` and those the configuration sets. */
    labels?: OpaLabels,
    /** The decision's id, which OPA also returns to the client. */
    decision_id: string,
    /** The id that groups the decisions of one batch request. */
    batch_decision_id?: string,
    /** The request's trace id in W3C trace context, with tracing on. */
    trace_id?: string,
    /** The request's span id in W3C trace context, with tracing on. */
    span_id?: string,
    /** The bundles whose policy made the decision, by name. */
    bundles?: {[index: OpaDecisionBundleName]: OpaDecisionBundle },
    /** The decision's path in the data tree, such as `http/example/authz/allow`. */
    path?: string,
    /** The ad hoc query the Query API received. */
    query?: string,
    /** The input of the query. */
    input?: OpaValue,
    /** The result the client received. */
    result?: OpaValue,
    /** The intermediate results the evaluation recorded, when OPA runs with the environment variable OPA_DECISIONS_INTERMEDIATE_RESULTS set. */
    intermediate_results?: OpaObject,
    /** The result as the result mapper of a decision made through OPA's Go SDK wrote it. */
    mapped_result?: OpaValue,
    /** What each non-deterministic built-in function returned, by function and arguments, with `nd_builtin_cache` on. */
    nd_builtin_cache?: OpaObject,
    /** JSON pointers to the fields a mask policy removed. */
    erased?: string[],
    /** JSON pointers to the fields a mask policy replaced. */
    masked?: string[],
    /** The error the evaluation raised, as OPA writes it in JSON. */
    error?: OpaValue,
    /** The address of the client that asked. */
    requested_by?: string,
    /** The query's metrics, by name. */
    metrics?: OpaObject,
    /** The number OPA gave the HTTP request, which its request and response logs also carry. */
    req_id?: number,
    /** The merged `labels` annotations of each rule the evaluation used. */
    rule_labels?: OpaObject[],
    /** The parts of the HTTP request the configuration asks OPA to log. */
    request_context?: OpaRequestContext,
    /** Fields the server or a plugin adds, such as `request_metadata`, the top-level keys of a Data API request body besides `input`. */
    custom?: OpaObject,
}


/**
 * A bundle whose policy made a decision.
 */
export interface OpaDecisionBundle {
    /** The bundle's revision when OPA made the decision. */
    revision?: string,
    /** The bundle's name. */
    name: string,
}


/**
 * The parts of the request that a decision log event logs.
 */
export interface OpaRequestContext {
    /** The logged parts of the HTTP request. */
    http?: OpaHttpRequestContext,
}


/**
 * The logged parts of an HTTP request.
 */
export interface OpaHttpRequestContext {
    /** The headers the configuration names, each with its values. */
    headers?: OpaStringListMap,
}


/**
 * A report on an OPA instance: the state of its bundles, its decision log uploads and its plugins, and its metrics.
 */
export interface OpaStatusReport {
    /** The labels of the OPA instance that sends the report. */
    labels?: OpaLabels,
    /** The status of the one bundle of the legacy `bundle` configuration. */
    bundle?: OpaBundleStatus,
    /** The status of each bundle OPA downloads, by name. */
    bundles?: {[index: OpaBundleStatusName]: OpaBundleStatus },
    /** The status of the discovery bundle. */
    discovery?: OpaBundleStatus,
    /** The status of the decision log uploads. */
    decision_logs?: OpaDecisionLogStatus,
    /** The instance's metrics, under the name of their provider, such as `prometheus`. */
    metrics?: OpaObject,
    /** The state of each plugin, by name. */
    plugins?: {[index: OpaPluginStatusName]: OpaPluginStatus },
}


/**
 * The status of a bundle: its active revision, when OPA last asked for, downloaded and activated it, and the errors of the last attempt.
 */
export interface OpaBundleStatus {
    /** The bundle's type. */
    type?: string,
    /** The bundle's name. */
    name: string,
    /** The revision of the bundle OPA last activated. */
    active_revision?: string,
    /** When OPA last activated the bundle. */
    last_successful_activation: string,
    /** The bundle's size in bytes. */
    size?: number,
    /** When OPA last downloaded the bundle. */
    last_successful_download: string,
    /** When a request for the bundle last succeeded. */
    last_successful_request: string,
    /** When OPA last asked for the bundle. */
    last_request: string,
    /** The error code, when the last download or activation failed. */
    code?: string,
    /** What went wrong, in words. */
    message?: string,
    /** The parse and compile errors of the last activation. */
    errors?: OpaObject[],
    /** The metrics of the last download and activation. */
    metrics?: OpaObject,
    /** The HTTP status code of a download the server refused. */
    http_code?: number,
}


/**
 * The status of the decision log uploads.
 */
export interface OpaDecisionLogStatus {
    /** The error code, when the last upload failed. */
    code?: string,
    /** What went wrong, in words. */
    message?: string,
    /** The HTTP status code of an upload the server refused. */
    http_code?: number,
    /** The decision logger's metrics. */
    metrics?: OpaObject,
}


/**
 * The state of a plugin.
 */
export interface OpaPluginStatus {
    /** The plugin's name. */
    name: string,
    /** The plugin's state. */
    state: string,
    /** More about the state, in words. */
    message?: string,
}



