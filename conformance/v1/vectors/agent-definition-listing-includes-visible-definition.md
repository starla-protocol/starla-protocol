# Agent Definition Listing Includes Visible Definition

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `agent definition` appears in the canonical HTTP list route.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `agent definition` exists

## Request Sequence

1. Issue `GET /v1/agent-definitions`.

## Expected Result

- the request succeeds with `200 OK`
- the response body is a JSON array
- at least one array item contains:
  - `agent_definition_id`
  - `state`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- non-array response body
- visible definition omitted from the returned listing
- listed item missing `agent_definition_id`
- listed item missing `state`

## Conformance Hooks Exercised

- definition list route exposes visible definition identifier and lifecycle state
