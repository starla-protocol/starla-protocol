# Execution Lifecycle Minimal

State: Draft
Profile: `Core`
Scenario: execution created by `submit work` progresses to successful completion without approval
blocking or delegation
Related Spec: `drafts/core-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target a `ready` `agent instance`
2. issue `submit work`
3. allow execution to progress normally to success

## Required Event Order

1. `execution.created`
2. `execution.state_changed` with lifecycle state `running`
3. `execution.completed`

## Terminal Condition

- the target execution ends in `completed`

## Forbidden Missing Or Reordered Events

- `execution.completed` before `execution.created`
- `execution.completed` without a prior `execution.created`
- terminal success without an externally visible completion event
- any event after `execution.completed` that changes the lifecycle state again

## Conformance Hooks Exercised

- `execution.created` is first for the execution
- non-terminal execution may progress to `running`
- `completed` is terminal
