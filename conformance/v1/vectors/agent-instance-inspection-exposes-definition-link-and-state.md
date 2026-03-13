# Agent Instance Inspection Exposes Definition Link And State

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `agent instance` is inspected on the public HTTP binding.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `agent instance` exists
- the visible `agent instance` references one visible `agent definition`

## Request Sequence

1. Issue `GET /v1/agent-instances/{agent_instance_id}`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `agent_instance_id`
  - `agent_definition_id`
  - `state`
- `agent_definition_id` equals the visible linked definition identifier

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- omission of `agent_instance_id`
- omission of `agent_definition_id`
- omission of `state`
- rewritten definition link

## Conformance Hooks Exercised

- instance inspection exposes definition link and lifecycle state
