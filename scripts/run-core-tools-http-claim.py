#!/usr/bin/env python3
import argparse
import sys
from datetime import date
from pathlib import Path

from http_claim_common import CORE_CHECKS, CORE_TRACES, CORE_VECTORS, ClaimFailure, Runner, render_report, run_checks


TOOL_VECTORS = [
    "tool-definition-listing-includes-visible-tool.md",
    "tool-definition-inspection-exposes-state.md",
    "missing-tool-definition-inspection-returns-not-found.md",
    "invoke-tool-success.md",
    "invoke-tool-rejected-when-tool-disabled.md",
    "invoke-tool-rejected-when-tool-deleted.md",
    "invoke-tool-denied-by-capability.md",
]


def check_tool_definition_list(runner: Runner) -> None:
    response = runner.get("/v1/tools")
    if response.status != 200:
        raise ClaimFailure(f"expected status 200, got {response.status}")
    if not any(item["tool_id"] == "tool-echo" for item in response.body):
        raise ClaimFailure("tool-echo missing")


def check_tool_definition_get(runner: Runner) -> None:
    response = runner.get("/v1/tools/tool-echo")
    if response.status != 200:
        raise ClaimFailure(f"expected status 200, got {response.status}")
    if response.body["state"] != "enabled":
        raise ClaimFailure("expected enabled tool")


def check_missing_tool_definition(runner: Runner) -> None:
    response = runner.get("/v1/tools/missing-tool")
    if response.status != 404:
        raise ClaimFailure(f"expected status 404, got {response.status}")
    if response.body.get("error", {}).get("code") != "not_found":
        raise ClaimFailure("expected not_found")


def check_invoke_tool_success(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/execution-running/tools/tool-echo/invoke",
        {"input": {"message": "tool hello"}},
    )
    if response.status != 200:
        raise ClaimFailure(f"expected status 200, got {response.status}")
    if response.body["execution_id"] != "execution-running":
        raise ClaimFailure("execution id mismatch")
    if response.body["tool_result"]["tool_id"] != "tool-echo":
        raise ClaimFailure("tool id mismatch")
    if response.body["tool_result"]["outcome"] != "completed":
        raise ClaimFailure("tool outcome mismatch")
    if response.body["tool_result"]["result"]["echo"]["message"] != "tool hello":
        raise ClaimFailure("tool echo mismatch")

    execution = runner.get("/v1/executions/execution-running")
    if execution.status != 200:
        raise ClaimFailure(f"expected status 200, got {execution.status}")
    if "tool_derived_material" in execution.body["context"]:
        raise ClaimFailure("tool_derived_material should remain absent")
    if execution.body["recent_events"][2]["event"] != "tool.invoked":
        raise ClaimFailure("tool.invoked missing")
    if execution.body["recent_events"][3]["event"] != "tool.completed":
        raise ClaimFailure("tool.completed missing")


def check_invoke_tool_disabled(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/execution-running/tools/tool-disabled/invoke",
        {"input": {"message": "tool hello"}},
    )
    if response.status != 409:
        raise ClaimFailure(f"expected status 409, got {response.status}")
    if response.body.get("error", {}).get("code") != "invalid_state":
        raise ClaimFailure("expected invalid_state")


def check_invoke_tool_deleted(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/execution-running/tools/tool-deleted/invoke",
        {"input": {"message": "tool hello"}},
    )
    if response.status != 409:
        raise ClaimFailure(f"expected status 409, got {response.status}")
    if response.body.get("error", {}).get("code") != "invalid_state":
        raise ClaimFailure("expected invalid_state")


def check_invoke_tool_capability_denied(runner: Runner) -> None:
    response = runner.post(
        "/v1/executions/execution-running/tools/tool-capability-denied/invoke",
        {"input": {"message": "tool hello"}},
    )
    if response.status != 403:
        raise ClaimFailure(f"expected status 403, got {response.status}")
    if response.body.get("error", {}).get("code") != "capability_denied":
        raise ClaimFailure("expected capability_denied")


TOOL_CHECKS = [
    ("tool-definition-listing-includes-visible-tool.md", check_tool_definition_list),
    ("tool-definition-inspection-exposes-state.md", check_tool_definition_get),
    ("missing-tool-definition-inspection-returns-not-found.md", check_missing_tool_definition),
    ("invoke-tool-success.md", check_invoke_tool_success),
    ("invoke-tool-rejected-when-tool-disabled.md", check_invoke_tool_disabled),
    ("invoke-tool-rejected-when-tool-deleted.md", check_invoke_tool_deleted),
    ("invoke-tool-denied-by-capability.md", check_invoke_tool_capability_denied),
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--implementation-name", required=True)
    parser.add_argument("--implementation-version", required=True)
    parser.add_argument("--runner-identity", default="scripts/run-core-tools-http-claim.py")
    parser.add_argument("--output", required=True, help="path to the markdown report to write")
    parser.add_argument("--run-date", default=str(date.today()))
    args = parser.parse_args()

    runner = Runner(args.base_url)

    try:
        results = run_checks(runner, CORE_CHECKS + TOOL_CHECKS)
    except ClaimFailure as error:
        print(f"claim failure: {error}", file=sys.stderr)
        return 1

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    render_report(
        output_path=output_path,
        title="Core Tools HTTP",
        claim_path="conformance/v1/claims/core-tools-http-claim-seed.md",
        implementation_name=args.implementation_name,
        implementation_version=args.implementation_version,
        runner_identity=args.runner_identity,
        run_date=args.run_date,
        vectors=CORE_VECTORS + TOOL_VECTORS,
        traces=CORE_TRACES,
        results=results,
        notes=[
            "claimed surface remains `Core + Tools` over `HTTP Binding v1`",
            "excluded optional surfaces were not exercised",
            "generated by the standalone external conformance runner",
        ],
    )
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
