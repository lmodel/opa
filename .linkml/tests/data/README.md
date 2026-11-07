# Test data

Each file is a document in one of OPA's formats, or a broken copy of one, named
`<Class>-<what it shows>.yaml` after the class it must validate against.

- `problem/valid/` holds documents that must pass. Every format has one.
- `problem/invalid/` holds documents that must fail, each breaking one rule the
  schema states.

The examples use OPA's keys, such as `_categories`, `Major` and `return`, which
differ from the slot names. The example runner reads keys by slot name, so the
examples are kept under `problem/`, where it does not look, and `tests/test_data.py`
validates them against the JSON Schema the schema generates. `valid/` and
`invalid/` stay empty.
