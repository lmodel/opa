# Explanations

* [How the schema is written](how-the-schema-is-written.md) - `.linkml/scripts/opa_to_linkml.py` writes each module from OPA's JSON Schemas, data files and Go types at the merged release, and a test fails when a module differs.
* [Where the model differs from OPA's JSON Schemas](differences-from-opa.md) - Four reasons cover every case where the schema and OPA's JSON Schemas decide a document differently.
* [What the schema leaves out](what-is-left-out.md) - The configuration file and the discovery bundle are left out, since OPA's configuration type keeps most sections as raw JSON that each plugin parses with its own types.
* [The fork layout](fork-layout.md) - OPA's tree sits unchanged at the repository's root, and everything this project adds is listed in `.linkml/NOTICE`.
