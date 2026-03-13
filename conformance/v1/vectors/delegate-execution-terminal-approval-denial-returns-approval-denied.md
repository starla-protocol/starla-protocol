# Delegate Execution Terminal Approval Denial Returns Approval Denied

State: Draft
Profile: `Core + Approvals`
Condition: required when the implementation exposes visible terminal approval denial during
delegation on the public binding
Binding: `HTTP v1`
Related Spec: `drafts/coordination-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

Delegation fails when one visible terminal approval denial applies to the delegation action.

## Preconditions

- one visible non-terminal parent `execution` exists
- one visible target `agent instance` exists in `ready`
- the target `agent instance` differs from the parent execution's owning `agent instance`
- one visible terminal approval denial applies to the delegation action

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/delegate` with:
   - `target_agent_instance_id`
   - `input`

## Expected Result

- the request fails with `403 Forbidden`
- the returned protocol error class is `approval_denied`
- the response body contains `error.code` equal to `approval_denied`

## Expected Created Or Changed Resources

- zero new child `execution` resources
- zero new `execution-lineage` relations

## Expected Events

- no child `execution.created` event is emitted
- no `execution.delegated` event is emitted

## Forbidden Outcomes

- request success
- blocked child creation under visible terminal approval denial

## Conformance Hooks Exercised

- visible terminal approval denial rejects `delegate execution` with `approval_denied`
