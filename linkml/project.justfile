## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Reads ../builtin_metadata.json, ../capabilities.json, ../v1/ast/version_index.json,
# and ../v1/schemas/authorizationPolicy.json. Writes both schema YAMLs under
# src/opa/schema/ and instance fixtures under tests/data/valid/.
# Also applies the hand-curated SSSOM mappings from src/opa/mappings/ so the
# regenerated schemas carry their cross-vocabulary alignments (D3FEND, OSCAL,
# DPV, SLSA, ISO 27001).
# Regenerate every LinkML schema submodule from upstream OPA source artifacts.
[group('model development')]
gen-linkml: && overlay-sssom
  uv run python scripts/gen_linkml.py all

# Usage: just gen-one-linkml capabilities
# Followed by overlay-sssom so the regenerated module reacquires its mappings.
# Regenerate just one submodule. Useful while iterating on a single source.
[group('model development')]
gen-one-linkml target: && overlay-sssom
  uv run python scripts/gen_linkml.py {{target}}

# Injects *_mappings entries on the matching classes/slots/attributes/enums/types
# and adds any newly-referenced object-side prefix declarations. Idempotent:
# running on an already-overlaid tree is a no-op.
# Overlay SSSOM mappings from src/opa/mappings/*.sssom.tsv onto the LinkML Schema.
[group('model development')]
overlay-sssom:
  uv run python scripts/overlay_sssom.py

# Preview the overlay without writing any files.
[group('model development')]
overlay-sssom-dry-run:
  uv run python scripts/overlay_sssom.py --dry-run --verbose
