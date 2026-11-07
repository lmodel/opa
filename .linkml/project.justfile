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

# ============ Upstream ============

# Report whether OPA has released past the merged tag, and what moved on its default branch
[group('model development')]
check-upstream:
  uv run python scripts/check_upstream_release.py

# Write tests/upstream_tree.tsv from OPA's tree at a commit, after a merge of its release
[group('model development')]
pin-opa-tree commit:
  uv run python scripts/pin_opa_tree.py {{commit}}
