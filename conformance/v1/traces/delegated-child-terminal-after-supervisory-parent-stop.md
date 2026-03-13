# Delegated Child Terminal After Supervisory Parent Stop

State: Draft
Profile: `Core`
Condition: required when the implementation exposes parent-driven supervisory child-terminal
behavior on the public binding
Scenario: one delegated child `execution` reaches visible terminal state because implementation
supervision follows one visible parent terminal transition
Related Spec: `drafts/coordination-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible non-terminal parent `execution`
2. issue `delegate execution`
3. cause the parent `execution` to reach one visible terminal state through an implementation-exposed
   action
4. allow the implementation's supervisory policy to apply to the child `execution`

## Required Event Order

1. child `execution.created`
2. `execution.delegated`
3. one visible parent terminal `execution.failed` or `execution.canceled` event, if exposed in the
   scenario
4. child `execution.failed` or child `execution.canceled`

## Terminal Condition

- the child `execution` ends in `failed` or `canceled`

## Forbidden Missing Or Reordered Events

- child terminal event before child `execution.created`
- child terminal event before `execution.delegated`
- supervisory child terminal outcome without normal child terminal event visibility
- rewritten or missing visible lineage at child terminal observation time
- rewritten or missing visible session membership at child terminal observation time

## Conformance Hooks Exercised

- supervisory action uses normal child `execution` lifecycle and event surface
- supervisory action preserves child identity, ownership, visible session membership, and visible
  lineage
