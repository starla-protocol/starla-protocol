# Approval Inspection Exposes State

State: Draft
Profile: `Core + Approvals`
Condition: required when the implementation claims `Core + Approvals` and claims `HTTP Binding v1`,
or exposes approval inspection on the public binding
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `approval` is inspected on the public HTTP binding.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `approval` exists

## Request Sequence

1. Issue `GET /v1/approvals/{approval_id}`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `approval_id`
  - `state`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required

## Forbidden Outcomes

- omission of `approval_id`
- omission of `state`
- rewriting the visible approval identifier

## Conformance Hooks Exercised

- approval inspection exposes identifier and lifecycle state
