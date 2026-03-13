# Tool Invocation With Artifact

State: Draft
Profile: `Core + Tools`
Condition: required when the implementation exposes visible artifact emission during `invoke tool`
Scenario: one enabled tool invocation completes successfully and emits one visible artifact
Related Spec: `drafts/tools-v1.md`, `drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible non-terminal `execution`
2. invoke one enabled `tool definition`
3. allow the accepted invocation to emit one visible `artifact` and complete successfully

## Required Event Order

1. `tool.invoked`
2. `artifact.emitted`
3. `tool.completed`

## Terminal Condition

- the accepted invocation ends with outcome `completed`

## Forbidden Missing Or Reordered Events

- `tool.completed` before `tool.invoked`
- `artifact.emitted` before `tool.invoked`
- `artifact.emitted` after `tool.completed`
- `tool.failed` after `tool.completed`
- `tool.blocked` after `tool.completed`
- more than one terminal tool event for the same accepted invocation

## Conformance Hooks Exercised

- accepted invocation emits `tool.invoked` first
- emitted artifacts preserve `artifact-provenance`
- emitted artifacts are ordered between `tool.invoked` and the terminal tool event
