# Ingress Message Preserves Routing And Trace Fields

State: Draft
Profile: `Core + Channels`
Binding: `HTTP v1`
Related Spec: `drafts/channels-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible canonical `ingress message` preserves routing fields and any exposed trace fields.

## Preconditions

- the implementation claims `Core + Channels`
- one visible canonical `ingress message` exists
- the visible ingress message includes:
  - `channel_adapter_id`
  - `channel_kind`
  - `message_id`
  - `sender_id`
  - `reply_target`
  - `content`
  - `received_at`
- the visible ingress message MAY include:
  - `thread_reference`
  - `correlation_id`
  - `causation_id`

## Request Sequence

1. Issue `POST /v1/channel-adapters/{channel_adapter_id}/ingress-messages` with one canonical
   `ingress message`.
2. Issue `GET /v1/channel-adapters/{channel_adapter_id}/ingress-messages/{message_id}`.

## Expected Result

- the `POST` request succeeds with `202 Accepted`
- the `POST` response body contains:
  - `channel_adapter_id`
  - `channel_kind`
  - `message_id`
- the `GET` request succeeds with `200 OK`
- the response body contains:
  - `channel_adapter_id`
  - `channel_kind`
  - `message_id`
  - `sender_id`
  - `reply_target`
  - `content`
  - `received_at`
- if `thread_reference` is exposed, it remains distinct from `reply_target`
- if `correlation_id` is exposed, it remains stable in the visible envelope
- if `causation_id` is exposed, it remains stable in the visible envelope

## Expected Created Or Changed Resources

- zero new protocol resources
- zero changed lifecycle states

## Forbidden Outcomes

- omission of any required routing field
- `thread_reference` copied into `reply_target`
- `reply_target` copied into `thread_reference`
- exposed trace fields renamed to connector-specific top-level fields

## Conformance Hooks Exercised

- ingress message preserves adapter, kind, message, sender, and reply routing fields
- ingress message keeps `thread_reference` distinct from `reply_target`
- ingress message preserves exposed trace fields
