# Submit Work Success

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

A ready `agent instance` accepts `submit work` and creates exactly one new `execution`.

## Preconditions

- an `agent definition` exists in `enabled`
- an `agent instance` exists for that definition in `ready`
- the caller is authorized to address the target `agent instance`
- no approval is required for this scenario
- no conflicting idempotency key has been used

## Request Sequence

1. Issue `POST /v1/agent-instances/{agent_instance_id}/submit-work` with:
   - `input`
   - optional `references`
   - optional `Idempotency-Key` header

## Expected Result

- the request succeeds with `201 Created`
- the response body contains:
  - `execution_id`
  - `state`
- `approval_ids` is absent
- exactly one new `execution` is created
- the new `execution` initially enters `pending`
- explicit payload becomes part of the execution's visible `context`
- explicit references remain explicit references in the execution's visible `context`

## Expected Created Or Changed Resources

- one new `execution`
- zero `approval` resources
- zero new `artifact` resources at command completion

## Expected Events

1. `execution.created`
2. the first subsequent lifecycle event is one of:
   - `execution.state_changed`
   - `execution.blocked`
   - `execution.failed`
   - `execution.canceled`

`execution.created` MUST appear before any other event for the created execution.

## Forbidden Outcomes

- `invalid_state`
- `capability_denied`
- more than one new execution
- hidden rewriting of explicit references into caller payload

## Conformance Hooks Exercised

- `submit work` creates exactly one execution
- every execution begins in `pending`
- explicit payload remains part of visible context
- explicit references are preserved
- `execution.created` is ordered before any later event for the same execution
