# Status Delivery Inspection Preserves Request Linkage

State: Draft
Profile: `Core + Channels`
Condition: required when the implementation claims `HTTP Binding v1` and claims or exposes status
delivery
Binding: `HTTP v1`
Related Spec: `drafts/channels-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible status-delivery inspection route returns canonical `status delivery` items for one
visible `delivery request`.

## Preconditions

- the implementation claims `HTTP Binding v1`
- the implementation claims or exposes status delivery
- one visible `channel adapter` exists
- one visible `delivery request` exists
- one or more visible `status delivery` updates exist for that request

## Request Sequence

1. Issue
   `GET /v1/channel-adapters/{channel_adapter_id}/delivery-requests/{delivery_request_id}/status-deliveries`.

## Expected Result

- the request succeeds with `200 OK`
- the response body is a JSON array
- every array item contains:
  - `delivery_request_id`
  - `channel_adapter_id`
  - `channel_kind`
  - `status`
  - `emitted_at`
- every array item `delivery_request_id` equals the path `delivery_request_id`
- every array item `channel_adapter_id` equals the path `channel_adapter_id`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed delivery outcomes required

## Forbidden Outcomes

- visible final `delivery result` object returned in place of one `status delivery`
- array item missing request linkage
- array item missing `status`
- array item missing `emitted_at`

## Conformance Hooks Exercised

- status delivery remains distinct from `delivery result`
- status delivery preserves request linkage
