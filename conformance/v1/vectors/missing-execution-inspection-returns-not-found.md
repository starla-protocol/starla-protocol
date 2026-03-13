# Missing Execution Inspection Returns Not Found

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

Inspection of one non-existent or non-visible `execution` returns `not_found`.

## Preconditions

- the target `execution_id` does not identify one visible `execution`

## Request Sequence

1. Issue `GET /v1/executions/{execution_id}` for the missing or non-visible execution identifier.

## Expected Result

- the request fails with `404 Not Found`
- the response body uses the normal error envelope
- `error.code` equals `not_found`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states

## Forbidden Outcomes

- `200 OK` for a missing or non-visible execution
- `409 Conflict` for a missing or non-visible execution
- transport-specific error body without protocol-law `error.code`

## Conformance Hooks Exercised

- missing visible-target inspection returns `not_found`
