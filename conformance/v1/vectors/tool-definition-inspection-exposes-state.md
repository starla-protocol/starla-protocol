# Tool Definition Inspection Exposes State

State: Draft
Profile: `Core + Tools`
Condition: required when the implementation claims `Core + Tools` and claims `HTTP Binding v1`, or
exposes tool inspection on the public binding
Binding: `HTTP v1`
Related Spec: `drafts/tools-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `tool definition` is inspected on the public HTTP binding.

## Preconditions

 - the implementation claims `HTTP Binding v1`
 - one visible `tool definition` exists

## Request Sequence

1. Issue `GET /v1/tools/{tool_id}`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `tool_id`
  - `state`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- omission of `tool_id`
- omission of `state`
- rewriting the visible tool identifier

## Conformance Hooks Exercised

- tool inspection exposes identifier and lifecycle state
