# Close Session Transitions To Closed

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `session` in `open` transitions to `closed`.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `session` exists in `open`

## Request Sequence

1. Issue `POST /v1/sessions/{session_id}/close`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `session_id`
  - `state`
- `state` equals `closed`

## Expected Created Or Changed Resources

- zero new protocol resources required
- the target `session` transitions to `closed`

## Forbidden Outcomes

- request success with `state` other than `closed`
- rewritten visible session identifier

## Conformance Hooks Exercised

- `open` session transitions to `closed`
