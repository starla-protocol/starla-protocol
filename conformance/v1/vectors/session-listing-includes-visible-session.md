# Session Listing Includes Visible Session

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `session` appears in the canonical HTTP list route.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `session` exists

## Request Sequence

1. Issue `GET /v1/sessions`.

## Expected Result

- the request succeeds with `200 OK`
- the response body is a JSON array
- at least one array item contains:
  - `session_id`
  - `state`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- non-array response body
- visible session omitted from the returned listing
- listed item missing `session_id`
- listed item missing `state`

## Conformance Hooks Exercised

- session list route exposes visible session identifier and lifecycle state
