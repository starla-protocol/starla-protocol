# Invoke Tool Blocked When Approval Required

State: Draft
Profile: `Core + Tools`
Condition: required when the implementation claims `Core + Approvals` or exposes approval-gated
tool invocation
Binding: `HTTP v1`
Related Spec: `drafts/tools-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

One enabled tool requires unresolved approval before execution may begin.

## Preconditions

- one visible non-terminal `execution` exists
- one visible `tool definition` exists in `enabled`
- capability checks pass
- unresolved approval is required before tool execution may begin

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/tools/{tool_id}/invoke` with `input`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `tool_id`
  - `outcome`
  - `approval_ids`
- `outcome` equals `blocked`
- `approval_ids` identifies one or more visible pending approvals created or attached for the
  invocation
- `result` is absent
- `artifact_ids` is absent

## Expected Created Or Changed Resources

- zero emitted `artifact` resources
- zero changed tool lifecycle states
- zero visible `tool_derived_material` sections
- one or more visible `approval` resources in `pending`

## Expected Events

1. `tool.invoked`
2. `approval.created`
3. `tool.blocked`

## Forbidden Outcomes

- `403 Forbidden` with `approval_denied` for unresolved approval requirement
- blocked result with no visible pending approval linkage
- `tool.completed`
- `tool.failed`
- `artifact.emitted`
- visible tool-derived contribution

## Conformance Hooks Exercised

- unresolved approval requirement yields outcome `blocked`
- blocked invocation exposes visible pending approval linkage
- blocked invocation emits no artifacts
- blocked invocation emits no visible tool-derived contribution
