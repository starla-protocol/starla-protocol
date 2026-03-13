# Execution Stream Missing Target Returns Not Found

State: Draft
Profile: `Core`
Condition: required when the implementation claims `Stream Binding v1`
Binding: `Stream v1`
Related Spec: `drafts/stream-binding-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One execution-event stream request targets one missing or non-visible `execution`.

## Preconditions

- the implementation claims `Stream Binding v1`
- the target `execution_id` does not identify one visible `execution`

## Request Sequence

1. Issue `GET /v1/executions/{execution_id}/events`.

## Expected Result

- the request fails with `404 Not Found`
- the response body uses the normal error envelope
- `error.code` equals `not_found`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed lifecycle states required by stream target rejection alone

## Forbidden Outcomes

- `200 OK` stream response for one missing or non-visible `execution`
- `409 Conflict` for one missing or non-visible `execution`
- transport-specific error body without protocol-law `error.code`

## Conformance Hooks Exercised

- missing visible stream target returns `not_found`
