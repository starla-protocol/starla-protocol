# Context Snapshot Omits Absent Contribution Sections

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Related Spec: `drafts/context-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

`GET /v1/executions/{execution_id}/context` omits absent contribution sections.

## Preconditions

- one visible `execution` exists
- the `execution` has visible explicit caller input
- the `execution` has visible explicit caller references
- the `execution` has no visible `session-scoped material`
- the `execution` has no visible `inherited lineage material`
- the `execution` exposes no visible `tool-derived material`
- the `execution` exposes no visible `event-derived material`
- the `execution` exposes no visible `implementation-supplied material`

## Request Sequence

1. Issue `GET /v1/executions/{execution_id}/context`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `agent_instance_id`
  - `explicit_input`
  - `explicit_references`
- the response body omits:
  - `session_material`
  - `inherited_lineage_material`
  - `tool_derived_material`
  - `event_derived_material`
  - `implementation_supplied`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states

## Forbidden Outcomes

- absent contribution classes represented as empty or relabeled sections
- `session_material` present without visible session-scoped material
- `implementation_supplied` present without visible implementation-supplied material

## Conformance Hooks Exercised

- omitted contribution classes are omitted rather than silently relabeled
- explicit caller references remain distinct from direct input material
