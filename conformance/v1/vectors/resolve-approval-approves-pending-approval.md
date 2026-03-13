# Resolve Approval Approves Pending Approval

State: Draft
Profile: `Core + Approvals`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

One visible `pending` approval is resolved to `approved`.

## Preconditions

- one visible `approval` exists in `pending`
- the caller is authorized to address the target `approval`

## Request Sequence

1. Issue `POST /v1/approvals/{approval_id}/resolve` with:
   - `decision` equal to `approved`

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `approval_id`
  - `state`
- `state` equals `approved`

## Expected Created Or Changed Resources

- zero new `approval` resources
- the target `approval` transitions from `pending` to `approved`

## Expected Events

1. `approval.resolved`

## Forbidden Outcomes

- `invalid_state`
- `approval_id` changes
- target approval remains `pending`

## Conformance Hooks Exercised

- `pending` approvals resolve to exactly one terminal state
