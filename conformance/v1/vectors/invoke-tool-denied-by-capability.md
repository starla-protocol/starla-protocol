# Invoke Tool Denied By Capability

State: Draft
Profile: `Core + Tools`
Binding: `HTTP v1`
Related Spec: `drafts/tools-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

Tool invocation is denied by capability policy at the tool boundary.

## Preconditions

- one visible non-terminal `execution` exists
- one visible `tool definition` exists in `enabled`
- capability checks fail at the tool boundary

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/tools/{tool_id}/invoke` with `input`.

## Expected Result

- the request fails with `403 Forbidden`
- the returned protocol error class is `capability_denied`
- the response body contains `error.code` equal to `capability_denied`

## Expected Created Or Changed Resources

- zero emitted `artifact` resources
- zero changed tool lifecycle states

## Expected Events

- no `tool.invoked` event is emitted
- no `tool.completed` event is emitted
- no `tool.failed` event is emitted

## Forbidden Outcomes

- request success
- invocation reported as blocked instead of denied
- visible tool-derived contribution emitted despite denial

## Conformance Hooks Exercised

- capability denial prevents `invoke tool`
