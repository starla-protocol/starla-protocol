# Resolve Approval Rejected When Already Resolved

State: Draft
Profile: `Core + Approvals`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

One visible terminal `approval` rejects another `resolve approval` request.

## Preconditions

- one visible `approval` exists in `approved` or `denied`
- the caller is authorized to address the target `approval`

## Request Sequence

1. Issue `POST /v1/approvals/{approval_id}/resolve` with:
   - `decision` equal to `approved` or `denied`

## Expected Result

- the request fails with `409 Conflict`
- the returned protocol error class is `invalid_state`
- the response body contains `error.code` equal to `invalid_state`

## Expected Created Or Changed Resources

- zero new `approval` resources
- the target `approval` remains in its prior terminal state

## Expected Events

- no new `approval.resolved` event is emitted

## Forbidden Outcomes

- request success
- target approval changes terminal state

## Conformance Hooks Exercised

- non-`pending` approval rejects `resolve approval`
- terminal approval state is immutable
