---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/opa/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: opa Knowledge Bundle
description: Open Policy Agent (OPA) v1.22.2 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/opa/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# opa Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for opa. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website on GitHub Pages, built from `website/` with a page per concept, the docs pages, the changelog and the schema's pages.

# References

* [Open Policy Agent (open-policy-agent/opa)](references/opa.md) - OPA's repository, of which this repository is a fork; release v1.22.2 sits unchanged at the repository's root.

# Datasets

* [OPA's tree at v1.22.2](datasets/opa-tree.md) - Every file of OPA's release v1.22.2, listed with its git object hash in `.linkml/tests/upstream_tree.tsv`, which a test holds the checkout to.
* [The OPA LinkML schema](datasets/opa-linkml-schema.md) - The LinkML model of eight of OPA v1.22.2's JSON formats in `.linkml/src/opa/schema/`: one module per format, `Opa` classes that keep OPA's keys, and the umbrella `opa.yaml`.
* [The adapt copy](datasets/adapt-copy.md) - `.lokf/schema/opa.yaml`, the copy `just lokf-adapt` writes from the schema for the bundle to validate against, which a release attaches as `schema-<tag>-opa.yaml`.
* [Parity allowances](datasets/parity-allowances.md) - `.linkml/parity/structural.yaml`: each case where the schema's verdict differs from OPA's JSON Schema's, with its reason.
* [Example data](datasets/example-data.md) - The examples under `.linkml/tests/data/`: a valid document per format, documents that each break one rule, and documents OPA's own binary wrote.
* [The neighbours' adapt copies](datasets/neighbour-copies.md) - The adapt copies other lmodel repositories release, under `.linkml/tests/neighbours/`, each pinned by the checksum of its release asset.

# Explanations

* [How the schema is written](explanations/how-the-schema-is-written.md) - `.linkml/scripts/opa_to_linkml.py` writes each module from OPA's JSON Schemas, data files and Go types at the merged release, and a test fails when a module differs.
* [Where the model differs from OPA's JSON Schemas](explanations/differences-from-opa.md) - Four reasons cover every case where the schema and OPA's JSON Schemas decide a document differently.
* [What the schema leaves out](explanations/what-is-left-out.md) - The configuration file and the discovery bundle are left out, since OPA's configuration type keeps most sections as raw JSON that each plugin parses with its own types.
* [The fork layout](explanations/fork-layout.md) - OPA's tree sits unchanged at the repository's root, and everything this project adds is listed in `.linkml/NOTICE`.

# Playbooks

* [Regenerate and test](playbooks/regenerate-and-test.md) - Edit the converter, regenerate the schema and its artefacts, and run the tests from `.linkml/` before a pull request.
* [Take a new OPA release](playbooks/take-a-new-opa-release.md) - Merge the release's tag with a merge commit, pin its tree, move the release in the converter, the watch and the capture script, regenerate, and capture OPA's documents again.
* [Release](playbooks/release.md) - A merge to `main` whose commits carry a releasing type is released by semantic-release, which promotes the changelog's Unreleased section.
* [Knowledge sources map](playbooks/knowledge-sources.md) - Where this repository's knowledge lives: the schema project, its docs and tests, OPA's tree, the workflows and the governance files.

# Policies

* [Licence and attribution](policies/license-and-attribution.md) - The schema project is under the Apache License 2.0 and the bundle under CC BY 4.0; OPA's tree is the OPA Authors', and NOTICE says what comes from where.
* [Security policy](policies/security-policy.md) - Report a vulnerability through GitHub's private reporting; SECURITY.md says what executes here and what holds each surface.
* [AI covenant](policies/ai-covenant.md) - Each contributor owns what they contribute, whatever tools helped; an element of the schema says what OPA's files say.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - Builds the project, lints the schema, runs the tests on five Python versions and checks the adapt copy.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - Runs ShellCheck, actionlint, markdownlint, lychee and codespell over this project's files, never OPA's, and holds the governance files to word budgets.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - Checks every week whether OPA has released past the merged tag, and opens an issue when it has.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - Releases a merge to `main` whose commits carry a releasing type, and dispatches the knowledge release.
* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - Runs the KTL librarian agent on a schedule and opens a pull request with its changes to the bundle.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - Checks every pull request that touches `.lokf/`: the bundle's form, its conventions and each person's confirmation.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - Attaches the bundle, the adapt copy and the Copilot skill to a release when the bundle or the schema changed.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - Checks every week for a newer KTL release and opens a pull request that syncs the sidecar's copies.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - Builds the site from `website/` and publishes it to GitHub Pages.
