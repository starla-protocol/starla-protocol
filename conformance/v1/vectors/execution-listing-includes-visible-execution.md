# Execution Listing Includes Visible Execution

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `execution` appears in the canonical HTTP list route.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `execution` exists

## Request Sequence

1. Issue `GET /v1/executions`.

## Expected Result

- the request succeeds with `200 OK`
- the response body is a JSON array
- at least one array item contains:
  - `execution_id`
  - `agent_instance_id`
  - `state`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- non-array response body
- visible execution omitted from the returned listing
- listed item missing `execution_id`
- listed item missing `agent_instance_id`
- listed item missing `state`

## Conformance Hooks Exercised

- execution list route exposes visible execution identifier, owner, and lifecycle state
