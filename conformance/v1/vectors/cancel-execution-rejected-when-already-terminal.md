# Cancel Execution Rejected When Already Terminal

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

One visible terminal `execution` rejects `cancel execution`.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `execution` exists in `completed`, `failed`, or `canceled`

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/cancel`.

## Expected Result

- the request fails with `409 Conflict`
- the returned protocol error class is `invalid_state`
- the response body contains `error.code` equal to `invalid_state`

## Expected Created Or Changed Resources

- zero new protocol resources
- the target `execution` remains in its prior terminal state

## Forbidden Outcomes

- request success
- target execution changes terminal state

## Conformance Hooks Exercised

- terminal `execution` rejects `cancel execution`
- terminal states are immutable
