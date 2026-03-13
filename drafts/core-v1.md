# Core v1

State: Draft
Kind: Core Specification
Version: v1
Last Updated: 2026-03-13
Related Context Doc: `context-v1.md`
Related Coordination Doc: `coordination-v1.md`
Related Tools Doc: `tools-v1.md`
Draft Notice: This document does not yet authorize compliance claims.

## Scope

This document is the draft core specification for `starla-protocol`.

Version 1 defines draft transport-independent semantics for a compliant multi-agent harness:

- agent definitions
- agent instances
- sessions
- executions
- artifacts and references
- base lifecycle and error semantics
- core attachment points for context, approvals, tools, and coordination

Out of scope for the first core-specification pass:

- internal memory storage
- retrieval and ranking strategy
- summarization and prompt assembly
- provider and model management
- workflows and automations
- adapters beyond the primary HTTP and streaming bindings
- marketplace or distribution mechanics

Detailed context-construction, inheritance, and exclusion law may be tightened in `context-v1.md`.
Detailed delegation and lineage law may be tightened in `coordination-v1.md`.
Detailed tool-definition and tool-invocation law may be tightened in `tools-v1.md`.

## Compliance Profiles

Profiles:

- `Core` — `Core v1` plus `Context v1` base runtime semantics
- `Core + Tools` — adds tool behavior and capability behavior
- `Core + Approvals` — adds approval-gated behavior
- `Core + Channels` — adds canonical channel ingress and outbound delivery behavior

## Terminology

Normative requirements in this document use `MUST`, `SHOULD`, and `MAY` literally.

Primary terms in this document MUST be classified using `SPEC_METHOD.md`.
Primary terms in this document MUST align with `../VOCABULARY.md`.

This document is authoritative for the externally observable meaning required by compliant
implementations.

## Vocabulary

Each primary term in `Core v1` MUST have exactly one primary classification.

### Resources

- `agent definition` — durable configuration from which agent instances are activated
- `agent instance` — addressable active protocol subject derived from an agent definition
- `session` — addressable shared work context that scopes coordination and visibility
- `execution` — addressable unit of submitted or delegated work
- `approval` — addressable authorization decision associated with one or more executions or actions
- `artifact` — addressable output material emitted by an execution

### Commands

- `submit work` — request that an agent instance create or continue an execution
- `resolve approval` — request that a pending approval transition to a terminal decision

### Relations

- `definition-instance` — relation between an agent instance and the agent definition from which it
  was activated
- `session-membership` — relation between a session and the agent instances or executions scoped by
  it
- `artifact-provenance` — relation between an artifact and the execution that emitted it

### Policy Primitives

- `capability` — named permission or limit evaluated at externally visible boundaries

### Value Objects

- `reference` — portable handle that refers to prior material without reifying it as a new resource

### Derived Views

- `busy` — externally visible occupancy state derived from the state of one or more executions

### Excluded From The Primary Noun Set

- `message submission` is treated as part of the `submit work` command rather than as a standalone
  resource
- `delegate execution` is owned by `coordination-v1.md`
- `execution-lineage` is owned by `coordination-v1.md`
- `tool invocation` is treated as the `invoke tool` command defined in `tools-v1.md`

## Resource Records

### Agent Definition

- Definition: An `agent definition` is a durable configuration resource from which one or more
  `agent instances` may be activated.
- Identity: Every `agent definition` MUST have a stable definition identifier unique within the
  implementation's address space.
- Ownership: Every `agent definition` MUST belong to exactly one owning administrative scope.
- Lifecycle States:
  - `enabled` — new agent instances MAY be activated from the definition.
  - `disabled` — new agent instances MUST NOT be activated from the definition.
  - `deleted` — terminal state; the definition MUST NOT be used again.
- Allowed Transitions:
  - create -> `enabled`
  - `enabled` <-> `disabled`
  - `enabled` or `disabled` -> `deleted`
  - `deleted` -> no further transitions
- Visibility: An implementation MUST expose the definition identifier and current lifecycle state to
  callers authorized to inspect or activate the definition.
- Invariants:
  - every `agent instance` MUST reference exactly one `agent definition`
  - a `deleted` definition MUST NOT gain new `definition-instance` relations
  - a definition MUST NOT transition to `deleted` while any referencing `agent instance` is not in
    a terminal state
- Commands That Create Or Change It:
  - disable definition
  - enable definition
- Events That Expose It:
  - `agent_definition.created`
  - `agent_definition.updated`
  - `agent_definition.state_changed`
  - `agent_definition.deleted`
- Errors Involving It:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - create yields `enabled`
  - `disabled` rejects new instance activation
  - `deleted` is terminal
  - deletion is rejected while any non-terminal `agent instance` still references the definition

### Agent Instance

- Definition: An `agent instance` is an addressable active protocol subject derived from exactly one
  `agent definition`.
- Identity: Every `agent instance` MUST have a stable instance identifier distinct from its
  definition identifier.
- Ownership: Every `agent instance` MUST inherit the owning administrative scope of its
  `agent definition`.
- Lifecycle States:
  - `ready` — the instance MAY accept `submit work`
  - `paused` — the instance MUST NOT accept `submit work`
  - `terminated` — terminal state; the instance MUST NOT accept any new work
- Allowed Transitions:
  - activate -> `ready`
  - `ready` <-> `paused`
  - `ready` or `paused` -> `terminated`
  - `terminated` -> no further transitions
- Visibility: An implementation MUST expose the instance identifier, definition identifier, and
  current lifecycle state to callers authorized to inspect the instance.
- Invariants:
  - every `agent instance` MUST reference exactly one `agent definition`
  - a `paused` or `terminated` instance MUST NOT accept `submit work`
  - a `terminated` instance MUST NOT gain new owning `execution` resources
  - `busy` is a derived view and MUST NOT be modeled as a separate lifecycle state
- Commands That Create Or Change It:
  - pause instance
  - resume instance
  - terminate instance
- Events That Expose It:
  - `agent_instance.activated`
  - `agent_instance.paused`
  - `agent_instance.resumed`
  - `agent_instance.terminated`
- Errors Involving It:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - activation from a `disabled` or `deleted` definition is rejected
  - `paused` rejects `submit work`
  - `terminated` is terminal
  - `busy` becomes externally visible when the instance owns one or more non-terminal executions

### Session

- Definition: A `session` is an addressable shared coordination scope that may carry shared context
  and shared visibility for multiple executions and agent instances.
- Identity: Every `session` MUST have a stable session identifier unique within the implementation's
  address space.
- Ownership: Every `session` MUST belong to exactly one owning administrative scope.
- Lifecycle States:
  - `open` — new work MAY be submitted against the session
  - `closed` — new work MUST NOT be newly attached to the session
  - `deleted` — terminal state; the session MUST NOT be reused
- Allowed Transitions:
  - create -> `open`
  - `open` -> `closed`
  - `open` or `closed` -> `deleted`
  - `closed` -> no transition back to `open` in `Core v1`
  - `deleted` -> no further transitions
- Visibility: An implementation MUST expose the session identifier and lifecycle state to callers
  authorized to inspect or target the session.
- Invariants:
  - `session-membership` MUST refer only to an existing non-`deleted` session
  - a `closed` session MUST NOT gain new attached executions
  - a `deleted` session MUST NOT gain new `session-membership` relations
  - deleting a session MUST NOT mutate already-created executions into a different session
- Commands That Create Or Change It:
  - close session
- Events That Expose It:
  - `session.created`
  - `session.closed`
  - `session.deleted`
- Errors Involving It:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - create yields `open`
  - `closed` rejects new session-attached work
  - `deleted` is terminal
  - attaching work to a missing session is rejected

### Execution

- Definition: An `execution` is an addressable unit of submitted or delegated work owned by exactly
  one `agent instance`.
- Identity: Every `execution` MUST have a stable execution identifier unique within the
  implementation's address space.
- Ownership:
  - every `execution` MUST belong to exactly one owning `agent instance`
  - every delegated `execution` MUST have at most one parent execution in `execution-lineage`
- Lifecycle States:
  - `pending` — created but not yet started
  - `running` — actively progressing
  - `blocked` — unable to progress because an external condition such as approval is unresolved
  - `completed` — terminal successful state
  - `failed` — terminal unsuccessful state
  - `canceled` — terminal canceled state
- Allowed Transitions:
  - create -> `pending`
  - `pending` -> `running` | `blocked` | `failed` | `canceled`
  - `running` -> `blocked` | `completed` | `failed` | `canceled`
  - `blocked` -> `pending` | `running` | `failed` | `canceled`
  - `completed` | `failed` | `canceled` -> no further transitions
- Visibility: An implementation MUST expose the execution identifier, owning instance identifier,
  current lifecycle state, and parent execution identifier if one exists.
- Invariants:
  - terminal executions MUST NOT transition again
  - visible `failed` and `canceled` states MUST remain execution terminal outcomes rather than
    transport-level errors
  - every emitted `artifact` MUST reference exactly one source `execution`
  - a child execution MUST NOT outlive the visibility of its parent `execution-lineage` relation
  - a blocked execution MUST expose the fact that it is blocked even if the implementation does not
    expose the full internal reason
- Commands That Create Or Change It:
  - `submit work`
  - `delegate execution`, as defined by `coordination-v1.md`
  - `cancel execution`
- Events That Expose It:
  - `execution.created`
  - `execution.state_changed`
  - `execution.blocked`
  - `execution.completed`
  - `execution.failed`
  - `execution.canceled`
  - `artifact.emitted`
- Errors Involving It:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
  - `approval_denied`
- Conformance Hooks:
  - every execution begins in `pending`
  - terminal states are immutable
  - visible failed execution inspection remains normal resource inspection
  - parent-child lineage is preserved for delegated executions
  - emitted artifacts preserve `artifact-provenance`

### Approval

- Definition: An `approval` is an addressable authorization decision associated with one or more
  gated executions or execution-scoped actions.
- Identity: Every `approval` MUST have a stable approval identifier unique within the
  implementation's address space.
- Ownership: Every `approval` MUST belong to exactly one owning administrative scope.
- Lifecycle States:
  - `pending` — unresolved; the gated execution or action MUST remain gated
  - `approved` — terminal allow decision
  - `denied` — terminal deny decision
- Allowed Transitions:
  - create -> `pending`
  - `pending` -> `approved` | `denied`
  - `approved` | `denied` -> no further transitions
- Visibility: An implementation MUST expose the approval identifier and current lifecycle state to
  callers authorized to inspect the approval.
- Invariants:
  - terminal approvals MUST NOT transition again
  - a `pending` approval MUST NOT expose a terminal decision
  - a terminal approval identifier MUST NOT later represent the opposite terminal decision
- Commands That Create Or Change It:
  - create approval
  - `resolve approval`
- Events That Expose It:
  - `approval.created`
  - `approval.resolved`
- Errors Involving It:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - approval-gated work yields a visible `pending` approval
  - terminal approval state is immutable
  - non-`pending` approval rejects `resolve approval`

### Artifact

- Definition: An `artifact` is an addressable output material emitted by exactly one `execution`.
- Identity: Every `artifact` MUST have a stable artifact identifier unique within the
  implementation's address space.
- Ownership: Every `artifact` MUST inherit the owning administrative scope of its source
  `execution`.
- Lifecycle States:
  - `available` — emitted and visible for inspection where the binding exposes artifact inspection
- Allowed Transitions:
  - emit -> `available`
  - `available` -> no further lifecycle transition is defined in `Core v1`
- Visibility:
  - if the binding exposes artifact inspection, the implementation MUST expose the artifact
    identifier and source execution identifier to authorized callers
- Invariants:
  - every `artifact` MUST reference exactly one source `execution`
  - an `artifact` source execution identifier MUST NOT change after emission
  - `artifact.emitted` MUST NOT appear before the source `execution` exists
- Commands That Create Or Change It:
  - emit artifact
- Events That Expose It:
  - `artifact.emitted`
- Errors Involving It:
  - `not_found`
  - `capability_denied`
- Conformance Hooks:
  - every visible `artifact` preserves `artifact-provenance`
  - source execution identifier is immutable
  - `artifact.emitted` follows source execution creation

## Value Object Records

### Reference

- Definition: A `reference` is a portable protocol-visible handle to prior material without creating
  a new standalone resource.
- Shape:
  - reference handle
  - optional visible source kind
  - optional visible source identifier
- Validation Rules:
  - accepted `reference` input MUST remain distinguishable from direct input material
  - one visible `reference` MUST NOT imply creation of a new resource
  - if one visible `reference` includes a visible source identifier, that identifier MUST remain
    stable for that visible `reference`
- Equality Or Identity Rules:
  - `reference` has no standalone lifecycle or resource identity in `Core v1`
- Visibility:
  - explicit caller `reference` input accepted by `submit work` MUST remain visible only as
    explicit references at the originating execution boundary
  - explicit caller `reference` input carried across lineage MUST follow `context-v1.md`
- Invariants:
  - accepting one visible `reference` MUST NOT by itself expose hidden source material
  - a visible `reference` MUST NOT be relabeled as direct caller input
- Conformance Hooks:
  - explicit references remain references
  - explicit caller references remain distinct from payload
  - carried-forward parent references do not remain explicit references at the child boundary

## Command Records

`Core v1` in the current `v1` target defines only the stable lifecycle-mutation commands listed
below.

Bootstrap or provisioning commands for creating, updating, deleting, or activating core resources
are outside the current `v1` public command surface unless standardized later.

### Disable Agent Definition

- Actor: A caller authorized to address the target `agent definition`.
- Target: Exactly one `agent definition`.
- Preconditions:
  - the target `agent definition` MUST exist
  - the target `agent definition` MUST be visible to the caller
  - the target `agent definition` MUST be in `enabled`
  - the caller MUST satisfy capability checks required by the definition boundary
- Inputs:
  - target definition identifier
- Side Effects:
  - `disable agent definition` MUST transition exactly one target `agent definition` to `disabled`
- Resources Created Or Changed:
  - changes one `agent definition`
- Events Emitted:
  - `agent_definition.state_changed`
- Errors:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - enabled definition transitions to `disabled`

### Enable Agent Definition

- Actor: A caller authorized to address the target `agent definition`.
- Target: Exactly one `agent definition`.
- Preconditions:
  - the target `agent definition` MUST exist
  - the target `agent definition` MUST be visible to the caller
  - the target `agent definition` MUST be in `disabled`
  - the caller MUST satisfy capability checks required by the definition boundary
- Inputs:
  - target definition identifier
- Side Effects:
  - `enable agent definition` MUST transition exactly one target `agent definition` to `enabled`
- Resources Created Or Changed:
  - changes one `agent definition`
- Events Emitted:
  - `agent_definition.state_changed`
- Errors:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - disabled definition transitions to `enabled`

### Pause Agent Instance

- Actor: A caller authorized to address the target `agent instance`.
- Target: Exactly one `agent instance`.
- Preconditions:
  - the target `agent instance` MUST exist
  - the target `agent instance` MUST be visible to the caller
  - the target `agent instance` MUST be in `ready`
  - the caller MUST satisfy capability checks required by the instance boundary
- Inputs:
  - target instance identifier
- Side Effects:
  - `pause agent instance` MUST transition exactly one target `agent instance` to `paused`
- Resources Created Or Changed:
  - changes one `agent instance`
- Events Emitted:
  - `agent_instance.paused`
- Errors:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - ready instance transitions to `paused`
  - `paused` rejects `submit work`

### Resume Agent Instance

- Actor: A caller authorized to address the target `agent instance`.
- Target: Exactly one `agent instance`.
- Preconditions:
  - the target `agent instance` MUST exist
  - the target `agent instance` MUST be visible to the caller
  - the target `agent instance` MUST be in `paused`
  - the caller MUST satisfy capability checks required by the instance boundary
- Inputs:
  - target instance identifier
- Side Effects:
  - `resume agent instance` MUST transition exactly one target `agent instance` to `ready`
- Resources Created Or Changed:
  - changes one `agent instance`
- Events Emitted:
  - `agent_instance.resumed`
- Errors:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - paused instance transitions to `ready`

### Terminate Agent Instance

- Actor: A caller authorized to address the target `agent instance`.
- Target: Exactly one `agent instance`.
- Preconditions:
  - the target `agent instance` MUST exist
  - the target `agent instance` MUST be visible to the caller
  - the target `agent instance` MUST be in `ready` or `paused`
  - the caller MUST satisfy capability checks required by the instance boundary
- Inputs:
  - target instance identifier
- Side Effects:
  - `terminate agent instance` MUST transition exactly one target `agent instance` to `terminated`
  - `terminate agent instance` MUST NOT create a new `execution`
- Resources Created Or Changed:
  - changes one `agent instance`
- Events Emitted:
  - `agent_instance.terminated`
- Errors:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - ready or paused instance transitions to `terminated`
  - `terminated` is terminal

### Close Session

- Actor: A caller authorized to address the target `session`.
- Target: Exactly one `session`.
- Preconditions:
  - the target `session` MUST exist
  - the target `session` MUST be visible to the caller
  - the target `session` MUST be in `open`
  - the caller MUST satisfy capability checks required by the session boundary
- Inputs:
  - target session identifier
- Side Effects:
  - `close session` MUST transition exactly one target `session` to `closed`
- Resources Created Or Changed:
  - changes one `session`
- Events Emitted:
  - `session.closed`
- Errors:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - open session transitions to `closed`
  - `closed` rejects new session-attached work

### Submit Work

- Actor: A caller authorized to address the target `agent instance`.
- Target: Exactly one `agent instance`.
- Preconditions:
  - the target `agent instance` MUST exist
  - the target `agent instance` MUST be in `ready`
  - the caller MUST satisfy capability checks required by the target boundary
  - if a `session` is supplied, that `session` MUST exist, be visible to the caller, and be in
    `open`
- Inputs:
  - target instance identifier
  - work payload
  - optional session identifier
  - optional references
  - optional idempotency key
- Side Effects:
  - a successful `submit work` MUST create exactly one new `execution` unless it resolves through a
    prior idempotent result
  - the created execution MUST initially enter `pending`
  - explicit payload and explicit references MUST become part of the execution's visible `context`
    as defined by `context-v1.md`
  - if a `session` is supplied, the created execution MUST gain `session-membership` in that
    session
  - if approval is required before progress may continue, the execution MUST enter `blocked` before
    `submit work` completes rather than causing `submit work` itself to fail
  - if approval is required before progress may continue, at least one visible `pending`
    `approval` MUST exist before `submit work` completes
- Resources Created Or Changed:
  - creates an `execution`
  - may create an `approval`
  - may create or attach `artifact` references only after the execution progresses
- Events Emitted:
  - `execution.created` MUST be emitted if a new execution is created
  - `approval.created`, if emitted for the created execution, MUST appear after `execution.created`
    and before `execution.blocked`
  - the first subsequent lifecycle event MUST be one of `execution.state_changed`,
    `execution.blocked`, `execution.failed`, or `execution.canceled`
  - `execution.created` MUST appear before any other event for the same execution
- Errors:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
  - `idempotency_conflict`
- Idempotency:
  - if the binding exposes an idempotency key, repeated `submit work` requests with the same key
    and the same semantic target MUST resolve to the same execution result
  - if the same idempotency key is reused with materially different input, the implementation MUST
    reject the request with `idempotency_conflict`
- Conformance Hooks:
  - `paused` and `terminated` instances reject `submit work`
  - `closed` sessions reject new session-attached work
  - approval-gated work creates a blocked execution and visible pending approval rather than
    failing the command
  - `execution.created` is ordered before any other event for the created execution

### Resolve Approval

- Actor: A caller authorized to address the target `approval`.
- Target: Exactly one `approval`.
- Preconditions:
  - the target `approval` MUST exist
  - the target `approval` MUST be in `pending`
  - the caller MUST satisfy capability checks required by the approval boundary
- Inputs:
  - target approval identifier
  - approval decision
- Side Effects:
  - `resolve approval` MUST transition exactly one `pending` approval to one terminal decision
  - `resolve approval` MUST NOT by itself imply successful completion of the associated execution
    or action
- Resources Created Or Changed:
  - changes one `approval`
  - may change associated execution visible state after approval resolution
- Events Emitted:
  - `approval.resolved`
- Errors:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - `pending` approvals resolve to exactly one terminal state
  - `approved` and `denied` approvals reject further `resolve approval`

### Cancel Execution

- Actor: A caller authorized to address the target `execution`.
- Target: Exactly one `execution`.
- Preconditions:
  - the target `execution` MUST exist
  - the target `execution` MUST be visible to the caller
  - the target `execution` MUST be in `pending`, `running`, or `blocked`
  - the caller MUST satisfy capability checks required by the execution boundary
- Inputs:
  - target execution identifier
- Side Effects:
  - `cancel execution` MUST transition exactly one target `execution` to `canceled`
  - `cancel execution` MUST NOT create a new `execution`
  - `cancel execution` MUST NOT rewrite visible ownership, session, or parent identifiers of the
    target `execution`
- Resources Created Or Changed:
  - changes one `execution`
- Events Emitted:
  - `execution.canceled`
- Errors:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - one visible non-terminal `execution` transitions to `canceled`
  - terminal `execution` rejects `cancel execution`
  - `execution.canceled` is the only terminal event for the canceled `execution`

## Event Model

Core event ordering rules:

- `execution.created` MUST precede any later event for the same created `execution`
- `approval.created` for new approval-gated submitted work MUST follow `execution.created` and
  precede `execution.blocked`
- `approval.resolved` MUST NOT precede `approval.created` for the same `approval`
- `artifact.emitted` MUST follow source `execution` creation
- `execution.canceled` MUST NOT precede `execution.created` for the same `execution`
- exactly one of `execution.completed`, `execution.failed`, or `execution.canceled` MAY appear for
  the same `execution`
- no later `execution.state_changed`, `execution.blocked`, or `artifact.emitted` event for that
  `execution` MAY appear after `execution.completed`, `execution.failed`, or `execution.canceled`

Conformance hooks:

- `../conformance/v1/traces/execution-lifecycle-minimal.md`
- `../conformance/v1/traces/execution-completion-terminal.md`
- `../conformance/v1/traces/execution-cancel-terminal.md`
- `../conformance/v1/traces/execution-failure-terminal.md`

## Error Model

Core error-selection rules:

- `not_found` MUST be used only when the addressed resource does not exist or is not visible at
  the protocol boundary
- `invalid_state` MUST be used only when the addressed resource is visible and its current state
  forbids the requested operation
- `capability_denied` MUST be used only when a visible resource or action target is denied by
  capability policy after target resolution
- `approval_denied` MUST be used only when a visible terminal approval decision denies a visible
  action after target resolution
- inspection of an existing visible `execution` in `failed` or `canceled` MUST remain normal
  resource inspection rather than `not_found` or transport-level error
- caller timeout, caller disconnect, or stream interruption MUST NOT by itself be interpreted as a
  terminal `execution` state

Conformance hooks:

- `../conformance/v1/vectors/missing-execution-inspection-returns-not-found.md`
- `../conformance/v1/vectors/cancel-execution-rejected-when-already-terminal.md`
- `../conformance/v1/vectors/submit-work-rejected-when-instance-paused.md`
- `../conformance/v1/vectors/resolve-approval-rejected-when-already-resolved.md`
- `../conformance/v1/vectors/invoke-tool-denied-by-capability.md`
- `../conformance/v1/vectors/invoke-tool-terminal-approval-denial-returns-approval-denied.md`
- `../conformance/v1/vectors/failed-execution-inspection-is-not-transport-error.md`
- `../conformance/v1/vectors/execution-stream-disconnect-does-not-create-terminal-outcome.md`

## Conformance Hooks

The conformance specification for `Core v1` is defined in `conformance-v1.md`.
