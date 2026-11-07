-- # Class: OpaObject Description: A JSON object whose keys OPA leaves open.
--     * Slot: id
--     * Slot: OpaAuthorizationInput_id Description: Autocreated FK slot
--     * Slot: OpaWasmResolver_id Description: Autocreated FK slot
-- # Class: OpaValue Description: Any JSON value.
--     * Slot: id
-- # Abstract Class: OpaType Description: A Rego type, as OPA's types package writes it in JSON. A named type is an argument or result of a built-in function, with a name and a description.
--     * Slot: id
--     * Slot: name Description: The argument's or result's name, on a named type.
--     * Slot: description Description: What the argument or result holds, on a named type.
--     * Slot: OpaAnyType_id Description: Autocreated FK slot
--     * Slot: OpaArrayType_id Description: Autocreated FK slot
--     * Slot: OpaFunctionType_id Description: Autocreated FK slot
-- # Class: OpaAnyType Description: A union of the types it lists in `of`, or any value when it lists none.
--     * Slot: id
--     * Slot: type Description: The kind of type.
--     * Slot: name Description: The argument's or result's name, on a named type.
--     * Slot: description Description: What the argument or result holds, on a named type.
-- # Class: OpaArrayType Description: An array, with a type per position in `static` and one for the rest in `dynamic`.
--     * Slot: id
--     * Slot: type Description: The kind of type.
--     * Slot: name Description: The argument's or result's name, on a named type.
--     * Slot: description Description: What the argument or result holds, on a named type.
--     * Slot: dynamic_id Description: The type of the elements after the static ones.
-- # Class: OpaBooleanType Description: A boolean.
--     * Slot: id
--     * Slot: type Description: The kind of type.
--     * Slot: name Description: The argument's or result's name, on a named type.
--     * Slot: description Description: What the argument or result holds, on a named type.
-- # Class: OpaFunctionType Description: A function, with its arguments, its result and a variadic argument type.
--     * Slot: id
--     * Slot: type Description: The kind of type.
--     * Slot: name Description: The argument's or result's name, on a named type.
--     * Slot: description Description: What the argument or result holds, on a named type.
--     * Slot: result_id Description: The result type.
--     * Slot: variadic_id Description: The type of any further arguments.
-- # Class: OpaNullType Description: The null value.
--     * Slot: id
--     * Slot: type Description: The kind of type.
--     * Slot: name Description: The argument's or result's name, on a named type.
--     * Slot: description Description: What the argument or result holds, on a named type.
-- # Class: OpaNumberType Description: A number.
--     * Slot: id
--     * Slot: type Description: The kind of type.
--     * Slot: name Description: The argument's or result's name, on a named type.
--     * Slot: description Description: What the argument or result holds, on a named type.
-- # Class: OpaObjectType Description: An object, with typed known keys in `static` and a key and value type for the rest in `dynamic`.
--     * Slot: id
--     * Slot: type Description: The kind of type.
--     * Slot: name Description: The argument's or result's name, on a named type.
--     * Slot: description Description: What the argument or result holds, on a named type.
--     * Slot: dynamic_id Description: The key type and value type of the other keys.
-- # Class: OpaSetType Description: A set, whose members have the type in `of`.
--     * Slot: id
--     * Slot: type Description: The kind of type.
--     * Slot: name Description: The argument's or result's name, on a named type.
--     * Slot: description Description: What the argument or result holds, on a named type.
--     * Slot: of_id Description: The type of the set's members.
-- # Class: OpaStringType Description: A string.
--     * Slot: id
--     * Slot: type Description: The kind of type.
--     * Slot: name Description: The argument's or result's name, on a named type.
--     * Slot: description Description: What the argument or result holds, on a named type.
-- # Class: OpaStaticProperty Description: A known key of an object type and the type of its value.
--     * Slot: id
--     * Slot: OpaObjectType_id Description: Autocreated FK slot
--     * Slot: key_id Description: The key, as a JSON value.
--     * Slot: value_id Description: The type of the key's value.
-- # Class: OpaDynamicProperty Description: The key type and value type that an object type gives its other keys.
--     * Slot: id
--     * Slot: key_id Description: The type of the keys.
--     * Slot: value_id Description: The type of the values.
-- # Class: OpaCapabilities Description: What an OPA version supports, which a policy can be checked against.
--     * Slot: id
-- # Class: OpaBuiltin Description: A built-in function and its type declaration.
--     * Slot: id
--     * Slot: name Description: The function's name, such as `array.concat`.
--     * Slot: description Description: What the function does.
--     * Slot: infix Description: The infix operator that calls the function, such as `+`.
--     * Slot: relation Description: Whether the function acts as a relation.
--     * Slot: deprecated Description: Whether the function is deprecated.
--     * Slot: nondeterministic Description: Whether the function may return different results for the same arguments.
--     * Slot: OpaCapabilities_id Description: Autocreated FK slot
--     * Slot: decl_id Description: The function's type declaration.
-- # Class: OpaWasmAbiVersion Description: A Wasm ABI version, as a major and a minor number.
--     * Slot: id
--     * Slot: version Description: The major version.
--     * Slot: minor_version Description: The minor version.
--     * Slot: OpaCapabilities_id Description: Autocreated FK slot
-- # Class: OpaBuiltinMetadataCatalog Description: The catalogue: two keys that start with an underscore, and one key per built-in function, whose value describes it.
--     * Slot: id
-- # Class: OpaBuiltinCategory Description: A category of built-in functions.
--     * Slot: name Description: The category's name.
--     * Slot: OpaBuiltinMetadataCatalog_id Description: Autocreated FK slot
-- # Class: OpaImplementation Description: An implementation of Rego besides OPA.
--     * Slot: uid
--     * Slot: version Description: The implementation's version the catalogue reflects.
--     * Slot: id Description: The implementation's key in each function's `implementations`.
--     * Slot: label Description: The implementation's display name.
--     * Slot: repo Description: The implementation's GitHub repository, as owner/name.
--     * Slot: OpaBuiltinMetadataCatalog_id Description: Autocreated FK slot
-- # Class: OpaBuiltinMetadata Description: What the catalogue says about one built-in function.
--     * Slot: id
--     * Slot: description Description: What the function does.
--     * Slot: introduced Description: The OPA version that added the function.
--     * Slot: wasm Description: Whether OPA's Wasm target implements the function.
--     * Slot: infix Description: The infix operator that calls the function.
--     * Slot: relation Description: Whether the function acts as a relation.
--     * Slot: deprecated Description: Whether the function is deprecated.
--     * Slot: result_id Description: The result.
-- # Class: OpaBuiltinArgument Description: An argument of a built-in function.
--     * Slot: id
--     * Slot: type Description: The argument's type, written as OPA prints types, such as `array[string]`.
--     * Slot: name Description: The argument's name.
--     * Slot: description Description: What the argument holds.
--     * Slot: OpaBuiltinMetadata_id Description: Autocreated FK slot
-- # Class: OpaBuiltinResult Description: The result of a built-in function. Some functions declare none.
--     * Slot: id
--     * Slot: type Description: The result's type, written as OPA prints types.
--     * Slot: name Description: The result's name.
--     * Slot: description Description: What the result holds.
-- # Class: OpaImplementationSupport Description: An implementation that supports a function, and the version that added it.
--     * Slot: version Description: The implementation's version that added the function.
--     * Slot: implementation Description: The implementation's id.
--     * Slot: OpaBuiltinMetadata_id Description: Autocreated FK slot
-- # Class: OpaVersionIndex Description: The version index.
--     * Slot: id
-- # Class: OpaVersionEntry Description: A built-in function, feature or keyword, and the OPA version that introduced it.
--     * Slot: name Description: The name of the function, feature or keyword.
--     * Slot: Major Description: The major version.
--     * Slot: Minor Description: The minor version.
--     * Slot: Patch Description: The patch version.
--     * Slot: PreRelease Description: The pre-release label, such as `rc2`.
--     * Slot: OpaVersionIndex_id Description: Autocreated FK slot
-- # Class: OpaAuthorizationInput Description: The OPA Authorization Policy Input document.
--     * Slot: id
--     * Slot: identity Description: The bearer token or client certificate subject that identifies the caller.
--     * Slot: method Description: The HTTP method of the request.
--     * Slot: body_id Description: The request body.
--     * Slot: params_id Description: The query parameters.
--     * Slot: headers_id Description: The request headers.
-- # Class: OpaManifest Description: A bundle manifest. OPA's schema leaves the manifest open to other keys.
--     * Slot: id
--     * Slot: revision Description: The bundle's revision, a string the bundle's author chooses.
--     * Slot: rego_version Description: The Rego version of the bundle's files: 0 for v0, 1 for v1.
--     * Slot: metadata_id Description: Metadata the bundle's author adds.
-- # Class: OpaWasmResolver Description: A Wasm module in a bundle, and the entrypoint it resolves.
--     * Slot: id
--     * Slot: entrypoint Description: The entrypoint the module resolves.
--     * Slot: module Description: The module's path in the bundle.
--     * Slot: OpaManifest_id Description: Autocreated FK slot
-- # Class: OpaFileRegoVersion Description: The Rego version of one file in the bundle.
--     * Slot: version Description: The file's Rego version.
--     * Slot: path Description: The file's path in the bundle.
--     * Slot: OpaManifest_id Description: Autocreated FK slot
-- # Class: OpaPolicy Description: Policy represents a planned policy query.
--     * Slot: id
--     * Slot: funcs_id Description: The functions the plans call.
--     * Slot: plans_id Description: The query plans the policy exposes.
--     * Slot: static_id Description: The constants the plan indexes into.
-- # Class: OpaStatic Description: Static represents a static data segment that is indexed into by the policy.
--     * Slot: id
-- # Class: OpaStringConst Description: StringConst represents a string value.
--     * Slot: id
--     * Slot: value Description: The string.
--     * Slot: OpaStatic_id Description: Autocreated FK slot
-- # Class: OpaBuiltinFunc Description: BuiltinFunc represents a built-in function that may be required by the policy.
--     * Slot: id
--     * Slot: name Description: The function's name.
--     * Slot: OpaStatic_id Description: Autocreated FK slot
--     * Slot: decl_id Description: BuiltinFunc declaration; opaque in this schema.
-- # Class: OpaPlans Description: Plans represents a collection of named query plans to expose in the policy.
--     * Slot: id
-- # Class: OpaPlan Description: Plan represents an ordered series of blocks to execute. Plan execution stops when a return statement is reached.
--     * Slot: id
--     * Slot: name Description: The plan's name, which is its entrypoint.
--     * Slot: OpaPlans_id Description: Autocreated FK slot
-- # Class: OpaFuncs Description: Funcs represents a collection of planned functions to include in the policy.
--     * Slot: id
-- # Class: OpaFunc Description: Func represents a named plan (function) that can be invoked. Functions accept one or more parameters and return a value.
--     * Slot: id
--     * Slot: name Description: The function's name.
--     * Slot: return Description: The local that holds the return value.
--     * Slot: OpaFuncs_id Description: Autocreated FK slot
-- # Class: OpaBlock Description: Block represents an ordered sequence of statements to execute. Blocks are executed until a return statement is encountered, a statement is undefined, or there are no more statements.
--     * Slot: id
--     * Slot: OpaPlan_id Description: Autocreated FK slot
--     * Slot: OpaFunc_id Description: Autocreated FK slot
--     * Slot: OpaBlockStmtBody_id Description: Autocreated FK slot
-- # Class: OpaUnplannedRule Description: UnplannedRule represents a rule that was parsed but not included in the plan because it is not reachable from the entrypoint. This is used for coverage reporting, to distinguish rules that were never planned from rules that were planned but never executed.
--     * Slot: id
--     * Slot: path Description: The rule's path.
--     * Slot: OpaPolicy_id Description: Autocreated FK slot
--     * Slot: location_id Description: Where the rule is defined.
-- # Class: OpaLocation Description: Location records the filen index, and the row and column inside that file that a statement can be connected to.
--     * Slot: id
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Abstract Class: OpaStmt Description: Stmt represents an operation (e.g., comparison, loop, dot, etc.) to execute. OPA writes each statement as its kind in `type` and its fields in `stmt`.
--     * Slot: id
--     * Slot: OpaBlock_id Description: Autocreated FK slot
-- # Abstract Class: OpaStmtBody Description: The fields of a statement. Every kind carries the location of its source text.
--     * Slot: id
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaArrayAppendStmt Description: A statement of kind ArrayAppendStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaArrayAppendStmtBody Description: ArrayAppendStmt represents a dynamic append operation of a value onto an array.
--     * Slot: id
--     * Slot: array Description: The local that holds the array.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: value_id Description: The value.
-- # Class: OpaAssignIntStmt Description: A statement of kind AssignIntStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaAssignIntStmtBody Description: AssignIntStmt represents an assignment of an integer value to a local variable.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: value Description: The value.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaAssignVarOnceStmt Description: A statement of kind AssignVarOnceStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaAssignVarOnceStmtBody Description: AssignVarOnceStmt represents an assignment of one local variable to another. If the target is defined, execution aborts with a conflict error.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: source_id Description: What the statement reads.
-- # Class: OpaAssignVarStmt Description: A statement of kind AssignVarStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaAssignVarStmtBody Description: AssignVarStmt represents an assignment of one local variable to another.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: source_id Description: What the statement reads.
-- # Class: OpaBlockStmt Description: A statement of kind BlockStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaBlockStmtBody Description: BlockStmt represents a nested block. Nested blocks and break statements can be used to short-circuit execution.
--     * Slot: id
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaBreakStmt Description: A statement of kind BreakStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaBreakStmtBody Description: BreakStmt represents a jump out of the current block. The index specifies how many blocks to jump starting from zero (the current block).
--     * Slot: id
--     * Slot: index Description: How many enclosing blocks to leave, counting the current block as zero.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaCallDynamicStmt Description: A statement of kind CallDynamicStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaCallDynamicStmtBody Description: CallDynamicStmt represents an indirect (data) function call. The result should be stored in the result local.
--     * Slot: id
--     * Slot: result Description: The local that receives the result.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaCallStmt Description: A statement of kind CallStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaCallStmtBody Description: CallStmt represents a named function call. The result should be stored in the result local.
--     * Slot: id
--     * Slot: func Description: The name of the function called.
--     * Slot: result Description: The local that receives the result.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaDotStmt Description: A statement of kind DotStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaDotStmtBody Description: DotStmt represents a lookup operation on a value (e.g., array, object, etc.) The source of a DotStmt may be a scalar value in which case the statement will be undefined.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: source_id Description: What the statement reads.
--     * Slot: key_id Description: The key.
-- # Class: OpaEqualStmt Description: A statement of kind EqualStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaEqualStmtBody Description: EqualStmt represents an value-equality check of two local variables.
--     * Slot: id
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: a_id Description: The first value.
--     * Slot: b_id Description: The second value.
-- # Class: OpaIsArrayStmt Description: A statement of kind IsArrayStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaIsArrayStmtBody Description: IsArrayStmt represents a dynamic type check on a local variable.
--     * Slot: id
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: source_id Description: What the statement reads.
-- # Class: OpaIsDefinedStmt Description: A statement of kind IsDefinedStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaIsDefinedStmtBody Description: IsDefinedStmt represents a check of whether a local variable is defined.
--     * Slot: id
--     * Slot: source Description: The local checked.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaIsObjectStmt Description: A statement of kind IsObjectStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaIsObjectStmtBody Description: IsObjectStmt represents a dynamic type check on a local variable.
--     * Slot: id
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: source_id Description: What the statement reads.
-- # Class: OpaIsSetStmt Description: A statement of kind IsSetStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaIsSetStmtBody Description: IsSetStmt represents a dynamic type check on a local variable.
--     * Slot: id
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: source_id Description: What the statement reads.
-- # Class: OpaIsUndefinedStmt Description: A statement of kind IsUndefinedStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaIsUndefinedStmtBody Description: IsUndefinedStmt represents a check of whether local variable is undefined.
--     * Slot: id
--     * Slot: source Description: The local checked.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaLenStmt Description: A statement of kind LenStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaLenStmtBody Description: LenStmt represents a length() operation on a local variable. The result is stored in the target local variable.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: source_id Description: What the statement reads.
-- # Class: OpaMakeArrayStmt Description: A statement of kind MakeArrayStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaMakeArrayStmtBody Description: MakeArrayStmt constructs a local variable that refers to an array value.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: capacity Description: The capacity to allocate.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaMakeNullStmt Description: A statement of kind MakeNullStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaMakeNullStmtBody Description: MakeNullStmt constructs a local variable that refers to a null value.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaMakeNumberIntStmt Description: A statement of kind MakeNumberIntStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaMakeNumberIntStmtBody Description: MakeNumberIntStmt constructs a local variable that refers to an integer value.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: value Description: The value.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaMakeNumberRefStmt Description: A statement of kind MakeNumberRefStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaMakeNumberRefStmtBody Description: MakeNumberRefStmt constructs a local variable that refers to a number stored as a string.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: index Description: Index, in the plan's static strings, of the number written as a string.
--     * Slot: Index Description: Deprecated alias for `index`. Both keys are emitted by current OPA versions for backwards compatibility; will be removed in a future major release. Read `index` instead.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaMakeObjectStmt Description: A statement of kind MakeObjectStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaMakeObjectStmtBody Description: MakeObjectStmt constructs a local variable that refers to an object value.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaMakeSetStmt Description: A statement of kind MakeSetStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaMakeSetStmtBody Description: MakeSetStmt constructs a local variable that refers to a set value.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaNopStmt Description: A statement of kind NopStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaNopStmtBody Description: NopStmt adds a nop instruction. Useful during development and debugging only.
--     * Slot: id
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaNotEqualStmt Description: A statement of kind NotEqualStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaNotEqualStmtBody Description: NotEqualStmt represents a != check of two local variables.
--     * Slot: id
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: a_id Description: The first value.
--     * Slot: b_id Description: The second value.
-- # Class: OpaNotStmt Description: A statement of kind NotStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaNotStmtBody Description: NotStmt represents a negated statement.
--     * Slot: id
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: block_id Description: The block the statement runs.
-- # Class: OpaObjectInsertOnceStmt Description: A statement of kind ObjectInsertOnceStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaObjectInsertOnceStmtBody Description: ObjectInsertOnceStmt represents a dynamic insert operation of a key/value pair into an object. If the key already exists and the value differs, execution aborts with a conflict error.
--     * Slot: id
--     * Slot: object Description: The local that holds the object.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: key_id Description: The key.
--     * Slot: value_id Description: The value.
-- # Class: OpaObjectInsertStmt Description: A statement of kind ObjectInsertStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaObjectInsertStmtBody Description: ObjectInsertStmt represents a dynamic insert operation of a key/value pair into an object.
--     * Slot: id
--     * Slot: object Description: The local that holds the object.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: key_id Description: The key.
--     * Slot: value_id Description: The value.
-- # Class: OpaObjectMergeStmt Description: A statement of kind ObjectMergeStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaObjectMergeStmtBody Description: ObjectMergeStmt performs a recursive merge of two object values. If either of the locals refer to non-object values this operation will abort with a conflict error.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: a Description: The local that holds the first object.
--     * Slot: b Description: The local that holds the second object.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaResetLocalStmt Description: A statement of kind ResetLocalStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaResetLocalStmtBody Description: ResetLocalStmt resets a local variable to 0.
--     * Slot: id
--     * Slot: target Description: The local that receives the result.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaResultSetAddStmt Description: A statement of kind ResultSetAddStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaResultSetAddStmtBody Description: ResultSetAddStmt adds a value into the result set returned by the query plan.
--     * Slot: id
--     * Slot: value Description: The local added to the result set.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaReturnLocalStmt Description: A statement of kind ReturnLocalStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaReturnLocalStmtBody Description: ReturnLocalStmt represents a return statement that yields a local value.
--     * Slot: id
--     * Slot: source Description: The local returned.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
-- # Class: OpaScanStmt Description: A statement of kind ScanStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaScanStmtBody Description: ScanStmt represents a linear scan over a composite value. The source may be a scalar in which case the block will never execute.
--     * Slot: id
--     * Slot: source Description: The local whose value is scanned.
--     * Slot: key Description: The local that receives each key.
--     * Slot: value Description: The local that receives each value.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: block_id Description: The block run for each key and value.
-- # Class: OpaSetAddStmt Description: A statement of kind SetAddStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaSetAddStmtBody Description: SetAddStmt represents a dynamic add operation of an element into a set.
--     * Slot: id
--     * Slot: set Description: The local that holds the set.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: value_id Description: The value.
-- # Class: OpaWithStmt Description: A statement of kind WithStmt, with its fields in `stmt`.
--     * Slot: id
--     * Slot: type Description: The kind of statement.
--     * Slot: stmt_id Description: The statement's fields.
-- # Class: OpaWithStmtBody Description: WithStmt replaces the Local or a portion of the document referred to by the Local with the Value and executes the contained block. If the Path is non-empty, the Value is upserted into the Local.
--     * Slot: id
--     * Slot: local Description: The local whose value, or part of it, is replaced.
--     * Slot: file Description: Index, in the plan's static files, of the policy file the statement comes from.
--     * Slot: col Description: Column where the statement's source text starts.
--     * Slot: row Description: Line where the statement's source text starts.
--     * Slot: end_col Description: Column where the statement's source text ends.
--     * Slot: end_row Description: Line where the statement's source text ends.
--     * Slot: block_id Description: The block the statement runs.
--     * Slot: value_id Description: The replacement value.
-- # Abstract Class: OpaOperand Description: Operand represents a value that a statement operates on. OPA writes it as its kind in `type` and the value in `value`.
--     * Slot: id
--     * Slot: OpaCallDynamicStmtBody_id Description: Autocreated FK slot
--     * Slot: OpaCallStmtBody_id Description: Autocreated FK slot
-- # Class: OpaBoolOperand Description: Bool represents a constant boolean.
--     * Slot: id
--     * Slot: type Description: The kind of operand.
--     * Slot: value Description: The operand's value.
-- # Class: OpaLocalOperand Description: A local variable, by its number.
--     * Slot: id
--     * Slot: type Description: The kind of operand.
--     * Slot: value Description: The operand's value.
-- # Class: OpaStringIndexOperand Description: StringIndex represents the index into the plan's list of constant strings of a constant string.
--     * Slot: id
--     * Slot: type Description: The kind of operand.
--     * Slot: value Description: The operand's value.
-- # Class: OpaCapabilities_future_keywords
--     * Slot: OpaCapabilities_id Description: Autocreated FK slot
--     * Slot: future_keywords Description: The keywords a policy may import from future.keywords.
-- # Class: OpaCapabilities_features
--     * Slot: OpaCapabilities_id Description: Autocreated FK slot
--     * Slot: features Description: The language features supported.
-- # Class: OpaCapabilities_allow_net
--     * Slot: OpaCapabilities_id Description: Autocreated FK slot
--     * Slot: allow_net Description: The hosts OPA may connect to, as host names or IP addresses. OPA reaches any host when the key is absent, and none when the list is empty.
-- # Class: OpaBuiltin_categories
--     * Slot: OpaBuiltin_id Description: Autocreated FK slot
--     * Slot: categories Description: The categories the function belongs to.
-- # Class: OpaBuiltinCategory_builtins
--     * Slot: OpaBuiltinCategory_name Description: Autocreated FK slot
--     * Slot: builtins Description: The names of the category's functions.
-- # Class: OpaBuiltinMetadata_available
--     * Slot: OpaBuiltinMetadata_id Description: Autocreated FK slot
--     * Slot: available Description: The OPA versions that have the function, and `edge`.
-- # Class: OpaAuthorizationInput_path
--     * Slot: OpaAuthorizationInput_id Description: Autocreated FK slot
--     * Slot: path Description: The request path, one segment per element.
-- # Class: OpaManifest_roots
--     * Slot: OpaManifest_id Description: Autocreated FK slot
--     * Slot: roots Description: The paths in the data tree the bundle owns. A bundle without the key owns the whole tree.
-- # Class: OpaFunc_params
--     * Slot: OpaFunc_id Description: Autocreated FK slot
--     * Slot: params Description: The locals that hold the parameters. The first two are the input and data documents.
-- # Class: OpaFunc_path
--     * Slot: OpaFunc_id Description: Autocreated FK slot
--     * Slot: path Description: Where the function sits in the data tree, when it has a path.
-- # Class: OpaCallDynamicStmtBody_args
--     * Slot: OpaCallDynamicStmtBody_id Description: Autocreated FK slot
--     * Slot: args Description: The locals passed as arguments.
-- # Class: OpaWithStmtBody_path
--     * Slot: OpaWithStmtBody_id Description: Autocreated FK slot
--     * Slot: path Description: The path within the local's value to replace, as indices of static strings. Empty replaces the whole value.

CREATE TABLE "OpaObject" (
	id INTEGER NOT NULL,
	"OpaAuthorizationInput_id" INTEGER,
	"OpaWasmResolver_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaAuthorizationInput_id") REFERENCES "OpaAuthorizationInput" (id),
	FOREIGN KEY("OpaWasmResolver_id") REFERENCES "OpaWasmResolver" (id)
);
CREATE INDEX "ix_OpaObject_id" ON "OpaObject" (id);

CREATE TABLE "OpaValue" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaValue_id" ON "OpaValue" (id);

CREATE TABLE "OpaType" (
	id INTEGER NOT NULL,
	name TEXT,
	description TEXT,
	"OpaAnyType_id" INTEGER,
	"OpaArrayType_id" INTEGER,
	"OpaFunctionType_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaAnyType_id") REFERENCES "OpaAnyType" (id),
	FOREIGN KEY("OpaArrayType_id") REFERENCES "OpaArrayType" (id),
	FOREIGN KEY("OpaFunctionType_id") REFERENCES "OpaFunctionType" (id)
);
CREATE INDEX "ix_OpaType_id" ON "OpaType" (id);

CREATE TABLE "OpaAnyType" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaAnyType_id" ON "OpaAnyType" (id);

CREATE TABLE "OpaArrayType" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	name TEXT,
	description TEXT,
	dynamic_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(dynamic_id) REFERENCES "OpaType" (id)
);
CREATE INDEX "ix_OpaArrayType_id" ON "OpaArrayType" (id);

CREATE TABLE "OpaBooleanType" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaBooleanType_id" ON "OpaBooleanType" (id);

CREATE TABLE "OpaFunctionType" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	name TEXT,
	description TEXT,
	result_id INTEGER,
	variadic_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(result_id) REFERENCES "OpaType" (id),
	FOREIGN KEY(variadic_id) REFERENCES "OpaType" (id)
);
CREATE INDEX "ix_OpaFunctionType_id" ON "OpaFunctionType" (id);

CREATE TABLE "OpaNullType" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaNullType_id" ON "OpaNullType" (id);

CREATE TABLE "OpaNumberType" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaNumberType_id" ON "OpaNumberType" (id);

CREATE TABLE "OpaStringType" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaStringType_id" ON "OpaStringType" (id);

CREATE TABLE "OpaCapabilities" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaCapabilities_id" ON "OpaCapabilities" (id);

CREATE TABLE "OpaBuiltinMetadataCatalog" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaBuiltinMetadataCatalog_id" ON "OpaBuiltinMetadataCatalog" (id);

CREATE TABLE "OpaBuiltinResult" (
	id INTEGER NOT NULL,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaBuiltinResult_id" ON "OpaBuiltinResult" (id);

CREATE TABLE "OpaVersionIndex" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaVersionIndex_id" ON "OpaVersionIndex" (id);

CREATE TABLE "OpaAuthorizationInput" (
	id INTEGER NOT NULL,
	identity TEXT NOT NULL,
	method TEXT NOT NULL,
	body_id INTEGER NOT NULL,
	params_id INTEGER NOT NULL,
	headers_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(body_id) REFERENCES "OpaObject" (id),
	FOREIGN KEY(params_id) REFERENCES "OpaObject" (id),
	FOREIGN KEY(headers_id) REFERENCES "OpaObject" (id)
);
CREATE INDEX "ix_OpaAuthorizationInput_id" ON "OpaAuthorizationInput" (id);

CREATE TABLE "OpaManifest" (
	id INTEGER NOT NULL,
	revision TEXT NOT NULL,
	rego_version INTEGER,
	metadata_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(metadata_id) REFERENCES "OpaObject" (id)
);
CREATE INDEX "ix_OpaManifest_id" ON "OpaManifest" (id);

CREATE TABLE "OpaWasmResolver" (
	id INTEGER NOT NULL,
	entrypoint TEXT,
	module TEXT,
	"OpaManifest_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaManifest_id") REFERENCES "OpaManifest" (id)
);
CREATE INDEX "ix_OpaWasmResolver_id" ON "OpaWasmResolver" (id);

CREATE TABLE "OpaStatic" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaStatic_id" ON "OpaStatic" (id);

CREATE TABLE "OpaPlans" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaPlans_id" ON "OpaPlans" (id);

CREATE TABLE "OpaFuncs" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaFuncs_id" ON "OpaFuncs" (id);

CREATE TABLE "OpaLocation" (
	id INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaLocation_id" ON "OpaLocation" (id);

CREATE TABLE "OpaStmtBody" (
	id INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaStmtBody_id" ON "OpaStmtBody" (id);

CREATE TABLE "OpaAssignIntStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	value INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaAssignIntStmtBody_id" ON "OpaAssignIntStmtBody" (id);

CREATE TABLE "OpaBlockStmtBody" (
	id INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaBlockStmtBody_id" ON "OpaBlockStmtBody" (id);

CREATE TABLE "OpaBreakStmtBody" (
	id INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaBreakStmtBody_id" ON "OpaBreakStmtBody" (id);

CREATE TABLE "OpaCallDynamicStmtBody" (
	id INTEGER NOT NULL,
	result INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaCallDynamicStmtBody_id" ON "OpaCallDynamicStmtBody" (id);

CREATE TABLE "OpaCallStmtBody" (
	id INTEGER NOT NULL,
	func TEXT NOT NULL,
	result INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaCallStmtBody_id" ON "OpaCallStmtBody" (id);

CREATE TABLE "OpaIsDefinedStmtBody" (
	id INTEGER NOT NULL,
	source INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaIsDefinedStmtBody_id" ON "OpaIsDefinedStmtBody" (id);

CREATE TABLE "OpaIsUndefinedStmtBody" (
	id INTEGER NOT NULL,
	source INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaIsUndefinedStmtBody_id" ON "OpaIsUndefinedStmtBody" (id);

CREATE TABLE "OpaMakeArrayStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	capacity INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaMakeArrayStmtBody_id" ON "OpaMakeArrayStmtBody" (id);

CREATE TABLE "OpaMakeNullStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaMakeNullStmtBody_id" ON "OpaMakeNullStmtBody" (id);

CREATE TABLE "OpaMakeNumberIntStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	value INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaMakeNumberIntStmtBody_id" ON "OpaMakeNumberIntStmtBody" (id);

CREATE TABLE "OpaMakeNumberRefStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	"Index" INTEGER,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaMakeNumberRefStmtBody_id" ON "OpaMakeNumberRefStmtBody" (id);

CREATE TABLE "OpaMakeObjectStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaMakeObjectStmtBody_id" ON "OpaMakeObjectStmtBody" (id);

CREATE TABLE "OpaMakeSetStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaMakeSetStmtBody_id" ON "OpaMakeSetStmtBody" (id);

CREATE TABLE "OpaNopStmtBody" (
	id INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaNopStmtBody_id" ON "OpaNopStmtBody" (id);

CREATE TABLE "OpaObjectMergeStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	a INTEGER NOT NULL,
	b INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaObjectMergeStmtBody_id" ON "OpaObjectMergeStmtBody" (id);

CREATE TABLE "OpaResetLocalStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaResetLocalStmtBody_id" ON "OpaResetLocalStmtBody" (id);

CREATE TABLE "OpaResultSetAddStmtBody" (
	id INTEGER NOT NULL,
	value INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaResultSetAddStmtBody_id" ON "OpaResultSetAddStmtBody" (id);

CREATE TABLE "OpaReturnLocalStmtBody" (
	id INTEGER NOT NULL,
	source INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaReturnLocalStmtBody_id" ON "OpaReturnLocalStmtBody" (id);

CREATE TABLE "OpaBoolOperand" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	value BOOLEAN NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaBoolOperand_id" ON "OpaBoolOperand" (id);

CREATE TABLE "OpaLocalOperand" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	value INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaLocalOperand_id" ON "OpaLocalOperand" (id);

CREATE TABLE "OpaStringIndexOperand" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	value INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OpaStringIndexOperand_id" ON "OpaStringIndexOperand" (id);

CREATE TABLE "OpaSetType" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	name TEXT,
	description TEXT,
	of_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(of_id) REFERENCES "OpaType" (id)
);
CREATE INDEX "ix_OpaSetType_id" ON "OpaSetType" (id);

CREATE TABLE "OpaDynamicProperty" (
	id INTEGER NOT NULL,
	key_id INTEGER NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(key_id) REFERENCES "OpaType" (id),
	FOREIGN KEY(value_id) REFERENCES "OpaType" (id)
);
CREATE INDEX "ix_OpaDynamicProperty_id" ON "OpaDynamicProperty" (id);

CREATE TABLE "OpaBuiltin" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	infix TEXT,
	relation BOOLEAN,
	deprecated BOOLEAN,
	nondeterministic BOOLEAN,
	"OpaCapabilities_id" INTEGER,
	decl_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaCapabilities_id") REFERENCES "OpaCapabilities" (id),
	FOREIGN KEY(decl_id) REFERENCES "OpaFunctionType" (id)
);
CREATE INDEX "ix_OpaBuiltin_id" ON "OpaBuiltin" (id);

CREATE TABLE "OpaWasmAbiVersion" (
	id INTEGER NOT NULL,
	version INTEGER NOT NULL,
	minor_version INTEGER NOT NULL,
	"OpaCapabilities_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaCapabilities_id") REFERENCES "OpaCapabilities" (id)
);
CREATE INDEX "ix_OpaWasmAbiVersion_id" ON "OpaWasmAbiVersion" (id);

CREATE TABLE "OpaBuiltinCategory" (
	name TEXT NOT NULL,
	"OpaBuiltinMetadataCatalog_id" INTEGER,
	PRIMARY KEY (name, "OpaBuiltinMetadataCatalog_id"),
	UNIQUE ("OpaBuiltinMetadataCatalog_id", name),
	FOREIGN KEY("OpaBuiltinMetadataCatalog_id") REFERENCES "OpaBuiltinMetadataCatalog" (id)
);
CREATE INDEX "OpaBuiltinCategory_OpaBuiltinMetadataCatalog_id_name_idx" ON "OpaBuiltinCategory" ("OpaBuiltinMetadataCatalog_id", name);
CREATE INDEX "ix_OpaBuiltinCategory_OpaBuiltinMetadataCatalog_id" ON "OpaBuiltinCategory" ("OpaBuiltinMetadataCatalog_id");
CREATE INDEX "ix_OpaBuiltinCategory_name" ON "OpaBuiltinCategory" (name);

CREATE TABLE "OpaImplementation" (
	uid INTEGER NOT NULL,
	version TEXT NOT NULL,
	id TEXT NOT NULL,
	label TEXT NOT NULL,
	repo TEXT NOT NULL,
	"OpaBuiltinMetadataCatalog_id" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("OpaBuiltinMetadataCatalog_id") REFERENCES "OpaBuiltinMetadataCatalog" (id)
);
CREATE INDEX "ix_OpaImplementation_uid" ON "OpaImplementation" (uid);

CREATE TABLE "OpaBuiltinMetadata" (
	id INTEGER NOT NULL,
	description TEXT,
	introduced TEXT NOT NULL,
	wasm BOOLEAN NOT NULL,
	infix TEXT,
	relation BOOLEAN,
	deprecated BOOLEAN,
	result_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(result_id) REFERENCES "OpaBuiltinResult" (id)
);
CREATE INDEX "ix_OpaBuiltinMetadata_id" ON "OpaBuiltinMetadata" (id);

CREATE TABLE "OpaVersionEntry" (
	name TEXT NOT NULL,
	"Major" INTEGER NOT NULL,
	"Minor" INTEGER NOT NULL,
	"Patch" INTEGER NOT NULL,
	"PreRelease" TEXT,
	"OpaVersionIndex_id" INTEGER,
	PRIMARY KEY (name, "Major", "Minor", "Patch", "PreRelease", "OpaVersionIndex_id"),
	UNIQUE ("OpaVersionIndex_id", name),
	FOREIGN KEY("OpaVersionIndex_id") REFERENCES "OpaVersionIndex" (id)
);
CREATE INDEX "OpaVersionEntry_OpaVersionIndex_id_name_idx" ON "OpaVersionEntry" ("OpaVersionIndex_id", name);
CREATE INDEX "ix_OpaVersionEntry_Major" ON "OpaVersionEntry" ("Major");
CREATE INDEX "ix_OpaVersionEntry_Minor" ON "OpaVersionEntry" ("Minor");
CREATE INDEX "ix_OpaVersionEntry_OpaVersionIndex_id" ON "OpaVersionEntry" ("OpaVersionIndex_id");
CREATE INDEX "ix_OpaVersionEntry_Patch" ON "OpaVersionEntry" ("Patch");
CREATE INDEX "ix_OpaVersionEntry_PreRelease" ON "OpaVersionEntry" ("PreRelease");
CREATE INDEX "ix_OpaVersionEntry_name" ON "OpaVersionEntry" (name);

CREATE TABLE "OpaFileRegoVersion" (
	version INTEGER NOT NULL,
	path TEXT NOT NULL,
	"OpaManifest_id" INTEGER,
	PRIMARY KEY (version, path, "OpaManifest_id"),
	FOREIGN KEY("OpaManifest_id") REFERENCES "OpaManifest" (id)
);
CREATE INDEX "ix_OpaFileRegoVersion_path" ON "OpaFileRegoVersion" (path);
CREATE INDEX "ix_OpaFileRegoVersion_OpaManifest_id" ON "OpaFileRegoVersion" ("OpaManifest_id");
CREATE INDEX "ix_OpaFileRegoVersion_version" ON "OpaFileRegoVersion" (version);

CREATE TABLE "OpaPolicy" (
	id INTEGER NOT NULL,
	funcs_id INTEGER,
	plans_id INTEGER,
	static_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(funcs_id) REFERENCES "OpaFuncs" (id),
	FOREIGN KEY(plans_id) REFERENCES "OpaPlans" (id),
	FOREIGN KEY(static_id) REFERENCES "OpaStatic" (id)
);
CREATE INDEX "ix_OpaPolicy_id" ON "OpaPolicy" (id);

CREATE TABLE "OpaStringConst" (
	id INTEGER NOT NULL,
	value TEXT NOT NULL,
	"OpaStatic_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaStatic_id") REFERENCES "OpaStatic" (id)
);
CREATE INDEX "ix_OpaStringConst_id" ON "OpaStringConst" (id);

CREATE TABLE "OpaBuiltinFunc" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"OpaStatic_id" INTEGER,
	decl_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaStatic_id") REFERENCES "OpaStatic" (id),
	FOREIGN KEY(decl_id) REFERENCES "OpaFunctionType" (id)
);
CREATE INDEX "ix_OpaBuiltinFunc_id" ON "OpaBuiltinFunc" (id);

CREATE TABLE "OpaPlan" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"OpaPlans_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaPlans_id") REFERENCES "OpaPlans" (id)
);
CREATE INDEX "ix_OpaPlan_id" ON "OpaPlan" (id);

CREATE TABLE "OpaFunc" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	return INTEGER NOT NULL,
	"OpaFuncs_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaFuncs_id") REFERENCES "OpaFuncs" (id)
);
CREATE INDEX "ix_OpaFunc_id" ON "OpaFunc" (id);

CREATE TABLE "OpaAssignIntStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaAssignIntStmtBody" (id)
);
CREATE INDEX "ix_OpaAssignIntStmt_id" ON "OpaAssignIntStmt" (id);

CREATE TABLE "OpaBlockStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaBlockStmtBody" (id)
);
CREATE INDEX "ix_OpaBlockStmt_id" ON "OpaBlockStmt" (id);

CREATE TABLE "OpaBreakStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaBreakStmtBody" (id)
);
CREATE INDEX "ix_OpaBreakStmt_id" ON "OpaBreakStmt" (id);

CREATE TABLE "OpaCallDynamicStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaCallDynamicStmtBody" (id)
);
CREATE INDEX "ix_OpaCallDynamicStmt_id" ON "OpaCallDynamicStmt" (id);

CREATE TABLE "OpaCallStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaCallStmtBody" (id)
);
CREATE INDEX "ix_OpaCallStmt_id" ON "OpaCallStmt" (id);

CREATE TABLE "OpaIsDefinedStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaIsDefinedStmtBody" (id)
);
CREATE INDEX "ix_OpaIsDefinedStmt_id" ON "OpaIsDefinedStmt" (id);

CREATE TABLE "OpaIsUndefinedStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaIsUndefinedStmtBody" (id)
);
CREATE INDEX "ix_OpaIsUndefinedStmt_id" ON "OpaIsUndefinedStmt" (id);

CREATE TABLE "OpaMakeArrayStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaMakeArrayStmtBody" (id)
);
CREATE INDEX "ix_OpaMakeArrayStmt_id" ON "OpaMakeArrayStmt" (id);

CREATE TABLE "OpaMakeNullStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaMakeNullStmtBody" (id)
);
CREATE INDEX "ix_OpaMakeNullStmt_id" ON "OpaMakeNullStmt" (id);

CREATE TABLE "OpaMakeNumberIntStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaMakeNumberIntStmtBody" (id)
);
CREATE INDEX "ix_OpaMakeNumberIntStmt_id" ON "OpaMakeNumberIntStmt" (id);

CREATE TABLE "OpaMakeNumberRefStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaMakeNumberRefStmtBody" (id)
);
CREATE INDEX "ix_OpaMakeNumberRefStmt_id" ON "OpaMakeNumberRefStmt" (id);

CREATE TABLE "OpaMakeObjectStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaMakeObjectStmtBody" (id)
);
CREATE INDEX "ix_OpaMakeObjectStmt_id" ON "OpaMakeObjectStmt" (id);

CREATE TABLE "OpaMakeSetStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaMakeSetStmtBody" (id)
);
CREATE INDEX "ix_OpaMakeSetStmt_id" ON "OpaMakeSetStmt" (id);

CREATE TABLE "OpaNopStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaNopStmtBody" (id)
);
CREATE INDEX "ix_OpaNopStmt_id" ON "OpaNopStmt" (id);

CREATE TABLE "OpaObjectMergeStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaObjectMergeStmtBody" (id)
);
CREATE INDEX "ix_OpaObjectMergeStmt_id" ON "OpaObjectMergeStmt" (id);

CREATE TABLE "OpaResetLocalStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaResetLocalStmtBody" (id)
);
CREATE INDEX "ix_OpaResetLocalStmt_id" ON "OpaResetLocalStmt" (id);

CREATE TABLE "OpaResultSetAddStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaResultSetAddStmtBody" (id)
);
CREATE INDEX "ix_OpaResultSetAddStmt_id" ON "OpaResultSetAddStmt" (id);

CREATE TABLE "OpaReturnLocalStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaReturnLocalStmtBody" (id)
);
CREATE INDEX "ix_OpaReturnLocalStmt_id" ON "OpaReturnLocalStmt" (id);

CREATE TABLE "OpaOperand" (
	id INTEGER NOT NULL,
	"OpaCallDynamicStmtBody_id" INTEGER,
	"OpaCallStmtBody_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaCallDynamicStmtBody_id") REFERENCES "OpaCallDynamicStmtBody" (id),
	FOREIGN KEY("OpaCallStmtBody_id") REFERENCES "OpaCallStmtBody" (id)
);
CREATE INDEX "ix_OpaOperand_id" ON "OpaOperand" (id);

CREATE TABLE "OpaCapabilities_future_keywords" (
	"OpaCapabilities_id" INTEGER,
	future_keywords VARCHAR(8),
	PRIMARY KEY ("OpaCapabilities_id", future_keywords),
	FOREIGN KEY("OpaCapabilities_id") REFERENCES "OpaCapabilities" (id)
);
CREATE INDEX "ix_OpaCapabilities_future_keywords_OpaCapabilities_id" ON "OpaCapabilities_future_keywords" ("OpaCapabilities_id");
CREATE INDEX "ix_OpaCapabilities_future_keywords_future_keywords" ON "OpaCapabilities_future_keywords" (future_keywords);

CREATE TABLE "OpaCapabilities_features" (
	"OpaCapabilities_id" INTEGER,
	features VARCHAR(29),
	PRIMARY KEY ("OpaCapabilities_id", features),
	FOREIGN KEY("OpaCapabilities_id") REFERENCES "OpaCapabilities" (id)
);
CREATE INDEX "ix_OpaCapabilities_features_OpaCapabilities_id" ON "OpaCapabilities_features" ("OpaCapabilities_id");
CREATE INDEX "ix_OpaCapabilities_features_features" ON "OpaCapabilities_features" (features);

CREATE TABLE "OpaCapabilities_allow_net" (
	"OpaCapabilities_id" INTEGER,
	allow_net TEXT,
	PRIMARY KEY ("OpaCapabilities_id", allow_net),
	FOREIGN KEY("OpaCapabilities_id") REFERENCES "OpaCapabilities" (id)
);
CREATE INDEX "ix_OpaCapabilities_allow_net_allow_net" ON "OpaCapabilities_allow_net" (allow_net);
CREATE INDEX "ix_OpaCapabilities_allow_net_OpaCapabilities_id" ON "OpaCapabilities_allow_net" ("OpaCapabilities_id");

CREATE TABLE "OpaAuthorizationInput_path" (
	"OpaAuthorizationInput_id" INTEGER,
	path TEXT NOT NULL,
	PRIMARY KEY ("OpaAuthorizationInput_id", path),
	FOREIGN KEY("OpaAuthorizationInput_id") REFERENCES "OpaAuthorizationInput" (id)
);
CREATE INDEX "ix_OpaAuthorizationInput_path_OpaAuthorizationInput_id" ON "OpaAuthorizationInput_path" ("OpaAuthorizationInput_id");
CREATE INDEX "ix_OpaAuthorizationInput_path_path" ON "OpaAuthorizationInput_path" (path);

CREATE TABLE "OpaManifest_roots" (
	"OpaManifest_id" INTEGER,
	roots TEXT,
	PRIMARY KEY ("OpaManifest_id", roots),
	FOREIGN KEY("OpaManifest_id") REFERENCES "OpaManifest" (id)
);
CREATE INDEX "ix_OpaManifest_roots_roots" ON "OpaManifest_roots" (roots);
CREATE INDEX "ix_OpaManifest_roots_OpaManifest_id" ON "OpaManifest_roots" ("OpaManifest_id");

CREATE TABLE "OpaCallDynamicStmtBody_args" (
	"OpaCallDynamicStmtBody_id" INTEGER,
	args INTEGER,
	PRIMARY KEY ("OpaCallDynamicStmtBody_id", args),
	FOREIGN KEY("OpaCallDynamicStmtBody_id") REFERENCES "OpaCallDynamicStmtBody" (id)
);
CREATE INDEX "ix_OpaCallDynamicStmtBody_args_OpaCallDynamicStmtBody_id" ON "OpaCallDynamicStmtBody_args" ("OpaCallDynamicStmtBody_id");
CREATE INDEX "ix_OpaCallDynamicStmtBody_args_args" ON "OpaCallDynamicStmtBody_args" (args);

CREATE TABLE "OpaObjectType" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	name TEXT,
	description TEXT,
	dynamic_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(dynamic_id) REFERENCES "OpaDynamicProperty" (id)
);
CREATE INDEX "ix_OpaObjectType_id" ON "OpaObjectType" (id);

CREATE TABLE "OpaBuiltinArgument" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"OpaBuiltinMetadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaBuiltinMetadata_id") REFERENCES "OpaBuiltinMetadata" (id)
);
CREATE INDEX "ix_OpaBuiltinArgument_id" ON "OpaBuiltinArgument" (id);

CREATE TABLE "OpaImplementationSupport" (
	version TEXT NOT NULL,
	implementation TEXT NOT NULL,
	"OpaBuiltinMetadata_id" INTEGER,
	PRIMARY KEY (version, implementation, "OpaBuiltinMetadata_id"),
	UNIQUE ("OpaBuiltinMetadata_id", implementation),
	FOREIGN KEY("OpaBuiltinMetadata_id") REFERENCES "OpaBuiltinMetadata" (id)
);
CREATE INDEX "ix_OpaImplementationSupport_OpaBuiltinMetadata_id" ON "OpaImplementationSupport" ("OpaBuiltinMetadata_id");
CREATE INDEX "ix_OpaImplementationSupport_version" ON "OpaImplementationSupport" (version);
CREATE INDEX "ix_OpaImplementationSupport_implementation" ON "OpaImplementationSupport" (implementation);
CREATE INDEX "OpaImplementationSupport_OpaBuiltinMetadata_id_implementation_idx" ON "OpaImplementationSupport" ("OpaBuiltinMetadata_id", implementation);

CREATE TABLE "OpaBlock" (
	id INTEGER NOT NULL,
	"OpaPlan_id" INTEGER,
	"OpaFunc_id" INTEGER,
	"OpaBlockStmtBody_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaPlan_id") REFERENCES "OpaPlan" (id),
	FOREIGN KEY("OpaFunc_id") REFERENCES "OpaFunc" (id),
	FOREIGN KEY("OpaBlockStmtBody_id") REFERENCES "OpaBlockStmtBody" (id)
);
CREATE INDEX "ix_OpaBlock_id" ON "OpaBlock" (id);

CREATE TABLE "OpaUnplannedRule" (
	id INTEGER NOT NULL,
	path TEXT NOT NULL,
	"OpaPolicy_id" INTEGER,
	location_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaPolicy_id") REFERENCES "OpaPolicy" (id),
	FOREIGN KEY(location_id) REFERENCES "OpaLocation" (id)
);
CREATE INDEX "ix_OpaUnplannedRule_id" ON "OpaUnplannedRule" (id);

CREATE TABLE "OpaArrayAppendStmtBody" (
	id INTEGER NOT NULL,
	array INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(value_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaArrayAppendStmtBody_id" ON "OpaArrayAppendStmtBody" (id);

CREATE TABLE "OpaAssignVarOnceStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaAssignVarOnceStmtBody_id" ON "OpaAssignVarOnceStmtBody" (id);

CREATE TABLE "OpaAssignVarStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaAssignVarStmtBody_id" ON "OpaAssignVarStmtBody" (id);

CREATE TABLE "OpaDotStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	key_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "OpaOperand" (id),
	FOREIGN KEY(key_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaDotStmtBody_id" ON "OpaDotStmtBody" (id);

CREATE TABLE "OpaEqualStmtBody" (
	id INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	a_id INTEGER NOT NULL,
	b_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(a_id) REFERENCES "OpaOperand" (id),
	FOREIGN KEY(b_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaEqualStmtBody_id" ON "OpaEqualStmtBody" (id);

CREATE TABLE "OpaIsArrayStmtBody" (
	id INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaIsArrayStmtBody_id" ON "OpaIsArrayStmtBody" (id);

CREATE TABLE "OpaIsObjectStmtBody" (
	id INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaIsObjectStmtBody_id" ON "OpaIsObjectStmtBody" (id);

CREATE TABLE "OpaIsSetStmtBody" (
	id INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaIsSetStmtBody_id" ON "OpaIsSetStmtBody" (id);

CREATE TABLE "OpaLenStmtBody" (
	id INTEGER NOT NULL,
	target INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaLenStmtBody_id" ON "OpaLenStmtBody" (id);

CREATE TABLE "OpaNotEqualStmtBody" (
	id INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	a_id INTEGER NOT NULL,
	b_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(a_id) REFERENCES "OpaOperand" (id),
	FOREIGN KEY(b_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaNotEqualStmtBody_id" ON "OpaNotEqualStmtBody" (id);

CREATE TABLE "OpaObjectInsertOnceStmtBody" (
	id INTEGER NOT NULL,
	object INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	key_id INTEGER NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(key_id) REFERENCES "OpaOperand" (id),
	FOREIGN KEY(value_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaObjectInsertOnceStmtBody_id" ON "OpaObjectInsertOnceStmtBody" (id);

CREATE TABLE "OpaObjectInsertStmtBody" (
	id INTEGER NOT NULL,
	object INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	key_id INTEGER NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(key_id) REFERENCES "OpaOperand" (id),
	FOREIGN KEY(value_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaObjectInsertStmtBody_id" ON "OpaObjectInsertStmtBody" (id);

CREATE TABLE "OpaSetAddStmtBody" (
	id INTEGER NOT NULL,
	"set" INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(value_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaSetAddStmtBody_id" ON "OpaSetAddStmtBody" (id);

CREATE TABLE "OpaBuiltin_categories" (
	"OpaBuiltin_id" INTEGER,
	categories TEXT,
	PRIMARY KEY ("OpaBuiltin_id", categories),
	FOREIGN KEY("OpaBuiltin_id") REFERENCES "OpaBuiltin" (id)
);
CREATE INDEX "ix_OpaBuiltin_categories_OpaBuiltin_id" ON "OpaBuiltin_categories" ("OpaBuiltin_id");
CREATE INDEX "ix_OpaBuiltin_categories_categories" ON "OpaBuiltin_categories" (categories);

CREATE TABLE "OpaBuiltinCategory_builtins" (
	"OpaBuiltinCategory_name" TEXT,
	builtins TEXT NOT NULL,
	PRIMARY KEY ("OpaBuiltinCategory_name", builtins),
	FOREIGN KEY("OpaBuiltinCategory_name") REFERENCES "OpaBuiltinCategory" (name)
);
CREATE INDEX "ix_OpaBuiltinCategory_builtins_OpaBuiltinCategory_name" ON "OpaBuiltinCategory_builtins" ("OpaBuiltinCategory_name");
CREATE INDEX "ix_OpaBuiltinCategory_builtins_builtins" ON "OpaBuiltinCategory_builtins" (builtins);

CREATE TABLE "OpaBuiltinMetadata_available" (
	"OpaBuiltinMetadata_id" INTEGER,
	available TEXT NOT NULL,
	PRIMARY KEY ("OpaBuiltinMetadata_id", available),
	FOREIGN KEY("OpaBuiltinMetadata_id") REFERENCES "OpaBuiltinMetadata" (id)
);
CREATE INDEX "ix_OpaBuiltinMetadata_available_OpaBuiltinMetadata_id" ON "OpaBuiltinMetadata_available" ("OpaBuiltinMetadata_id");
CREATE INDEX "ix_OpaBuiltinMetadata_available_available" ON "OpaBuiltinMetadata_available" (available);

CREATE TABLE "OpaFunc_params" (
	"OpaFunc_id" INTEGER,
	params INTEGER,
	PRIMARY KEY ("OpaFunc_id", params),
	FOREIGN KEY("OpaFunc_id") REFERENCES "OpaFunc" (id)
);
CREATE INDEX "ix_OpaFunc_params_OpaFunc_id" ON "OpaFunc_params" ("OpaFunc_id");
CREATE INDEX "ix_OpaFunc_params_params" ON "OpaFunc_params" (params);

CREATE TABLE "OpaFunc_path" (
	"OpaFunc_id" INTEGER,
	path TEXT,
	PRIMARY KEY ("OpaFunc_id", path),
	FOREIGN KEY("OpaFunc_id") REFERENCES "OpaFunc" (id)
);
CREATE INDEX "ix_OpaFunc_path_OpaFunc_id" ON "OpaFunc_path" ("OpaFunc_id");
CREATE INDEX "ix_OpaFunc_path_path" ON "OpaFunc_path" (path);

CREATE TABLE "OpaStaticProperty" (
	id INTEGER NOT NULL,
	"OpaObjectType_id" INTEGER,
	key_id INTEGER NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaObjectType_id") REFERENCES "OpaObjectType" (id),
	FOREIGN KEY(key_id) REFERENCES "OpaValue" (id),
	FOREIGN KEY(value_id) REFERENCES "OpaType" (id)
);
CREATE INDEX "ix_OpaStaticProperty_id" ON "OpaStaticProperty" (id);

CREATE TABLE "OpaStmt" (
	id INTEGER NOT NULL,
	"OpaBlock_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OpaBlock_id") REFERENCES "OpaBlock" (id)
);
CREATE INDEX "ix_OpaStmt_id" ON "OpaStmt" (id);

CREATE TABLE "OpaArrayAppendStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaArrayAppendStmtBody" (id)
);
CREATE INDEX "ix_OpaArrayAppendStmt_id" ON "OpaArrayAppendStmt" (id);

CREATE TABLE "OpaAssignVarOnceStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaAssignVarOnceStmtBody" (id)
);
CREATE INDEX "ix_OpaAssignVarOnceStmt_id" ON "OpaAssignVarOnceStmt" (id);

CREATE TABLE "OpaAssignVarStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaAssignVarStmtBody" (id)
);
CREATE INDEX "ix_OpaAssignVarStmt_id" ON "OpaAssignVarStmt" (id);

CREATE TABLE "OpaDotStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaDotStmtBody" (id)
);
CREATE INDEX "ix_OpaDotStmt_id" ON "OpaDotStmt" (id);

CREATE TABLE "OpaEqualStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaEqualStmtBody" (id)
);
CREATE INDEX "ix_OpaEqualStmt_id" ON "OpaEqualStmt" (id);

CREATE TABLE "OpaIsArrayStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaIsArrayStmtBody" (id)
);
CREATE INDEX "ix_OpaIsArrayStmt_id" ON "OpaIsArrayStmt" (id);

CREATE TABLE "OpaIsObjectStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaIsObjectStmtBody" (id)
);
CREATE INDEX "ix_OpaIsObjectStmt_id" ON "OpaIsObjectStmt" (id);

CREATE TABLE "OpaIsSetStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaIsSetStmtBody" (id)
);
CREATE INDEX "ix_OpaIsSetStmt_id" ON "OpaIsSetStmt" (id);

CREATE TABLE "OpaLenStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaLenStmtBody" (id)
);
CREATE INDEX "ix_OpaLenStmt_id" ON "OpaLenStmt" (id);

CREATE TABLE "OpaNotEqualStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaNotEqualStmtBody" (id)
);
CREATE INDEX "ix_OpaNotEqualStmt_id" ON "OpaNotEqualStmt" (id);

CREATE TABLE "OpaNotStmtBody" (
	id INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	block_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(block_id) REFERENCES "OpaBlock" (id)
);
CREATE INDEX "ix_OpaNotStmtBody_id" ON "OpaNotStmtBody" (id);

CREATE TABLE "OpaObjectInsertOnceStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaObjectInsertOnceStmtBody" (id)
);
CREATE INDEX "ix_OpaObjectInsertOnceStmt_id" ON "OpaObjectInsertOnceStmt" (id);

CREATE TABLE "OpaObjectInsertStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaObjectInsertStmtBody" (id)
);
CREATE INDEX "ix_OpaObjectInsertStmt_id" ON "OpaObjectInsertStmt" (id);

CREATE TABLE "OpaScanStmtBody" (
	id INTEGER NOT NULL,
	source INTEGER NOT NULL,
	"key" INTEGER NOT NULL,
	value INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	block_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(block_id) REFERENCES "OpaBlock" (id)
);
CREATE INDEX "ix_OpaScanStmtBody_id" ON "OpaScanStmtBody" (id);

CREATE TABLE "OpaSetAddStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaSetAddStmtBody" (id)
);
CREATE INDEX "ix_OpaSetAddStmt_id" ON "OpaSetAddStmt" (id);

CREATE TABLE "OpaWithStmtBody" (
	id INTEGER NOT NULL,
	local INTEGER NOT NULL,
	file INTEGER NOT NULL,
	col INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	end_col INTEGER NOT NULL,
	end_row INTEGER NOT NULL,
	block_id INTEGER,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(block_id) REFERENCES "OpaBlock" (id),
	FOREIGN KEY(value_id) REFERENCES "OpaOperand" (id)
);
CREATE INDEX "ix_OpaWithStmtBody_id" ON "OpaWithStmtBody" (id);

CREATE TABLE "OpaNotStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaNotStmtBody" (id)
);
CREATE INDEX "ix_OpaNotStmt_id" ON "OpaNotStmt" (id);

CREATE TABLE "OpaScanStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaScanStmtBody" (id)
);
CREATE INDEX "ix_OpaScanStmt_id" ON "OpaScanStmt" (id);

CREATE TABLE "OpaWithStmt" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(stmt_id) REFERENCES "OpaWithStmtBody" (id)
);
CREATE INDEX "ix_OpaWithStmt_id" ON "OpaWithStmt" (id);

CREATE TABLE "OpaWithStmtBody_path" (
	"OpaWithStmtBody_id" INTEGER,
	path INTEGER,
	PRIMARY KEY ("OpaWithStmtBody_id", path),
	FOREIGN KEY("OpaWithStmtBody_id") REFERENCES "OpaWithStmtBody" (id)
);
CREATE INDEX "ix_OpaWithStmtBody_path_OpaWithStmtBody_id" ON "OpaWithStmtBody_path" ("OpaWithStmtBody_id");
CREATE INDEX "ix_OpaWithStmtBody_path_path" ON "OpaWithStmtBody_path" (path);
