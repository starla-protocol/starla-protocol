# Status Stream Replay Resumes After Last Event ID

State: Draft
Profile: `Core + Channels`
Condition: required when the implementation claims `Stream Binding v1` and claims or exposes status
delivery
Binding: `Stream v1`
Related Spec: `drafts/stream-binding-v1.md`, `drafts/channels-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One status-delivery stream reconnects with `Last-Event-ID` and resumes strictly after the retained
visible status event identified by that value.

## Preconditions

- the implementation claims `Stream Binding v1`
- the implementation claims or exposes status delivery
- one visible `channel adapter` exists
- one visible `delivery request` exists
- one visible status-delivery stream has already emitted at least one retained status frame with one
  stable `id`

## Request Sequence

1. Open
   `GET /v1/channel-adapters/{channel_adapter_id}/delivery-requests/{delivery_request_id}/status-events`.
2. Record one visible status frame `id`.
3. Reopen the same route with `Last-Event-ID` equal to that `id`.

## Expected Result

- the resumed stream request succeeds with `200 OK`
- the resumed stream does not replay the status frame identified by `Last-Event-ID`
- the first replayed status frame, if any exists, belongs strictly after the referenced retained
  status frame

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required by reconnect alone

## Forbidden Outcomes

- replay begins at or before the referenced status frame
- the same visible status frame appears with a different `id` on equivalent replay

## Conformance Hooks Exercised

- stable stream `id` for the same visible status delivery
- replay resumes strictly after `Last-Event-ID`
