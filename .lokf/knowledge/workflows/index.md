# Workflows

* [Build and test (main.yaml)](main.md) - Builds the project, lints the schema, runs the tests on five Python versions and checks the adapt copy.
* [Lint and docs (lint-and-docs.yaml)](lint-and-docs.md) - Runs ShellCheck, actionlint, markdownlint, lychee and codespell over this project's files, never OPA's, and holds the governance files to word budgets.
* [Upstream watch (upstream-watch.yaml)](upstream-watch.md) - Checks every week whether OPA has released past the merged tag, and opens an issue when it has.
* [Semantic release (semantic-release.yml)](semantic-release.md) - Releases a merge to `main` whose commits carry a releasing type, and dispatches the knowledge release.
* [Knowledge librarian (knowledge-librarian.yaml)](knowledge-librarian.md) - Runs the KTL librarian agent on a schedule and opens a pull request with its changes to the bundle.
* [Knowledge registrar (knowledge-registrar.yaml)](knowledge-registrar.md) - Checks every pull request that touches `.lokf/`: the bundle's form, its conventions and each person's confirmation.
* [Knowledge release (knowledge-release.yaml)](knowledge-release.md) - Attaches the bundle, the adapt copy and the Copilot skill to a release when the bundle or the schema changed.
* [Knowledge sync (knowledge-sync.yaml)](knowledge-sync.md) - Checks every week for a newer KTL release and opens a pull request that syncs the sidecar's copies.
* [Knowledge website (knowledge-website.yaml)](knowledge-website.md) - Builds the site from `website/` and publishes it to GitHub Pages.
