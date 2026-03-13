# Recomputed Implementation-Supplied Visible On Child Execution

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Vector Class: `conditional`
Activation Rule: required when a visible child `execution` exposes independently recomputed visible
implementation-supplied material at the context boundary
Related Spec: `drafts/context-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

Independently recomputed visible implementation-supplied material appears only in
`implementation_supplied` on a child execution.

## Preconditions

- one visible parent `execution` exists
- one visible child `execution` exists
- a visible `execution-lineage` relation exists between them
- the child `execution` exposes independently recomputed visible implementation-supplied material
  at the context boundary

## Request Sequence

1. Issue `GET /v1/executions/{child_execution_id}/context`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `agent_instance_id`
  - `implementation_supplied`
- independently recomputed child-boundary material appears only in `implementation_supplied`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states

## Forbidden Outcomes

- independently recomputed child-boundary material relabeled as `inherited_lineage_material`
- independently recomputed child-boundary material relabeled as `explicit_input`
- independently recomputed child-boundary material relabeled as `explicit_references`

## Conformance Hooks Exercised

- independently recomputed implementation-supplied material remains `implementation_supplied`
- independently recomputed implementation-supplied material remains distinct from visible lineage
  material
