#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check open-policy-agent/opa against the release this fork holds.

The rest of this repository is OPA's tree at the release in EDITION, merged unchanged,
and the schema renders the formats that release defines. Three things can change
without any change here, and each fails the check:

- OPA publishes a later release, so a merge of its tag is due;
- the pinned tag moves to another commit;
- the licence on OPA's default branch changes.

For information only, it reports which of the files that define a format the schema
renders key for key differ on OPA's default branch. Those files are the JSON Schemas of
the plan, the manifest and the authorization input, and the Go files of the decision log
event and the status report. That says what the next release may change.

The script reads only GitHub's API and compares git object hashes, so it downloads no
file. It prints a Markdown report, and exits 1 when a check fails or cannot finish. Text
a server chose is quoted as code on one line, so the issue the workflow opens from the
report cannot mention anyone. A redirect is followed only to an https address on
api.github.com. ``GITHUB_TOKEN`` raises the API's rate limit. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
TREE_PINS = ROOT / "tests" / "upstream_tree.tsv"
USER_AGENT = "lmodel-opa-upstream-check"
REPOSITORY = "open-policy-agent/opa"
HOST = "api.github.com"
API = f"https://{HOST}/repos/{REPOSITORY}"

# The most the script reads of one answer. A folder listing is a few kilobytes.
MAX_BYTES = 5_000_000

# The release merged into this repository. tests/test_upstream.py checks that the
# schema headers, the converter and these pins agree. Move them together, with
# tests/upstream_tree.tsv, after a merge of another release.
EDITION = {
    "label": "OPA v1.22.2",
    "version": "1.22.2",
    "tag": "v1.22.2",
    "commit": "482d9e368c2ddfed67ced59259fa6a247bb5f1e5",
}

# The files compared on OPA's default branch: its licence, which fails the check when it
# changes, and the files that define the formats the schema renders key for key, which
# are reported for information.
LICENCE = "LICENSE"
FORMATS = (
    "v1/ir/plan.schema.json",
    "v1/bundle/manifest.schema.json",
    "v1/schemas/authorizationPolicy.json",
    "v1/plugins/logs/plugin.go",
    "v1/plugins/status/plugin.go",
    "v1/plugins/bundle/status.go",
    "v1/plugins/logs/status/status.go",
    "v1/plugins/plugins.go",
)


class _ApiRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on the API's host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname != HOST:
            raise ValueError(f"a redirect leads off {HOST}, to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener in place of urlopen's, whose redirect handler follows any address.
_open = urllib.request.build_opener(_ApiRedirect).open


def _get(path: str):
    """The JSON answer to one API path under OPA's repository, read up to the cap."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"{API}{path}", headers=headers)
    with _open(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer to {path} is larger than {MAX_BYTES} bytes")
    return json.loads(body)


def _code(text: object) -> str:
    """Text a server chose, as a code span on one line, so it cannot mention a person or
    add a link in the issue. A blank line would end the span, so every run of spaces and
    line breaks is one space."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


def _quote(path: str) -> str:
    return urllib.parse.quote(path, safe="/")


def pinned(paths: set[str]) -> dict[str, str]:
    """The git object hash tests/upstream_tree.tsv pins for each named file."""
    found = {}
    for row in TREE_PINS.read_text(encoding="utf-8").splitlines():
        sha, path = row.split("\t", 1)
        if path in paths:
            found[path] = sha
    return found


def _files(paths: set[str], ref: str) -> dict[str, str]:
    """The git object hash of each named file at a ref, read folder by folder."""
    found = {}
    for folder in sorted({str(PurePosixPath(path).parent) for path in paths}):
        where = "" if folder == "." else folder
        answer = _get(f"/contents/{_quote(where)}?ref={_quote(ref)}")
        if not isinstance(answer, list):
            raise ValueError(f"{folder} at {ref} is not a folder")
        found |= {e["path"]: e["sha"] for e in answer if e["type"] == "file"}
    return {path: found[path] for path in paths if path in found}


def _commit_of(tag: str) -> str:
    """The commit a tag names, through any annotated tag objects on the way."""
    target = _get(f"/git/ref/tags/{_quote(tag)}")["object"]
    while target["type"] == "tag":
        target = _get(f"/git/tags/{target['sha']}")["object"]
    return target["sha"]


_default_branch: list[str] = []


def default_branch() -> str:
    """OPA's default branch, read once."""
    if not _default_branch:
        _default_branch.append(_get("")["default_branch"])
    return _default_branch[0]


def check_release() -> tuple[list[str], bool]:
    """Report whether OPA's latest release is the merged one."""
    latest = _get("/releases/latest")["tag_name"]
    if latest != EDITION["tag"]:
        return [
            f"- **OPA's latest release is {_code(latest)}, not {EDITION['tag']}.** Merge "
            "its tag, run `just pin-opa-tree <commit>` and `just gen-linkml`, and move "
            "TAG and COMMIT in scripts/opa_to_linkml.py and EDITION here with it."
        ], True
    return [f"- OPA's latest release is the merged {EDITION['tag']}."], False


def check_pinned_tag() -> tuple[list[str], bool]:
    """Report whether the pinned tag still names its commit."""
    found = _commit_of(EDITION["tag"])
    if found != EDITION["commit"]:
        return [
            f"- **The tag {EDITION['tag']} moved to {_code(found)}.** Find out why a "
            "published tag moved before merging anything from it."
        ], True
    return [f"- The tag {EDITION['tag']} names its pinned commit."], False


def check_licence() -> tuple[list[str], bool]:
    """Report whether the licence on OPA's default branch is the pinned file."""
    sha = pinned({LICENCE})[LICENCE]
    if _files({LICENCE}, default_branch()).get(LICENCE) != sha:
        return [
            f"- **{LICENCE} on OPA's default branch changed.** Read what changed, and "
            "update NOTICE if the licence moved."
        ], True
    return [f"- {LICENCE} on OPA's default branch is unchanged."], False


def check_formats() -> tuple[list[str], bool]:
    """Report, for information, which files that define a format differ on OPA's
    default branch."""
    pins = pinned(set(FORMATS))
    found = _files(set(FORMATS), default_branch())
    moved = sorted(path for path in FORMATS if found.get(path) != pins[path])
    if moved:
        shown = ", ".join(_code(path) for path in moved)
        return [
            f"- For information, OPA's default branch has format files that differ "
            f"from {EDITION['tag']}'s: {shown}. They are unreleased."
        ], False
    return [f"- OPA's default branch holds {EDITION['tag']}'s format files."], False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("release", check_release),
    ("pinned tag", check_pinned_tag),
    ("licence", check_licence),
    ("format", check_formats),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines = [f"- Merged release: {EDITION['label']}, at {EDITION['commit'][:7]}."]
    attention = False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout, HTTPException and
        # EOFError a connection cut off mid-answer, LookupError and ValueError an answer
        # of another shape or too large.
        except (
            OSError,
            http.client.HTTPException,
            EOFError,
            LookupError,
            ValueError,
        ) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
