# Delegate Execution Idempotent Replay Preserves Child

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1` and claims or exposes
idempotent `delegate execution`
Binding: `HTTP v1`
Related Spec: `drafts/coordination-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

Idempotent replay of the same delegated request resolves to the same visible child `execution`.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible non-terminal parent `execution` exists
- one visible target `agent instance` exists in `ready`
- the target `agent instance` differs from the parent execution's owning `agent instance`
- the implementation exposes idempotent `delegate execution`

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/delegate` with:
   - `target_agent_instance_id`
   - `input`
   - one `Idempotency-Key` header
2. Repeat the same request with the same `Idempotency-Key` header.

## Expected Result

- the first request succeeds with `201 Created`
- the replay succeeds with `200 OK`
- both response bodies contain:
  - `execution_id`
  - `parent_execution_id`
  - `agent_instance_id`
  - `state`
- both responses identify the same visible child `execution`
- both responses identify the same visible parent-child relation endpoints

## Expected Created Or Changed Resources

- exactly one child `execution`
- exactly one visible `execution-lineage` relation

## Forbidden Outcomes

- replay creates a second visible child `execution`
- replay rewrites the visible target `agent instance`
- replay rewrites the visible parent execution identifier

## Conformance Hooks Exercised

- idempotent replay preserves the same visible child execution result
