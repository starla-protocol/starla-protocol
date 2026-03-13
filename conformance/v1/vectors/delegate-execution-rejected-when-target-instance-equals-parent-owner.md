# Delegate Execution Rejected When Target Instance Equals Parent Owner

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/coordination-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

Delegation rejects a target `agent instance` that equals the parent execution's owning
`agent instance`.

## Preconditions

- one visible non-terminal parent `execution` exists
- one visible target `agent instance` exists
- the target `agent instance` equals the parent execution's owning `agent instance`

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/delegate` with:
   - `target_agent_instance_id`
   - `input`

## Expected Result

- the request fails with `409 Conflict`
- the returned protocol error class is `invalid_state`
- the response body contains `error.code` equal to `invalid_state`

## Expected Created Or Changed Resources

- zero new child `execution` resources
- zero new `execution-lineage` relations

## Expected Events

- no child `execution.created` event is emitted
- no `execution.delegated` event is emitted

## Forbidden Outcomes

- request success
- implicit self-delegation accepted as child creation

## Conformance Hooks Exercised

- target `agent instance` equal to the parent owning `agent instance` rejects `delegate execution`
