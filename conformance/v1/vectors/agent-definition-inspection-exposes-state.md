# Agent Definition Inspection Exposes State

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `agent definition` is inspected on the public HTTP binding.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `agent definition` exists

## Request Sequence

1. Issue `GET /v1/agent-definitions/{agent_definition_id}`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `agent_definition_id`
  - `state`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- omission of `agent_definition_id`
- omission of `state`
- rewriting the visible definition identifier

## Conformance Hooks Exercised

- definition inspection exposes identifier and lifecycle state
