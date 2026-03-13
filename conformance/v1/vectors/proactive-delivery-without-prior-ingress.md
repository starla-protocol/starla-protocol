# Proactive Delivery Without Prior Ingress

State: Draft
Profile: `Core + Channels`
Condition: required when the implementation claims or exposes proactive delivery
Binding: `HTTP v1`
Related Spec: `drafts/channels-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One canonical outbound delivery request succeeds without requiring one prior visible `ingress
message`.

## Preconditions

- the implementation claims or exposes proactive delivery
- one visible `channel adapter` exists

## Request Sequence

1. Issue `POST /v1/channel-adapters/{channel_adapter_id}/delivery-requests` with:
   - `delivery_request_id`
   - `channel_adapter_id`
   - `channel_kind`
   - `reply_target`
   - `content`
   - no `in_reply_to_message_id`

## Expected Result

- the request succeeds with `200 OK` or `202 Accepted`
- the request is not rejected only because no prior visible `ingress message` exists
- if the response body is a `delivery result`, it preserves the same `delivery_request_id`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- rejection only because the request is proactive
- rejection only because `in_reply_to_message_id` is absent

## Conformance Hooks Exercised

- proactive delivery does not require one prior visible ingress message
