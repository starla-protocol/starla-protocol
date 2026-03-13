# Channels v1

State: Draft
Kind: Core Specification
Version: v1
Last Updated: 2026-03-13
Related Core Doc: `core-v1.md`
Related Coordination Doc: `coordination-v1.md`
Draft Notice: This document does not yet authorize compliance claims.

## Scope

This document defines the draft channels specification for `starla-protocol`.

`Channels v1` in this pass defines:

- channel-surface ownership
- canonical `ingress message`
- canonical `delivery request`
- canonical `delivery result`
- optional `status delivery`
- optional proactive delivery through canonical envelopes
- connector-independent routing and trace fields
- `reply target` and `thread reference` separation
- exclusions from channel law

This pass does not define:

- typing-indicator-specific semantics
- draft-update-specific semantics
- reaction-specific semantics
- per-channel policy state model
- channel-health state model
- channel bindings

## Terminology

Primary terms in this document MUST align with `../VOCABULARY.md`.

## Vocabulary

Primary `Channels v1` terms:

- `channel adapter` — addressable channel integration boundary configured against one
  `channel kind`
- `channel kind` — open identifier naming one connector family
- `ingress message` — normalized inbound channel message presented at the protocol boundary
- `delivery request` — normalized outbound channel delivery request
- `delivery result` — visible outcome of one outbound channel delivery attempt
- `status delivery` — visible non-terminal delivery status update associated with one delivery
  attempt
- `reply target` — channel-specific routing target used for direct reply delivery
- `thread reference` — channel-specific subconversation identifier independent of `reply target`
- `channel health` — externally visible health view for one `channel adapter`

## Surface Rule

- `Channels v1` defines connector-independent channel semantics.
- `Channels v1` MUST use open `channel kind` identifiers.
- `Channels v1` MUST keep `reply target` distinct from `thread reference`.
- canonical ingress and delivery envelopes MUST preserve stable routing fields.
- canonical ingress and delivery envelopes SHOULD preserve stable trace fields when those fields are
  exposed.
- `Channels v1` MAY define optional status-delivery and proactive-delivery surfaces.
- typing indicators, draft updates, and reactions, if exposed, MUST remain optional
  `status delivery` behavior rather than distinct required protocol surfaces.
- `Channels v1` MUST NOT define a closed vendor catalog.
- `Channels v1` MUST NOT define per-channel model or prompt override semantics.
- `Channels v1` MUST NOT define a plugin ABI, sandbox ABI, or component ABI.

## Ownership Boundary

`Channels v1` owns:

- external ingress normalization
- outbound delivery normalization
- `reply target` semantics
- `thread reference` semantics
- channel routing targets

`Channels v1` does not own:

- execution semantics
- context semantics
- tool semantics
- runtime plugin loading
- sandbox host contracts
- product UI channel management

Current `v1` boundary:

- `status delivery` and proactive delivery remain inside the current `v1` channel surface
- typing-indicator-specific semantics, draft-update-specific semantics, and reaction-specific
  semantics are deferred from the current `v1` target
- per-channel policy state model is deferred from the current `v1` target
- channel-health state model is deferred from the current `v1` target

## Resource Records

### Channel Adapter

- Definition: A `channel adapter` is an addressable channel integration boundary configured against
  exactly one `channel kind`.
- Identity: Every `channel adapter` MUST have a stable adapter identifier unique within the
  implementation's address space.
- Visibility:
  - adapter inspection MUST expose:
    - `channel_adapter_id`
    - `channel_kind`
  - if `channel health` is exposed, it MUST remain scoped to the same `channel adapter`
- Invariants:
  - one visible `channel adapter` MUST expose exactly one visible `channel kind`
  - visible `channel kind` MUST remain an open identifier
  - visible `channel_adapter_id` MUST remain stable for the same adapter
- Conformance Hooks:
  - adapter inspection exposes `channel_adapter_id`
  - adapter inspection exposes open `channel_kind`

## Shared Envelope Rules

- `content` MUST be a JSON object.
- `content` MUST contain `parts`.
- `parts` MUST be an ordered JSON array.
- each `parts[]` item MUST contain `kind`.
- `kind` MUST use an open identifier.
- `kind = text` MUST contain `text`.
- non-`text` parts MAY use implementation-defined fields under `data`.
- connector-specific fields MUST NOT appear at the top level of canonical channel envelopes.
- connector-specific fields MAY appear under `metadata`.

## Value Object Records

### Ingress Message

- Definition: An `ingress message` is the normalized inbound channel envelope presented at the
  protocol boundary.
- Required Members:
  - `channel_adapter_id`
  - `channel_kind`
  - `message_id`
  - `sender_id`
  - `reply_target`
  - `content`
  - `received_at`
- Optional Members:
  - `thread_reference`
  - `correlation_id`
  - `causation_id`
  - `metadata`
- Invariants:
  - `channel_adapter_id` MUST identify one visible `channel adapter`
  - `channel_kind` MUST equal the visible `channel kind` of that adapter
  - `message_id` MUST remain stable for the same visible ingress message
  - `reply_target` MUST identify the direct reply route for this ingress message
  - if `thread_reference` is absent, it MUST remain absent and MUST NOT be synthesized from
    `reply_target`
  - if `correlation_id` or `causation_id` is exposed, it SHOULD remain stable across equivalent
    re-reads of the same visible ingress message
  - top-level routing fields outside this record MUST NOT be required
- Conformance Hooks:
  - ingress message preserves adapter, kind, message, sender, and reply routing fields
  - ingress message keeps `thread_reference` distinct from `reply_target`
  - ingress message preserves exposed trace fields

### Delivery Request

- Definition: A `delivery request` is the normalized outbound channel delivery envelope presented at
  the protocol boundary.
- Required Members:
  - `delivery_request_id`
  - `channel_adapter_id`
  - `channel_kind`
  - `reply_target`
  - `content`
- Optional Members:
  - `thread_reference`
  - `in_reply_to_message_id`
  - `correlation_id`
  - `causation_id`
  - `metadata`
- Invariants:
  - `delivery_request_id` MUST identify exactly one visible delivery attempt request
  - `channel_adapter_id` MUST identify one visible `channel adapter`
  - `channel_kind` MUST equal the visible `channel kind` of that adapter
  - `reply_target` MUST identify the direct delivery route for this request
  - if `thread_reference` is absent, it MUST remain absent and MUST NOT be synthesized from
    `reply_target`
  - if `in_reply_to_message_id` is present, it MUST identify the visible message being replied to
    within the same adapter address space
  - if `correlation_id` or `causation_id` is exposed, it SHOULD remain stable through the visible
    result of the same delivery attempt
  - top-level routing fields outside this record MUST NOT be required
- Conformance Hooks:
  - delivery request preserves adapter, kind, and reply routing fields
  - delivery request keeps `thread_reference` distinct from `reply_target`
  - delivery request preserves exposed trace fields

### Delivery Result

- Definition: A `delivery result` is the visible outcome of one outbound channel delivery attempt.
- Required Members:
  - `delivery_request_id`
  - `channel_adapter_id`
  - `channel_kind`
  - `outcome`
  - `attempted_at`
- Optional Members:
  - `message_id`
  - `thread_reference`
  - `correlation_id`
  - `causation_id`
  - `error`
  - `metadata`
- Invariants:
  - `delivery_request_id` MUST identify the visible request being reported
  - `channel_adapter_id` MUST identify one visible `channel adapter`
  - `channel_kind` MUST equal the visible `channel kind` of that adapter
  - `outcome` MUST be one of `sent`, `delivered`, `best_effort`, or `failed`
  - `failed` MUST expose `error`
  - `outcome` other than `failed` MUST NOT expose `error`
  - if `message_id` is present, it MUST identify the visible outbound channel message created or
    updated by the request
  - if `thread_reference` is absent, it MUST remain absent and MUST NOT be synthesized from any
    reply-routing field
  - if `correlation_id` or `causation_id` is exposed, it SHOULD preserve the visible trace linkage
    of the corresponding delivery request
- Conformance Hooks:
  - delivery result exposes request linkage
  - delivery result exposes one visible outcome
  - delivery result preserves exposed trace fields

### Status Delivery

- Definition: A `status delivery` is a visible non-terminal delivery status update associated with
  one delivery attempt.
- Required Members:
  - `delivery_request_id`
  - `channel_adapter_id`
  - `channel_kind`
  - `status`
  - `emitted_at`
- Optional Members:
  - `thread_reference`
  - `correlation_id`
  - `causation_id`
  - `metadata`
- Invariants:
  - `delivery_request_id` MUST identify the visible request being updated
  - `channel_adapter_id` MUST identify one visible `channel adapter`
  - `channel_kind` MUST equal the visible `channel kind` of that adapter
  - `status` MUST use an open identifier
  - `status delivery` MUST remain distinct from `delivery result`
  - `status delivery` MUST NOT imply final delivery outcome
  - if `thread_reference` is absent, it MUST remain absent and MUST NOT be synthesized from any
    reply-routing field
- Conformance Hooks:
  - status delivery remains distinct from `delivery result`
  - status delivery does not imply final delivery outcome

## Optional Channel Surfaces

### Status Delivery

- if a `status delivery` surface is exposed, it MUST use canonical `status delivery`
- if a `status delivery` surface is exposed, it MUST remain distinct from `delivery result`
- `status delivery` MUST NOT imply final delivery outcome
- typing indicators, draft updates, and reactions, if exposed, MUST be treated as optional
  `status delivery` behavior rather than `delivery result`
- if `status delivery` is associated with one visible `delivery request`, it SHOULD preserve
  `delivery_request_id`
- Conformance Hooks:
  - conditional trace for `status delivery` preceding final `delivery result`

### Proactive Delivery

- if a proactive-delivery surface is exposed, it MUST use canonical `delivery request` and
  `delivery result`
- proactive delivery MUST NOT require one prior visible `ingress message`
- proactive delivery MAY omit `in_reply_to_message_id`
- proactive delivery MUST preserve routing fields defined by `Channels v1`
- Conformance Hooks:
  - conditional vector for proactive delivery without prior ingress

## Implementation-Defined Boundaries

### Connector Implementation

- Boundary Name: connector implementation
- Why The Area Is Left Implementation-Defined:
  - independent implementations may use native code, subprocesses, webhook handlers, websocket
    clients, polling loops, or sandboxed components without breaking interoperability when public
    channel semantics match
- Fixed Externally Observable Constraints:
  - visible `reply target` and `thread reference` semantics MUST match `Channels v1`
  - visible ingress and delivery semantics MUST match `Channels v1` once those surfaces are
    defined
- Allowed Variability:
  - adapter process model
  - polling versus webhook internals
  - reconnection strategy
  - plugin or sandbox implementation
- Forbidden Assumptions For Clients Or Implementations:
  - clients MUST NOT assume a specific connector runtime model
  - implementations MUST NOT collapse `reply target` and `thread reference` into one public field
    when both are exposed
- Non-Normative Implementation Guidance:
  - preserve connector-independent routing fields at the public boundary
  - treat typing indicators, draft edits, and reactions as optional capabilities

## Command Surface

- `Channels v1` defines no standalone transport-independent command record in current `v1`
- channel ingress acceptance and delivery submission are binding-owned mappings over canonical
  `ingress message` and `delivery request`

## Event Surface

- optional `status delivery` is the only event-like non-terminal channel surface in current `v1`
- `delivery result` remains distinct from `status delivery`

## Error Surface

- channel acceptance, inspection, and delivery failures use normal binding error envelopes

## Conformance Hooks

- `../conformance/v1/vectors/open-channel-kind-accepted.md`
- `../conformance/v1/vectors/ingress-message-preserves-routing-and-trace-fields.md`
- `../conformance/v1/vectors/delivery-request-preserves-routing-and-trace-fields.md`
- `../conformance/v1/vectors/delivery-result-reports-outcome-and-request-linkage.md`
- `../conformance/v1/vectors/status-delivery-inspection-preserves-request-linkage.md`
- `../conformance/v1/vectors/proactive-delivery-without-prior-ingress.md`
- `../conformance/v1/traces/delivery-request-accepted-before-final-result.md`
- `../conformance/v1/traces/proactive-delivery-accepted-before-final-result.md`
- `../conformance/v1/traces/proactive-status-delivery-precedes-final-result.md`
- `../conformance/v1/traces/status-delivery-precedes-final-delivery-result.md`
