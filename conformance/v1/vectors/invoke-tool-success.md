# Invoke Tool Success

State: Draft
Profile: `Core + Tools`
Binding: `HTTP v1`
Related Spec: `drafts/tools-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

One enabled tool is invoked successfully by one visible execution.

## Preconditions

- one visible non-terminal `execution` exists
- one visible `tool definition` exists in `enabled`
- capability checks pass
- no conflicting idempotency key has been used

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/tools/{tool_id}/invoke` with:
   - `input`
   - optional `Idempotency-Key` header

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `tool_id`
  - `outcome`
- `outcome` equals `completed`
- `artifact_ids`, if present, identify artifacts emitted by the invoking `execution` during the
  same accepted invocation

## Expected Created Or Changed Resources

- zero or more emitted `artifact` resources
- zero changed tool lifecycle states

## Expected Events

1. `tool.invoked`
2. `tool.completed`

## Forbidden Outcomes

- `tool.failed`
- `tool.blocked`
- visible tool-derived contribution relabeled as another contribution class

## Conformance Hooks Exercised

- enabled tools accept `invoke tool`
- successful visible tool contribution appears only as `tool_derived_material`
- successful emitted artifacts preserve `artifact-provenance`
