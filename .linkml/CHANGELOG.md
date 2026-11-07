# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Added

- **The first release: a LinkML schema of the JSON formats OPA v1.22.2 defines.** It renders the IR plan, the bundle manifest and the authorization policy input from OPA's JSON Schemas, and the capabilities document, the built-in function metadata and the version index from OPA's data files and Go types.
