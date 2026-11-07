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
