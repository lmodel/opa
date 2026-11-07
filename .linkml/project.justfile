## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ OPA's formats ============

# Write src/opa/schema/ from OPA's files at the merged release (run after a merge of OPA)
[group('model development')]
gen-linkml:
  uv run python scripts/opa_to_linkml.py

# Fail when src/opa/schema/ differs from what OPA's files give
[group('model development')]
check-linkml:
  uv run python scripts/opa_to_linkml.py --check

# Write the schema's pages into docs/elements for the website, and leave docs/schema as it is
[group('model development')]
gen-doc-pages:
  uv run gen-doc {{gen_doc_args}} -d {{docdir}} {{source_schema_path}}

# Write tests/data/captured/ from OPA's release image (needs podman, or OPA_CONTAINER_CLI, and the network)
[group('model development')]
capture-opa-documents:
  uv run python scripts/capture_opa_documents.py

# ============ Upstream ============

# Report whether OPA has released past the merged tag, and what moved on its default branch
[group('model development')]
check-upstream:
  uv run python scripts/check_upstream_release.py

# Write tests/upstream_tree.tsv from OPA's tree at a commit, after a merge of its release
[group('model development')]
pin-opa-tree commit:
  uv run python scripts/pin_opa_tree.py {{commit}}

# ============ Knowledge bundle: the adapted domain schema ============

# `../.lokf/schema/opa.yaml` is the copy `lokf adapt` writes from the schema so that it
# can sit beside `../.lokf/schema/lokf.yaml` (`lokf adapt --help` lists the moves). The
# roots are the classes a knowledge concept may use as its `type`. The recipes run
# the `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD runs another, such
# as a checkout: LOKF_CMD="uv run --project ../../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project ../.lokf lokf")
# Each `name` below carries the IRI of LOKF's `name` but keeps its key: folded, it would
# become LOKF's `title`, and the copy would no longer read OPA's objects.
lokf_adapt_keep := "--keep OpaBuiltinCategory.name --keep OpaBuiltinArgument.name --keep OpaBuiltinResult.name --keep OpaBuiltin.name --keep OpaType.name --keep OpaBuiltinFunc.name --keep OpaPlan.name --keep OpaFunc.name --keep OpaVersionEntry.name --keep OpaDecisionBundle.name --keep OpaBundleStatus.name --keep OpaPluginStatus.name"
lokf_adapt_roots := "--root OpaManifest --root OpaCapabilities --root OpaBuiltin --root OpaPolicy --prefix openpolicyagent " + lokf_adapt_keep

# Rewrite ../.lokf/schema/opa.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf ../.lokf/schema/lokf.yaml -o ../.lokf/schema/opa.yaml

# Fail when ../.lokf/schema/opa.yaml is stale against the schema or lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf ../.lokf/schema/lokf.yaml -o ../.lokf/schema/opa.yaml --check

# ---- linkml-sidecar: the linkml_schema doorway (kept across `just update`) ----
# The schema folder under an ordinary, visible name at the host root, for
# folder pickers and file managers that hide dot-folders. Git carries the
# link; a sync service does not, so this recipe recreates it on a machine
# where it is missing. POSIX only; on Windows run, from the host root,
# mklink /J linkml_schema .linkml\src\opa\schema

# Create (or recreate) the linkml_schema link at the host root, to .linkml/src/opa/schema
[group('sidecar')]
linkml-link:
    #!/usr/bin/env bash
    set -euo pipefail
    target=".linkml/src/{{schema_name}}/schema"
    [ -d "../$target" ] || { echo "no $target to link to" >&2; exit 1; }
    if [ -L ../linkml_schema ]; then
      if [ "$(readlink ../linkml_schema)" = "$target" ]; then echo "linkml_schema already present - nothing to link"; exit 0; fi
      echo "../linkml_schema is a link elsewhere ($(readlink ../linkml_schema)) - remove it and re-run" >&2; exit 1
    fi
    if [ -e ../linkml_schema ]; then echo "../linkml_schema exists and is not a link - leaving it alone" >&2; exit 1; fi
    ln -s "$target" ../linkml_schema && echo "linked linkml_schema -> $target"
