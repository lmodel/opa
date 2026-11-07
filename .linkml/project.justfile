## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Reads ../builtin_metadata.json, ../capabilities.json, ../v1/ast/version_index.json,
# and ../v1/schemas/authorizationPolicy.json. Writes both schema YAMLs under
# src/opa/schema/ and instance fixtures under tests/data/valid/.
# Regenerate every LinkML schema submodule from upstream OPA source artifacts.
[group('model development')]
gen-linkml:
  uv run python scripts/gen_linkml.py all

# Usage: just gen-one-linkml capabilities
# Regenerate just one submodule. Useful while iterating on a single source.
[group('model development')]
gen-one-linkml target:
  uv run python scripts/gen_linkml.py {{target}}
