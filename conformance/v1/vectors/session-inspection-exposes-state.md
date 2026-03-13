# Session Inspection Exposes State

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `session` is inspected on the public HTTP binding.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `session` exists

## Request Sequence

1. Issue `GET /v1/sessions/{session_id}`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `session_id`
  - `state`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- omission of `session_id`
- omission of `state`
- rewriting the visible session identifier

## Conformance Hooks Exercised

- session inspection exposes identifier and lifecycle state
