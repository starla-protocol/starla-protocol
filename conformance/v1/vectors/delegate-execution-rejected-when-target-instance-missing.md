# Delegate Execution Rejected When Target Instance Missing

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/coordination-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

Delegation rejects a missing or non-visible target `agent instance`.

## Preconditions

- one visible non-terminal parent `execution` exists
- the requested `target_agent_instance_id` does not resolve to one visible target `agent instance`

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
- implicit retargeting to a different visible `agent instance`

## Conformance Hooks Exercised

- missing target rejects `delegate execution` with `not_found`
