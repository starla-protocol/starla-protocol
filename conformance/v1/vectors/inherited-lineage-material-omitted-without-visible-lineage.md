# Inherited Lineage Material Omitted Without Visible Lineage

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/context-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

`GET /v1/executions/{execution_id}/context` omits `inherited_lineage_material` when no visible
parent-child relation exists at the target boundary.

## Preconditions

- one visible `execution` exists
- no visible `execution-lineage` relation exists at the target boundary
- the `execution` has visible context material from at least one other contribution class

## Request Sequence

1. Issue `GET /v1/executions/{execution_id}/context`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `agent_instance_id`
- the response body omits `inherited_lineage_material`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states

## Forbidden Outcomes

- `inherited_lineage_material` present without a visible `execution-lineage` relation
- hidden lineage-carried material relabeled as `explicit_input`
- hidden lineage-carried material relabeled as `explicit_references`

## Conformance Hooks Exercised

- `inherited_lineage_material` is omitted when no visible parent-child relation exists
- hidden lineage material is not relabeled as direct caller material
