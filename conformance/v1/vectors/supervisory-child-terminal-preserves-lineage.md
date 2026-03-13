# Supervisory Child Terminal Preserves Lineage

State: Draft
Profile: `Core`
Condition: required when the implementation exposes parent-driven supervisory child-terminal
behavior on the public binding
Binding: `HTTP v1`
Related Spec: `drafts/coordination-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One delegated child `execution` reaches terminal `failed` or `canceled` because exposed
supervisory behavior follows one visible parent terminal transition, and child lineage remains
stable.

## Preconditions

- one visible parent `execution` exists
- one visible delegated child `execution` exists
- the child `execution` is attached to one visible `session`
- the implementation exposes parent-driven supervisory child-terminal behavior

## Request Sequence

1. Trigger the documented implementation action that causes the parent `execution` to reach one
   visible terminal state and applies supervisory policy to the child.
2. Issue `GET /v1/executions/{child_execution_id}`.

## Expected Result

- the child inspection request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `parent_execution_id`
  - `agent_instance_id`
  - `session_id`
  - `state`
- `execution_id` equals the pre-existing child execution identifier
- `parent_execution_id` equals the pre-existing parent execution identifier
- `agent_instance_id` equals the pre-existing child owning `agent instance` identifier
- `session_id` equals the pre-existing child visible session identifier
- `state` equals `failed` or `canceled`

## Expected Created Or Changed Resources

- zero new child `execution` resources created by the supervisory terminal effect
- zero rewritten `execution-lineage` relations

## Forbidden Outcomes

- new child execution identifier replacing the existing child
- missing `parent_execution_id` after visible child terminal transition
- rewritten `agent_instance_id` after visible child terminal transition
- missing or rewritten `session_id` after visible child terminal transition
- child terminal inspection without visible lineage

## Conformance Hooks Exercised

- supervisory action preserves child identity, ownership, and visible lineage
- supervisory action preserves visible child session membership
