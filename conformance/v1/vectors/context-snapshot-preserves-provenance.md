# Context Snapshot Preserves Provenance

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

`GET /v1/executions/{execution_id}/context` returns one `context snapshot` with preserved
provenance buckets.

## Preconditions

- one visible `execution` exists
- the `execution` has visible explicit caller input
- the `execution` has visible explicit caller references
- the `execution` MAY have visible session-scoped material
- the implementation MAY expose visible implementation-supplied material at the protocol boundary

## Request Sequence

1. Issue `GET /v1/executions/{execution_id}/context`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `agent_instance_id`
  - `explicit_input`
  - `explicit_references`
- `explicit_references` remains distinct from `explicit_input`
- if session material is present, it appears only in `session_material`
- if implementation-supplied material is exposed, it appears only in `implementation_supplied`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states

## Forbidden Outcomes

- `explicit_references` flattened into `explicit_input`
- any present `session_material` merged into direct caller input
- any exposed `implementation_supplied` relabeled as caller input
- omission of `execution_id`
- omission of `agent_instance_id`

## Conformance Hooks Exercised

- exported context preserves provenance buckets
- explicit caller references remain distinct from payload
- implementation-supplied material is never labeled as caller input
