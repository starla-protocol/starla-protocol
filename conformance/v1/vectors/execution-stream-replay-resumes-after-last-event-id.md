# Execution Stream Replay Resumes After Last Event ID

State: Draft
Profile: `Core`
Binding: `Stream v1`
Related Spec: `drafts/stream-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

One execution-event stream reconnects with `Last-Event-ID` and resumes strictly after the retained
visible event identified by that value.

## Preconditions

- the implementation claims `Stream Binding v1`
- one visible `execution` exists
- one visible execution-event stream has already emitted at least one retained event with one
  stable `id`

## Request Sequence

1. Open `GET /v1/executions/{execution_id}/events`.
2. Record one visible event-frame `id`.
3. Reopen `GET /v1/executions/{execution_id}/events` with `Last-Event-ID` equal to that `id`.

## Expected Result

- the resumed stream request succeeds with `200 OK`
- the resumed stream does not replay the event identified by `Last-Event-ID`
- the first replayed frame, if any exists, belongs strictly after the referenced retained event

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required by reconnect alone

## Forbidden Outcomes

- replay begins at or before the referenced event
- the same visible event appears with a different `id` on equivalent replay

## Conformance Hooks Exercised

- stable stream `id` for the same visible event
- replay resumes strictly after `Last-Event-ID`
