# Coordination v1

State: Draft
Kind: Core Specification
Version: v1
Last Updated: 2026-03-13
Related Core Doc: `core-v1.md`
Related Context Doc: `context-v1.md`
Draft Notice: This document does not yet authorize compliance claims.

## Scope

This document defines the draft coordination specification for `starla-protocol`.

`Coordination v1` in this pass defines:

- delegated child-execution creation
- parent-child lineage relation semantics
- delegated target addressing
- delegated session carry-forward
- cross-agent coordination only through explicit delegated execution

This pass does not define:

- direct agent-to-agent message surfaces
- generic inter-agent message resources
- generic inter-agent message buses
- multi-recipient routing
- supervision policy
- escalation policy

## Terminology

Primary terms in this document MUST align with `../VOCABULARY.md`.

## Vocabulary

Primary `Coordination v1` terms:

- `delegate execution` — request that one visible `execution` create one child `execution` under
  one target `agent instance`
- `execution-lineage` — parent-child relation between one delegating `execution` and one delegated
  child `execution`

## Surface Rule

- this pass defines cross-agent coordination through `delegate execution` and
  `execution-lineage`
- this pass does not define a generic inter-agent message surface
- any future generic inter-agent message surface SHOULD use durable protocol-visible identifiers
  rather than runtime-local process identity
- implementations MAY expose product-specific message surfaces outside `Coordination v1`
- those product-specific message surfaces are outside `Coordination v1` compliance claims

## Relation Records

### Execution-Lineage

- Endpoints:
  - exactly one parent `execution`
  - exactly one child `execution`
- Ownership Or Scope:
  - the relation is scoped to the child `execution`
- Visibility:
  - the relation MUST expose the parent execution identifier wherever the child execution exposes
    visible inherited lineage material
  - the relation MUST remain visible while the child execution remains visible
- Invariants:
  - one child `execution` MUST have at most one parent `execution`
  - parent and child execution identifiers MUST differ
  - the relation MUST be immutable after creation
  - the relation MUST be created only by successful `delegate execution`
  - visible `inherited_lineage_material` MUST NOT exist without visible `execution-lineage`
- Conformance Hooks:
  - delegated child execution has exactly one visible parent execution identifier
  - relation is immutable
  - inherited lineage material requires visible lineage

## Command Records

### Delegate Execution

- Actor: One visible non-terminal parent `execution` acting through the implementation boundary.
- Target:
  - exactly one parent `execution`
  - exactly one target `agent instance`
- Preconditions:
  - the parent `execution` MUST exist
  - the parent `execution` MUST be non-terminal
  - the target `agent instance` MUST exist
  - the target `agent instance` MUST be in `ready`
  - the target `agent instance` MUST differ from the parent execution's owning `agent instance`
  - capability checks required at the parent or target boundary MUST pass
  - if a visible terminal approval denial already applies to the delegation action, the request
    MUST fail with `approval_denied`
- Inputs:
  - parent execution identifier
  - target agent instance identifier
  - delegated work payload
  - optional delegated references
  - optional idempotency key
- Side Effects:
  - a successful `delegate execution` MUST create exactly one child `execution` unless it resolves
    through a prior idempotent result
  - the child `execution` MUST initially enter `pending`
  - the child `execution` MUST belong to the explicitly requested target `agent instance`
  - the child `execution` MUST gain exactly one `execution-lineage` relation to the parent
    `execution`
  - delegated work payload MUST become the child execution's visible `explicit_input`
  - delegated references MUST remain visible `explicit_references` at the child boundary
  - carried-forward parent material, if visible at the child boundary, MUST appear only as
    `inherited_lineage_material` as defined by `context-v1.md`
  - if the parent execution has visible `session-membership`, the child execution MUST attach to
    the same visible `session`
  - if approval is required before child progress may continue, the child execution MUST enter
    `blocked` before `delegate execution` completes and visible pending approval MUST exist
- Resources Created Or Changed:
  - creates one child `execution`
  - creates one `execution-lineage` relation
  - may create one or more `approval`
- Events Emitted:
  - child `execution.created` MUST be emitted if a new child execution is created
  - `execution.delegated` MUST be emitted after child `execution.created`
  - `execution.delegated` MUST appear before any `execution.blocked`, `execution.completed`,
    `execution.failed`, or `execution.canceled` event for the child execution
  - `approval.created`, if emitted before delegated command completion, MUST appear after child
    `execution.created` and before child `execution.blocked`
- Errors:
  - `not_found`
  - `invalid_state`
  - `capability_denied`
  - `approval_denied`
  - `idempotency_conflict`
- Idempotency:
  - if the binding exposes an idempotency key, repeated `delegate execution` requests with the same
    key and same semantic target MUST resolve to the same visible child execution result
  - if the same idempotency key is reused with materially different input, the implementation MUST
    reject the request with `idempotency_conflict`
- Conformance Hooks:
  - successful delegation creates one child execution and one visible lineage relation
  - successful delegation preserves the explicit target `agent instance`
  - delegated child parent execution identifier is visible
  - delegated child attached to a visible parent session remains attached to that session
  - missing parent rejects `delegate execution` with `not_found`
  - missing target rejects `delegate execution` with `not_found`
  - terminal parent rejects `delegate execution`
  - target `agent instance` equal to the parent owning `agent instance` rejects `delegate
    execution`
  - visible terminal approval denial rejects `delegate execution` with `approval_denied`
  - idempotent replay preserves the same visible child execution result
  - `execution.delegated` follows child `execution.created`

## Error Selection

- missing or non-visible parent `execution` MUST yield `not_found`
- missing or non-visible target `agent instance` MUST yield `not_found`
- visible terminal parent `execution` MUST yield `invalid_state`
- visible target `agent instance` not in `ready` MUST yield `invalid_state`
- visible target `agent instance` equal to the parent owning `agent instance` MUST yield
  `invalid_state`
- visible target denied by capability policy after target resolution MUST yield `capability_denied`
- visible terminal approval denial for the delegation action after target resolution MUST yield
  `approval_denied`

## Implementation-Defined Boundaries

### Delegation Routing

- Boundary Name: delegation routing
- Why The Area Is Left Implementation-Defined:
  - independent implementations may use different target-selection or scheduling strategies without
    breaking interoperability when the public target is explicit
- Fixed Externally Observable Constraints:
  - externally visible parent and child identifiers MUST match `Coordination v1`
  - successful delegation MUST NOT reroute to a different visible `agent instance` than the
    explicit public target
  - lineage creation and visibility MUST match `Coordination v1`
  - visible delegated context contribution classes MUST match `context-v1.md`
- Allowed Variability:
  - internal scheduler choice
  - queue choice
  - placement strategy
  - retry strategy before public command completion
- Forbidden Assumptions For Clients Or Implementations:
  - clients MUST NOT assume a specific scheduler or queue model
  - implementations MUST NOT relabel carried-forward parent material as child caller input
- Non-Normative Implementation Guidance:
  - keep delegation target resolution explicit at the public boundary
  - preserve stable lineage inspection across equivalent retries

### Supervision Boundary

- Boundary Name: supervision boundary
- Why The Area Is Left Implementation-Defined:
  - independent implementations may use different parent-child cancellation, retry, or restart
    strategies without breaking interoperability when visible execution law remains stable
- Fixed Externally Observable Constraints:
  - supervisory action MUST NOT rewrite child `execution` identity, ownership, visible
    `session-membership`, or `execution-lineage`
  - if supervisory action causes a visible child terminal transition, that transition MUST use the
    normal child `execution` lifecycle and event surface
- Allowed Variability:
  - parent-driven child cancellation policy
  - child retry policy before terminal visibility
  - supervisor restart strategy
- Forbidden Assumptions For Clients Or Implementations:
  - clients MUST NOT assume parent terminal transition always cancels or fails the child
  - implementations MUST NOT treat supervisor restart mechanics as a visible success outcome
- Non-Normative Implementation Guidance:
  - expose supervisory consequences through normal child `execution` state and event inspection
  - keep lineage stable across supervisory retries that do not create a new visible child

## Conformance Hooks

- `../conformance/v1/vectors/delegate-execution-success.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-parent-missing.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-parent-terminal.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-target-instance-missing.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-target-instance-not-ready.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-target-instance-equals-parent-owner.md`
- `../conformance/v1/vectors/delegate-execution-idempotent-replay-preserves-child.md`
- `../conformance/v1/vectors/delegate-execution-terminal-approval-denial-returns-approval-denied.md`
- `../conformance/v1/vectors/supervisory-child-terminal-preserves-lineage.md`
- `../conformance/v1/traces/delegated-execution-minimal.md`
- `../conformance/v1/traces/delegated-execution-blocked-when-approval-required.md`
- `../conformance/v1/traces/delegated-blocked-child-terminal-after-supervisory-parent-stop.md`
- `../conformance/v1/traces/delegated-child-terminal-after-supervisory-parent-stop.md`
