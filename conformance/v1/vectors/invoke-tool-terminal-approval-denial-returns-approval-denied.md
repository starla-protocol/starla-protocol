# Invoke Tool Terminal Approval Denial Returns Approval Denied

State: Draft
Profile: `Core + Tools`
Condition: required when the implementation exposes visible terminal approval denial during tool
invocation on the public binding
Binding: `HTTP v1`
Related Spec: `drafts/tools-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible tool invocation is denied by one visible terminal approval decision.

## Preconditions

- one visible non-terminal `execution` exists
- one visible enabled `tool definition` exists
- the implementation exposes visible terminal approval denial during tool invocation

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/tools/{tool_id}/invoke`.

## Expected Result

- the request fails with `403 Forbidden`
- the response body uses the normal error envelope
- `error.code` equals `approval_denied`

## Expected Created Or Changed Resources

- zero visible terminal tool success outcomes
- zero visible tool result payloads

## Forbidden Outcomes

- `200 OK` with `outcome = blocked` for a terminal denial
- `403 Forbidden` with any `error.code` other than `approval_denied`
- visible successful tool completion after terminal approval denial

## Conformance Hooks Exercised

- visible terminal approval denial returns `approval_denied`
