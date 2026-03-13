# Artifact Listing Includes Visible Artifact

State: Draft
Profile: `Core + Tools`
Condition: required when the implementation claims `HTTP Binding v1` and exposes artifact
inspection on the public binding
Binding: `HTTP v1`
Related Spec: `drafts/core-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Scenario

One visible `artifact` appears in the canonical HTTP list route.

## Preconditions

- the implementation claims `HTTP Binding v1`
- one visible `artifact` exists

## Request Sequence

1. Issue `GET /v1/artifacts`.

## Expected Result

- the request succeeds with `200 OK`
- the response body is a JSON array
- at least one array item contains:
  - `artifact_id`
  - `source_execution_id`

## Expected Created Or Changed Resources

- zero new protocol resources required
- zero changed artifact provenance required

## Forbidden Outcomes

- non-array response body
- visible artifact omitted from the returned listing
- listed item missing `artifact_id`
- listed item missing `source_execution_id`

## Conformance Hooks Exercised

- artifact list route exposes visible artifact identifier and source execution provenance
