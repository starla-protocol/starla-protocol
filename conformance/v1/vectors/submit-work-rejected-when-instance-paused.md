# Submit Work Rejected When Instance Paused

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

A paused `agent instance` rejects `submit work`.

## Preconditions

- an `agent definition` exists in `enabled`
- an `agent instance` exists for that definition in `paused`
- the caller is authorized to address the target `agent instance`

## Request Sequence

1. Issue `POST /v1/agent-instances/{agent_instance_id}/submit-work` with `input`.

## Expected Result

- the request fails with `409 Conflict`
- the returned protocol error class is `invalid_state`
- the response body contains `error.code` equal to `invalid_state`
- no new `execution` is created
- the target `agent instance` remains in `paused`

## Expected Created Or Changed Resources

- zero new `execution` resources
- zero new `approval` resources
- zero new `artifact` resources

## Expected Events

- no `execution.created` event is emitted
- no execution lifecycle event is emitted for rejected work

## Forbidden Outcomes

- request success
- implicit auto-resume of the paused instance
- creation of a blocked or failed execution as a substitute for rejection

## Conformance Hooks Exercised

- `paused` rejects `submit work`
- rejected `submit work` does not create an execution
- invalid state is surfaced as `invalid_state`
