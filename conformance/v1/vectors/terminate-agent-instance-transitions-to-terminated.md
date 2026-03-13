# Terminate Agent Instance Transitions To Terminated

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible non-terminal `agent instance` transitions to `terminated`.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `agent instance` exists in `ready` or `paused`

## Request Sequence

1. Issue `POST /v1/agent-instances/{agent_instance_id}/terminate`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `agent_instance_id`
  - `state`
- `state` equals `terminated`

## Expected Created Or Changed Resources

- zero new protocol resources required
- the target `agent instance` transitions to `terminated`

## Forbidden Outcomes

- request success with `state` other than `terminated`
- rewritten visible instance identifier

## Conformance Hooks Exercised

- non-terminal instance transitions to `terminated`
