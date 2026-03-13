# Tools v1

State: Draft
Kind: Core Specification
Version: v1
Last Updated: 2026-03-13
Related Core Doc: `core-v1.md`
Related Context Doc: `context-v1.md`
Draft Notice: This document does not yet authorize compliance claims.

## Scope

This document defines the draft tools specification for `starla-protocol`.

`Tools v1` defines draft:

- tool definition identity and visibility
- tool invocation semantics
- tool input and result shape
- tool failure semantics
- capability and approval gating at the tool boundary
- visible tool event ordering
- emitted artifact behavior at the tool boundary
- visible tool-derived contribution to context

This pass does not define tool-definition bootstrap or lifecycle mutation routing on the current
`v1` public binding surface.

## Terminology

Primary terms in this document MUST align with `../VOCABULARY.md`.

## Vocabulary

Primary `Tools v1` terms:

- `tool definition` — addressable definition of one invocable tool boundary
- `invoke tool` — request that one `execution` perform one tool action
- `tool result` — visible outcome value produced by one accepted `invoke tool`

## Resource Records

### Tool Definition

- Definition: A `tool definition` is an addressable description of one invocable tool boundary.
- Identity: Every `tool definition` MUST have a stable tool identifier unique within the
  implementation's address space.
- Ownership: Every `tool definition` MUST belong to exactly one owning administrative scope.
- Lifecycle States:
  - `enabled` — the tool MAY be invoked when all other boundary conditions pass
  - `disabled` — the tool MUST NOT be invoked
  - `deleted` — terminal state; the tool MUST NOT be invoked again
- Allowed Transitions:
  - create -> `enabled`
  - `enabled` <-> `disabled`
  - `enabled` or `disabled` -> `deleted`
  - `deleted` -> no further transitions
- Visibility:
  - an implementation MUST expose the tool identifier and lifecycle state to callers authorized to
    inspect the tool
- Invariants:
  - a `disabled` or `deleted` `tool definition` MUST NOT accept `invoke tool`
  - a `deleted` `tool definition` MUST NOT gain new successful invocations
- Commands That Create Or Change It:
  - no tool-definition lifecycle mutation command is standardized on the current `v1` public
    surface
- Events That Expose It:
  - `tool_definition.created`
  - `tool_definition.state_changed`
  - `tool_definition.deleted`
- Errors Involving It:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
- Conformance Hooks:
  - `disabled` rejects `invoke tool`
  - `deleted` is terminal

## Value Object Records

### Tool Result

- Definition: A `tool result` is the visible outcome value produced by one accepted `invoke tool`.
- Shape:
  - tool identifier
  - invocation outcome
  - optional result payload
  - optional emitted artifact identifiers
- Validation Rules:
  - every `tool result` MUST identify the source `tool definition`
  - invocation outcome MUST be one of `completed`, `failed`, or `blocked`
  - `blocked` MUST NOT include result payload
  - `blocked` MUST NOT include emitted artifact identifiers
  - emitted artifact identifiers, if present, MUST identify artifacts emitted by the invoking
    `execution` during the same accepted invocation
- Equality Or Identity Rules:
  - `tool result` has no standalone identity in `Tools v1`
- Visibility:
  - `tool result` is visible only where the invoking `execution` is visible

## Command Records

### Invoke Tool

- Actor: One visible `execution` acting through the implementation boundary.
- Target: Exactly one `tool definition`.
- Preconditions:
  - the invoking `execution` MUST exist
  - the invoking `execution` MUST be non-terminal
  - the target `tool definition` MUST exist
  - the target `tool definition` MUST be in `enabled`
  - capability checks required at the tool boundary MUST pass
  - if a visible terminal approval denial already applies to the action, the request MUST fail with
    `approval_denied`
- Inputs:
  - invoking execution identifier
  - target tool identifier
  - tool input payload
  - optional idempotency key
- Side Effects:
  - an accepted `invoke tool` MUST produce exactly one visible `tool result`
  - unresolved approval required before tool execution begins MUST yield outcome `blocked`
  - unresolved approval required before tool execution begins MUST create or attach at least one
    visible pending `approval` before the blocked result is returned
  - `blocked` MUST NOT emit visible `tool_derived_material`
  - `blocked` MUST NOT emit new `artifact`
  - visible tool-derived contribution, if exposed at the context boundary, MUST appear only as
    `tool_derived_material` as defined by `context-v1.md`
  - emitted artifacts, if any, MUST preserve `artifact-provenance`
- Resources Created Or Changed:
  - may create emitted `artifact` resources only for accepted invocations with outcome `completed`
    or `failed`
  - may create or attach `approval`
  - may change the invoking execution's visible state
- Events Emitted:
  - accepted invocation MUST emit `tool.invoked` first for that invocation
  - exactly one terminal event MUST follow:
    - `tool.completed`
    - `tool.failed`
    - `tool.blocked`
  - `approval.created`, if emitted before blocked result visibility, MUST appear after
    `tool.invoked` and before `tool.blocked`
  - `artifact.emitted`, if any, MUST appear after `tool.invoked` and before the terminal tool
    event for the same invocation
  - no terminal tool event MAY appear before `tool.invoked`
- Errors:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
  - `approval_denied`
  - `idempotency_conflict`
- Idempotency:
  - if the binding exposes an idempotency key, repeated `invoke tool` requests with the same key
    and same semantic target MUST resolve to the same visible result
  - if the same idempotency key is reused with materially different input, the implementation MUST
    reject the request with `idempotency_conflict`
- Conformance Hooks:
  - `disabled` and `deleted` tools reject `invoke tool`
  - unresolved approval requirement yields outcome `blocked`
  - blocked invocation exposes visible pending approval linkage
  - visible terminal approval denial rejects `invoke tool` with `approval_denied`
  - accepted invocation emits exactly one terminal tool event
  - successful visible tool contribution appears only as `tool_derived_material`
  - emitted artifacts preserve `artifact-provenance`
  - emitted artifacts, if any, are ordered between `tool.invoked` and the terminal tool event

## Implementation-Defined Boundaries

### Tool Driver Execution

- Boundary Name: tool driver execution
- Why The Area Is Left Implementation-Defined:
  - independent implementations may use different driver code, subprocess strategy, transport
    strategy, or provider strategy without breaking interoperability
- Fixed Externally Observable Constraints:
  - externally visible success and failure semantics MUST match `Tools v1`
  - visible tool-derived contribution MUST remain distinguishable from other context contribution
    classes
  - externally visible event order MUST match `Tools v1`
  - blocked invocation MUST NOT emit artifacts or visible tool-derived contribution
  - capability and approval constraints MUST be enforced before externally visible tool success is
    reported
- Allowed Variability:
  - subprocess execution
  - RPC transport
  - sandbox model
  - retry strategy
  - internal timeout handling
- Forbidden Assumptions For Clients Or Implementations:
  - clients MUST NOT assume a specific driver process model or transport model
  - implementations MUST NOT relabel driver-internal output as explicit caller input
- Non-Normative Implementation Guidance:
  - keep visible tool results stable across equivalent invocations
  - preserve audit linkage between tool result, emitted artifacts, and invoking execution

## Conformance Hooks

- `../conformance/v1/vectors/tool-definition-listing-includes-visible-tool.md`
- `../conformance/v1/vectors/tool-definition-inspection-exposes-state.md`
- `../conformance/v1/vectors/missing-tool-definition-inspection-returns-not-found.md`
- `../conformance/v1/vectors/invoke-tool-success.md`
- `../conformance/v1/vectors/invoke-tool-rejected-when-tool-disabled.md`
- `../conformance/v1/vectors/invoke-tool-rejected-when-tool-deleted.md`
- `../conformance/v1/vectors/invoke-tool-denied-by-capability.md`
- `../conformance/v1/vectors/invoke-tool-blocked-when-approval-required.md`
- `../conformance/v1/vectors/invoke-tool-terminal-approval-denial-returns-approval-denied.md`
- `../conformance/v1/vectors/invoke-tool-idempotent-replay-preserves-result.md`
- `../conformance/v1/vectors/tool-derived-material-visible-when-exposed.md`
- `../conformance/v1/traces/tool-invocation-with-artifact.md`
- `../conformance/v1/traces/tool-invocation-blocked-when-approval-required.md`
