# Status Stream Missing Target Returns Not Found

State: Draft
Profile: `Core + Channels`
Condition: required when the implementation claims `Stream Binding v1` and claims or exposes status
delivery
Binding: `Stream v1`
Related Spec: `drafts/stream-binding-v1.md`, `drafts/http-binding-v1.md`,
`drafts/channels-v1.md`, `drafts/conformance-v1.md`

## Scenario

One status-delivery stream request targets one missing or non-visible `delivery request` within one
visible or addressed `channel adapter`.

## Preconditions

- the implementation claims `Stream Binding v1`
- the implementation claims or exposes status delivery
- the target `delivery_request_id` does not identify one visible status stream target for the
  addressed `channel_adapter_id`

## Request Sequence

1. Issue
   `GET /v1/channel-adapters/{channel_adapter_id}/delivery-requests/{delivery_request_id}/status-events`.

## Expected Result

- the request fails with `404 Not Found`
- the response body uses the normal error envelope
- `error.code` equals `not_found`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed delivery outcomes required by stream target rejection alone

## Forbidden Outcomes

- `200 OK` stream response for one missing or non-visible status stream target
- `409 Conflict` for one missing or non-visible status stream target
- transport-specific error body without protocol-law `error.code`

## Conformance Hooks Exercised

- missing visible stream target returns `not_found`
