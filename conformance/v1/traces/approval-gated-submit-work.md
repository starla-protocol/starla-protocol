# Approval-Gated Submit Work

State: Draft
Profile: `Core + Approvals`
Condition: required when the implementation claims `Core + Approvals` or exposes approval-gated
submit-work behavior
Scenario: one `submit work` request creates one new `execution`, creates one new visible
`approval`, and blocks the execution pending resolution
Related Spec: `drafts/core-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one `ready` `agent instance`
2. issue `submit work`
3. require unresolved approval before progress may continue

## Required Event Order

1. `execution.created`
2. `approval.created`
3. `execution.blocked`

## Terminal Condition

- the created `execution` is visible in `blocked`
- at least one visible associated `approval` remains in `pending`

## Forbidden Missing Or Reordered Events

- `approval.created` before `execution.created`
- `execution.blocked` before `execution.created`
- `execution.completed` before approval resolution
- blocked execution with no visible `pending` approval

## Conformance Hooks Exercised

- approval-gated work creates a blocked execution and visible pending approval
- `approval.created` for approval-gated submitted work follows `execution.created` and precedes
  `execution.blocked`
