# Execution Stream Emits No Later Event After Terminal

State: Draft
Profile: `Core`
Condition: required when the implementation claims `Stream Binding v1`
Binding: `Stream v1`
Related Spec: `drafts/core-v1.md`, `drafts/stream-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One execution-event stream observes one visible terminal execution event and then observes no later
execution event for the same `execution`.

## Preconditions

- the implementation claims `Stream Binding v1`
- one visible `execution` exists
- the `execution` reaches one visible terminal event during observation

## Request Sequence

1. Open `GET /v1/executions/{execution_id}/events`.
2. Observe one terminal event for the target `execution`.
3. Continue observing until the stream closes or one bounded post-terminal observation window
   expires.

## Expected Result

- the terminal event is one of:
  - `execution.completed`
  - `execution.failed`
  - `execution.canceled`
- no later execution-event frame for the same `execution_id` is emitted after that terminal event

## Expected Created Or Changed Resources

- zero new protocol resources required after the visible terminal event
- zero later lifecycle transitions for the same `execution`

## Forbidden Outcomes

- a later `execution.state_changed` frame for the same `execution_id`
- a later `execution.blocked` frame for the same `execution_id`
- a later `artifact.emitted` frame for the same `execution_id`
- a second terminal execution event for the same `execution_id`

## Conformance Hooks Exercised

- no later execution event follows one terminal execution event on the stream
