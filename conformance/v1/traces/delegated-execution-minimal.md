# Delegated Execution Minimal

State: Draft
Profile: `Core`
Scenario: one visible parent `execution` delegates one child `execution` that progresses to
successful completion without approval blocking
Related Spec: `drafts/coordination-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible non-terminal parent `execution`
2. issue `delegate execution`
3. allow the created child `execution` to progress normally to success

## Required Event Order

1. child `execution.created`
2. `execution.delegated`
3. child `execution.state_changed` with lifecycle state `running`
4. child `execution.completed`

## Terminal Condition

- the child `execution` ends in `completed`

## Forbidden Missing Or Reordered Events

- `execution.delegated` before child `execution.created`
- child `execution.completed` before `execution.delegated`
- child terminal success without a visible lineage-creation event

## Conformance Hooks Exercised

- successful delegation creates visible child lineage
- `execution.delegated` follows child `execution.created`
