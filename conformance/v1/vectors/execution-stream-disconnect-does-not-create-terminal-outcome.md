# Execution Stream Disconnect Does Not Create Terminal Outcome

State: Draft
Profile: `Core`
Condition: required when the implementation claims `Stream Binding v1`
Binding: `Stream v1`
Related Spec: `drafts/core-v1.md`, `drafts/stream-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One client disconnects from one execution-event stream while the visible `execution` remains
non-terminal and externally blocked.

## Preconditions

- the implementation claims `Stream Binding v1`
- one visible `execution` exists in `blocked`
- one visible `pending` `approval` still gates that `execution`

## Request Sequence

1. Open `GET /v1/executions/{execution_id}/events`.
2. Disconnect the client stream without resolving the visible `approval` or issuing any execution
   state-changing command.
3. Issue `GET /v1/executions/{execution_id}`.

## Expected Result

- the inspection request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `state`
- `state` equals `blocked`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero terminal execution transitions caused by disconnect alone

## Forbidden Outcomes

- `state` equals `completed`
- `state` equals `failed`
- `state` equals `canceled`
- `404 Not Found` for the still-visible blocked execution

## Conformance Hooks Exercised

- stream disconnect does not by itself create a terminal execution outcome
