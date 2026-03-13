# Delegated Blocked Child Terminal After Supervisory Parent Stop

State: Draft
Profile: `Core + Approvals`
Condition: required when the implementation exposes parent-driven supervisory child-terminal
behavior on the public binding and claims `Core + Approvals` or exposes approval-gated delegation
on the public binding
Scenario: one delegated child `execution` is created, delegated, blocked pending visible approval,
and later reaches visible terminal state because supervision follows one visible parent terminal
transition
Related Spec: `drafts/coordination-v1.md`, `drafts/core-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible non-terminal parent `execution`
2. issue `delegate execution`
3. require unresolved approval before delegated child progress may continue
4. cause the parent `execution` to reach one visible terminal state through an implementation-exposed
   action
5. allow the implementation's supervisory policy to apply to the blocked child `execution`

## Required Event Order

1. child `execution.created`
2. `execution.delegated`
3. `approval.created`
4. child `execution.blocked`
5. one visible parent terminal `execution.failed` or `execution.canceled` event, if exposed in the
   scenario
6. child `execution.failed` or child `execution.canceled`

## Terminal Condition

- the child `execution` ends in `failed` or `canceled`

## Forbidden Missing Or Reordered Events

- `approval.created` before child `execution.created`
- child `execution.blocked` before `execution.delegated`
- child terminal event before child `execution.blocked`
- child `execution.completed` before approval resolution
- supervisory child terminal outcome without normal child terminal event visibility
- rewritten or missing visible lineage at child terminal observation time

## Conformance Hooks Exercised

- delegated child enters `blocked` before delegated command completion when approval is required
- visible pending approval exists before blocked delegated child observation
- supervisory action uses normal child `execution` lifecycle and event surface after blocked state
