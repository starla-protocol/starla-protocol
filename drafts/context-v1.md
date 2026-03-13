# Context v1

State: Draft
Kind: Core Specification
Version: v1
Last Updated: 2026-03-13
Related Core Doc: `core-v1.md`
Draft Notice: This document does not yet authorize compliance claims.

## Scope

This document defines the draft context specification for `starla-protocol`.

`Context v1` defines:

- context construction inputs
- context contribution classes
- context scope classes
- inheritance rules
- visibility rules
- exclusion rules
- exported context views
- implementation-defined memory participation boundary

This pass does not define caller-controlled exclusion operations on the current `v1` public
surface.

## Terminology

Primary terms in this document MUST align with `../VOCABULARY.md`.

## Vocabulary

Primary `Context v1` terms:

- `context` — externally visible context available to one `execution`
- `context contribution` — one visible contribution to `context` with exactly one provenance class
- `context snapshot` — canonical exported view of visible `context`
- `execution snapshot` — canonical exported view of `execution` state plus visible context and
  adjacent exposed sections

## Context Construction

Visible context for one `execution` MUST be constructed from zero or more `context` contributions.

Each visible contribution MUST have exactly one provenance class.

Visible contribution classes:

- explicit caller input
- explicit caller references
- session-scoped material
- inherited lineage material
- tool-derived material
- event-derived material
- implementation-supplied material

Core rules:

- visible non-caller contribution MUST NOT be relabeled as explicit caller input
- visible `reference` material MUST remain distinguishable from direct input material
- omitted contribution classes MUST be omitted rather than silently relabeled

## Value Object Records

### Context Contribution

- Definition: A `context contribution` is one visible input to `context` with exactly one
  provenance class.
- Shape:
  - provenance class
  - contributed material
  - optional source identifier visible at the protocol boundary
- Validation Rules:
  - one contribution MUST have exactly one provenance class
  - contributed `reference` material MUST remain distinguishable from direct input material
  - implementation-supplied contribution MUST NOT be relabeled as explicit caller input
- Equality Or Identity Rules:
  - `context contribution` has no standalone identity in `Context v1`
- Visibility:
  - only visible contribution belongs in exported context views

### Context

- Definition: `context` is the externally visible collection of `context` contributions made
  available to one `execution`.
- Shape:
  - zero or more `context contributions`
- Validation Rules:
  - explicit caller input MUST remain distinguishable from implementation-supplied contribution
  - explicit caller references MUST remain distinguishable from direct input material
  - if session-scoped material is included, the source `session` MUST be visible to the caller and
    to the target execution boundary
- Equality Or Identity Rules:
  - `context` has no standalone identity in `Context v1`
  - equality of `context` is not a protocol requirement in `Context v1`
- Visibility:
  - an implementation MUST expose enough information for a caller to distinguish visible
    contribution classes at the protocol boundary
  - hidden internal assembly MAY remain unexposed
- Invariants:
  - explicit caller payload supplied by `submit work` MUST become part of the execution's visible
    `context`
  - explicit caller references MUST be preserved as references
  - session-scoped material MUST NOT be exposed if the associated `session` is not visible to the
    caller
  - implementation-supplied contribution MUST NOT bypass visibility, capability, or approval
    constraints
- Conformance Hooks:
  - explicit payload is visible as caller input
  - explicit references remain references
  - hidden implementation-supplied material is never misrepresented as caller input
  - closed or deleted sessions do not retroactively rewrite existing execution context

## Context Scope Classes

`Context v1` defines these scope classes:

- agent definition scope
- agent instance scope
- session scope
- execution scope
- lineage scope

## Scope Matrix

| Scope class | Direct visible contribution classes | Visibility rule |
| --- | --- | --- |
| agent definition scope | none required in `Context v1` | no direct visible contribution by default |
| agent instance scope | `implementation-supplied material` | visible only at executions owned by that `agent instance` |
| session scope | `session-scoped material` | visible only at executions attached to that `session` |
| execution scope | `explicit caller input`, `explicit caller references`, `tool-derived material`, `event-derived material`, `implementation-supplied material` | visible only at the target `execution` unless another visible rule reintroduces the material |
| lineage scope | `inherited lineage material` | visible only where a visible `execution-lineage` relation exists |

## Agent Definition And Agent Instance Scope Rules

Draft rules:

- `agent definition scope` contributes no required visible class in `Context v1`
- if definition-scoped material becomes visible at the context boundary, it MUST appear as
  `implementation-supplied material`
- visible definition-scoped material MUST NOT be relabeled as `explicit_input`,
  `session_material`, or `inherited_lineage_material`
- `agent instance scope` MAY contribute visible `implementation-supplied material`
- visible instance-scoped material MUST appear only on executions owned by that `agent instance`
- visible instance-scoped material MUST NOT automatically appear on executions owned by another
  `agent instance`, even when both instances derive from the same `agent definition`
- if visible instance-scoped material reaches a child execution owned by another `agent instance`,
  it MUST appear as `inherited_lineage_material` or as newly recomputed `implementation-supplied`
  material at the child boundary

## Inheritance

Draft inheritance rules:

- session-scoped material MAY contribute only to work attached to that `session`
- lineage material MAY contribute only where a visible parent-child execution relation exists
- tool-derived and event-derived material originate at execution scope unless another protocol
  surface defines a wider visible scope

## Lineage Inheritance Rules

Draft rules:

- carried-forward parent material MUST appear only as `inherited_lineage_material` at the child
  boundary
- a child `execution` MUST NOT expose `inherited_lineage_material` unless a visible
  `execution-lineage` relation exists
- visible parent `explicit_input` MUST NOT remain `explicit_input` at the child boundary
- visible parent `explicit_references` MUST NOT remain `explicit_references` at the child boundary
- visible parent `tool-derived material` MUST NOT remain `tool_derived_material` at the child
  boundary
- visible parent `event-derived material` MUST NOT remain `event_derived_material` at the child
  boundary
- visible parent `implementation-supplied material` MUST NOT remain `implementation_supplied` at
  the child boundary unless it is independently recomputed there
- independently recomputed implementation-supplied material exposed at the child boundary MUST
  appear only as `implementation_supplied`
- independently recomputed implementation-supplied material exposed at the child boundary MUST
  remain distinguishable from any visible `inherited_lineage_material`
- shared session visibility MUST remain `session_material`, not `inherited_lineage_material`, when
  the visible basis is `session-membership`
- `Context v1` defines representation of visible lineage-carried material
- `Coordination v1` defines creation and persistence of the corresponding visible
  `execution-lineage` relation

## Inheritance Matrix

| Source class at origin execution | Origin execution | Child execution | Same-session unrelated execution | Rule |
| --- | --- | --- | --- | --- |
| explicit caller input | visible as `explicit caller input` | MUST NOT copy by default; if carried forward, it MUST appear as `inherited lineage material` | MUST NOT appear unless separately represented as `session-scoped material` | direct caller input is not automatically reclassified across executions |
| explicit caller references | visible as `explicit caller references` | MUST NOT copy by default; if carried forward, they MUST appear as `inherited lineage material` or explicit `reference` input at the child boundary | MUST NOT appear unless separately represented as `session-scoped material` | direct caller references are not automatically session-visible |
| session-scoped material | visible when the execution is attached to the source `session` | visible only if the child execution is attached to the same visible `session` | visible only if the execution is attached to the same visible `session` | session visibility follows `session-membership`, not lineage |
| inherited lineage material | not applicable | visible only where a visible parent-child relation exists | MUST NOT appear | lineage material is lineage-scoped only |
| tool-derived material | visible at the origin execution if exposed | MUST NOT copy by default; if carried forward, it MUST appear as `inherited lineage material` or `session-scoped material` | MUST NOT appear unless separately represented as `session-scoped material` | origin execution provenance does not survive unchanged across execution boundaries |
| event-derived material | visible at the origin execution if exposed | MUST NOT copy by default; if carried forward, it MUST appear as `inherited lineage material` or `session-scoped material` | MUST NOT appear unless separately represented as `session-scoped material` | origin execution provenance does not survive unchanged across execution boundaries |
| implementation-supplied material | visible at the origin execution only if exposed | MUST NOT copy by default; if lineage-carried it MUST appear as `inherited lineage material`; if independently recomputed it MAY appear again as `implementation-supplied material` | MUST NOT appear unless independently recomputed or separately represented as `session-scoped material` | implementation recomputation is distinct from visible inheritance |

## Visibility And Exclusion

Draft visibility and exclusion rules:

- a caller MUST inspect only context visible at the target execution boundary
- hidden implementation assembly MAY remain unexposed
- excluded material MUST NOT appear in exported context views
- hidden material MUST NOT be represented as explicit caller input

## Visibility And Exclusion Matrix

| Condition | Required effect |
| --- | --- |
| caller lacks inspection authority for the target `execution` | access to exported context views MUST be denied |
| explicit caller input was accepted by `submit work` | it MUST appear only in `explicit_input` |
| explicit caller references were accepted by `submit work` | they MUST appear only in `explicit_references` |
| contribution class is absent at the target boundary | the corresponding exported section MUST be omitted |
| source `session` is not visible at the target boundary | `session-scoped material` MUST be omitted |
| no visible parent-child relation exists for the target boundary | `inherited_lineage_material` MUST be omitted |
| tool-derived material is not exposed at the target boundary | `tool_derived_material` MUST be omitted |
| event-derived material is not exposed at the target boundary | `event_derived_material` MUST be omitted |
| implementation-supplied material is kept internal | `implementation_supplied` MUST be omitted |
| visible material is excluded at the target boundary | it MUST be omitted and MUST NOT be relabeled as another contribution class |

## Exported Views

`Context v1` uses these exported views:

- `context snapshot`
- `execution snapshot`

`context snapshot` is the authoritative exported view of visible context for one `execution`.

`execution snapshot` MUST preserve `context snapshot` as a distinct nested section.

## Command Surface

- `Context v1` defines no standalone transport-independent command in current `v1`

## Event Surface

- `Context v1` defines no standalone event in current `v1`

## Error Surface

- context-view inspection failures use `Core v1` visibility law and binding error mapping

## Derived View Records

### Context Snapshot

- Definition: A `context snapshot` is the canonical exported derived view of visible `context`
  associated with exactly one `execution`.
- Source State:
  - execution identifier
  - owning agent instance identifier
  - optional session identifier
  - visible `context contributions`
- Derivation Rule:
  - any protocol surface that exports execution context MUST preserve visible provenance classes as
    distinct sections
  - explicit caller input MUST NOT be merged into implementation-supplied contribution
  - explicit caller references MUST NOT be flattened into direct input material
  - session-scoped material MUST remain distinguishable from direct caller input
- implementation-supplied material MAY be omitted if the binding does not expose it, but if it is
  exposed it MUST be identified as implementation-supplied
- independently recomputed implementation-supplied material at a child boundary MUST remain in
  `implementation_supplied` rather than `inherited_lineage_material`
- Visibility:
  - a `context snapshot` MUST be visible only to callers authorized to inspect the target
    execution's visible context
  - hidden internal assembly details MAY remain unexposed
- Canonical Shape:
  - execution identifier
  - owning agent instance identifier
  - optional session identifier
  - `explicit_input`
  - `explicit_references`
  - optional `session_material`
  - optional `inherited_lineage_material`
  - optional `tool_derived_material`
  - optional `event_derived_material`
  - optional `implementation_supplied`
- Conformance Hooks:
  - exported context preserves provenance buckets
  - explicit caller references remain distinct from payload
  - implementation-supplied material is never labeled as caller input

### Execution Snapshot

- Definition: An `execution snapshot` is the canonical exported derived view of one `execution` and
  its immediately relevant observable surroundings.
- Source State:
  - execution identity and lifecycle state
  - parent execution identifier, if any
  - owning agent instance identifier
  - optional session identifier
  - `context snapshot`
  - associated approvals, if any
  - available tool descriptors, if exposed at the execution boundary
  - emitted artifacts, if any
  - recent execution events, if exposed through the snapshot
- Derivation Rule:
  - any protocol surface that exports an execution introspection view broader than pure context MUST
    use the `execution snapshot` shape
  - `context snapshot` MUST remain a nested, distinguishable section
  - event material, tool availability, approvals, and artifacts MUST NOT be collapsed into context
  - omitted optional sections MUST be omitted explicitly rather than silently relabeled
- Visibility:
  - an `execution snapshot` MUST be visible only to callers authorized to inspect the target
    execution
- Canonical Shape:
  - execution identifier
  - current lifecycle state
  - owning agent instance identifier
  - optional parent execution identifier
  - optional session identifier
  - `context snapshot`
  - optional approvals section
  - optional available tools section
  - optional artifacts section
  - optional recent events section
- Conformance Hooks:
  - exported execution snapshots preserve separation between context, tools, approvals, artifacts,
    and events
  - lifecycle state matches the underlying execution
  - parent execution linkage, if present, matches `execution-lineage`

## Memory Participation Boundary

Internal memory may participate in context construction.

Only externally observable results of that participation belong in protocol law by default.

`Context v1` defines:

- how visible memory-derived contribution appears at the context boundary
- what provenance rules apply to that contribution
- what visibility and exclusion rules apply to that contribution

`Context v1` should not define:

- storage engines
- retrieval ranking
- summarization internals
- prompt assembly

## Implementation-Defined Boundaries

### Internal Memory And Context Assembly

- Boundary Name: internal memory and context assembly
- Why The Area Is Left Implementation-Defined:
  - internal memory may participate in context construction without requiring a shared internal
    strategy
  - implementations may use different storage, retrieval, ranking, summarization, or prompt
    assembly techniques without breaking interoperability
- Fixed Externally Observable Constraints:
  - only externally observable results of implementation-defined memory participation belong to
    protocol law by default
  - explicit payload supplied through `submit work` MUST remain part of the execution's visible
    `context`
  - explicit `reference` inputs MUST be preserved as explicit references and MUST NOT be rewritten
    as if they were user-supplied payload
  - implementations MUST enforce visibility and capability constraints before implementation-
    defined recall material influences execution behavior
  - if an implementation exposes implementation-defined recalled material at the protocol boundary,
    it MUST identify that material as implementation-supplied rather than caller-supplied
- Allowed Variability:
  - storage model
  - indexing strategy
  - retrieval ranking
  - summarization strategy
  - prompt assembly
  - context-window budgeting
- Forbidden Assumptions For Clients Or Implementations:
  - clients MUST NOT assume a specific retrieval algorithm, ranking function, prompt structure, or
    internal memory object model
  - implementations MUST NOT treat hidden internal recall as though it were explicit caller input
  - implementations MUST NOT bypass visibility, capability, or approval constraints through
    implementation-defined recall
- Non-Normative Implementation Guidance:
  - preserve an audit distinction between explicit caller input, explicit references, and
    implementation-supplied recall
  - apply visibility and capability filtering before retrieval results are assembled into context
  - keep context budgeting deterministic enough that repeated executions with the same explicit
    inputs do not produce arbitrarily unstable visible behavior

## Conformance Hooks

`Context v1` requires at least:

- vectors for preserved provenance classes
- vectors for hidden or excluded contribution classes
- vectors for visible inherited contribution
- vectors for visible implementation-supplied contribution
