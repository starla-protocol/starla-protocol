# Missing Approval Inspection Returns Not Found

State: Draft
Profile: `Core + Approvals`
Condition: required when the implementation claims `HTTP Binding v1` and exposes approval
inspection on the public binding
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

Inspection of one non-existent or non-visible `approval` returns `not_found`.

## Preconditions

- the target `approval_id` does not identify one visible `approval`

## Request Sequence

1. Issue `GET /v1/approvals/{approval_id}` for the missing or non-visible approval identifier.

## Expected Result

- the request fails with `404 Not Found`
- the response body uses the normal error envelope
- `error.code` equals `not_found`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states

## Forbidden Outcomes

- `200 OK` for a missing or non-visible approval
- `409 Conflict` for a missing or non-visible approval
- transport-specific error body without protocol-law `error.code`

## Conformance Hooks Exercised

- missing visible-target approval inspection returns `not_found`
