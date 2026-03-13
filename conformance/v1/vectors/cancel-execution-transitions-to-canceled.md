# Cancel Execution Transitions To Canceled

State: Draft
Profile: `Core`
Condition: required when the implementation claims `HTTP Binding v1`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

One visible non-terminal `execution` transitions to `canceled`.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `execution` exists in `pending`, `running`, or `blocked`

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/cancel`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `agent_instance_id`
  - `state`
- `state` equals `canceled`

## Expected Created Or Changed Resources

- zero new protocol resources required
- the target `execution` transitions to `canceled`

## Forbidden Outcomes

- request success with `state` other than `canceled`
- rewritten visible execution identifier
- created replacement `execution`

## Conformance Hooks Exercised

- one visible non-terminal `execution` transitions to `canceled`
