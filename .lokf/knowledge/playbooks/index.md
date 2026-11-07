# Playbooks

* [Regenerate and test](regenerate-and-test.md) - Edit the converter, regenerate the schema and its artefacts, and run the tests from `.linkml/` before a pull request.
* [Take a new OPA release](take-a-new-opa-release.md) - Merge the release's tag with a merge commit, pin its tree, move the release in the converter and the watch, and regenerate.
* [Release](release.md) - A merge to `main` whose commits carry a releasing type is released by semantic-release, which promotes the changelog's Unreleased section.
* [Knowledge sources map](knowledge-sources.md) - Where this repository's knowledge lives: the schema project, its docs and tests, OPA's tree, the workflows and the governance files.
