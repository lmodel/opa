#!/usr/bin/env python3
"""Write tests/upstream_tree.tsv: each file of OPA's tree at a commit, by git object hash.

tests/test_upstream.py holds every file to it, so a change to one of OPA's files
fails the tests. Run it after merging an OPA release, with the release's commit, and
move COMMIT in scripts/opa_to_linkml.py and EDITION in scripts/check_upstream_release.py
with it. Usage::

    python scripts/pin_opa_tree.py <commit>
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "tests" / "upstream_tree.tsv"


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    listing = subprocess.run(
        ["git", "-C", str(ROOT.parent), "ls-tree", "-r", "-z", argv[0]],
        capture_output=True,
        check=True,
    ).stdout.decode("utf-8")
    rows = []
    for entry in filter(None, listing.split("\0")):
        meta, path = entry.split("\t", 1)
        mode, kind, sha = meta.split()
        if kind != "blob" or "\t" in path or "\n" in path:
            raise SystemExit(f"cannot pin {path!r}, a {kind} of mode {mode}")
        rows.append(f"{sha}\t{path}\n")
    MANIFEST.write_text("".join(rows), encoding="utf-8")
    print(f"Wrote {len(rows)} files to {MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
