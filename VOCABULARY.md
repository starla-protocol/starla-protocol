# Vocabulary

Canonical primary terms for `starla-protocol`.

- A new primary term MUST appear here before first normative use.
- Each primary term MUST have exactly one primary classification.
- Each primary term MUST have exactly one owning specification.

## Canonical Terms

### Resources

- `agent definition` — owner: `drafts/core-v1.md`
- `agent instance` — owner: `drafts/core-v1.md`
- `session` — owner: `drafts/core-v1.md`
- `execution` — owner: `drafts/core-v1.md`
- `approval` — owner: `drafts/core-v1.md`
- `artifact` — owner: `drafts/core-v1.md`
- `channel adapter` — owner: `drafts/channels-v1.md`
- `tool definition` — owner: `drafts/tools-v1.md`

### Commands

- `disable agent definition` — owner: `drafts/core-v1.md`
- `enable agent definition` — owner: `drafts/core-v1.md`
- `pause agent instance` — owner: `drafts/core-v1.md`
- `resume agent instance` — owner: `drafts/core-v1.md`
- `terminate agent instance` — owner: `drafts/core-v1.md`
- `close session` — owner: `drafts/core-v1.md`
- `submit work` — owner: `drafts/core-v1.md`
- `cancel execution` — owner: `drafts/core-v1.md`
- `delegate execution` — owner: `drafts/coordination-v1.md`
- `invoke tool` — owner: `drafts/tools-v1.md`
- `resolve approval` — owner: `drafts/core-v1.md`

### Events

- `agent_definition.created` — owner: `drafts/core-v1.md`
- `agent_definition.updated` — owner: `drafts/core-v1.md`
- `agent_definition.state_changed` — owner: `drafts/core-v1.md`
- `agent_definition.deleted` — owner: `drafts/core-v1.md`
- `agent_instance.activated` — owner: `drafts/core-v1.md`
- `agent_instance.paused` — owner: `drafts/core-v1.md`
- `agent_instance.resumed` — owner: `drafts/core-v1.md`
- `agent_instance.terminated` — owner: `drafts/core-v1.md`
- `session.created` — owner: `drafts/core-v1.md`
- `session.closed` — owner: `drafts/core-v1.md`
- `session.deleted` — owner: `drafts/core-v1.md`
- `execution.created` — owner: `drafts/core-v1.md`
- `execution.state_changed` — owner: `drafts/core-v1.md`
- `execution.blocked` — owner: `drafts/core-v1.md`
- `execution.completed` — owner: `drafts/core-v1.md`
- `execution.failed` — owner: `drafts/core-v1.md`
- `execution.canceled` — owner: `drafts/core-v1.md`
- `execution.delegated` — owner: `drafts/coordination-v1.md`
- `artifact.emitted` — owner: `drafts/core-v1.md`
- `approval.created` — owner: `drafts/core-v1.md`
- `approval.resolved` — owner: `drafts/core-v1.md`
- `tool_definition.created` — owner: `drafts/tools-v1.md`
- `tool_definition.state_changed` — owner: `drafts/tools-v1.md`
- `tool_definition.deleted` — owner: `drafts/tools-v1.md`
- `tool.invoked` — owner: `drafts/tools-v1.md`
- `tool.completed` — owner: `drafts/tools-v1.md`
- `tool.failed` — owner: `drafts/tools-v1.md`
- `tool.blocked` — owner: `drafts/tools-v1.md`

### Relations

- `definition-instance` — owner: `drafts/core-v1.md`
- `session-membership` — owner: `drafts/core-v1.md`
- `execution-lineage` — owner: `drafts/coordination-v1.md`
- `artifact-provenance` — owner: `drafts/core-v1.md`

### Policy Primitives

- `capability` — owner: `drafts/core-v1.md`

### Value Objects

- `channel kind` — owner: `drafts/channels-v1.md`
- `ingress message` — owner: `drafts/channels-v1.md`
- `delivery request` — owner: `drafts/channels-v1.md`
- `delivery result` — owner: `drafts/channels-v1.md`
- `status delivery` — owner: `drafts/channels-v1.md`
- `reply target` — owner: `drafts/channels-v1.md`
- `thread reference` — owner: `drafts/channels-v1.md`
- `context` — owner: `drafts/context-v1.md`
- `context contribution` — owner: `drafts/context-v1.md`
- `reference` — owner: `drafts/core-v1.md`
- `tool result` — owner: `drafts/tools-v1.md`

### Derived Views

- `busy` — owner: `drafts/core-v1.md`
- `channel health` — owner: `drafts/channels-v1.md`
- `context snapshot` — owner: `drafts/context-v1.md`
- `execution snapshot` — owner: `drafts/context-v1.md`

## Non-Canonical Terms

- `Agent` — use `agent definition` or `agent instance`
- `Harness Core` — use `Core v1`
- `connector` — use `channel kind` or `channel adapter`
- `context dump` — use `context snapshot` or `execution snapshot`
- `delegation` — use `delegate execution` or `execution-lineage`
- `tool invocation` — use `invoke tool`
