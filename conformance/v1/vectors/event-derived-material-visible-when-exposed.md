# Event-Derived Material Visible When Exposed

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Vector Class: `conditional`
Activation Rule: required when an execution exposes visible `event_derived_material` in a context
snapshot
Related Spec: `drafts/context-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

Visible event-derived contribution appears only in `event_derived_material`.

## Preconditions

- one visible `execution` exists
- the `execution` exposes visible event-derived contribution at the context boundary

## Request Sequence

1. Issue `GET /v1/executions/{execution_id}/context`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `agent_instance_id`
  - `event_derived_material`
- visible event-derived contribution appears only in `event_derived_material`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states

## Forbidden Outcomes

- visible event-derived contribution relabeled as `explicit_input`
- visible event-derived contribution relabeled as `implementation_supplied`
- visible event-derived contribution relabeled as `tool_derived_material`

## Conformance Hooks Exercised

- event-derived material remains distinguishable from other contribution classes
