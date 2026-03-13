# Charter

## Purpose

`starla-protocol` exists to define a strict, implementation-independent protocol for multi-agent
harness behavior.

The protocol should be modular. Major protocol surfaces should be specified independently when they
have distinct nouns, commands, events, errors, or conformance claims.

The protocol should also be as concrete and deterministic as possible. When implementation internals
are intentionally left open, those boundaries should be named explicitly and bounded clearly.

## Primary Goals

- define strict cross-agent communication and delegation semantics
- define strict external channel ingress, delivery, routing, and policy semantics where independent
  implementations must interoperate
- define strict context scope, inheritance, and visibility semantics
- define strict execution, approval, artifact, and reference semantics
- define strict extension-management semantics where higher-order protocol objects must be created,
  attached, versioned, governed, or inspected across implementations
- define externally visible tool semantics where independent implementations must interoperate
- allow externally visible recall or memory semantics to be standardized as a separate protocol
  surface when needed
- keep the protocol transport-independent at the semantic layer and bind it cleanly to HTTP and
  streaming transports

## Modular Surfaces

The protocol is expected to decompose into surfaces such as:

- `Core v1` — agent definitions, agent instances, sessions, executions, approvals, artifacts,
  references, identity, lifecycle, errors, and core events
- `Coordination v1` — cross-agent communication, delegation, lineage, routing, and supervision
- `Context v1` — context scope, inheritance, visibility, attachment, and exclusion semantics
- `Tools v1` — tool definitions, invocation, result semantics, and policy gating, if standardized
- `Channels v1` — external ingress, outbound delivery, channel routing, per-channel policy, and
  adapter health, if standardized
- `Skill Management v1` — skill definitions, versioning, attachment, enablement, and governance, if
  standardized
- `Recall v1` — externally visible memory or recall semantics, if standardized
- bindings — transport mappings such as HTTP and streaming
- conformance — evidence and reporting rules for claims against the specification

These names are directional until the corresponding specifications exist.

## Substrate Definition

The protocol substrate is the minimum universal semantic layer that all compliant implementations
MUST share before optional surfaces are added.

The substrate is:

- mandatory
- transport-independent
- implementation-independent
- universal across compliant implementations

The substrate should contain only the nouns, commands, relations, invariants, errors, and event
rules required for the rest of the protocol to make sense.

The substrate is not:

- the full product surface
- the full connector catalog
- the packaging model
- the implementation architecture

## Context Boundary

`Context v1` is a promoted protocol surface.

It should be developed before `Tools v1` because tool results, event material, session material,
and implementation-supplied memory contribution all feed visible context.

`Context v1` should define:

- context contribution classes
- context scope classes
- inheritance rules
- visibility and exclusion rules
- exported context views
- the visible boundary for memory participation in context construction

`Context v1` should not define:

- storage engines
- retrieval ranking
- summarization internals
- prompt assembly

## Coordination Boundary

`Coordination v1` should begin with explicit delegated execution and lineage.

It should not define a generic inter-agent message surface until independent implementations need
that surface to interoperate.

Product-specific message buses, mailboxes, or relay mechanisms should remain outside protocol law
until a dedicated coordination surface requires them.

If a generic inter-agent message surface is later standardized, it should prefer one canonical
typed message envelope with stable routing and trace fields rather than multiple ad hoc message
shapes.

Coordination law should use durable protocol-visible identifiers.

It should not depend on runtime-local process identity.

## Core Boundary

`Core v1` should define what all compliant implementations must share at the semantic boundary.

A concern belongs in `Core v1` only if all of these are true:

- it is required for a minimal compliant multi-agent runtime
- it is externally observable
- interoperability breaks if independent implementations model it differently
- it affects identity, lifecycle, visibility, security, event ordering, or error semantics

If a concern does not satisfy that test, it should remain outside `Core v1`.

When `Core v1` leaves an area implementation-defined, it should still define:

- fixed externally observable behavior
- allowed implementation variability
- any non-normative guidance that would help independent implementors succeed

It should not define:

- internal memory storage
- retrieval ranking
- summarization strategy
- prompt assembly
- scheduler internals
- queue internals
- placement and scaling strategy

`Core v1` may leave bootstrap and provisioning mutations outside the public command surface when the
resource semantics remain interoperable without standardizing those commands in `v1`.

Core law should distinguish terminal business outcome from infrastructure failure.

Terminal failure of a visible protocol resource should not be collapsed into transport, process, or
host-runtime error.

## Extension Boundary

An extension surface should be standardized when a concern is not core but still requires shared
external management or interoperability.

An extension surface may define:

- creation and deletion
- identity and versioning
- attachment points
- enablement and disablement
- capability and approval requirements
- inspection and health views
- externally visible failure semantics

An extension surface should not define internal execution strategy unless interoperability requires
it.

The protocol should standardize management surfaces before standardizing internal composition
surfaces.

Some extension surfaces may be practically foundational to real products even when they do not
belong in the smallest possible substrate.

That does not make them part of `Core v1`.

It means they should be treated as early high-priority protocol surfaces.

## Channel Boundary

`channels` are a first-class protocol concern.

They are not part of the smallest possible `Core v1` by default.

They should become a dedicated protocol surface when independent implementations must interoperate
over:

- canonical ingress message envelopes
- external ingress envelopes
- canonical outbound delivery requests and delivery results
- outbound delivery envelopes
- reply-target semantics distinct from thread semantics
- status-update delivery, if exposed
- proactive outbound delivery, if exposed
- channel routing
- per-channel policy
- rate-limit or approval-visible denial behavior
- adapter health and inspection

A channel surface should prefer connector-independent envelopes and open connector kinds over a
closed vendor catalog.

A channel surface should prefer one canonical ingress and delivery envelope shape with stable
routing and trace fields over connector-specific public shapes.

A channel surface should not define:

- every vendor-specific adapter setting
- a plugin ABI
- a sandbox contract
- per-channel model or prompt overrides
- marketplace or catalog breadth
- product-specific UI behavior
- transport implementation internals unless interoperability requires them

## Coverage Rule

Every planned protocol surface should map to at least one downstream product capability family that
would otherwise remain underspecified or non-interoperable.

A surface should not exist only because it is architecturally tidy.

If a planned surface does not protect a real downstream capability, it should be deferred or
removed.

## Composition Deferral Rule

Composition surfaces should not be standardized before the substrate surfaces they compose are
stable enough to prevent back-propagating hidden assumptions.

This applies especially to:

- workflows
- automations
- higher-order package activation flows

Composition law should follow stable law for:

- execution
- coordination
- context
- channels, where relevant
- management surfaces, where relevant

## Application Boundary

Application-layer concepts may remain outside protocol law even when they are operationally
important.

A concern should stay application-defined when:

- clients do not need cross-implementation interoperability for it
- the concern is packaging, UX, prompting, or internal composition
- independent implementations may differ without breaking protocol compatibility

Application-layer concepts may still map onto protocol resources or extension surfaces.

## Skill Boundary

`skills` should remain outside `Core v1`.

If `skills` are standardized, the protocol should first standardize skill management rather than
skill internals.

A skill-management surface may define:

- skill definition identity
- versioning and compatibility
- attachment to agent definitions or agent instances
- enablement, disablement, deprecation, and deletion
- declared capability requirements
- declared tool dependencies
- visibility and inspection

A skill-management surface should not define:

- prompt internals
- internal planning strategy
- internal execution graphs
- implementation-specific optimization

## Tool Boundary

`tools` are not part of the smallest possible `Core v1`, but they are a primary protocol primitive.

`Tools v1` should follow `Context v1`.

If `tools` are standardized, the protocol should define:

- tool definition identity
- invocation semantics
- input and result shape
- failure semantics
- capability and approval requirements
- event and artifact semantics, if exposed

The protocol should not define tool-driver internals or provider-specific execution machinery unless
interoperability requires it.

## Memory Boundary

Internal memory remains implementation-defined by default.

Memory may participate in context construction.

Only the externally observable results of that participation belong in protocol law by default.

If recall or memory becomes a protocol surface, the protocol should define only externally visible
semantics such as:

- addressable memory objects, if any
- visibility and scope
- read, write, or search behavior at the API boundary
- retention or deletion behavior, if exposed

It should not define storage engines, ranking algorithms, embeddings, or prompt composition.

The protocol may still include non-normative guidance on successful recall designs if that guidance
is clearly marked as implementation advice rather than law.

## Deferred Device-Control Boundary

`hands` and device control are deferred.

They are not part of the active protocol surface set.

They should remain application-defined unless later interoperability work proves that a dedicated
protocol surface is necessary.
