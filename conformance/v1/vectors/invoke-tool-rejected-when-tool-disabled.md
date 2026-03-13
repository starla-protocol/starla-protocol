# Invoke Tool Rejected When Tool Disabled

State: Draft
Profile: `Core + Tools`
Binding: `HTTP v1`
Related Spec: `drafts/tools-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

One disabled tool rejects invocation.

## Preconditions

- one visible non-terminal `execution` exists
- one visible `tool definition` exists in `disabled`

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/tools/{tool_id}/invoke` with `input`.

## Expected Result

- the request fails with `409 Conflict`
- the returned protocol error class is `invalid_state`
- the response body contains `error.code` equal to `invalid_state`

## Expected Created Or Changed Resources

- zero emitted `artifact` resources
- zero changed tool lifecycle states

## Expected Events

- no `tool.invoked` event is emitted
- no `tool.completed` event is emitted
- no `tool.failed` event is emitted

## Forbidden Outcomes

- request success
- implicit tool enablement
- invocation reported as blocked instead of rejected

## Conformance Hooks Exercised

- `disabled` rejects `invoke tool`
