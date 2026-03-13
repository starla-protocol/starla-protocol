# Delegate Execution Success

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/coordination-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible non-terminal parent `execution` delegates work successfully to one different `ready`
target `agent instance`.

## Preconditions

- one visible non-terminal parent `execution` exists
- the parent `execution` is attached to one visible `session`
- one visible target `agent instance` exists in `ready`
- the target `agent instance` differs from the parent execution's owning `agent instance`
- capability checks pass
- no conflicting idempotency key has been used

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/delegate` with:
   - `target_agent_instance_id`
   - `input`
   - optional `references`
   - optional `Idempotency-Key` header

## Expected Result

- the request succeeds with `201 Created`
- the response body contains:
  - `execution_id`
  - `parent_execution_id`
  - `agent_instance_id`
  - `state`
  - `session_id`
- `parent_execution_id` equals the delegated parent execution identifier
- `agent_instance_id` equals the explicit `target_agent_instance_id`
- `session_id` equals the parent session identifier
- exactly one new child `execution` is created
- the child `execution` initially enters `pending`

## Expected Created Or Changed Resources

- one new child `execution`
- one visible `execution-lineage` relation
- zero new `artifact` resources at command completion

## Expected Events

1. child `execution.created`
2. `execution.delegated`

## Forbidden Outcomes

- request success without visible child parent execution identifier
- request success without visible lineage
- child created under the parent owning `agent instance`

## Conformance Hooks Exercised

- successful delegation creates one child execution and one visible lineage relation
- successful delegation preserves the explicit target `agent instance`
- delegated child parent execution identifier is visible
- delegated child attached to a visible parent session remains attached to that session
- `execution.delegated` follows child `execution.created`
