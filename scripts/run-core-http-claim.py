#!/usr/bin/env python3
import argparse
import json
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Callable


VECTORS = [
    "agent-definition-listing-includes-visible-definition.md",
    "agent-definition-inspection-exposes-state.md",
    "disable-agent-definition-transitions-to-disabled.md",
    "enable-agent-definition-transitions-to-enabled.md",
    "agent-instance-listing-includes-visible-instance.md",
    "agent-instance-inspection-exposes-definition-link-and-state.md",
    "pause-agent-instance-transitions-to-paused.md",
    "resume-agent-instance-transitions-to-ready.md",
    "terminate-agent-instance-transitions-to-terminated.md",
    "session-listing-includes-visible-session.md",
    "session-inspection-exposes-state.md",
    "close-session-transitions-to-closed.md",
    "submit-work-success.md",
    "execution-listing-includes-visible-execution.md",
    "cancel-execution-transitions-to-canceled.md",
    "cancel-execution-rejected-when-already-terminal.md",
    "submit-work-rejected-when-instance-paused.md",
    "delegate-execution-success.md",
    "delegate-execution-rejected-when-parent-missing.md",
    "delegate-execution-rejected-when-parent-terminal.md",
    "delegate-execution-rejected-when-target-instance-missing.md",
    "delegate-execution-rejected-when-target-instance-not-ready.md",
    "delegate-execution-rejected-when-target-instance-equals-parent-owner.md",
    "missing-execution-inspection-returns-not-found.md",
    "failed-execution-inspection-is-not-transport-error.md",
    "context-snapshot-preserves-provenance.md",
    "context-snapshot-omits-absent-contribution-sections.md",
    "inherited-lineage-material-visible-on-child-execution.md",
    "inherited-lineage-material-omitted-without-visible-lineage.md",
    "session-material-visible-on-session-attached-execution.md",
    "execution-snapshot-separates-sections.md",
]

TRACES = [
    "execution-completion-terminal.md",
    "execution-cancel-terminal.md",
    "execution-lifecycle-minimal.md",
    "execution-failure-terminal.md",
    "delegated-execution-minimal.md",
]


class ClaimFailure(Exception):
    pass


@dataclass
class Response:
    status: int
    body: dict | list | None


class Runner:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get(self, path: str) -> Response:
        return self.request("GET", path)

    def post(self, path: str, body: dict | None = None, headers: dict[str, str] | None = None) -> Response:
        return self.request("POST", path, body=body, headers=headers)

    def request(
        self,
        method: str,
        path: str,
        body: dict | None = None,
        headers: dict[str, str] | None = None,
    ) -> Response:
        request_headers = {"Accept": "application/json"}
        if headers:
            request_headers.update(headers)

        data = None
        if body is not None:
            request_headers["Content-Type"] = "application/json"
            data = json.dumps(body).encode("utf-8")

        request = urllib.request.Request(
            f"{self.base_url}{path}",
            method=method,
            data=data,
            headers=request_headers,
        )

        try:
            with urllib.request.urlopen(request) as response:
                payload = response.read()
                return Response(response.status, decode_json(payload))
        except urllib.error.HTTPError as error:
            payload = error.read()
            return Response(error.code, decode_json(payload))


def decode_json(payload: bytes) -> dict | list | None:
    if not payload:
        return None
    return json.loads(payload.decode("utf-8"))


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise ClaimFailure(message)


def expect_status(response: Response, status: int) -> None:
    expect(response.status == status, f"expected status {status}, got {response.status}")


def expect_error_code(response: Response, code: str) -> None:
    expect_status(response, 409 if code != "not_found" else 404)
    expect(isinstance(response.body, dict), "expected error body object")
    expect(response.body.get("error", {}).get("code") == code, f"expected error code {code}")


def run_claim(runner: Runner) -> dict[str, str]:
    results: dict[str, str] = {}

    checks: list[tuple[str, Callable[[Runner], None]]] = [
        ("agent-definition-listing-includes-visible-definition.md", check_agent_definition_list),
        ("agent-definition-inspection-exposes-state.md", check_agent_definition_get),
        ("disable-agent-definition-transitions-to-disabled.md", check_agent_definition_disable),
        ("enable-agent-definition-transitions-to-enabled.md", check_agent_definition_enable),
        ("agent-instance-listing-includes-visible-instance.md", check_agent_instance_list),
        ("agent-instance-inspection-exposes-definition-link-and-state.md", check_agent_instance_get),
        ("pause-agent-instance-transitions-to-paused.md", check_agent_instance_pause),
        ("resume-agent-instance-transitions-to-ready.md", check_agent_instance_resume),
        ("session-listing-includes-visible-session.md", check_session_list),
        ("session-inspection-exposes-state.md", check_session_get),
        ("submit-work-success.md", check_submit_work_success),
        ("execution-listing-includes-visible-execution.md", check_execution_list),
        ("submit-work-rejected-when-instance-paused.md", check_submit_work_paused_reject),
        ("delegate-execution-success.md", check_delegate_execution_success),
        ("delegate-execution-rejected-when-parent-missing.md", check_delegate_missing_parent),
        ("delegate-execution-rejected-when-parent-terminal.md", check_delegate_terminal_parent),
        ("delegate-execution-rejected-when-target-instance-missing.md", check_delegate_missing_target),
        ("delegate-execution-rejected-when-target-instance-not-ready.md", check_delegate_target_not_ready),
        ("delegate-execution-rejected-when-target-instance-equals-parent-owner.md", check_delegate_self_target),
        ("missing-execution-inspection-returns-not-found.md", check_missing_execution),
        ("failed-execution-inspection-is-not-transport-error.md", check_failed_execution_inspection),
        ("context-snapshot-preserves-provenance.md", check_context_preserves_provenance),
        ("context-snapshot-omits-absent-contribution-sections.md", check_context_omits_absent_sections),
        ("inherited-lineage-material-visible-on-child-execution.md", check_inherited_lineage_visible),
        ("inherited-lineage-material-omitted-without-visible-lineage.md", check_inherited_lineage_omitted),
        ("session-material-visible-on-session-attached-execution.md", check_session_material_visible),
        ("execution-snapshot-separates-sections.md", check_execution_snapshot_separation),
        ("execution-completion-terminal.md", check_execution_completion_terminal),
        ("execution-cancel-terminal.md", check_execution_cancel_terminal),
        ("execution-lifecycle-minimal.md", check_execution_lifecycle_minimal),
        ("execution-failure-terminal.md", check_execution_failure_terminal),
        ("delegated-execution-minimal.md", check_delegated_execution_minimal),
        ("close-session-transitions-to-closed.md", check_session_close),
        ("cancel-execution-transitions-to-canceled.md", check_cancel_execution_success),
        ("cancel-execution-rejected-when-already-terminal.md", check_cancel_execution_terminal_reject),
        ("terminate-agent-instance-transitions-to-terminated.md", check_agent_instance_terminate),
    ]

    for artifact, check in checks:
        try:
            check(runner)
        except ClaimFailure as error:
            raise ClaimFailure(f"{artifact}: {error}") from error
        results[artifact] = "pass"

    return results


def check_agent_definition_list(runner: Runner) -> None:
    response = runner.get("/v1/agent-definitions")
    expect_status(response, 200)
    expect(any(item["agent_definition_id"] == "agent-def-enabled" for item in response.body), "enabled definition missing")


def check_agent_definition_get(runner: Runner) -> None:
    response = runner.get("/v1/agent-definitions/agent-def-enabled")
    expect_status(response, 200)
    expect(response.body["state"] == "enabled", "expected enabled definition")


def check_agent_definition_disable(runner: Runner) -> None:
    response = runner.post("/v1/agent-definitions/agent-def-enabled/disable")
    expect_status(response, 200)
    expect(response.body["state"] == "disabled", "expected disabled definition")


def check_agent_definition_enable(runner: Runner) -> None:
    runner.post("/v1/agent-definitions/agent-def-enabled/disable")
    response = runner.post("/v1/agent-definitions/agent-def-enabled/enable")
    expect_status(response, 200)
    expect(response.body["state"] == "enabled", "expected re-enabled definition")


def check_agent_instance_list(runner: Runner) -> None:
    response = runner.get("/v1/agent-instances")
    expect_status(response, 200)
    expect(any(item["agent_instance_id"] == "agent-inst-primary" for item in response.body), "primary instance missing")


def check_agent_instance_get(runner: Runner) -> None:
    response = runner.get("/v1/agent-instances/agent-inst-primary")
    expect_status(response, 200)
    expect(response.body["agent_definition_id"] == "agent-def-enabled", "wrong definition link")
    expect(response.body["state"] == "ready", "expected ready instance")


def check_agent_instance_pause(runner: Runner) -> None:
    response = runner.post("/v1/agent-instances/agent-inst-primary/pause")
    expect_status(response, 200)
    expect(response.body["state"] == "paused", "expected paused instance")


def check_agent_instance_resume(runner: Runner) -> None:
    runner.post("/v1/agent-instances/agent-inst-primary/pause")
    response = runner.post("/v1/agent-instances/agent-inst-primary/resume")
    expect_status(response, 200)
    expect(response.body["state"] == "ready", "expected resumed instance")


def check_agent_instance_terminate(runner: Runner) -> None:
    response = runner.post("/v1/agent-instances/agent-inst-helper/terminate")
    expect_status(response, 200)
    expect(response.body["state"] == "terminated", "expected terminated instance")


def check_session_list(runner: Runner) -> None:
    response = runner.get("/v1/sessions")
    expect_status(response, 200)
    expect(any(item["session_id"] == "session-open" for item in response.body), "open session missing")


def check_session_get(runner: Runner) -> None:
    response = runner.get("/v1/sessions/session-open")
    expect_status(response, 200)
    expect(response.body["state"] == "open", "expected open session")


def check_session_close(runner: Runner) -> None:
    response = runner.post("/v1/sessions/session-open/close")
    expect_status(response, 200)
    expect(response.body["state"] == "closed", "expected closed session")


def check_submit_work_success(runner: Runner) -> None:
    response = runner.post(
        "/v1/agent-instances/agent-inst-primary/submit-work",
        {"input": {"message": "hello"}, "references": [{"kind": "doc", "id": "doc-1"}]},
    )
    expect_status(response, 201)
    execution_id = response.body["execution_id"]
    expect(response.body["state"] == "pending", "expected pending execution")
    expect("approval_ids" not in response.body, "approval_ids should be absent")

    context = runner.get(f"/v1/executions/{execution_id}/context")
    expect_status(context, 200)
    expect(context.body["explicit_input"]["message"] == "hello", "explicit input missing")
    expect(context.body["explicit_references"][0]["id"] == "doc-1", "reference missing")


def check_execution_list(runner: Runner) -> None:
    response = runner.get("/v1/executions")
    expect_status(response, 200)
    expect(any(item["execution_id"] == "execution-running" for item in response.body), "running execution missing")


def check_cancel_execution_success(runner: Runner) -> None:
    create = runner.post("/v1/agent-instances/agent-inst-primary/submit-work", {"input": {"message": "cancel me"}})
    expect_status(create, 201)
    execution_id = create.body["execution_id"]

    response = runner.post(f"/v1/executions/{execution_id}/cancel")
    expect_status(response, 200)
    expect(response.body["state"] == "canceled", "expected canceled state")


def check_cancel_execution_terminal_reject(runner: Runner) -> None:
    response = runner.post("/v1/executions/execution-completed/cancel")
    expect_error_code(response, "invalid_state")


def check_submit_work_paused_reject(runner: Runner) -> None:
    response = runner.post("/v1/agent-instances/agent-inst-paused/submit-work", {"input": {"message": "hi"}})
    expect_error_code(response, "invalid_state")


def check_delegate_execution_success(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/execution-running/delegate",
        {
            "target_agent_instance_id": "agent-inst-helper",
            "input": {"message": "child", "synthetic_outcome": "failed"},
            "references": [{"kind": "doc", "id": "child-ref"}],
        },
    )
    expect_status(response, 201)
    expect(response.body["parent_execution_id"] == "execution-running", "parent id missing")
    expect(response.body["agent_instance_id"] == "agent-inst-helper", "target instance missing")
    expect(response.body["session_id"] == "session-open", "session should carry")


def check_delegate_missing_parent(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/missing-parent/delegate",
        {"target_agent_instance_id": "agent-inst-helper", "input": {"message": "child"}},
    )
    expect_error_code(response, "not_found")


def check_delegate_terminal_parent(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/execution-completed/delegate",
        {"target_agent_instance_id": "agent-inst-helper", "input": {"message": "child"}},
    )
    expect_error_code(response, "invalid_state")


def check_delegate_missing_target(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/execution-running/delegate",
        {"target_agent_instance_id": "missing-target", "input": {"message": "child"}},
    )
    expect_error_code(response, "not_found")


def check_delegate_target_not_ready(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/execution-running/delegate",
        {"target_agent_instance_id": "agent-inst-paused", "input": {"message": "child"}},
    )
    expect_error_code(response, "invalid_state")


def check_delegate_self_target(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/execution-running/delegate",
        {"target_agent_instance_id": "agent-inst-primary", "input": {"message": "child"}},
    )
    expect_error_code(response, "invalid_state")


def check_missing_execution(runner: Runner) -> None:
    response = runner.get("/v1/executions/missing")
    expect_error_code(response, "not_found")


def check_failed_execution_inspection(runner: Runner) -> None:
    response = runner.get("/v1/executions/execution-failed")
    expect_status(response, 200)
    expect(response.body["state"] == "failed", "failed execution should remain inspectable")


def check_context_preserves_provenance(runner: Runner) -> None:
    response = runner.post(
        "/v1/agent-instances/agent-inst-primary/submit-work",
        {
            "input": {"message": "hello"},
            "session_id": "session-open",
            "references": [{"kind": "doc", "id": "doc-1"}],
        },
    )
    expect_status(response, 201)
    execution_id = response.body["execution_id"]

    context = runner.get(f"/v1/executions/{execution_id}/context")
    expect_status(context, 200)
    expect(context.body["explicit_input"]["message"] == "hello", "explicit input missing")
    expect(context.body["explicit_references"][0]["id"] == "doc-1", "explicit reference missing")
    expect(context.body["session_material"]["scope"] == "session-open", "session material missing")
    expect("implementation_supplied" not in context.body, "implementation_supplied should be absent")


def check_context_omits_absent_sections(runner: Runner) -> None:
    response = runner.post(
        "/v1/agent-instances/agent-inst-primary/submit-work",
        {"input": {"message": "standalone"}},
    )
    expect_status(response, 201)
    execution_id = response.body["execution_id"]

    context = runner.get(f"/v1/executions/{execution_id}/context")
    expect_status(context, 200)
    expect(context.body["explicit_references"] == [], "explicit references should remain empty")
    expect("session_material" not in context.body, "session_material should be absent")
    expect("inherited_lineage_material" not in context.body, "lineage should be absent")


def check_inherited_lineage_visible(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/execution-running/delegate",
        {
            "target_agent_instance_id": "agent-inst-helper",
            "input": {"message": "child"},
            "references": [{"kind": "doc", "id": "child-ref"}],
        },
    )
    expect_status(response, 201)
    execution_id = response.body["execution_id"]

    context = runner.get(f"/v1/executions/{execution_id}/context")
    expect_status(context, 200)
    expect(context.body["session_material"]["scope"] == "session-open", "session material missing")
    expect(
        context.body["inherited_lineage_material"]["parent_execution_id"] == "execution-running",
        "parent execution id missing",
    )


def check_inherited_lineage_omitted(runner: Runner) -> None:
    response = runner.post("/v1/agent-instances/agent-inst-primary/submit-work", {"input": {"message": "hello"}})
    expect_status(response, 201)
    execution_id = response.body["execution_id"]
    context = runner.get(f"/v1/executions/{execution_id}/context")
    expect_status(context, 200)
    expect("inherited_lineage_material" not in context.body, "lineage should be absent")


def check_session_material_visible(runner: Runner) -> None:
    response = runner.post(
        "/v1/agent-instances/agent-inst-primary/submit-work",
        {"input": {"message": "hello"}, "session_id": "session-open"},
    )
    expect_status(response, 201)
    execution_id = response.body["execution_id"]
    context = runner.get(f"/v1/executions/{execution_id}/context")
    expect_status(context, 200)
    expect(context.body["session_material"]["scope"] == "session-open", "session material missing")


def check_execution_snapshot_separation(runner: Runner) -> None:
    response = runner.get("/v1/executions/execution-running")
    expect_status(response, 200)
    expect("context" in response.body, "context missing")
    expect("recent_events" in response.body, "recent_events missing")
    expect("recent_events" not in response.body["context"], "events must stay out of context")


def check_execution_completion_terminal(runner: Runner) -> None:
    response = runner.post("/v1/agent-instances/agent-inst-primary/submit-work", {"input": {"message": "run"}})
    expect_status(response, 201)
    execution_id = response.body["execution_id"]
    wait_for_terminal_state(runner, execution_id, "completed", "execution.completed")


def check_execution_cancel_terminal(runner: Runner) -> None:
    create = runner.post("/v1/agent-instances/agent-inst-primary/submit-work", {"input": {"message": "cancel me"}})
    expect_status(create, 201)
    execution_id = create.body["execution_id"]

    response = runner.post(f"/v1/executions/{execution_id}/cancel")
    expect_status(response, 200)
    snapshot = runner.get(f"/v1/executions/{execution_id}")
    expect_status(snapshot, 200)
    expect(snapshot.body["state"] == "canceled", "execution should be canceled")
    expect(snapshot.body["recent_events"][-1]["event"] == "execution.canceled", "cancel event missing")


def check_execution_lifecycle_minimal(runner: Runner) -> None:
    response = runner.post("/v1/agent-instances/agent-inst-primary/submit-work", {"input": {"message": "run"}})
    expect_status(response, 201)
    execution_id = response.body["execution_id"]
    snapshot = wait_for_terminal_state(runner, execution_id, "completed", "execution.completed")
    expect(snapshot["recent_events"][0]["event"] == "execution.created", "execution.created missing")
    expect(snapshot["recent_events"][1]["event"] == "execution.state_changed", "state change missing")


def check_execution_failure_terminal(runner: Runner) -> None:
    response = runner.post(
        "/v1/agent-instances/agent-inst-primary/submit-work",
        {"input": {"message": "run", "synthetic_outcome": "failed"}},
    )
    expect_status(response, 201)
    execution_id = response.body["execution_id"]
    wait_for_terminal_state(runner, execution_id, "failed", "execution.failed")


def check_delegated_execution_minimal(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/execution-running/delegate",
        {"target_agent_instance_id": "agent-inst-helper", "input": {"message": "child"}},
    )
    expect_status(response, 201)
    execution_id = response.body["execution_id"]
    snapshot = wait_for_terminal_state(runner, execution_id, "completed", "execution.completed")
    expect(snapshot["recent_events"][0]["event"] == "execution.created", "child create missing")
    expect(snapshot["recent_events"][1]["event"] == "execution.delegated", "delegate event missing")


def wait_for_terminal_state(runner: Runner, execution_id: str, expected_state: str, expected_terminal_event: str) -> dict:
    import time

    deadline = time.time() + 2.0
    while time.time() < deadline:
        response = runner.get(f"/v1/executions/{execution_id}")
        expect_status(response, 200)
        body = response.body
        if body["state"] == expected_state:
            expect(body["recent_events"][-1]["event"] == expected_terminal_event, "terminal event mismatch")
            return body
        time.sleep(0.05)

    raise ClaimFailure(f"execution {execution_id} did not reach {expected_state}")


def render_report(
    output_path: Path,
    implementation_name: str,
    implementation_version: str,
    runner_identity: str,
    run_date: str,
    results: dict[str, str],
) -> None:
    lines = [
        f"# {implementation_name} Core HTTP {run_date}",
        "",
        "Implementation Claim: `conformance/v1/claims/core-http-claim-seed.md`",
        f"Runner Identity: `{runner_identity}`",
        f"Run Date: `{run_date}`",
        "",
        "## Vectors Executed",
        "",
    ]
    lines.extend([f"- `{artifact}`" for artifact in VECTORS])
    lines.extend(
        [
            "",
            "## Traces Executed",
            "",
        ]
    )
    lines.extend([f"- `{artifact}`" for artifact in TRACES])
    lines.extend(["", "## Results", ""])
    for artifact in VECTORS + TRACES:
        lines.append(f"- `{artifact}`: {results[artifact]}")

    lines.extend(
        [
            "",
            "## Overall Decision",
            "",
            "- pass",
            "",
            "## Notes",
            "",
            "- claimed surface remains `Core` over `HTTP Binding v1`",
            "- excluded optional surfaces were not exercised",
            "- generated by the standalone external conformance runner",
        ]
    )

    output_path.write_text("\n".join(lines) + "\n", encoding="ascii")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--implementation-name", required=True)
    parser.add_argument("--implementation-version", required=True)
    parser.add_argument("--runner-identity", default="scripts/run-core-http-claim.py")
    parser.add_argument(
        "--output",
        required=True,
        help="path to the markdown report to write",
    )
    parser.add_argument("--run-date", default=str(date.today()))
    args = parser.parse_args()

    runner = Runner(args.base_url)

    try:
        results = run_claim(runner)
    except ClaimFailure as error:
        print(f"claim failure: {error}", file=sys.stderr)
        return 1

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    render_report(
        output_path=output_path,
        implementation_name=args.implementation_name,
        implementation_version=args.implementation_version,
        runner_identity=args.runner_identity,
        run_date=args.run_date,
        results=results,
    )
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
