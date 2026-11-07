---
type: Policy
id: https://w3id.org/lmodel/opa/knowledge/policies/security-policy
genre: reference
title: Security policy
description: Report a vulnerability through GitHub's private reporting; SECURITY.md says what executes here and what holds each surface.
resource: .github/SECURITY.md
sources:
  - id: security.md
    resource: .github/SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-07T04:10:40Z"
status: draft
---

# Security policy

Report a vulnerability through GitHub's private reporting, not in an issue.[^security.md] The upstream watch reads open-policy-agent/opa through the GitHub API alone.[^security.md]

[^security.md]: .github/SECURITY.md
