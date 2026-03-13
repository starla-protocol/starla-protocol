# Approval Resolution Terminal

State: Draft
Profile: `Core + Approvals`
Condition: required when the implementation claims `Core + Approvals` or exposes approval
resolution on the public binding
Scenario: one visible `approval` is created in `pending` and later resolves once to one terminal
decision
Related Spec: `drafts/core-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one `ready` `agent instance`
2. issue `submit work`
3. require unresolved approval before progress may continue
4. issue `resolve approval`

## Required Event Order

1. `approval.created`
2. `approval.resolved`

## Terminal Condition

- the target `approval` ends in `approved` or `denied`

## Forbidden Missing Or Reordered Events

- `approval.resolved` before `approval.created`
- more than one `approval.resolved` event for the same `approval`
- target `approval` remaining in `pending` after visible successful resolution

## Conformance Hooks Exercised

- `approval.resolved` does not precede `approval.created`
- `pending` approval resolves to exactly one terminal state
