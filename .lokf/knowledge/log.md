# Change Log

## 2026-11-07

* **Changed**: The adapt copy says what `tests/test_schema_rules.py` compares, which imports nothing.
* **Changed**: What the schema leaves out names `v1/plugins/` and `v1/config/`, where the Go types are; `plugins/` and `config/` hold only aliases.
* **Prose**: reworded 9 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: the adapt copy renames the six keys LOKF defines with another meaning.
* **Changed**: the schema concept cites the umbrella for its imports.
* **Bootstrap**: the first concepts, derived from the schema project, its docs, tests and workflows.
* **Removal**: the dummy service the sidecar installs.
* **Initialization**: Scaffolded the LOKF bundle for opa with placeholder
  services. Real concepts to follow.
