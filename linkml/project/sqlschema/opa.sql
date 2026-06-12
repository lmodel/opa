-- # Class: Any Description: Free-form value placeholder (scalar, list, or object). Used to model source slots whose representation is heterogeneous or intentionally open (e.g. ``TypeDecl.key``, ``AuthorizationInput.body``).
--     * Slot: id
--     * Slot: AuthorizationInput_id Description: Autocreated FK slot
-- # Class: Capabilities Description: Top-level capabilities document published by an OPA build. Lists every built-in function the runtime supports along with Wasm ABI compatibility, future keywords and feature flags.
--     * Slot: id
-- # Class: Builtin Description: A Rego built-in function exposed by the OPA runtime.
--     * Slot: name Description: Built-in identifier (dotted path, e.g. ``array.concat``).
--     * Slot: infix Description: Optional infix operator symbol (e.g. ``&``, ``==``).
--     * Slot: deprecated Description: True when the built-in is scheduled for removal.
--     * Slot: nondeterministic Description: True when invocations may produce different results across runs.
--     * Slot: relation Description: True when the built-in is a relation (binds output variables).
--     * Slot: Capabilities_id Description: Autocreated FK slot
--     * Slot: decl_id Description: Type declaration: signature plus return type.
-- # Class: BuiltinDecl Description: Type declaration of a built-in: function signature and return type.
--     * Slot: id
--     * Slot: type Description: Always the literal string ``function``.
--     * Slot: result_id Description: Type of the result returned by the built-in.
--     * Slot: variadic_id Description: When present, indicates the built-in accepts any number of trailing arguments of this type.
-- # Class: TypeDecl Description: Recursive type expression used throughout Capabilities declarations.All slots are optional because TypeDecl doubles as the structural envelopefor the various heterogeneous shapes the source JSON uses:* ``string|number|boolean|null|function`` -- atomic; only ``type`` is set.* ``any`` -- ``of`` is a list of alternative TypeDecls.* ``set`` -- ``of`` holds the (single) element TypeDecl.* ``array`` -- ``dynamic`` is the homogeneous element TypeDecl, or  ``static`` is an ordered list describing a fixed-length tuple.* ``object`` -- ``static`` lists named property pairs (TypeDecls with  ``key`` and ``value`` populated); ``dynamic`` is a TypeDecl whose  ``key``/``value`` describe additional property typing.* Inside an ``object``'s ``dynamic`` value, the TypeDecl has only  ``key`` and ``value`` populated -- ``type`` is absent.
--     * Slot: id
--     * Slot: type Description: Discriminator: the kind of value this TypeDecl describes.
--     * Slot: BuiltinDecl_id Description: Autocreated FK slot
--     * Slot: TypeDecl_id Description: Autocreated FK slot
--     * Slot: dynamic_id Description: For ``array`` types this is the element TypeDecl; for ``object`` types it is a TypeDecl with ``key`` and ``value`` populated.
--     * Slot: key_id Description: Key of an object's dynamic-property mapping or static-property entry. When the parent TypeDecl is an object's ``dynamic`` slot, this is itself a TypeDecl (e.g. ``{type: string}``); when the parent is an object's ``static`` entry, it is a string literal naming the property.
--     * Slot: value_id Description: Value type of an object's dynamic property mapping or static property entry. Always a TypeDecl.
-- # Class: WasmABIVersion Description: A supported Wasm ABI version pair.
--     * Slot: id
--     * Slot: version Description: Major ABI version.
--     * Slot: minor_version Description: Minor ABI version.
--     * Slot: Capabilities_id Description: Autocreated FK slot
-- # Class: BuiltinMetadataCatalog Description: Wrapper class for the contents of ``builtin_metadata.json``. The source document is a flat map keyed by built-in name plus a ``_categories`` map; the generator script reshapes it so ``categories`` and ``builtins`` are explicit, inlined-as-dict slots on this wrapper.
--     * Slot: id
-- # Class: BuiltinCategoryGroup Description: Membership of built-ins in a documentation category.
--     * Slot: name Description: Category identifier. Plain string (not the BuiltinCategory enum) so gen-python's identifier-slot machinery does not forward-reference the enum class.
--     * Slot: category Description: Same value as ``name``, typed against the BuiltinCategory enum for downstream consumers.
--     * Slot: BuiltinMetadataCatalog_id Description: Autocreated FK slot
-- # Class: BuiltinMetadata Description: Human-readable metadata for a single Rego built-in function.
--     * Slot: name Description: Built-in identifier (dotted path).
--     * Slot: description Description: Markdown description of the built-in.
--     * Slot: introduced Description: Earliest OPA release tag in which the built-in was available.
--     * Slot: wasm Description: True if the built-in is implemented for the Wasm target.
--     * Slot: infix Description: Optional infix operator symbol.
--     * Slot: deprecated Description: True when the built-in is scheduled for removal.
--     * Slot: relation Description: True when the built-in is a relation.
--     * Slot: BuiltinMetadataCatalog_id Description: Autocreated FK slot
--     * Slot: result_id Description: Descriptor for the value returned by the built-in.
-- # Class: BuiltinArg Description: Documentation for one positional argument of a built-in.
--     * Slot: id
--     * Slot: name Description: Argument identifier as documented (often single-letter).
--     * Slot: description Description: Markdown description of the argument.
--     * Slot: type Description: Compact textual form of the argument type (e.g. ``number``, ``set[any]``, ``any<string, number>``).
--     * Slot: BuiltinMetadata_name Description: Autocreated FK slot
-- # Class: BuiltinResult Description: Documentation for the value returned by a built-in.
--     * Slot: id
--     * Slot: name Description: Result identifier as documented.
--     * Slot: description Description: Markdown description of the result.
--     * Slot: type Description: Compact textual form of the result type.
-- # Class: VersionIndex Description: Mapping from language-element names to the OPA semantic version that first introduced them. Grouped into built-ins, future-keywords, and features.
--     * Slot: id
-- # Class: ElementVersion Description: Semantic version triple identifying when an element was introduced.
--     * Slot: name Description: Name of the language element (built-in, keyword, or feature).
--     * Slot: major Description: Major version number (source field ``Major``).
--     * Slot: minor Description: Minor version number (source field ``Minor``).
--     * Slot: patch Description: Patch version number (source field ``Patch``).
--     * Slot: VersionIndex_id Description: Autocreated FK slot
-- # Class: AuthorizationInput Description: Input document the example HTTP API Authorization policy receives. Mirrors the OPA-provided JSON Schema at ``v1/schemas/authorizationPolicy.json``.
--     * Slot: id
--     * Slot: identity Description: Caller identity, typically extracted from an authentication token.
--     * Slot: method Description: HTTP method of the request being authorized (e.g. ``GET``, ``POST``).
--     * Slot: params_id Description: Query-string parameters as a free-form object.
--     * Slot: headers_id Description: Request headers as a free-form object (case insensitive in HTTP).
--     * Slot: body_id Description: Decoded request body as a free-form object.
-- # Class: Manifest Description: ``Manifest`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: rego_version Description: Rego language version pinned for files in this bundle. ``0`` = Rego v0 (legacy); ``1`` = Rego v1 (default since OPA 1.0). See ``v1/bundle/bundle.go`` for the canonical mapping.
--     * Slot: revision Description: ``revision`` field of ``Manifest`` (from upstream JSON Schema).
--     * Slot: metadata_id Description: ``metadata`` field of ``Manifest`` (from upstream JSON Schema).
-- # Class: WasmResolver Description: ``WasmResolver`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: entrypoint Description: ``entrypoint`` field of ``WasmResolver`` (from upstream JSON Schema).
--     * Slot: module Description: ``module`` field of ``WasmResolver`` (from upstream JSON Schema).
--     * Slot: Manifest_id Description: Autocreated FK slot
-- # Class: FileRegoVersion Description: Typed override record for ``Manifest.file_rego_versions``. Provides stronger validation than a free-form map while keeping the same semantics.
--     * Slot: path Description: Bundle-relative file path receiving a Rego version override.
--     * Slot: version Description: Rego version for this file: ``0`` (v0) or ``1`` (v1).
--     * Slot: Manifest_id Description: Autocreated FK slot
-- # Class: ArrayAppendStmt Description: ``ArrayAppendStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``ArrayAppendStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``ArrayAppendStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``ArrayAppendStmt`` (from upstream JSON Schema).
--     * Slot: array Description: ``array`` field of ``ArrayAppendStmt`` (from upstream JSON Schema).
--     * Slot: value_id Description: ``value`` field of ``ArrayAppendStmt`` (from upstream JSON Schema).
-- # Class: AssignIntStmt Description: ``AssignIntStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``AssignIntStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``AssignIntStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``AssignIntStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``AssignIntStmt`` (from upstream JSON Schema).
--     * Slot: value Description: ``value`` field of ``AssignIntStmt`` (from upstream JSON Schema).
-- # Class: AssignVarOnceStmt Description: ``AssignVarOnceStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``AssignVarOnceStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``AssignVarOnceStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``AssignVarOnceStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``AssignVarOnceStmt`` (from upstream JSON Schema).
--     * Slot: source_id Description: ``source`` field of ``AssignVarOnceStmt`` (from upstream JSON Schema).
-- # Class: AssignVarStmt Description: ``AssignVarStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``AssignVarStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``AssignVarStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``AssignVarStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``AssignVarStmt`` (from upstream JSON Schema).
--     * Slot: source_id Description: ``source`` field of ``AssignVarStmt`` (from upstream JSON Schema).
-- # Class: Block Description: ``Block`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: BlockStmt_id Description: Autocreated FK slot
--     * Slot: Func_id Description: Autocreated FK slot
--     * Slot: Plan_id Description: Autocreated FK slot
-- # Class: BlockStmt Description: ``BlockStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``BlockStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``BlockStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``BlockStmt`` (from upstream JSON Schema).
-- # Class: BreakStmt Description: ``BreakStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``BreakStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``BreakStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``BreakStmt`` (from upstream JSON Schema).
--     * Slot: index Description: ``index`` field of ``BreakStmt`` (from upstream JSON Schema).
-- # Class: BuiltinFunc Description: ``BuiltinFunc`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: name Description: ``name`` field of ``BuiltinFunc`` (from upstream JSON Schema).
--     * Slot: Static_id Description: Autocreated FK slot
--     * Slot: decl_id Description: BuiltinFunc declaration; opaque in this schema.
-- # Class: CallDynamicStmt Description: ``CallDynamicStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``CallDynamicStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``CallDynamicStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``CallDynamicStmt`` (from upstream JSON Schema).
--     * Slot: result Description: ``result`` field of ``CallDynamicStmt`` (from upstream JSON Schema).
-- # Class: CallStmt Description: ``CallStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``CallStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``CallStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``CallStmt`` (from upstream JSON Schema).
--     * Slot: func Description: ``func`` field of ``CallStmt`` (from upstream JSON Schema).
--     * Slot: result Description: ``result`` field of ``CallStmt`` (from upstream JSON Schema).
-- # Class: DotStmt Description: ``DotStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``DotStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``DotStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``DotStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``DotStmt`` (from upstream JSON Schema).
--     * Slot: key_id Description: ``key`` field of ``DotStmt`` (from upstream JSON Schema).
--     * Slot: source_id Description: ``source`` field of ``DotStmt`` (from upstream JSON Schema).
-- # Class: EqualStmt Description: ``EqualStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``EqualStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``EqualStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``EqualStmt`` (from upstream JSON Schema).
--     * Slot: a_id Description: ``a`` field of ``EqualStmt`` (from upstream JSON Schema).
--     * Slot: b_id Description: ``b`` field of ``EqualStmt`` (from upstream JSON Schema).
-- # Class: Func Description: ``Func`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: name Description: ``name`` field of ``Func`` (from upstream JSON Schema).
--     * Slot: return_value Description: ``return`` field of ``Func`` (from upstream JSON Schema). (Renamed from upstream wire-format key ``return`` to avoid the Python reserved word.)
--     * Slot: Funcs_id Description: Autocreated FK slot
-- # Class: Funcs Description: ``Funcs`` definition from upstream JSON Schema.
--     * Slot: id
-- # Class: IsArrayStmt Description: ``IsArrayStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``IsArrayStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``IsArrayStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``IsArrayStmt`` (from upstream JSON Schema).
--     * Slot: source_id Description: ``source`` field of ``IsArrayStmt`` (from upstream JSON Schema).
-- # Class: IsDefinedStmt Description: ``IsDefinedStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``IsDefinedStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``IsDefinedStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``IsDefinedStmt`` (from upstream JSON Schema).
--     * Slot: source Description: ``source`` field of ``IsDefinedStmt`` (from upstream JSON Schema).
-- # Class: IsObjectStmt Description: ``IsObjectStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``IsObjectStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``IsObjectStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``IsObjectStmt`` (from upstream JSON Schema).
--     * Slot: source_id Description: ``source`` field of ``IsObjectStmt`` (from upstream JSON Schema).
-- # Class: IsSetStmt Description: ``IsSetStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``IsSetStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``IsSetStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``IsSetStmt`` (from upstream JSON Schema).
--     * Slot: source_id Description: ``source`` field of ``IsSetStmt`` (from upstream JSON Schema).
-- # Class: IsUndefinedStmt Description: ``IsUndefinedStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``IsUndefinedStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``IsUndefinedStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``IsUndefinedStmt`` (from upstream JSON Schema).
--     * Slot: source Description: ``source`` field of ``IsUndefinedStmt`` (from upstream JSON Schema).
-- # Class: LenStmt Description: ``LenStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``LenStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``LenStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``LenStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``LenStmt`` (from upstream JSON Schema).
--     * Slot: source_id Description: ``source`` field of ``LenStmt`` (from upstream JSON Schema).
-- # Class: MakeArrayStmt Description: ``MakeArrayStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``MakeArrayStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``MakeArrayStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``MakeArrayStmt`` (from upstream JSON Schema).
--     * Slot: capacity Description: ``capacity`` field of ``MakeArrayStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``MakeArrayStmt`` (from upstream JSON Schema).
-- # Class: MakeNullStmt Description: ``MakeNullStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``MakeNullStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``MakeNullStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``MakeNullStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``MakeNullStmt`` (from upstream JSON Schema).
-- # Class: MakeNumberIntStmt Description: ``MakeNumberIntStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``MakeNumberIntStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``MakeNumberIntStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``MakeNumberIntStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``MakeNumberIntStmt`` (from upstream JSON Schema).
--     * Slot: value Description: ``value`` field of ``MakeNumberIntStmt`` (from upstream JSON Schema).
-- # Class: MakeNumberRefStmt Description: ``MakeNumberRefStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``MakeNumberRefStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``MakeNumberRefStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``MakeNumberRefStmt`` (from upstream JSON Schema).
--     * Slot: index Description: ``index`` field of ``MakeNumberRefStmt`` (from upstream JSON Schema).
--     * Slot: Index Description: Deprecated alias for `index`. Both keys are emitted by current OPA versions for backwards compatibility; will be removed in a future major release. Read `index` instead.
--     * Slot: target Description: ``target`` field of ``MakeNumberRefStmt`` (from upstream JSON Schema).
-- # Class: MakeObjectStmt Description: ``MakeObjectStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``MakeObjectStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``MakeObjectStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``MakeObjectStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``MakeObjectStmt`` (from upstream JSON Schema).
-- # Class: MakeSetStmt Description: ``MakeSetStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``MakeSetStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``MakeSetStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``MakeSetStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``MakeSetStmt`` (from upstream JSON Schema).
-- # Class: NopStmt Description: ``NopStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``NopStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``NopStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``NopStmt`` (from upstream JSON Schema).
-- # Class: NotEqualStmt Description: ``NotEqualStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``NotEqualStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``NotEqualStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``NotEqualStmt`` (from upstream JSON Schema).
--     * Slot: a_id Description: ``a`` field of ``NotEqualStmt`` (from upstream JSON Schema).
--     * Slot: b_id Description: ``b`` field of ``NotEqualStmt`` (from upstream JSON Schema).
-- # Class: NotStmt Description: ``NotStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``NotStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``NotStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``NotStmt`` (from upstream JSON Schema).
--     * Slot: block Description: ``block`` field of ``NotStmt`` (from upstream JSON Schema).
-- # Class: ObjectInsertOnceStmt Description: ``ObjectInsertOnceStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema).
--     * Slot: object Description: ``object`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema).
--     * Slot: key_id Description: ``key`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema).
--     * Slot: value_id Description: ``value`` field of ``ObjectInsertOnceStmt`` (from upstream JSON Schema).
-- # Class: ObjectInsertStmt Description: ``ObjectInsertStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``ObjectInsertStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``ObjectInsertStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``ObjectInsertStmt`` (from upstream JSON Schema).
--     * Slot: object Description: ``object`` field of ``ObjectInsertStmt`` (from upstream JSON Schema).
--     * Slot: key_id Description: ``key`` field of ``ObjectInsertStmt`` (from upstream JSON Schema).
--     * Slot: value_id Description: ``value`` field of ``ObjectInsertStmt`` (from upstream JSON Schema).
-- # Class: ObjectMergeStmt Description: ``ObjectMergeStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``ObjectMergeStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``ObjectMergeStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``ObjectMergeStmt`` (from upstream JSON Schema).
--     * Slot: a Description: ``a`` field of ``ObjectMergeStmt`` (from upstream JSON Schema).
--     * Slot: b Description: ``b`` field of ``ObjectMergeStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``ObjectMergeStmt`` (from upstream JSON Schema).
-- # Class: Plan Description: ``Plan`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: name Description: ``name`` field of ``Plan`` (from upstream JSON Schema).
--     * Slot: Plans_id Description: Autocreated FK slot
-- # Class: Plans Description: ``Plans`` definition from upstream JSON Schema.
--     * Slot: id
-- # Class: Policy Description: ``Policy`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: funcs_id Description: ``funcs`` field of ``Policy`` (from upstream JSON Schema).
--     * Slot: plans_id Description: ``plans`` field of ``Policy`` (from upstream JSON Schema).
--     * Slot: static_id Description: ``static`` field of ``Policy`` (from upstream JSON Schema).
-- # Class: ResetLocalStmt Description: ``ResetLocalStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``ResetLocalStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``ResetLocalStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``ResetLocalStmt`` (from upstream JSON Schema).
--     * Slot: target Description: ``target`` field of ``ResetLocalStmt`` (from upstream JSON Schema).
-- # Class: ResultSetAddStmt Description: ``ResultSetAddStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``ResultSetAddStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``ResultSetAddStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``ResultSetAddStmt`` (from upstream JSON Schema).
--     * Slot: value Description: ``value`` field of ``ResultSetAddStmt`` (from upstream JSON Schema).
-- # Class: ReturnLocalStmt Description: ``ReturnLocalStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``ReturnLocalStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``ReturnLocalStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``ReturnLocalStmt`` (from upstream JSON Schema).
--     * Slot: source Description: ``source`` field of ``ReturnLocalStmt`` (from upstream JSON Schema).
-- # Class: ScanStmt Description: ``ScanStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``ScanStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``ScanStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``ScanStmt`` (from upstream JSON Schema).
--     * Slot: block Description: ``block`` field of ``ScanStmt`` (from upstream JSON Schema).
--     * Slot: key Description: ``key`` field of ``ScanStmt`` (from upstream JSON Schema).
--     * Slot: source Description: ``source`` field of ``ScanStmt`` (from upstream JSON Schema).
--     * Slot: value Description: ``value`` field of ``ScanStmt`` (from upstream JSON Schema).
-- # Class: SetAddStmt Description: ``SetAddStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``SetAddStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``SetAddStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``SetAddStmt`` (from upstream JSON Schema).
--     * Slot: set Description: ``set`` field of ``SetAddStmt`` (from upstream JSON Schema).
--     * Slot: value_id Description: ``value`` field of ``SetAddStmt`` (from upstream JSON Schema).
-- # Class: Static Description: ``Static`` definition from upstream JSON Schema.
--     * Slot: id
-- # Class: Stmt Description: Tagged-wrapper class for the ``Stmt`` discriminated union fromthe upstream JSON Schema.The ``type`` slot carries the discriminator tag and the``stmt`` slot carries the typed payload. Because thepayload class varies by tag, ``stmt`` is typed as``Any`` with an ``any_of`` union over the known payload classes;consumers select the concrete class using the table below.* ``ArrayAppendStmt`` -- payload class ``ArrayAppendStmt``* ``AssignIntStmt`` -- payload class ``AssignIntStmt``* ``AssignVarOnceStmt`` -- payload class ``AssignVarOnceStmt``* ``AssignVarStmt`` -- payload class ``AssignVarStmt``* ``BlockStmt`` -- payload class ``BlockStmt``* ``BreakStmt`` -- payload class ``BreakStmt``* ``CallDynamicStmt`` -- payload class ``CallDynamicStmt``* ``CallStmt`` -- payload class ``CallStmt``* ``DotStmt`` -- payload class ``DotStmt``* ``EqualStmt`` -- payload class ``EqualStmt``* ``IsArrayStmt`` -- payload class ``IsArrayStmt``* ``IsDefinedStmt`` -- payload class ``IsDefinedStmt``* ``IsObjectStmt`` -- payload class ``IsObjectStmt``* ``IsSetStmt`` -- payload class ``IsSetStmt``* ``IsUndefinedStmt`` -- payload class ``IsUndefinedStmt``* ``LenStmt`` -- payload class ``LenStmt``* ``MakeArrayStmt`` -- payload class ``MakeArrayStmt``* ``MakeNullStmt`` -- payload class ``MakeNullStmt``* ``MakeNumberIntStmt`` -- payload class ``MakeNumberIntStmt``* ``MakeNumberRefStmt`` -- payload class ``MakeNumberRefStmt``* ``MakeObjectStmt`` -- payload class ``MakeObjectStmt``* ``MakeSetStmt`` -- payload class ``MakeSetStmt``* ``NopStmt`` -- payload class ``NopStmt``* ``NotEqualStmt`` -- payload class ``NotEqualStmt``* ``NotStmt`` -- payload class ``NotStmt``* ``ObjectInsertOnceStmt`` -- payload class ``ObjectInsertOnceStmt``* ``ObjectInsertStmt`` -- payload class ``ObjectInsertStmt``* ``ObjectMergeStmt`` -- payload class ``ObjectMergeStmt``* ``ResetLocalStmt`` -- payload class ``ResetLocalStmt``* ``ResultSetAddStmt`` -- payload class ``ResultSetAddStmt``* ``ReturnLocalStmt`` -- payload class ``ReturnLocalStmt``* ``ScanStmt`` -- payload class ``ScanStmt``* ``SetAddStmt`` -- payload class ``SetAddStmt``* ``WithStmt`` -- payload class ``WithStmt``
--     * Slot: id
--     * Slot: type Description: Discriminator tag identifying the Stmt variant.
--     * Slot: Block_id Description: Autocreated FK slot
--     * Slot: stmt_id Description: Typed payload; concrete class is selected by ``type``.
-- # Class: StringConst Description: ``StringConst`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: value Description: ``value`` field of ``StringConst`` (from upstream JSON Schema).
--     * Slot: Static_id Description: Autocreated FK slot
-- # Class: Val Description: Tagged-wrapper class for the ``Val`` discriminated union fromthe upstream JSON Schema.The ``type`` slot carries the discriminator tag and the``value`` slot carries the typed payload. Because thepayload class varies by tag, ``value`` is typed as``Any`` with an ``any_of`` union over the known payload classes;consumers select the concrete class using the table below.* ``bool`` -- payload class ``boolean``* ``local`` -- payload class ``integer``* ``string_index`` -- payload class ``integer``
--     * Slot: id
--     * Slot: type Description: Discriminator tag identifying the Val variant.
--     * Slot: value_id Description: Typed payload; concrete class is selected by ``type``.
-- # Class: WithStmt Description: ``WithStmt`` definition from upstream JSON Schema.
--     * Slot: id
--     * Slot: col Description: ``col`` field of ``WithStmt`` (from upstream JSON Schema).
--     * Slot: file Description: ``file`` field of ``WithStmt`` (from upstream JSON Schema).
--     * Slot: row Description: ``row`` field of ``WithStmt`` (from upstream JSON Schema).
--     * Slot: block Description: ``block`` field of ``WithStmt`` (from upstream JSON Schema).
--     * Slot: local Description: ``local`` field of ``WithStmt`` (from upstream JSON Schema).
--     * Slot: value_id Description: ``value`` field of ``WithStmt`` (from upstream JSON Schema).
-- # Class: Operand Description: Alias for ``Val`` (single-``$ref`` def in upstream JSON Schema).
--     * Slot: id
--     * Slot: type Description: Discriminator tag identifying the Val variant.
--     * Slot: CallDynamicStmt_id Description: Autocreated FK slot
--     * Slot: CallStmt_id Description: Autocreated FK slot
--     * Slot: value_id Description: Typed payload; concrete class is selected by ``type``.
-- # Class: Capabilities_future_keywords
--     * Slot: Capabilities_id Description: Autocreated FK slot
--     * Slot: future_keywords Description: Keywords reserved for future Rego releases.
-- # Class: Capabilities_features
--     * Slot: Capabilities_id Description: Autocreated FK slot
--     * Slot: features Description: Optional language / runtime features enabled in this build.
-- # Class: Capabilities_allow_net
--     * Slot: Capabilities_id Description: Autocreated FK slot
--     * Slot: allow_net Description: Network destinations the built-ins are allowed to contact. Absent or empty means unrestricted; an empty list means no network access.
-- # Class: BuiltinCategoryGroup_builtins
--     * Slot: BuiltinCategoryGroup_name Description: Autocreated FK slot
--     * Slot: builtins Description: Names of the built-ins belonging to this category.
-- # Class: BuiltinMetadata_available
--     * Slot: BuiltinMetadata_name Description: Autocreated FK slot
--     * Slot: available Description: Every OPA release tag in which the built-in is available.
-- # Class: AuthorizationInput_path
--     * Slot: AuthorizationInput_id Description: Autocreated FK slot
--     * Slot: path Description: Request URL path split on ``/`` and decoded into a list of path segments.
-- # Class: Manifest_roots
--     * Slot: Manifest_id Description: Autocreated FK slot
--     * Slot: roots Description: ``roots`` field of ``Manifest`` (from upstream JSON Schema).
-- # Class: WasmResolver_annotations
--     * Slot: WasmResolver_id Description: Autocreated FK slot
--     * Slot: annotations_id Description: ``annotations`` field of ``WasmResolver`` (from upstream JSON Schema).
-- # Class: CallDynamicStmt_args
--     * Slot: CallDynamicStmt_id Description: Autocreated FK slot
--     * Slot: args Description: ``args`` field of ``CallDynamicStmt`` (from upstream JSON Schema).
-- # Class: Func_params
--     * Slot: Func_id Description: Autocreated FK slot
--     * Slot: params Description: ``params`` field of ``Func`` (from upstream JSON Schema).
-- # Class: Func_path
--     * Slot: Func_id Description: Autocreated FK slot
--     * Slot: path Description: ``path`` field of ``Func`` (from upstream JSON Schema).
-- # Class: WithStmt_path
--     * Slot: WithStmt_id Description: Autocreated FK slot
--     * Slot: path Description: ``path`` field of ``WithStmt`` (from upstream JSON Schema).

CREATE TABLE "Any" (
	id INTEGER NOT NULL,
	"AuthorizationInput_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AuthorizationInput_id") REFERENCES "AuthorizationInput" (id)
);
CREATE INDEX "ix_Any_id" ON "Any" (id);

CREATE TABLE "Capabilities" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Capabilities_id" ON "Capabilities" (id);

CREATE TABLE "BuiltinDecl" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	result_id INTEGER,
	variadic_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(result_id) REFERENCES "TypeDecl" (id),
	FOREIGN KEY(variadic_id) REFERENCES "TypeDecl" (id)
);
CREATE INDEX "ix_BuiltinDecl_id" ON "BuiltinDecl" (id);

CREATE TABLE "TypeDecl" (
	id INTEGER NOT NULL,
	type VARCHAR(8),
	"BuiltinDecl_id" INTEGER,
	"TypeDecl_id" INTEGER,
	dynamic_id INTEGER,
	key_id INTEGER,
	value_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BuiltinDecl_id") REFERENCES "BuiltinDecl" (id),
	FOREIGN KEY("TypeDecl_id") REFERENCES "TypeDecl" (id),
	FOREIGN KEY(dynamic_id) REFERENCES "TypeDecl" (id),
	FOREIGN KEY(key_id) REFERENCES "Any" (id),
	FOREIGN KEY(value_id) REFERENCES "TypeDecl" (id)
);
CREATE INDEX "ix_TypeDecl_id" ON "TypeDecl" (id);

CREATE TABLE "BuiltinMetadataCatalog" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_BuiltinMetadataCatalog_id" ON "BuiltinMetadataCatalog" (id);

CREATE TABLE "BuiltinResult" (
	id INTEGER NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_BuiltinResult_id" ON "BuiltinResult" (id);

CREATE TABLE "VersionIndex" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_VersionIndex_id" ON "VersionIndex" (id);

CREATE TABLE "AuthorizationInput" (
	id INTEGER NOT NULL,
	identity TEXT NOT NULL,
	method TEXT NOT NULL,
	params_id INTEGER NOT NULL,
	headers_id INTEGER NOT NULL,
	body_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(params_id) REFERENCES "Any" (id),
	FOREIGN KEY(headers_id) REFERENCES "Any" (id),
	FOREIGN KEY(body_id) REFERENCES "Any" (id)
);
CREATE INDEX "ix_AuthorizationInput_id" ON "AuthorizationInput" (id);

CREATE TABLE "AssignIntStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	target INTEGER NOT NULL,
	value INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AssignIntStmt_id" ON "AssignIntStmt" (id);

CREATE TABLE "BlockStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_BlockStmt_id" ON "BlockStmt" (id);

CREATE TABLE "BreakStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_BreakStmt_id" ON "BreakStmt" (id);

CREATE TABLE "CallDynamicStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	result INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CallDynamicStmt_id" ON "CallDynamicStmt" (id);

CREATE TABLE "CallStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	func TEXT NOT NULL,
	result INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CallStmt_id" ON "CallStmt" (id);

CREATE TABLE "Funcs" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Funcs_id" ON "Funcs" (id);

CREATE TABLE "IsDefinedStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	source INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_IsDefinedStmt_id" ON "IsDefinedStmt" (id);

CREATE TABLE "IsUndefinedStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	source INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_IsUndefinedStmt_id" ON "IsUndefinedStmt" (id);

CREATE TABLE "MakeArrayStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	capacity INTEGER NOT NULL,
	target INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MakeArrayStmt_id" ON "MakeArrayStmt" (id);

CREATE TABLE "MakeNullStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	target INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MakeNullStmt_id" ON "MakeNullStmt" (id);

CREATE TABLE "MakeNumberIntStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	target INTEGER NOT NULL,
	value INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MakeNumberIntStmt_id" ON "MakeNumberIntStmt" (id);

CREATE TABLE "MakeNumberRefStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	"index" INTEGER NOT NULL,
	"Index" INTEGER,
	target INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MakeNumberRefStmt_id" ON "MakeNumberRefStmt" (id);

CREATE TABLE "MakeObjectStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	target INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MakeObjectStmt_id" ON "MakeObjectStmt" (id);

CREATE TABLE "MakeSetStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	target INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MakeSetStmt_id" ON "MakeSetStmt" (id);

CREATE TABLE "NopStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NopStmt_id" ON "NopStmt" (id);

CREATE TABLE "NotStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	block TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NotStmt_id" ON "NotStmt" (id);

CREATE TABLE "ObjectMergeStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	a INTEGER NOT NULL,
	b INTEGER NOT NULL,
	target INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ObjectMergeStmt_id" ON "ObjectMergeStmt" (id);

CREATE TABLE "Plans" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Plans_id" ON "Plans" (id);

CREATE TABLE "ResetLocalStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	target INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ResetLocalStmt_id" ON "ResetLocalStmt" (id);

CREATE TABLE "ResultSetAddStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	value INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ResultSetAddStmt_id" ON "ResultSetAddStmt" (id);

CREATE TABLE "ReturnLocalStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	source INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ReturnLocalStmt_id" ON "ReturnLocalStmt" (id);

CREATE TABLE "ScanStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	block TEXT NOT NULL,
	"key" INTEGER NOT NULL,
	source INTEGER NOT NULL,
	value INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ScanStmt_id" ON "ScanStmt" (id);

CREATE TABLE "Static" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Static_id" ON "Static" (id);

CREATE TABLE "Builtin" (
	name TEXT NOT NULL,
	infix TEXT,
	deprecated BOOLEAN,
	nondeterministic BOOLEAN,
	relation BOOLEAN,
	"Capabilities_id" INTEGER,
	decl_id INTEGER NOT NULL,
	PRIMARY KEY (name),
	FOREIGN KEY("Capabilities_id") REFERENCES "Capabilities" (id),
	FOREIGN KEY(decl_id) REFERENCES "BuiltinDecl" (id)
);
CREATE INDEX "ix_Builtin_name" ON "Builtin" (name);

CREATE TABLE "WasmABIVersion" (
	id INTEGER NOT NULL,
	version INTEGER NOT NULL,
	minor_version INTEGER NOT NULL,
	"Capabilities_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Capabilities_id") REFERENCES "Capabilities" (id)
);
CREATE INDEX "ix_WasmABIVersion_id" ON "WasmABIVersion" (id);

CREATE TABLE "BuiltinCategoryGroup" (
	name TEXT NOT NULL,
	category VARCHAR(13),
	"BuiltinMetadataCatalog_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("BuiltinMetadataCatalog_id") REFERENCES "BuiltinMetadataCatalog" (id)
);
CREATE INDEX "ix_BuiltinCategoryGroup_name" ON "BuiltinCategoryGroup" (name);

CREATE TABLE "BuiltinMetadata" (
	name TEXT NOT NULL,
	description TEXT,
	introduced TEXT,
	wasm BOOLEAN,
	infix TEXT,
	deprecated BOOLEAN,
	relation BOOLEAN,
	"BuiltinMetadataCatalog_id" INTEGER,
	result_id INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("BuiltinMetadataCatalog_id") REFERENCES "BuiltinMetadataCatalog" (id),
	FOREIGN KEY(result_id) REFERENCES "BuiltinResult" (id)
);
CREATE INDEX "ix_BuiltinMetadata_name" ON "BuiltinMetadata" (name);

CREATE TABLE "ElementVersion" (
	name TEXT NOT NULL,
	major INTEGER NOT NULL,
	minor INTEGER NOT NULL,
	patch INTEGER NOT NULL,
	"VersionIndex_id" INTEGER,
	PRIMARY KEY (name),
	FOREIGN KEY("VersionIndex_id") REFERENCES "VersionIndex" (id)
);
CREATE INDEX "ix_ElementVersion_name" ON "ElementVersion" (name);

CREATE TABLE "Manifest" (
	id INTEGER NOT NULL,
	rego_version INTEGER,
	revision TEXT NOT NULL,
	metadata_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(metadata_id) REFERENCES "Any" (id)
);
CREATE INDEX "ix_Manifest_id" ON "Manifest" (id);

CREATE TABLE "BuiltinFunc" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"Static_id" INTEGER,
	decl_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("Static_id") REFERENCES "Static" (id),
	FOREIGN KEY(decl_id) REFERENCES "Any" (id)
);
CREATE INDEX "ix_BuiltinFunc_id" ON "BuiltinFunc" (id);

CREATE TABLE "Func" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	return_value INTEGER NOT NULL,
	"Funcs_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Funcs_id") REFERENCES "Funcs" (id)
);
CREATE INDEX "ix_Func_id" ON "Func" (id);

CREATE TABLE "Plan" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"Plans_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Plans_id") REFERENCES "Plans" (id)
);
CREATE INDEX "ix_Plan_id" ON "Plan" (id);

CREATE TABLE "Policy" (
	id INTEGER NOT NULL,
	funcs_id INTEGER,
	plans_id INTEGER,
	static_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(funcs_id) REFERENCES "Funcs" (id),
	FOREIGN KEY(plans_id) REFERENCES "Plans" (id),
	FOREIGN KEY(static_id) REFERENCES "Static" (id)
);
CREATE INDEX "ix_Policy_id" ON "Policy" (id);

CREATE TABLE "StringConst" (
	id INTEGER NOT NULL,
	value TEXT NOT NULL,
	"Static_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Static_id") REFERENCES "Static" (id)
);
CREATE INDEX "ix_StringConst_id" ON "StringConst" (id);

CREATE TABLE "Val" (
	id INTEGER NOT NULL,
	type VARCHAR(12) NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(value_id) REFERENCES "Any" (id)
);
CREATE INDEX "ix_Val_id" ON "Val" (id);

CREATE TABLE "Operand" (
	id INTEGER NOT NULL,
	type VARCHAR(12) NOT NULL,
	"CallDynamicStmt_id" INTEGER,
	"CallStmt_id" INTEGER,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("CallDynamicStmt_id") REFERENCES "CallDynamicStmt" (id),
	FOREIGN KEY("CallStmt_id") REFERENCES "CallStmt" (id),
	FOREIGN KEY(value_id) REFERENCES "Any" (id)
);
CREATE INDEX "ix_Operand_id" ON "Operand" (id);

CREATE TABLE "Capabilities_future_keywords" (
	"Capabilities_id" INTEGER,
	future_keywords VARCHAR(3),
	PRIMARY KEY ("Capabilities_id", future_keywords),
	FOREIGN KEY("Capabilities_id") REFERENCES "Capabilities" (id)
);
CREATE INDEX "ix_Capabilities_future_keywords_Capabilities_id" ON "Capabilities_future_keywords" ("Capabilities_id");
CREATE INDEX "ix_Capabilities_future_keywords_future_keywords" ON "Capabilities_future_keywords" (future_keywords);

CREATE TABLE "Capabilities_features" (
	"Capabilities_id" INTEGER,
	features VARCHAR(16),
	PRIMARY KEY ("Capabilities_id", features),
	FOREIGN KEY("Capabilities_id") REFERENCES "Capabilities" (id)
);
CREATE INDEX "ix_Capabilities_features_Capabilities_id" ON "Capabilities_features" ("Capabilities_id");
CREATE INDEX "ix_Capabilities_features_features" ON "Capabilities_features" (features);

CREATE TABLE "Capabilities_allow_net" (
	"Capabilities_id" INTEGER,
	allow_net TEXT,
	PRIMARY KEY ("Capabilities_id", allow_net),
	FOREIGN KEY("Capabilities_id") REFERENCES "Capabilities" (id)
);
CREATE INDEX "ix_Capabilities_allow_net_Capabilities_id" ON "Capabilities_allow_net" ("Capabilities_id");
CREATE INDEX "ix_Capabilities_allow_net_allow_net" ON "Capabilities_allow_net" (allow_net);

CREATE TABLE "AuthorizationInput_path" (
	"AuthorizationInput_id" INTEGER,
	path TEXT NOT NULL,
	PRIMARY KEY ("AuthorizationInput_id", path),
	FOREIGN KEY("AuthorizationInput_id") REFERENCES "AuthorizationInput" (id)
);
CREATE INDEX "ix_AuthorizationInput_path_path" ON "AuthorizationInput_path" (path);
CREATE INDEX "ix_AuthorizationInput_path_AuthorizationInput_id" ON "AuthorizationInput_path" ("AuthorizationInput_id");

CREATE TABLE "CallDynamicStmt_args" (
	"CallDynamicStmt_id" INTEGER,
	args INTEGER NOT NULL,
	PRIMARY KEY ("CallDynamicStmt_id", args),
	FOREIGN KEY("CallDynamicStmt_id") REFERENCES "CallDynamicStmt" (id)
);
CREATE INDEX "ix_CallDynamicStmt_args_args" ON "CallDynamicStmt_args" (args);
CREATE INDEX "ix_CallDynamicStmt_args_CallDynamicStmt_id" ON "CallDynamicStmt_args" ("CallDynamicStmt_id");

CREATE TABLE "BuiltinArg" (
	id INTEGER NOT NULL,
	name TEXT,
	description TEXT,
	type TEXT,
	"BuiltinMetadata_name" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("BuiltinMetadata_name") REFERENCES "BuiltinMetadata" (name)
);
CREATE INDEX "ix_BuiltinArg_id" ON "BuiltinArg" (id);

CREATE TABLE "WasmResolver" (
	id INTEGER NOT NULL,
	entrypoint TEXT,
	module TEXT,
	"Manifest_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Manifest_id") REFERENCES "Manifest" (id)
);
CREATE INDEX "ix_WasmResolver_id" ON "WasmResolver" (id);

CREATE TABLE "FileRegoVersion" (
	path TEXT NOT NULL,
	version INTEGER NOT NULL,
	"Manifest_id" INTEGER,
	PRIMARY KEY (path),
	FOREIGN KEY("Manifest_id") REFERENCES "Manifest" (id)
);
CREATE INDEX "ix_FileRegoVersion_path" ON "FileRegoVersion" (path);

CREATE TABLE "ArrayAppendStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	array INTEGER NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(value_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_ArrayAppendStmt_id" ON "ArrayAppendStmt" (id);

CREATE TABLE "AssignVarOnceStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	target INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_AssignVarOnceStmt_id" ON "AssignVarOnceStmt" (id);

CREATE TABLE "AssignVarStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	target INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_AssignVarStmt_id" ON "AssignVarStmt" (id);

CREATE TABLE "Block" (
	id INTEGER NOT NULL,
	"BlockStmt_id" INTEGER,
	"Func_id" INTEGER,
	"Plan_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BlockStmt_id") REFERENCES "BlockStmt" (id),
	FOREIGN KEY("Func_id") REFERENCES "Func" (id),
	FOREIGN KEY("Plan_id") REFERENCES "Plan" (id)
);
CREATE INDEX "ix_Block_id" ON "Block" (id);

CREATE TABLE "DotStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	target INTEGER NOT NULL,
	key_id INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(key_id) REFERENCES "Operand" (id),
	FOREIGN KEY(source_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_DotStmt_id" ON "DotStmt" (id);

CREATE TABLE "EqualStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	a_id INTEGER NOT NULL,
	b_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(a_id) REFERENCES "Operand" (id),
	FOREIGN KEY(b_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_EqualStmt_id" ON "EqualStmt" (id);

CREATE TABLE "IsArrayStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_IsArrayStmt_id" ON "IsArrayStmt" (id);

CREATE TABLE "IsObjectStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_IsObjectStmt_id" ON "IsObjectStmt" (id);

CREATE TABLE "IsSetStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_IsSetStmt_id" ON "IsSetStmt" (id);

CREATE TABLE "LenStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	target INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_LenStmt_id" ON "LenStmt" (id);

CREATE TABLE "NotEqualStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	a_id INTEGER NOT NULL,
	b_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(a_id) REFERENCES "Operand" (id),
	FOREIGN KEY(b_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_NotEqualStmt_id" ON "NotEqualStmt" (id);

CREATE TABLE "ObjectInsertOnceStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	object INTEGER NOT NULL,
	key_id INTEGER NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(key_id) REFERENCES "Operand" (id),
	FOREIGN KEY(value_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_ObjectInsertOnceStmt_id" ON "ObjectInsertOnceStmt" (id);

CREATE TABLE "ObjectInsertStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	object INTEGER NOT NULL,
	key_id INTEGER NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(key_id) REFERENCES "Operand" (id),
	FOREIGN KEY(value_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_ObjectInsertStmt_id" ON "ObjectInsertStmt" (id);

CREATE TABLE "SetAddStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	"set" INTEGER NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(value_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_SetAddStmt_id" ON "SetAddStmt" (id);

CREATE TABLE "WithStmt" (
	id INTEGER NOT NULL,
	col INTEGER NOT NULL,
	file INTEGER NOT NULL,
	"row" INTEGER NOT NULL,
	block TEXT NOT NULL,
	local INTEGER NOT NULL,
	value_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(value_id) REFERENCES "Operand" (id)
);
CREATE INDEX "ix_WithStmt_id" ON "WithStmt" (id);

CREATE TABLE "BuiltinCategoryGroup_builtins" (
	"BuiltinCategoryGroup_name" TEXT,
	builtins TEXT NOT NULL,
	PRIMARY KEY ("BuiltinCategoryGroup_name", builtins),
	FOREIGN KEY("BuiltinCategoryGroup_name") REFERENCES "BuiltinCategoryGroup" (name)
);
CREATE INDEX "ix_BuiltinCategoryGroup_builtins_BuiltinCategoryGroup_name" ON "BuiltinCategoryGroup_builtins" ("BuiltinCategoryGroup_name");
CREATE INDEX "ix_BuiltinCategoryGroup_builtins_builtins" ON "BuiltinCategoryGroup_builtins" (builtins);

CREATE TABLE "BuiltinMetadata_available" (
	"BuiltinMetadata_name" TEXT,
	available TEXT,
	PRIMARY KEY ("BuiltinMetadata_name", available),
	FOREIGN KEY("BuiltinMetadata_name") REFERENCES "BuiltinMetadata" (name)
);
CREATE INDEX "ix_BuiltinMetadata_available_BuiltinMetadata_name" ON "BuiltinMetadata_available" ("BuiltinMetadata_name");
CREATE INDEX "ix_BuiltinMetadata_available_available" ON "BuiltinMetadata_available" (available);

CREATE TABLE "Manifest_roots" (
	"Manifest_id" INTEGER,
	roots TEXT,
	PRIMARY KEY ("Manifest_id", roots),
	FOREIGN KEY("Manifest_id") REFERENCES "Manifest" (id)
);
CREATE INDEX "ix_Manifest_roots_Manifest_id" ON "Manifest_roots" ("Manifest_id");
CREATE INDEX "ix_Manifest_roots_roots" ON "Manifest_roots" (roots);

CREATE TABLE "Func_params" (
	"Func_id" INTEGER,
	params INTEGER NOT NULL,
	PRIMARY KEY ("Func_id", params),
	FOREIGN KEY("Func_id") REFERENCES "Func" (id)
);
CREATE INDEX "ix_Func_params_Func_id" ON "Func_params" ("Func_id");
CREATE INDEX "ix_Func_params_params" ON "Func_params" (params);

CREATE TABLE "Func_path" (
	"Func_id" INTEGER,
	path TEXT,
	PRIMARY KEY ("Func_id", path),
	FOREIGN KEY("Func_id") REFERENCES "Func" (id)
);
CREATE INDEX "ix_Func_path_path" ON "Func_path" (path);
CREATE INDEX "ix_Func_path_Func_id" ON "Func_path" ("Func_id");

CREATE TABLE "Stmt" (
	id INTEGER NOT NULL,
	type VARCHAR(20) NOT NULL,
	"Block_id" INTEGER,
	stmt_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("Block_id") REFERENCES "Block" (id),
	FOREIGN KEY(stmt_id) REFERENCES "Any" (id)
);
CREATE INDEX "ix_Stmt_id" ON "Stmt" (id);

CREATE TABLE "WasmResolver_annotations" (
	"WasmResolver_id" INTEGER,
	annotations_id INTEGER,
	PRIMARY KEY ("WasmResolver_id", annotations_id),
	FOREIGN KEY("WasmResolver_id") REFERENCES "WasmResolver" (id),
	FOREIGN KEY(annotations_id) REFERENCES "Any" (id)
);
CREATE INDEX "ix_WasmResolver_annotations_annotations_id" ON "WasmResolver_annotations" (annotations_id);
CREATE INDEX "ix_WasmResolver_annotations_WasmResolver_id" ON "WasmResolver_annotations" ("WasmResolver_id");

CREATE TABLE "WithStmt_path" (
	"WithStmt_id" INTEGER,
	path INTEGER NOT NULL,
	PRIMARY KEY ("WithStmt_id", path),
	FOREIGN KEY("WithStmt_id") REFERENCES "WithStmt" (id)
);
CREATE INDEX "ix_WithStmt_path_path" ON "WithStmt_path" (path);
CREATE INDEX "ix_WithStmt_path_WithStmt_id" ON "WithStmt_path" ("WithStmt_id");
