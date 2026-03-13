# Inherited Lineage Material Visible On Child Execution

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Vector Class: `conditional`
Activation Rule: required when a visible child `execution` exposes visible inherited lineage
material at the context boundary
Related Spec: `drafts/context-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

Visible carried-forward parent material appears only as `inherited_lineage_material` on a child
execution.

## Preconditions

- one visible parent `execution` exists
- one visible child `execution` exists
- a visible `execution-lineage` relation exists between them
- the child `execution` exposes visible inherited lineage material at the context boundary

## Request Sequence

1. Issue `GET /v1/executions/{child_execution_id}/context`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `agent_instance_id`
  - `inherited_lineage_material`
- carried-forward parent material appears only in `inherited_lineage_material`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states

## Forbidden Outcomes

- carried-forward parent material relabeled as `explicit_input`
- carried-forward parent material relabeled as `explicit_references`
- carried-forward parent material relabeled as `implementation_supplied`
- `inherited_lineage_material` present without a visible parent-child relation

## Conformance Hooks Exercised

- lineage material appears only where a visible parent-child execution relation exists
- carried-forward parent material appears only as `inherited_lineage_material`
