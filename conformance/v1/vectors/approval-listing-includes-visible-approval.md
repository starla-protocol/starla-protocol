# Approval Listing Includes Visible Approval

State: Draft
Profile: `Core + Approvals`
Condition: required when the implementation claims `Core + Approvals` and claims `HTTP Binding v1`,
or exposes approval inspection on the public binding
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `approval` appears in the canonical HTTP list route.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `approval` exists

## Request Sequence

1. Issue `GET /v1/approvals`.

## Expected Result

- the request succeeds with `200 OK`
- the response body is a JSON array
- at least one array item contains:
  - `approval_id`
  - `state`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- non-array response body
- visible approval omitted from the returned listing
- listed item missing `approval_id`
- listed item missing `state`

## Conformance Hooks Exercised

- approval list route exposes visible approval identifier and lifecycle state
