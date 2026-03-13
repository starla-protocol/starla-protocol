# Working Decisions

Use this file for recurring project decisions and process rules.

Keep it short.
Move stable boundary law into `CHARTER.md`.
Move authoring method into `SPEC_METHOD.md`.

## Recurring Decisions

- `Core v1` stays minimal.
- A concern belongs in `Core v1` only if it is universal, externally observable, and
  interoperability-critical.
- `Context v1` is promoted ahead of `Tools v1`.
- `tools` are the next major action primitive after `Context v1`.
- the current `Coordination v1` pass uses delegated execution as the only internal cross-agent
  primitive
- `channels` are a first-class protocol concern, but not part of minimal `Core v1` by default.
- `Channels v1` should standardize connector-independent envelopes and management semantics, not a
  vendor adapter catalog
- connector kinds should remain extensible, not a closed protocol enum
- `Channels v1` should keep reply target separate from thread identity
- future message-like surfaces should prefer one canonical typed envelope with stable routing and
  trace fields over multiple ad hoc public shapes
- optional channel status delivery and proactive delivery are retained as `Channels v1` optional
  surfaces
- typing indicators, draft updates, and reactions should be optional channel capabilities, not base
  channel requirements
- typing-indicator-specific, draft-update-specific, and reaction-specific semantics stay outside the
  current `v1` channel law
- per-channel policy state model and channel-health state model stay outside the current `v1`
  channel law
- per-channel model or prompt overrides remain product-defined
- coordination law should use durable protocol-visible identifiers, not runtime process identity
- `hands` and device control are deferred.
- `skills` remain application-defined for now.
- current skill model: prompt packages that may use scripts or shell through the tool surface
- internal memory remains implementation-defined unless exposed as a protocol surface
- memory participates in context construction, but only externally observable results belong in
  protocol law by default
- terminal business failure and infrastructure failure should remain distinct at the protocol
  boundary
- bootstrap and provisioning lifecycle mutations stay outside the `v1` public command surface unless
  standardized explicitly
- standardize management surfaces before internal composition surfaces
- do not introduce a generic protocol-level `extension` abstraction unless two concrete surfaces
  prove the need
- `v1` scope stays frozen to `V1_TARGET.md` unless revised explicitly

## Working Sequence

- define one protocol surface at a time
- complete semantic law before broadening scope
- add binding mapping immediately after semantic law
- add conformance artifacts immediately after binding mapping
- name implementation-defined boundaries before leaving a surface

Current preferred sequence:

1. implement `FIRST_RUST_CLAIMANT_SCOPE.md`
2. prove first claim target: `Core` over `HTTP Binding v1`
3. reconsider `Recall v1`

Immediate deliverables:

1. create the first Rust claimant repo
2. implement `FIRST_RUST_CLAIMANT_SCOPE.md`
3. prove first claim target: `Core` over `HTTP Binding v1`

Working sequencing rule:

- `Workflow / Automation v1` should wait until coordination, channel, and management substrate
  decisions are stable enough to avoid back-propagating composition assumptions

## Stop Rules

- no new primary term without `VOCABULARY.md`
- no `MUST` or `MUST NOT` without a visible conformance hook
- no binding rule without a vector, trace, or clearly intended hook
- no optional surface without an activation rule
- no new abstraction until at least two concrete surfaces need it
