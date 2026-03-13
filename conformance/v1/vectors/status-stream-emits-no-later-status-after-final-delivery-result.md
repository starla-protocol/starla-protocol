# Status Stream Emits No Later Status After Final Delivery Result

State: Draft
Profile: `Core + Channels`
Condition: required when the implementation claims `Stream Binding v1` and claims or exposes
status delivery
Binding: `Stream v1`
Related Spec: `drafts/stream-binding-v1.md`, `drafts/channels-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One status-delivery stream remains open after one final visible `delivery result` and emits no
later `channel.status` frame for the same delivery attempt.

## Preconditions

- the implementation claims `Stream Binding v1`
- the implementation claims or exposes status delivery
- one visible `channel adapter` exists
- one visible `delivery request` exists
- the corresponding visible `delivery result` becomes final during observation

## Request Sequence

1. Open
   `GET /v1/channel-adapters/{channel_adapter_id}/delivery-requests/{delivery_request_id}/status-events`.
2. Observe zero or more `channel.status` frames.
3. Observe one final visible `delivery result` for the same `delivery_request_id` on the normal
   delivery-result surface.
4. Continue observing the status stream until the stream closes or one bounded post-result
   observation window expires.

## Expected Result

- the final visible `delivery result` remains distinct from `channel.status`
- no later `channel.status` frame for the same `delivery_request_id` is emitted after that final
  visible `delivery result`

## Expected Created Or Changed Resources

- zero new protocol resources required after the final visible `delivery result`
- zero later visible status-delivery updates for the same delivery attempt

## Forbidden Outcomes

- a later `channel.status` frame for the same `delivery_request_id`
- the final visible `delivery result` emitted as `channel.status`

## Conformance Hooks Exercised

- no later `channel.status` follows one final visible `delivery result`
- `status delivery` remains distinct from `delivery result`
