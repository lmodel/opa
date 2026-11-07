# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Added

- **The first release: a LinkML schema of eight of the JSON formats OPA v1.22.2 defines.** It renders the IR plan, the bundle manifest and the authorization input from OPA's JSON Schemas; the capabilities, built-in function metadata and version index from OPA's data files and Go types; and the decision log event and status report from OPA's Go structs. `scripts/opa_to_linkml.py` writes every module. Tests compare the schema's verdicts with OPA's JSON Schemas, and validate documents OPA's binary wrote.
- **A KTL v0.62.0 sidecar** with a knowledge bundle, the adapt copy `.lokf/schema/opa.yaml`, the knowledge website and a weekly watch of OPA's releases.

### Changed

- **The LinkML project moved from `linkml/` to `.linkml/`**, and OPA's README and workflows are as OPA v1.22.2 has them.

### Removed

- **The five SSSOM sets** to D3FEND, DPV, ISO 27001, OSCAL and SLSA, which a language model matched, with the script that copied them into the schema.
