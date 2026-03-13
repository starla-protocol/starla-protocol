# Status Stream Replay Rejected When Replay Unsupported

State: Draft
Profile: `Core + Channels`
Condition: required when the implementation claims `Stream Binding v1`, claims or exposes status
delivery, and does not support status-delivery replay
Binding: `Stream v1`
Related Spec: `drafts/stream-binding-v1.md`, `drafts/channels-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One status-delivery stream reconnect request supplies `Last-Event-ID` for one stream target that
does not support replay.

## Preconditions

- the implementation claims `Stream Binding v1`
- the implementation claims or exposes status delivery
- the implementation does not support status-delivery replay
- one visible `channel adapter` exists
- one visible `delivery request` exists
- one visible status-delivery stream has already emitted at least one visible frame with one `id`

## Request Sequence

1. Open
   `GET /v1/channel-adapters/{channel_adapter_id}/delivery-requests/{delivery_request_id}/status-events`.
2. Record one visible status frame `id`.
3. Reopen the same route with `Last-Event-ID` equal to that `id`.

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
- replay rejection that rewrites visible delivery status

## Conformance Hooks Exercised

- unsupported replay state returns `invalid_state`
