<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# opa

Open Policy Agent (OPA) v1.22.2 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/opa](https://lmodel.github.io/opa)

## What it models

The schema models the JSON formats [Open Policy Agent](https://www.openpolicyagent.org/) defines, at release [v1.22.2](https://github.com/open-policy-agent/opa/releases/tag/v1.22.2): the IR plan that `opa build -t plan` writes, the bundle manifest, the input of the authorization policy, the capabilities document, the built-in function metadata and the version index. [scripts/opa_to_linkml.py](scripts/opa_to_linkml.py) writes one module per format from OPA's JSON Schemas, data files and Go types, and [tests/test_parity.py](tests/test_parity.py) holds the schema's verdicts to OPA's own JSON Schemas.

This repository is a fork of [open-policy-agent/opa](https://github.com/open-policy-agent/opa). OPA's tree sits unchanged at the repository's root, and this project sits beside it, in this folder, `.lokf/` and `website/`. A weekly workflow opens an issue when OPA publishes a release.

## Mappings

* **OPA's JSON Schemas**: each class of the plan and the manifest names the definition it renders in `exact_mappings`, such as `opa_plan:CallStmt`. `tests/test_parity.py` resolves each one in OPA's file.

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

Run `just` from this folder to list the project's [just](https://github.com/casey/just/) recipes. Never run `just setup`, which nests a repository, or `just deploy`, which pushes the root of `gh-pages`.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) sidecar. Its domain schema, `.lokf/schema/opa.yaml`, is the copy `just lokf-adapt` writes from `src/opa/schema/opa.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the converter, never the copy. A release carries the copy as `schema-<tag>-opa.yaml`.

In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
OpaBuiltin, OpaCapabilities, OpaManifest, OpaPolicy
```

The copy roots `OpaManifest`, `OpaCapabilities`, `OpaBuiltin` and `OpaPolicy` on LOKF's `Concept`, and folds `description` into LOKF's. Each `name` keeps its key. Six keys mean something else in OPA than in LOKF: `body`, `revision`, `source`, `target`, `type` and an integer `version`. The schema keeps them, so a document OPA writes validates unchanged, and a composite's JSON-LD context reads them as LOKF's. Every class carries the `Opa` prefix, so none is a neighbour's. OPA's keys are ordinary words, so the copy shares some with other lmodel copies, which `tests/test_schema_rules.py` lists.

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier) published under [10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).

## License

The schema project is under the [Apache License 2.0](LICENSE), and the bundle under CC BY 4.0.

OPA is the OPA Authors', under the [Apache License 2.0](../LICENSE), and the plan's descriptions open with OPA's Go comments under the same terms. [NOTICE](NOTICE) says what comes from where. This project is not part of OPA, and the OPA project does not endorse it.
