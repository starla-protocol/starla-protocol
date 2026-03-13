# Artifact Record Preserves Provenance

State: Draft
Profile: `Core + Tools`
Condition: required when the implementation exposes visible artifact emission and artifact
inspection
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/tools-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One accepted tool invocation emits one visible artifact, and artifact inspection preserves source
execution provenance.

## Preconditions

- one visible non-terminal `execution` exists
- one visible `tool definition` exists in `enabled`
- capability checks pass
- the invocation emits one visible artifact identifier

## Request Sequence

1. Issue `POST /v1/executions/{execution_id}/tools/{tool_id}/invoke` with `input`.
2. Read one returned `artifact_id`.
3. Issue `GET /v1/artifacts/{artifact_id}`.
4. Issue `GET /v1/artifacts/{artifact_id}` again.

## Expected Result

- the invoke request succeeds
- each artifact read succeeds with `200 OK`
- each artifact response body contains:
  - `artifact_id`
  - `source_execution_id`
- `source_execution_id` equals the invoking `execution_id` on both reads

## Expected Created Or Changed Resources

- one or more visible `artifact` resources
- zero changed artifact provenance after emission

## Expected Events

- `artifact.emitted` is visible for the emitted artifact

## Forbidden Outcomes

- artifact response omits `source_execution_id`
- artifact response changes `source_execution_id` across reads
- artifact emitted before source execution creation

## Conformance Hooks Exercised

- every visible `artifact` preserves `artifact-provenance`
- source execution identifier is immutable
- `artifact.emitted` follows source execution creation
