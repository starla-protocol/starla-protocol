# 0001 starla-protocol Core V1

State: Draft
Last Updated: 2026-03-12
Owner: Alan
Kind: Core Law
Related Otto Product Docs: `0003-extensibility-and-automation-model.md`, `0005-stripped-down-feature-parity.md`, `0007-post-m1-api-surface.md`, `0008-kits-and-skill-boundaries.md`
Related Otto Design Docs: `0011-agent-platform-protocol-standard.md`, `0012-documentation-taxonomy-and-protocol-law-doc-set.md`

## Scope

This document is the draft home for `starla-protocol` core law.

Version 1 is intended to cover the minimum transport-independent behavior needed for a compliant
`starla-protocol` core implementation:

- agent semantics
- session semantics
- execution semantics
- approval semantics
- tool-definition semantics
- capability and approval interaction at the externally visible boundary

Out of scope for the first core-law pass:

- provider and model management
- workflows and automations
- adapters beyond the primary HTTP and streaming bindings
- marketplace or distribution mechanics

## Compliance Profiles

Draft profile shape:

- `Core` — agent, session, execution, and error semantics
- `Core + Tools` — adds tool-definition and capability behavior
- `Core + Approvals` — adds approval-gated execution behavior

Profile requirements are not final until this document is promoted beyond `Draft`.

## Terminology

Normative requirements in this document use `MUST`, `SHOULD`, and `MAY` literally.

Canonical product nouns are expected to align with the product vocabulary in
`0003-extensibility-and-automation-model.md`, but this protocol document will be authoritative for
the externally observable meaning required by compliant implementations.

## Semantic Model

The draft core semantic model is expected to define at least these nouns:

- `agent`
- `session`
- `message submission`
- `execution`
- `approval`
- `tool definition`
- `capability`

This section is not yet complete enough for compliance claims.

## State Machines / Invariants

Version 1 is expected to define:

- agent state rules
- execution state rules
- approval state rules
- derived-state rules such as when `busy` or equivalent state is externally observable
- invariants around ownership and allowed transitions

This section is not yet complete enough for compliance claims.

## Operations

Version 1 is expected to define transport-independent behavior for at least:

- creating and inspecting agents
- creating and activating sessions
- submitting a message to an agent
- creating or observing an execution
- listing and resolving approvals

This section is not yet complete enough for compliance claims.

## Event Model

Version 1 is expected to define ordered execution events, terminal conditions, and the relationship
between execution state and event emission.

This section is not yet complete enough for compliance claims.

## Error Model

Version 1 is expected to define:

- invalid request behavior
- invalid state behavior
- not found behavior
- approval and capability denial behavior

This section is not yet complete enough for compliance claims.

## Security / Policy Semantics

Version 1 is expected to define the externally visible semantics of:

- authentication expectations
- capability evaluation outcomes
- approval-required behavior
- denial and failure observability

This section is not yet complete enough for compliance claims.

## Versioning / Extensions

Version 1 is expected to define additive versus breaking change rules and how extensions or
profiles are named in compliance claims.

## Conformance Hooks

The conformance suite for this protocol law will be defined in `0004-conformance-v1.md`.
