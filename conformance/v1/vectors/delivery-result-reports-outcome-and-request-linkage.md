# Delivery Result Reports Outcome And Request Linkage

State: Draft
Profile: `Core + Channels`
Binding: `HTTP v1`
Related Spec: `drafts/channels-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible canonical `delivery result` reports one visible delivery outcome and the request it
belongs to.

## Preconditions

- the implementation claims `Core + Channels`
- one canonical outbound delivery attempt has been made through the public HTTP binding
- one visible canonical `delivery result` exists for that attempt

## Request Sequence

1. Issue
   `GET /v1/channel-adapters/{channel_adapter_id}/delivery-results/{delivery_request_id}`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `delivery_request_id`
  - `channel_adapter_id`
  - `channel_kind`
  - `outcome`
  - `attempted_at`
- `outcome` is one of:
  - `sent`
  - `delivered`
  - `best_effort`
  - `failed`
- if `outcome` is `failed`, `error` is present
- if `outcome` is not `failed`, `error` is absent
- if `message_id` is present, it identifies the visible outbound message created or updated by the
  request

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- omission of `delivery_request_id`
- omission of `outcome`
- `failed` without `error`
- non-`failed` result with `error`
- outcome outside the visible protocol set

## Conformance Hooks Exercised

- delivery result exposes request linkage
- delivery result exposes one visible outcome
