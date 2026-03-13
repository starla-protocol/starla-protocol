# Execution Completion Terminal

State: Draft
Profile: `Core`
Scenario: one visible `execution` reaches terminal `completed` state and no later lifecycle or
artifact event follows
Related Spec: `drafts/core-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible `ready` `agent instance`
2. issue `submit work`
3. allow the created `execution` to progress to visible `completed`

## Required Event Order

1. `execution.created`
2. zero or more non-terminal execution lifecycle events
3. `execution.completed`

## Terminal Condition

- the target `execution` ends in `completed`

## Forbidden Missing Or Reordered Events

- `execution.completed` before `execution.created`
- `execution.completed` without a prior `execution.created`
- `execution.failed` after `execution.completed`
- `execution.canceled` after `execution.completed`
- `execution.state_changed` after `execution.completed`
- `execution.blocked` after `execution.completed`
- `artifact.emitted` after `execution.completed`

## Conformance Hooks Exercised

- exactly one terminal execution event appears
- no later lifecycle or artifact event follows visible completed terminal outcome
