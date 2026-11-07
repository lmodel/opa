#!/usr/bin/env python3
"""Write tests/data/captured/: documents that OPA's own binary writes at the merged release.

The script runs OPA's release image in a container (podman, or the command in
OPA_CONTAINER_CLI) and keeps what OPA writes:

- the plan, and the manifests of a bundle, a plan bundle and a Wasm bundle, from
  `opa build`;
- the decision log events and status reports OPA's server sends to a service, here a
  server this script runs;
- the input the server gives the system.authz policy, which the authorization policy
  prints.

Each file is one document, re-indented with OPA's values, named `<Class>-<what it
is>.json` after the class tests/test_data.py validates it against. OPA picks ids, ports
and times, so each run writes other values. Run `just capture-opa-documents` after a
merge of an OPA release, with IMAGE moved to that release. It needs the container command
and the network, and CI never runs it. Usage::

    python scripts/capture_opa_documents.py
"""

from __future__ import annotations

import gzip
import http.server
import json
import os
import socket
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "tests" / "data" / "captured"

# OPA's image of the merged release, by the digest of its multi-platform index.
IMAGE = (
    "docker.io/openpolicyagent/opa:1.22.2-static"
    "@sha256:805656c845fb626b856fb4b4799d6c91e053a41eecc48537f4f1c2fd6974fbdd"
)
CLI = os.environ.get("OPA_CONTAINER_CLI", "podman")
# The container's user, which owns what OPA writes into the work folder. Rootless
# podman maps its root to the user who runs this script. Docker needs that user's ids.
USER = "0" if Path(CLI).name == "podman" else f"{os.getuid()}:{os.getgid()}"

# The policy the bundles hold: rules with labels, a non-deterministic call, a rule
# that conflicts on request, and the mask policy OPA applies to decision logs.
POLICY = {
    "authz.rego": """\
# METADATA
# labels:
#   team: identity
package http.example.authz

default allow := false

# METADATA
# labels:
#   severity: high
allow if {
\tinput.method == "GET"
\tsome role in data.roles[input.user]
\trole == "reader"
}

allow if input.user == "admin"

reasons contains msg if {
\tnot allow
\tmsg := sprintf("%s may not %s", [input.user, input.method])
}

stamp := time.now_ns()

pick := 1 if input.conflict

pick := 2 if input.conflict
""",
    "system/log/mask.rego": """\
package system.log

mask contains "/input/password"

mask contains {"op": "upsert", "path": "/input/token", "value": "***"} if input.input.token
""",
    "data.json": '{"roles": {"alice": ["reader"], "bob": ["writer"]}}\n',
}

# The policy's package as a path, and the Data API's address for it.
PACKAGE = "http/example/authz"
DECIDE = f"/v1/data/{PACKAGE}"

# The authorization policy: it allows every request and prints the input it gets.
AUTHZ_POLICY = """\
package system.authz

default allow := false

allow if print(json.marshal(input))
"""


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def opa(work: Path, *args: str, detach: bool = False) -> str:
    """Run OPA's image on the work folder, as the user who runs this script."""
    cmd = [CLI, "run", "--rm", "--user", USER, "--network=host"]
    cmd += ["-v", f"{work}:/work:Z", "-w", "/work"]
    if detach:
        cmd.append("-d")
    result = subprocess.run(
        [*cmd, IMAGE, *args], capture_output=True, text=True, check=True
    )
    return result.stdout.strip()


def write(name: str, doc: object) -> None:
    (OUT / f"{name}.json").write_text(
        json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def member(bundle: Path, name: str) -> object:
    """One JSON file of a bundle OPA built here, read without unpacking the rest."""
    with tarfile.open(bundle) as tar:
        return json.load(tar.extractfile(f"/{name}"))


class Sink(http.server.BaseHTTPRequestHandler):
    """The services OPA's configuration names. The server serves the bundle, records
    each upload, and refuses the first decision log upload, so that a status report
    carries the error."""

    bundle = b""
    received: list[tuple[str, object]] = []
    refused = False

    def do_GET(self) -> None:
        if self.path == "/bundles/authz.tar.gz":
            self.send_response(200)
            self.send_header("Content-Length", str(len(self.bundle)))
            self.end_headers()
            self.wfile.write(self.bundle)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self) -> None:
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        if self.headers.get("Content-Encoding") == "gzip":
            body = gzip.decompress(body)
        if self.path.startswith("/logs") and not Sink.refused:
            Sink.refused = True
            self.send_response(500)
        else:
            Sink.received.append((self.path, json.loads(body)))
            self.send_response(200)
        self.end_headers()

    def log_message(self, *args: object) -> None:
        pass


def call(base: str, method: str, path: str, body=None, headers=None) -> None:
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        base + path, data=data, method=method, headers=headers or {}
    )
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=10):
            pass
    except urllib.error.HTTPError:
        pass  # The script does not keep OPA's answer.


def wait_for(base: str) -> None:
    for _ in range(120):
        try:
            with urllib.request.urlopen(f"{base}/health", timeout=1):
                return
        except OSError:
            time.sleep(0.5)
    sys.exit(f"OPA did not answer at {base}")


def capture_builds(work: Path) -> None:
    entrypoints = ["-e", "http/example/authz/allow", "-e", "http/example/authz/reasons"]
    opa(work, "build", "-b", "policy", "-o", "authz.tar.gz", "--revision", "rev-1")
    opa(work, "build", "-t", "plan", *entrypoints, "-b", "policy", "-o", "plan.tar.gz")
    opa(work, "build", "-t", "wasm", *entrypoints, "-b", "policy", "-o", "wasm.tar.gz")
    write("OpaManifest-bundle", member(work / "authz.tar.gz", ".manifest"))
    write("OpaManifest-plan-bundle", member(work / "plan.tar.gz", ".manifest"))
    write("OpaManifest-wasm-bundle", member(work / "wasm.tar.gz", ".manifest"))
    write("OpaPolicy-plan", member(work / "plan.tar.gz", "plan.json"))


def capture_server(work: Path) -> None:
    Sink.bundle = (work / "authz.tar.gz").read_bytes()
    sink = http.server.ThreadingHTTPServer(("127.0.0.1", free_port()), Sink)
    threading.Thread(target=sink.serve_forever, daemon=True).start()
    port = free_port()
    delays = "polling: {min_delay_seconds: 1, max_delay_seconds: 2}"
    (work / "config.yaml").write_text(
        f"""\
labels: {{region: eu-west-1}}
services:
  sink: {{url: "http://127.0.0.1:{sink.server_port}"}}
bundles:
  authz: {{service: sink, resource: bundles/authz.tar.gz, {delays}}}
  missing: {{service: sink, resource: bundles/missing.tar.gz, {delays}}}
decision_logs:
  service: sink
  reporting: {{min_delay_seconds: 1, max_delay_seconds: 2}}
  request_context: {{http: {{headers: [X-Request-Id]}}}}
nd_builtin_cache: true
status: {{service: sink}}
""",
        encoding="utf-8",
    )
    name = opa(
        work,
        *("run", "--server", "--addr", f"127.0.0.1:{port}"),
        *("--config-file", "/work/config.yaml"),
        detach=True,
    )
    base = f"http://127.0.0.1:{port}"
    try:
        wait_for(base)
        for _ in range(40):  # until the bundle is active
            with urllib.request.urlopen(f"{base}/v1/data/roles") as resp:
                if json.load(resp).get("result"):
                    break
            time.sleep(0.5)
        call(base, "GET", f"{DECIDE}/allow")
        secret = {"method": "GET", "user": "alice", "password": "pw", "token": "t"}
        call(
            base,
            "POST",
            f"{DECIDE}/allow",
            {"input": secret, "trace": "abc"},
            {"X-Request-Id": "req-1"},
        )
        call(base, "POST", DECIDE, {"input": {"method": "PUT", "user": "bob"}})
        call(base, "POST", f"{DECIDE}/pick", {"input": {"conflict": True}})
        call(base, "POST", "/v1/query", {"query": "data.http.example.authz.allow"})
        for _ in range(60):  # until every event is uploaded
            events = [e for p, b in Sink.received if p.startswith("/logs") for e in b]
            if len(events) >= 5:
                break
            time.sleep(0.5)
        time.sleep(3)  # one more status report, after the uploads
    finally:
        subprocess.run([CLI, "stop", "-t", "5", name], capture_output=True)
        sink.shutdown()
    events = [e for p, b in Sink.received if p.startswith("/logs") for e in b]
    reports = [b for p, b in Sink.received if p.startswith("/status")]
    if len(events) < 5 or not reports:
        sys.exit(f"OPA sent {len(events)} events and {len(reports)} status reports")
    # Each event's file, by the decision's path and whether it holds an input.
    labels = {
        (f"{PACKAGE}/allow", False): "get-without-input",
        (f"{PACKAGE}/allow", True): "masked-input",
        (PACKAGE, True): "object-result",
        (f"{PACKAGE}/pick", True): "evaluation-error",
    }
    for event in events:
        if "query" in event:
            write("OpaDecisionLogEvent-query", event)
        elif event["path"] != "roles":  # the reads that waited for the bundle
            label = labels[(event["path"], "input" in event)]
            write(f"OpaDecisionLogEvent-{label}", event)
    # Keep one report: the last that holds the refused upload's error beside the state
    # of the bundles and plugins. It is about 90 kB, with the Prometheus metrics that a
    # server always adds.
    refused = [r for r in reports if (r.get("decision_logs") or {}).get("code")]
    write("OpaStatusReport-running", (refused or reports)[-1])


def capture_authorization(work: Path) -> None:
    (work / "authz").mkdir()
    (work / "authz" / "authz.rego").write_text(AUTHZ_POLICY, encoding="utf-8")
    port = free_port()
    name = opa(
        work,
        *("run", "--server", "--addr", f"127.0.0.1:{port}"),
        *("--authentication=token", "--authorization=basic", "/work/authz"),
        detach=True,
    )
    base = f"http://127.0.0.1:{port}"
    requests = {
        "health-check": ("GET", "/health", None, {}),
        "bearer-token": (
            "GET",
            "/v1/data/http?pretty=true&explain=notes",
            None,
            {"Authorization": "Bearer s3cret"},
        ),
        "v1-data-body": ("POST", "/v1/data/http/example", {"input": {"x": 1}}, {}),
        "v0-data-string-body": ("POST", "/v0/data/http/example", "hello", {}),
        "default-decision-array-body": ("POST", "/", [1, 2.5, None], {}),
    }
    try:
        wait_for(base)
        for method, path, body, headers in requests.values():
            call(base, method, path, body, headers)
        time.sleep(1)
        logs = subprocess.run([CLI, "logs", name], capture_output=True, text=True)
    finally:
        subprocess.run([CLI, "stop", "-t", "5", name], capture_output=True)
    # What the policy printed, by the request's method and path; the last print wins.
    printed = {}
    for line in (logs.stdout + logs.stderr).splitlines():
        entry = json.loads(line)
        if "line" in entry:
            printed[(entry["req_method"], entry["req_path"])] = json.loads(entry["msg"])
    for label, (method, path, _, _) in requests.items():
        write(f"OpaAuthorizationInput-{label}", printed[(method, path.split("?")[0])])


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.json"):
        old.unlink()
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        for rel, text in POLICY.items():
            (work / "policy" / rel).parent.mkdir(parents=True, exist_ok=True)
            (work / "policy" / rel).write_text(text, encoding="utf-8")
        capture_builds(work)
        capture_server(work)
        capture_authorization(work)
    print(f"Wrote {len(list(OUT.glob('*.json')))} documents to {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
