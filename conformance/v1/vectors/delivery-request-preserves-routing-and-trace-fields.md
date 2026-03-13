# Delivery Request Preserves Routing And Trace Fields

State: Draft
Profile: `Core + Channels`
Binding: `HTTP v1`
Related Spec: `drafts/channels-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One canonical `delivery request` is accepted on the public HTTP binding without collapsing routing
fields, and any exposed trace linkage remains visible.

## Preconditions

- the implementation claims `Core + Channels`
- the implementation exposes one HTTP surface for canonical outbound delivery
- one visible `channel adapter` exists

## Request Sequence

1. Issue `POST /v1/channel-adapters/{channel_adapter_id}/delivery-requests` with:
   - `delivery_request_id`
   - `channel_adapter_id`
   - `channel_kind`
   - `reply_target`
   - `content`
   - optional `thread_reference`
   - optional `in_reply_to_message_id`
   - optional `correlation_id`
   - optional `causation_id`

## Expected Result

- the request succeeds with `200 OK` or `202 Accepted`
- the request succeeds without requiring connector-specific top-level routing fields
- if the response is `202 Accepted`, the response body contains:
  - `delivery_request_id`
  - `channel_adapter_id`
  - `channel_kind`
- if the response is `200 OK`, the response body contains:
  - `delivery_request_id`
  - `channel_adapter_id`
  - `channel_kind`
  - `outcome`
- if the implementation returns or later exposes visible delivery linkage, `delivery_request_id`
  remains stable
- if `thread_reference` is supplied, it remains distinct from `reply_target`
- if `correlation_id` is exposed on a visible result, it equals the request value
- if `causation_id` is exposed on a visible result, it equals the request value

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- rejection only because the request omitted connector-specific top-level routing fields
- `thread_reference` copied into `reply_target`
- `reply_target` copied into `thread_reference`
- exposed trace linkage rewritten to unrelated values

## Conformance Hooks Exercised

- delivery request preserves adapter, kind, and reply routing fields
- delivery request keeps `thread_reference` distinct from `reply_target`
- delivery request preserves exposed trace fields
