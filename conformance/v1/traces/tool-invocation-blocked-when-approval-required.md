# Tool Invocation Blocked When Approval Required

State: Draft
Profile: `Core + Tools`
Condition: required when the implementation claims `Core + Approvals` or exposes approval-gated
tool invocation on the public binding
Scenario: one accepted tool invocation is blocked by unresolved approval and emits no artifact
Related Spec: `drafts/tools-v1.md`, `drafts/core-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible non-terminal `execution`
2. invoke one enabled `tool definition`
3. require unresolved approval before tool execution may begin

## Required Event Order

1. `tool.invoked`
2. `approval.created`
3. `tool.blocked`

## Terminal Condition

- the accepted invocation ends with outcome `blocked`
- at least one visible associated `approval` remains in `pending`

## Forbidden Missing Or Reordered Events

- `tool.blocked` before `tool.invoked`
- `approval.created` before `tool.invoked`
- `tool.blocked` before `approval.created`
- `artifact.emitted` before `tool.blocked`
- any `artifact.emitted` for the blocked invocation
- `tool.completed` after `tool.blocked`
- `tool.failed` after `tool.blocked`
- more than one terminal tool event for the same accepted invocation
- blocked invocation with no visible `pending` approval

## Conformance Hooks Exercised

- accepted invocation emits `tool.invoked` first
- unresolved approval requirement yields outcome `blocked`
- blocked invocation exposes visible pending approval linkage
- blocked invocation emits no artifact
