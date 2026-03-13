# Invoke Tool Idempotent Replay Preserves Result

State: Draft
Profile: `Core + Tools`
Condition: required when the implementation claims `HTTP Binding v1` and claims or exposes
idempotent `invoke tool`
Binding: `HTTP v1`
Related Spec: `drafts/tools-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

Idempotent replay of the same tool request resolves to the same visible result.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible non-terminal `execution` exists
- one visible `tool definition` exists in `enabled`
- the implementation exposes idempotent `invoke tool`

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/tools/{tool_id}/invoke` with:
   - `input`
   - one `Idempotency-Key` header
2. Repeat the same request with the same `Idempotency-Key` header.

## Expected Result

- both requests succeed with `200 OK`
- both response bodies contain:
  - `tool_id`
  - `outcome`
- both responses identify the same visible result
- if either response includes `artifact_ids`, the other response includes the same visible
  `artifact_ids`

## Expected Created Or Changed Resources

- exactly one visible invocation result
- zero duplicate visible artifacts created by replay alone

## Forbidden Outcomes

- replay changes the visible `outcome`
- replay creates duplicate visible artifact identifiers
- replay rewrites the visible `tool_id`

## Conformance Hooks Exercised

- idempotent replay preserves the same visible tool result
