# Contributing to opa

*This file is a checklist, not a design log. Each rule is a line or two that links to where its reasoning lives. `lint-and-docs.yaml` holds it to a word budget.*

## What this project is

A LinkML schema of eight of the JSON formats Open Policy Agent (OPA) defines, in a fork of OPA's repository. OPA's tree is unchanged at the repository's root, and this LinkML project is beside it in `.linkml/`.

| Path | Holds |
| --- | --- |
| `.linkml/scripts/opa_to_linkml.py` | The converter, which writes the schema from OPA's files. Edit it. |
| `.linkml/src/opa/schema/` | The LinkML schema, one module per format, which the converter writes. |
| `.linkml/src/opa/datamodel/`, `.linkml/project/`, `.linkml/docs/schema/` | Other artefacts generated from the schema. |
| `.linkml/parity/` | The differences from OPA's JSON Schemas that the tests allow, each with its reason. |
| `.linkml/scripts/check_upstream_release.py` | The weekly comparison with OPA's releases. |
| `.lokf/knowledge/` | This repository's knowledge bundle. |

Everything else is OPA's, but what [NOTICE](NOTICE) lists as this project's.

## Development setup

You need Python 3.10+, [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just).

```bash
git clone https://github.com/lmodel/opa.git
cd opa/.linkml
uv sync --group dev
just --list
```

Never run `just setup` (it nests a repository).

### Agent skills (optional, only for this repo's `.lokf/` bundle)

The bundle is maintained with the Knowledge Trust Ladder (KTL) skills, **installed, never committed**. Continuous integration (CI) installs the librarian skill at run time, pinned to a release. [The install page](https://w3id.org/ktl/docs/install/) lists every route. With npm:

```bash
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-librarian --yes   # derive concepts
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-curator --yes     # confirm them as a person
```

## Before opening a pull request

- **Leave OPA's files alone.** A change to one goes to [OPA](https://github.com/open-policy-agent/opa). `.linkml/tests/test_upstream.py` checks every file `.linkml/tests/upstream_tree.tsv` lists against its hash.
- **Edit the converter, then regenerate.** From `.linkml/`, run `just gen-linkml`, `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit the output. A test fails when the schema differs from what the converter writes.
- **Keep OPA's keys.** A slot whose name differs from OPA's key, such as `operand_a` for `a`, carries the key as its `alias`.
- **A difference from OPA is listed, not hidden.** `.linkml/tests/test_parity.py` fails on any difference that `.linkml/parity/structural.yaml` does not list with its reason. A fault of OPA's own goes to OPA too.
- **A mapping is read at its source.** A term with no sure match stays unmapped.
- **Keep names apart.** A host imports this adapt copy beside the Linked Open Knowledge Format (LOKF) schema and the released copies in `.linkml/tests/neighbours/`. `.linkml/tests/test_schema_rules.py` checks this.
- **Run the tests**: `just test` from `.linkml/`. Examples carry OPA's keys, which linkml-validate cannot read, so they go in `tests/data/problem/valid/` and `invalid/`, named `ClassName-suffix.yaml`, and `tests/test_data.py` checks them.
- **Follow the schema's conventions**: PascalCase classes and enums with the `Opa` prefix, snake_case slots, OPA's spelling for values, and a short description on every element.
- **Run the pre-commit hooks** on what you staged, from the root (`uvx pre-commit run -c .linkml/.pre-commit-config.yaml`).
- **Lock files are part of the change.** CI installs with `uv sync --locked`, so an edit without its `.linkml/uv.lock` (or `.lokf/uv.lock`) fails.
- **Knowledge-bundle changes**: `cd .lokf && just lokf-validate` must pass, and `knowledge-registrar.yaml` runs on any `.lokf/**` change.
- **`lint-and-docs.yaml`** runs ShellCheck, actionlint, markdownlint, lychee and codespell over this project's files, never OPA's.
- **Actions are pinned to commit hashes**; bump them by hand, since this fork leaves Dependabot off.
- **The skills pin moves with the sidecar copies.** When moving `TRUST_LADDER_SKILLS_REF` in `.github/workflows/knowledge-librarian.yaml`, copy the other `knowledge-*.yaml` workflows and `.lokf/scripts/` and `.lokf/m365/` from that release's `skills/ktl-sidecar/templates/` in the same pull request.
- **If your change alters behaviour**, add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).

## Taking a new release of OPA

The weekly watch opens an issue when OPA publishes a release. Then:

1. Merge the release's tag.
2. Run `just pin-opa-tree <commit>`.
3. Move `TAG`, `COMMIT` and `RELEASE_DATE` in `.linkml/scripts/opa_to_linkml.py`, `EDITION` in the watch and `IMAGE` in `.linkml/scripts/capture_opa_documents.py`.
4. Run `just gen-linkml` and the regeneration above.
5. Run `just capture-opa-documents`, which needs podman and the network.
6. Merge with a merge commit: a squash loses OPA's history, and the next merge conflicts on every file.

## Code of conduct

Participation here is covered by the [Contributor Covenant](CODE_OF_CONDUCT.md).

## Using AI tools

Artificial intelligence (AI) assistance is welcome; [AI_COVENANT.md](AI_COVENANT.md) sets the rules, for people and the scheduled `knowledge-librarian` agent alike.

## Reporting issues

Use the [issue tracker](https://github.com/lmodel/opa/issues) for the schema. A problem in OPA or its formats belongs with [OPA](https://github.com/open-policy-agent/opa/issues).

## Releasing (maintainers)

- Write `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) as you go. The release job refuses an empty one (`.github/scripts/changelog-release.mjs check`).
- Type the commit ([Conventional Commits](https://www.conventionalcommits.org/)) for what the change *is*. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release, and OPA's commits in a merge count too. A pull request that would release must carry a releasing type in its title.
- On merge, [`semantic-release.yml`](../.github/workflows/semantic-release.yml) retitles the section to `## [X.Y.Z] - YYYY-MM-DD`, commits `.linkml/CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub Release. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches `.github/workflows/knowledge-release.yaml`, which attaches the schema copy and the bundle when either changed.
- That step runs behind the `release` GitHub Environment. Configure required reviewers on it in Settings → Environments, or every qualifying merge is released unattended.
- Below 1.0.0: the `v0.0.0` baseline tag is on the merge of OPA's release, so OPA's older commits do not count. `.releaserc.json` maps `breaking: true` to `minor`.
- A branch rule requiring pull requests, status checks or signed commits would reject the release job's own push to `main`, so leave them off. [SECURITY.md](../.github/SECURITY.md) says what holds `main` instead.

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE). [NOTICE](NOTICE) says what comes from OPA. Update it when you add something from elsewhere.
