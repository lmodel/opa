# Test data

Each file is a document in one of OPA's formats, or a broken copy of one, named
after the class it must validate against: `<Class>-<what it shows>.yaml` under
`problem/`, and `<Class>-<what it is>.json` under `captured/`.

- `problem/valid/` holds documents that must pass. Every format has one.
- `problem/invalid/` holds documents that must fail, each breaking one rule the
  schema states.
- `captured/` holds documents OPA's own binary wrote, which must pass.
  `just capture-opa-documents` writes them again from OPA's release image.

The examples use OPA's keys, such as `_categories`, `Major` and `return`, which
differ from the slot names. The example runner reads keys by slot name, so the
examples are kept under `problem/`, where it does not look. `tests/test_data.py`
validates them against the JSON Schema the schema generates. `valid/` and
`invalid/` stay empty.
