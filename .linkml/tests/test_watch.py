"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py reads GitHub's API. These tests replace its one
network call, `_get`, with a table of answers, so they run offline. They show what the
report says in each case the watch knows.
"""

import importlib.util
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _answers(watch):
    """The answers of an unchanged upstream, built from the pins."""
    edition = watch.EDITION
    pins = watch.pinned({watch.LICENCE, *watch.SCHEMAS})
    folders = {}
    for path, sha in pins.items():
        folder = path.rpartition("/")[0]
        folders.setdefault(folder, []).append(
            {"path": path, "sha": sha, "type": "file"}
        )
    answers = {
        "": {"default_branch": "main"},
        "/releases/latest": {"tag_name": edition["tag"]},
        f"/git/ref/tags/{edition['tag']}": {
            "object": {"type": "commit", "sha": edition["commit"]}
        },
    }
    for folder, entries in folders.items():
        answers[f"/contents/{folder}?ref=main"] = entries
    return answers


def _stub(watch, answers):
    def get(path):
        if path not in answers:
            raise urllib.error.URLError(f"no stub for {path}")
        return answers[path]

    watch._get = get


def _run(watch, capsys):
    code = watch.main([])
    return code, capsys.readouterr().out


def test_unchanged_upstream_passes(watch, capsys):
    _stub(watch, _answers(watch))
    code, out = _run(watch, capsys)
    assert code == 0
    assert "latest release is the merged" in out
    assert "holds v1.22.2's JSON Schemas" in out


def test_a_later_release_fails(watch, capsys):
    answers = _answers(watch)
    answers["/releases/latest"] = {"tag_name": "v1.23.0"}
    _stub(watch, answers)
    code, out = _run(watch, capsys)
    assert code == 1
    assert "`v1.23.0`, not v1.22.2" in out


def test_a_moved_tag_fails(watch, capsys):
    answers = _answers(watch)
    answers["/git/ref/tags/v1.22.2"] = {"object": {"type": "commit", "sha": "f" * 40}}
    _stub(watch, answers)
    code, out = _run(watch, capsys)
    assert code == 1
    assert "moved to" in out


def test_an_annotated_tag_is_followed(watch, capsys):
    answers = _answers(watch)
    answers["/git/ref/tags/v1.22.2"] = {"object": {"type": "tag", "sha": "a" * 40}}
    answers[f"/git/tags/{'a' * 40}"] = {
        "object": {"type": "commit", "sha": watch.EDITION["commit"]}
    }
    _stub(watch, answers)
    assert _run(watch, capsys)[0] == 0


def test_a_changed_licence_fails(watch, capsys):
    answers = _answers(watch)
    answers["/contents/?ref=main"] = [
        {"path": "LICENSE", "sha": "0" * 40, "type": "file"}
    ]
    _stub(watch, answers)
    code, out = _run(watch, capsys)
    assert code == 1
    assert "LICENSE on OPA's default branch changed" in out


def test_a_changed_json_schema_is_reported_only(watch, capsys):
    answers = _answers(watch)
    answers["/contents/v1/ir?ref=main"] = [
        {"path": "v1/ir/plan.schema.json", "sha": "0" * 40, "type": "file"}
    ]
    _stub(watch, answers)
    code, out = _run(watch, capsys)
    assert code == 0
    assert "For information" in out and "`v1/ir/plan.schema.json`" in out


def test_a_failed_request_fails_and_says_which_check(watch, capsys):
    answers = _answers(watch)
    del answers["/releases/latest"]
    _stub(watch, answers)
    code, out = _run(watch, capsys)
    assert code == 1
    assert "The release check could not finish" in out


def test_server_text_cannot_mention_anyone(watch, capsys):
    answers = _answers(watch)
    answers["/releases/latest"] = {"tag_name": "v9`\n\n@someone"}
    _stub(watch, answers)
    out = _run(watch, capsys)[1]
    assert "`v9' @someone`" in out
