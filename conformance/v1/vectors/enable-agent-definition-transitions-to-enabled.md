# Enable Agent Definition Transitions To Enabled

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `agent definition` in `disabled` transitions to `enabled`.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `agent definition` exists in `disabled`

## Request Sequence

1. Issue `POST /v1/agent-definitions/{agent_definition_id}/enable`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `agent_definition_id`
  - `state`
- `state` equals `enabled`

## Expected Created Or Changed Resources

- zero new protocol resources required
- the target `agent definition` transitions to `enabled`

## Forbidden Outcomes

- request success with `state` other than `enabled`
- rewritten visible definition identifier

## Conformance Hooks Exercised

- `disabled` definition transitions to `enabled`
