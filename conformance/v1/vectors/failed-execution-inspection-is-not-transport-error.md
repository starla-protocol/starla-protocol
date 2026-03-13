# Failed Execution Inspection Is Not Transport Error

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `execution` reaches terminal `failed` state and remains inspectable as a normal
resource.

## Preconditions

- one visible `execution` exists
- the visible `execution` reaches terminal `failed` state

## Request Sequence

1. Issue `GET /v1/executions/{execution_id}` for the visible failed execution.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `state`
- `state` equals `failed`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states during inspection

## Forbidden Outcomes

- `404 Not Found` for an existing visible failed execution
- transport-level error used as the representation of visible failed execution state
- omission of `execution_id`
- omission of `state`

## Conformance Hooks Exercised

- visible failed execution inspection remains normal resource inspection
