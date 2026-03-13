# Execution Stream Replay Rejected When Last Event ID Not Retained

State: Draft
Profile: `Core`
Condition: required when the implementation claims `Stream Binding v1` and claims or exposes
execution-event replay support with retained-event replay
Binding: `Stream v1`
Related Spec: `drafts/stream-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

One execution-event stream reconnect request supplies `Last-Event-ID` for one same-target visible
event that is no longer retained for replay.

## Preconditions

- the implementation claims `Stream Binding v1`
- the implementation claims or exposes execution-event replay support
- one visible `execution` exists
- one previously visible execution-event `id` for the same stream target is no longer retained for
  replay

## Request Sequence

1. Issue `GET /v1/executions/{execution_id}/events` with `Last-Event-ID` equal to the no-longer
   retained `id`.

## Expected Result

- the replay request fails with `409 Conflict`
- the response body uses the normal error envelope
- `error.code` equals `invalid_state`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required by replay rejection alone

## Forbidden Outcomes

- replay beginning from one later retained event
- replay falling back to a fresh stream start without rejection
- any `error.code` other than `invalid_state`

## Conformance Hooks Exercised

- non-retained `Last-Event-ID` returns `invalid_state`
