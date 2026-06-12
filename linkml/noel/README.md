# OPA SSSOM Mappings

Hand-curated [SSSOM](https://mapping-commons.github.io/sssom/) cross-vocabulary
mappings between the OPA LinkML schema (`openpolicyagent:` prefix) and other
LinkML schemas in the lmodel ecosystem.

These files are **static, expert-curated TSVs** — they are not generated. They
are applied to the schema YAMLs in `../schema/` by a downstream overlay step
(`scripts/overlay_sssom.py`, invoked by a `project.justfile` recipe after
`gen-linkml`), which merges each row's predicate into the appropriate
LinkML `*_mappings` slot on the matching class or attribute.

## Files

| File | Target | Predicate mix |
|---|---|---|
| `opa-to-d3fend.sssom.tsv` | MITRE D3FEND defensive techniques | close / related / broad |
| `opa-to-oscal.sssom.tsv` | NIST OSCAL (catalog/profile/component/SSP) | close / related / broad |
| `opa-to-dpv.sssom.tsv` | W3C Data Privacy Vocabulary | close / related / broad |
| `opa-to-slsa.sssom.tsv` | SLSA provenance/verification | close / related / broad |
| `opa-to-iso27001.sssom.tsv` | ISO/IEC 27001:2022 ISMS | close / related / broad |

## Format conventions

Each file is a TSV with the lmodel-standard embedded SSSOM metadata block:

- Metadata lines prefixed with `# ` (single space after the hash).
- `mapping_set_id` of the form
  `https://w3id.org/lmodel/opa/mappings/opa_to_<target>`.
- `mapping_set_version: 0.1.0`.
- `license: https://creativecommons.org/licenses/by/4.0/`.
- `subject_source: https://w3id.org/lmodel/opa`.
- `object_source: https://w3id.org/lmodel/<target>`.
- `mapping_date: 2026-06-12`.
- `curie_map:` declares every CURIE prefix appearing in `subject_id` or
  `object_id` columns (`openpolicyagent`, the target prefix, `owl`, `semapv`,
  `skos`).

The data block is tab-separated with exactly 10 columns (in this order):

```
subject_id  subject_label  subject_category  predicate_id  predicate_label
object_id   object_label   object_category   mapping_justification   comment
```

Values used in this directory:

- `subject_category` / `object_category`: `owl:Class` (all rows; OPA classes
  mapped to target classes).
- `predicate_id`: one of `skos:closeMatch`, `skos:relatedMatch`,
  `skos:broadMatch` (no `exactMatch` claims; no `narrowMatch` rows yet).
- `mapping_justification`: `semapv:LLMBasedMatching` for every row
  (these are deliberate human design decisions about granularity and
  alignment, not lexical or LLM auto-matches).

## Adding a new mapping file

1. Create `opa-to-<target>.sssom.tsv` next to the existing files.
2. Copy a metadata header from one of the existing files and adjust
   `mapping_set_id`, `mapping_set_title`, `mapping_set_description`,
   `object_source`, and the target row in `curie_map`.
3. Add data rows following the 10-column convention. Tabs (`\t`) must be
   literal U+0009 — not spaces.
4. Keep `mapping_justification` honest: use `semapv:LLMBasedMatching`
   for hand-curated rows; use `semapv:LLMBasedMatching` only for unreviewed
   model-generated suggestions.
