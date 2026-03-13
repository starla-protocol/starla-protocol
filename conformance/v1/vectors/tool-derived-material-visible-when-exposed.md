# Tool-Derived Material Visible When Exposed

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Vector Class: `conditional`
Activation Rule: required when an execution exposes visible `tool_derived_material` in a context
snapshot
Related Spec: `drafts/context-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

Visible tool-derived contribution appears only in `tool_derived_material`.

## Preconditions

- one visible `execution` exists
- the `execution` exposes visible tool-derived contribution at the context boundary

## Request Sequence

1. Issue `GET /v1/executions/{execution_id}/context`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `agent_instance_id`
  - `tool_derived_material`
- visible tool-derived contribution appears only in `tool_derived_material`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states

## Forbidden Outcomes

- visible tool-derived contribution relabeled as `explicit_input`
- visible tool-derived contribution relabeled as `implementation_supplied`
- visible tool-derived contribution relabeled as `event_derived_material`

## Conformance Hooks Exercised

- tool-derived material remains distinguishable from other contribution classes
