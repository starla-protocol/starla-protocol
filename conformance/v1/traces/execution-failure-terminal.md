# Execution Failure Terminal

State: Draft
Profile: `Core`
Scenario: one visible `execution` reaches terminal `failed` state and no later lifecycle event
follows
Related Spec: `drafts/core-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible `ready` `agent instance`
2. issue `submit work`
3. allow the created `execution` to progress to visible `failed`

## Required Event Order

1. `execution.created`
2. zero or more non-terminal execution lifecycle events
3. `execution.failed`

## Terminal Condition

- the target `execution` ends in `failed`

## Forbidden Missing Or Reordered Events

- `execution.failed` before `execution.created`
- `execution.completed` after `execution.failed`
- `execution.canceled` after `execution.failed`
- `execution.state_changed` after `execution.failed`
- `execution.blocked` after `execution.failed`
- `artifact.emitted` after `execution.failed`

## Conformance Hooks Exercised

- exactly one terminal execution event appears
- no later lifecycle event follows visible failed terminal outcome
