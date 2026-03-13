# Execution Cancel Terminal

State: Draft
Profile: `Core`
Scenario: one visible `execution` reaches terminal `canceled` state and no later lifecycle or
artifact event follows
Related Spec: `drafts/core-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible non-terminal `execution`
2. issue `cancel execution`

## Required Event Order

1. `execution.created`
2. zero or more non-terminal execution lifecycle events
3. `execution.canceled`

## Terminal Condition

- the target `execution` ends in `canceled`

## Forbidden Missing Or Reordered Events

- `execution.canceled` before `execution.created`
- `execution.canceled` without a prior `execution.created`
- `execution.completed` after `execution.canceled`
- `execution.failed` after `execution.canceled`
- `execution.state_changed` after `execution.canceled`
- `execution.blocked` after `execution.canceled`
- `artifact.emitted` after `execution.canceled`

## Conformance Hooks Exercised

- exactly one terminal execution event appears
- no later lifecycle or artifact event follows visible canceled terminal outcome
