# Execution Stream Replay Rejected When Replay Unsupported

State: Draft
Profile: `Core`
Condition: required when the implementation claims `Stream Binding v1` and does not support
execution-event replay
Binding: `Stream v1`
Related Spec: `drafts/stream-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

One execution-event stream reconnect request supplies `Last-Event-ID` for one stream target that
does not support replay.

## Preconditions

- the implementation claims `Stream Binding v1`
- the implementation does not support execution-event replay
- one visible `execution` exists
- one visible execution-event stream has already emitted at least one visible frame with one `id`

## Request Sequence

1. Open `GET /v1/executions/{execution_id}/events`.
2. Record one visible event-frame `id`.
3. Reopen `GET /v1/executions/{execution_id}/events` with `Last-Event-ID` equal to that `id`.

## Expected Result

- the replay request fails with `409 Conflict`
- the response body uses the normal error envelope
- `error.code` equals `invalid_state`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required by replay rejection alone

## Forbidden Outcomes

- `200 OK` replay response for an unsupported replay request
- any `error.code` other than `invalid_state`
- replay rejection that creates or mutates visible execution state

## Conformance Hooks Exercised

- unsupported replay state returns `invalid_state`
