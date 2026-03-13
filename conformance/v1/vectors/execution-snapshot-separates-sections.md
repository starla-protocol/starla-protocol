# Execution Snapshot Separates Sections

State: Draft
Profile: `Core`
Binding: `HTTP v1`
Vector Class: `conditional`
Activation Rule: required when the implementation exposes any of `approvals`, `available_tools`,
`artifacts`, or `recent_events` in `GET /v1/executions/{execution_id}`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`, `drafts/conformance-v1.md`

## Scenario

`GET /v1/executions/{execution_id}` returns one `execution snapshot` with section separation
preserved.

## Preconditions

- one visible `execution` exists
- the implementation exposes at least one optional `execution snapshot` section
- the `execution` has a visible `context snapshot`

## Request Sequence

1. Issue `GET /v1/executions/{execution_id}`.

## Expected Result

- the request succeeds with `200 OK`
- the response body contains:
  - `execution_id`
  - `state`
  - `agent_instance_id`
  - `context`
- `context` satisfies the `context snapshot` shape
- each exposed optional section appears only in its named top-level member:
  - `approvals`
  - `available_tools`
  - `artifacts`
  - `recent_events`

## Expected Created Or Changed Resources

- zero new resources
- zero changed lifecycle states

## Forbidden Outcomes

- approval data embedded within `context`
- tool data embedded within `context`
- artifact data embedded within `context`
- event data embedded within `context`
- `context` replaced by a flattened mixed structure

## Conformance Hooks Exercised

- exported execution snapshots preserve separation between context, tools, approvals, artifacts,
  and events
- lifecycle state matches the underlying execution
