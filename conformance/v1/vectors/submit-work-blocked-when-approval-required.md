# Submit Work Blocked When Approval Required

State: Draft
Profile: `Core + Approvals`
Condition: required when the implementation claims `Core + Approvals` or exposes approval-gated
submit-work behavior
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

A ready `agent instance` accepts `submit work`, creates one new `execution`, and blocks it on
unresolved approval.

## Preconditions

- an `agent definition` exists in `enabled`
- an `agent instance` exists for that definition in `ready`
- the caller is authorized to address the target `agent instance`
- unresolved approval is required before progress may continue

## Request Sequence

1. Issue `POST /v1/agent-instances/{agent_instance_id}/submit-work` with `input`.

## Expected Result

- the request succeeds with `201 Created`
- the response body contains:
  - `execution_id`
  - `state`
  - `approval_ids`
- `state` equals `blocked`
- `approval_ids` identifies one or more visible `pending` approvals created for the new
  `execution`
- exactly one new `execution` is created

## Expected Created Or Changed Resources

- one new `execution`
- at least one visible `approval` resource in `pending`
- zero new `artifact` resources at command completion

## Expected Events

1. `execution.created`
2. `approval.created`
3. `execution.blocked`

## Forbidden Outcomes

- request failure with `approval_denied`
- execution state remains non-`blocked` at command completion
- blocked execution with no visible `pending` approval
- `approval.created` before `execution.created`

## Conformance Hooks Exercised

- approval-gated work creates a blocked execution and visible pending approval
- `approval.created` for new approval-gated submitted work follows `execution.created` and
  precedes `execution.blocked`
