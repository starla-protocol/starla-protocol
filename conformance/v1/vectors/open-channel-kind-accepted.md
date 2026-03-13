# Open Channel Kind Accepted

State: Draft
Profile: `Core + Channels`
Binding: `HTTP v1`
Related Spec: `drafts/channels-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

An implementation exposes one canonical channel envelope using one non-enumerated `channel_kind`
identifier.

## Preconditions

- the implementation claims `Core + Channels`
- one visible `channel adapter` exists
- the visible `channel_kind` is not limited to a fixed protocol enum chosen by the conformance
  runner

## Request Sequence

1. Issue `GET /v1/channel-adapters/{channel_adapter_id}`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `channel_adapter_id`
  - `channel_kind`
- `channel_kind` is preserved as an open identifier string
- the binding does not reject the visible adapter only because `channel_kind` is not part of a
  closed protocol enum

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- protocol-level rejection only because `channel_kind` is not part of a closed enum
- protocol-level rewriting of `channel_kind` into a different closed enum value

## Conformance Hooks Exercised

- adapter inspection exposes open `channel_kind`
- open `channel kind` acceptance without a closed protocol enum
