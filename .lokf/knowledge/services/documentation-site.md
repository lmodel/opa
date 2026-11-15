---
type: Service
id: https://w3id.org/lmodel/opa/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website on GitHub Pages, built from `website/` with a page per concept, the docs pages, the changelog and the schema's pages.
resource: website/site.toml
sources:
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:27:54Z"
status: draft
---

# Documentation site

The site takes its home page from `.linkml/README.md`, its docs from `.linkml/docs/` and its schema pages from gen-doc.[^site.toml] It redirects the old mkdocs site's addresses under `/elements/` to `/schema/`.[^site.toml]

[^site.toml]: website/site.toml, the site's address, title and redirects
