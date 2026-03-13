# Delegate Execution Rejected When Parent Missing

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/coordination-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

Delegation rejects a missing or non-visible parent `execution`.

## Preconditions

- the request path `execution_id` does not resolve to one visible parent `execution`
- one visible target `agent instance` exists in `ready`

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/delegate` with:
   - `target_agent_instance_id`
   - `input`

## Expected Result

- the request fails with `404 Not Found`
- the returned protocol error class is `not_found`
- the response body contains `error.code` equal to `not_found`

## Expected Created Or Changed Resources

- zero new child `execution` resources
- zero new `execution-lineage` relations

## Expected Events

- no child `execution.created` event is emitted
- no `execution.delegated` event is emitted

## Forbidden Outcomes

- request success
- implicit delegation from a different visible parent `execution`

## Conformance Hooks Exercised

- missing parent rejects `delegate execution` with `not_found`
