# Change Log

## 2026-11-07

* **Changed**: Licence and attribution says that only the authorization input's class description is OPA's, as NOTICE now does.
* **Changed**: the schema concept names the nine modules, with the decision log event and the status report.
* **Changed**: What the schema leaves out names only the configuration file and the discovery bundle, now that the decision log event and the status report are modelled.
* **Changed**: Where the model differs from OPA's JSON Schemas gives the fourth reason, the keys OPA's server leaves out of the authorization input.
* **Changed**: How the schema is written says how the authorization input, the decision log event and the status report are rendered.
* **Changed**: the adapt copy renames seven keys, `timestamp` among them.
* **Changed**: Example data covers the documents OPA's binary wrote, and the authorization input is no longer compared with OPA's schema.
* **Changed**: the upstream watch reports the Go files of the decision log event and the status report too.
* **Changed**: Take a new OPA release moves the capture script's image and captures OPA's documents again.
* **Changed**: Licence and attribution names the descriptions taken from OPA's JSON Schemas.
* **Changed**: The adapt copy says what `tests/test_schema_rules.py` compares, which imports nothing.
* **Changed**: What the schema leaves out names `v1/plugins/` and `v1/config/`, where the Go types are; `plugins/` and `config/` hold only aliases.
* **Prose**: reworded 9 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: the adapt copy renames the six keys LOKF defines with another meaning.
* **Changed**: the schema concept cites the umbrella for its imports.
* **Bootstrap**: the first concepts, derived from the schema project, its docs, tests and workflows.
* **Removal**: the dummy service the sidecar installs.
* **Initialization**: Scaffolded the LOKF bundle for opa with placeholder
  services. Real concepts to follow.
