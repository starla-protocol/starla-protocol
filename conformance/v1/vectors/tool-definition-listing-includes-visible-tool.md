# Tool Definition Listing Includes Visible Tool

State: Draft
Profile: `Core + Tools`
Condition: required when the implementation claims `Core + Tools` and claims `HTTP Binding v1`, or
exposes tool inspection on the public binding
Binding: `HTTP v1`
Related Spec: `drafts/tools-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `tool definition` appears in the canonical HTTP list route.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `tool definition` exists

## Request Sequence

1. Issue `GET /v1/tools`.

## Expected Result

- the request succeeds with `200 OK`
- the response body is a JSON array
- at least one array item contains:
  - `tool_id`
  - `state`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- non-array response body
- visible tool omitted from the returned listing
- listed item missing `tool_id`
- listed item missing `state`

## Conformance Hooks Exercised

- tool list route exposes visible tool identifier and lifecycle state
