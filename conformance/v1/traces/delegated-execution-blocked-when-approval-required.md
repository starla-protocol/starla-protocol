# Delegated Execution Blocked When Approval Required

State: Draft
Profile: `Core + Approvals`
Condition: required when the implementation claims `Core + Approvals` or exposes approval-gated
delegation on the public binding
Scenario: one delegated child `execution` is created, delegated, and blocked pending visible
approval before child progress continues
Related Spec: `drafts/coordination-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible non-terminal parent `execution`
2. issue `delegate execution`
3. require unresolved approval before delegated child progress may continue

## Required Event Order

1. child `execution.created`
2. `execution.delegated`
3. `approval.created`
4. child `execution.blocked`

## Terminal Condition

- the child `execution` is visible in `blocked`
- at least one visible associated `approval` remains in `pending`

## Forbidden Missing Or Reordered Events

- `execution.delegated` before child `execution.created`
- `approval.created` before child `execution.created`
- child `execution.blocked` before `execution.delegated`
- child `execution.completed` before approval resolution
- blocked delegated child with no visible `pending` approval

## Conformance Hooks Exercised

- delegated child enters `blocked` before delegated command completion when approval is required
- visible pending approval exists for blocked delegated child
- `execution.delegated` precedes child blocked observation
