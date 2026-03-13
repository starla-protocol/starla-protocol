# Session Material Visible On Session-Attached Execution

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/context-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

Visible session-scoped material appears on an execution attached to that `session`.

## Preconditions

- one visible `session` exists in `open` or `closed`
- one visible `execution` exists and is attached to that `session`
- the `session` has visible session-scoped material at the context boundary

## Request Sequence

1. Issue `GET /v1/executions/{execution_id}/context`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `agent_instance_id`
  - `session_id`
  - `session_material`
- `session_material` appears only in `session_material`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states

## Forbidden Outcomes

- visible session-scoped material omitted
- session-scoped material relabeled as `explicit_input`
- session-scoped material relabeled as `implementation_supplied`

## Conformance Hooks Exercised

- session-scoped material contributes only to work attached to that `session`
- session-scoped material remains distinguishable from direct caller input
