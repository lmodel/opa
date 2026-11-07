<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# opa

Open Policy Agent (OPA) v1.22.2 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/opa](https://lmodel.github.io/opa)

## What it models

The schema models the JSON formats [Open Policy Agent](https://www.openpolicyagent.org/) defines, at release [v1.22.2](https://github.com/open-policy-agent/opa/releases/tag/v1.22.2): the IR plan that `opa build -t plan` writes, the bundle manifest, the input of the authorization policy, the capabilities document, the built-in function metadata and the version index. [scripts/opa_to_linkml.py](scripts/opa_to_linkml.py) writes one module per format from OPA's JSON Schemas, data files and Go types, and [tests/test_parity.py](tests/test_parity.py) checks the schema's verdicts against OPA's own JSON Schemas.

This repository is a fork of [open-policy-agent/opa](https://github.com/open-policy-agent/opa). OPA's tree is unchanged at the repository's root, and this project's folders are beside it: this folder, `.lokf/` and `website/`. A weekly workflow opens an issue when OPA publishes a release.

## Mappings

* **OPA's JSON Schemas**: each class that renders a definition of OPA's plan or manifest schema names it in `exact_mappings`, such as `opa_plan:CallStmt`. `tests/test_parity.py` resolves each one in OPA's file.

## Repository Structure

* [docs/](docs/): the website's own pages
* [parity/](parity): the differences from OPA's JSON Schemas the tests allow, each with its reason
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the converter, the upstream watch and the sidecar's preflight
* [src/opa/schema/](src/opa/schema): the LinkML schema, which the converter writes, also at `linkml_schema/` in the repository's root
* [src/opa/datamodel/](src/opa/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/problem/](tests/data/problem) and the neighbours' adapt copies in [neighbours/](tests/neighbours)

The knowledge bundle is in `.lokf/` and the website in `website/`, at the repository's root.

## Developer Tools

Run `just` from this folder to list the project's [just](https://github.com/casey/just/) recipes. Never run `just setup`, which nests a repository.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) sidecar. Its domain schema, `.lokf/schema/opa.yaml`, is the copy `just lokf-adapt` writes from `src/opa/schema/opa.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the converter, never the copy. A release carries the copy as `schema-<tag>-opa.yaml`.

In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
OpaBuiltin, OpaCapabilities, OpaManifest, OpaPolicy
```

In the copy, `OpaManifest`, `OpaCapabilities`, `OpaBuiltin` and `OpaPolicy` descend from LOKF's `Concept`, and `description` folds into LOKF's. Each `name` keeps its key. Six of OPA's keys are words LOKF defines with another meaning: `body`, `revision`, `source`, `target`, `type` and `version`. Each is a top-level slot with an IRI of this schema's, so the schema keeps OPA's key and the copy renames the slot: `openpolicyagent_body`, `openpolicyagent_revision`, `openpolicyagent_source`, `openpolicyagent_target`, `openpolicyagent_type` and `openpolicyagent_version`. A document with OPA's keys therefore validates against the schema, not the copy. Every class carries the `Opa` prefix, so no class name is also a neighbour's. OPA's keys are ordinary words, so the copy shares some with other lmodel copies, which `tests/test_schema_rules.py` lists.

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier) published under [10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).

## License

The schema project is under the [Apache License 2.0](LICENSE), and the bundle under CC BY 4.0.

OPA is the OPA Authors', under the [Apache License 2.0](../LICENSE), and the plan's descriptions open with OPA's Go comments under the same terms. [NOTICE](NOTICE) says what comes from where. This project is not part of OPA, and the OPA project does not endorse it.
