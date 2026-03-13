# Conformance v1

State: Draft
Kind: Conformance Specification
Version: v1
Last Updated: 2026-03-13
Related Core Doc: `core-v1.md`
Related Context Doc: `context-v1.md`
Related Tools Doc: `tools-v1.md`
Related Coordination Doc: `coordination-v1.md`
Related Channels Doc: `channels-v1.md`
Related Binding Docs: `http-binding-v1.md`, `stream-binding-v1.md`
Draft Notice: This document does not yet authorize compliance claims.

## Scope

This document is the draft conformance specification for active semantic surfaces and their
bindings.

This document defines the evidence required before an implementation may claim compliance with any
`starla-protocol` profile.

The conformance system and artifact layout are defined in `../CONFORMANCE_SYSTEM.md` and
`../conformance/v1/`.

## Compliance Targets

`Conformance v1` defines compliance targets for:

- `Core` — `Core v1` plus `Context v1`
- `Core + Tools`
- `Core + Approvals`
- `Core + Channels`

## Required Evidence Classes

Required evidence classes:

- canonical HTTP fixtures
- canonical error fixtures
- canonical event traces
- profile-specific success cases
- implementation claims
- conformance reports

## Conditional Vectors

Conditional vector rule:

- a conditional vector becomes required when the implementation claim declares the corresponding
  optional surface
- a conditional vector becomes required when the runner observes the corresponding optional surface
  on the public binding under test

## Required Vectors

These artifacts should be stored under `../conformance/v1/`.

Seed vectors:

- `../conformance/v1/vectors/agent-definition-listing-includes-visible-definition.md`
- `../conformance/v1/vectors/agent-definition-inspection-exposes-state.md`
- `../conformance/v1/vectors/disable-agent-definition-transitions-to-disabled.md`
- `../conformance/v1/vectors/enable-agent-definition-transitions-to-enabled.md`
- `../conformance/v1/vectors/agent-instance-listing-includes-visible-instance.md`
- `../conformance/v1/vectors/agent-instance-inspection-exposes-definition-link-and-state.md`
- `../conformance/v1/vectors/pause-agent-instance-transitions-to-paused.md`
- `../conformance/v1/vectors/resume-agent-instance-transitions-to-ready.md`
- `../conformance/v1/vectors/terminate-agent-instance-transitions-to-terminated.md`
- `../conformance/v1/vectors/session-listing-includes-visible-session.md`
- `../conformance/v1/vectors/session-inspection-exposes-state.md`
- `../conformance/v1/vectors/close-session-transitions-to-closed.md`
- `../conformance/v1/vectors/submit-work-success.md`
- `../conformance/v1/vectors/execution-listing-includes-visible-execution.md`
- `../conformance/v1/vectors/cancel-execution-transitions-to-canceled.md`
- `../conformance/v1/vectors/cancel-execution-rejected-when-already-terminal.md`
- `../conformance/v1/vectors/submit-work-rejected-when-instance-paused.md`
- `../conformance/v1/vectors/submit-work-blocked-when-approval-required.md`
- `../conformance/v1/vectors/approval-inspection-exposes-state.md`
- `../conformance/v1/vectors/approval-listing-includes-visible-approval.md`
- `../conformance/v1/vectors/missing-approval-inspection-returns-not-found.md`
- `../conformance/v1/vectors/resolve-approval-approves-pending-approval.md`
- `../conformance/v1/vectors/resolve-approval-rejected-when-already-resolved.md`
- `../conformance/v1/vectors/delegate-execution-success.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-parent-missing.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-parent-terminal.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-target-instance-missing.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-target-instance-not-ready.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-target-instance-equals-parent-owner.md`
- `../conformance/v1/vectors/delegate-execution-idempotent-replay-preserves-child.md`
- `../conformance/v1/vectors/delegate-execution-terminal-approval-denial-returns-approval-denied.md`
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
- `../conformance/v1/vectors/artifact-listing-includes-visible-artifact.md`
- `../conformance/v1/vectors/artifact-record-preserves-provenance.md`
- `../conformance/v1/vectors/missing-artifact-inspection-returns-not-found.md`
- `../conformance/v1/vectors/missing-execution-inspection-returns-not-found.md`
- `../conformance/v1/vectors/failed-execution-inspection-is-not-transport-error.md`
- `../conformance/v1/vectors/execution-stream-missing-target-returns-not-found.md`
- `../conformance/v1/vectors/execution-stream-disconnect-does-not-create-terminal-outcome.md`
- `../conformance/v1/vectors/execution-stream-emits-no-later-event-after-terminal.md`
- `../conformance/v1/vectors/context-snapshot-preserves-provenance.md`
- `../conformance/v1/vectors/context-snapshot-omits-absent-contribution-sections.md`
- `../conformance/v1/vectors/inherited-lineage-material-visible-on-child-execution.md`
- `../conformance/v1/vectors/inherited-lineage-material-omitted-without-visible-lineage.md`
- `../conformance/v1/vectors/recomputed-implementation-supplied-visible-on-child-execution.md`
- `../conformance/v1/vectors/session-material-visible-on-session-attached-execution.md`
- `../conformance/v1/vectors/tool-derived-material-visible-when-exposed.md`
- `../conformance/v1/vectors/event-derived-material-visible-when-exposed.md`
- `../conformance/v1/vectors/execution-snapshot-separates-sections.md`
- `../conformance/v1/vectors/open-channel-kind-accepted.md`
- `../conformance/v1/vectors/ingress-message-preserves-routing-and-trace-fields.md`
- `../conformance/v1/vectors/delivery-request-preserves-routing-and-trace-fields.md`
- `../conformance/v1/vectors/delivery-result-reports-outcome-and-request-linkage.md`
- `../conformance/v1/vectors/status-delivery-inspection-preserves-request-linkage.md`
- `../conformance/v1/vectors/proactive-delivery-without-prior-ingress.md`
- `../conformance/v1/vectors/execution-stream-replay-resumes-after-last-event-id.md`
- `../conformance/v1/vectors/execution-stream-replay-rejected-when-replay-unsupported.md`
- `../conformance/v1/vectors/execution-stream-replay-rejected-when-last-event-id-not-retained.md`
- `../conformance/v1/vectors/status-stream-missing-target-returns-not-found.md`
- `../conformance/v1/vectors/status-stream-replay-resumes-after-last-event-id.md`
- `../conformance/v1/vectors/status-stream-replay-rejected-when-replay-unsupported.md`
- `../conformance/v1/vectors/status-stream-replay-rejected-when-last-event-id-not-retained.md`
- `../conformance/v1/vectors/status-stream-emits-no-later-status-after-final-delivery-result.md`

`context-snapshot-preserves-provenance.md` and `execution-snapshot-separates-sections.md` are
required for the `Core` target because `Context v1` is part of `Core` compliance.

`inherited-lineage-material-omitted-without-visible-lineage.md` is required for the `Core`
target.

`recomputed-implementation-supplied-visible-on-child-execution.md` is conditionally required when
the implementation exposes independently recomputed visible implementation-supplied material at a
child execution boundary.

`missing-execution-inspection-returns-not-found.md` is required for the `Core` target.

`failed-execution-inspection-is-not-transport-error.md` is required for the `Core` target.

`delegate-execution-success.md`,
`delegate-execution-rejected-when-parent-missing.md`,
`delegate-execution-rejected-when-parent-terminal.md`,
`delegate-execution-rejected-when-target-instance-missing.md`,
`delegate-execution-rejected-when-target-instance-not-ready.md`, and
`delegate-execution-rejected-when-target-instance-equals-parent-owner.md` are required for the
`Core` target.

`agent-definition-listing-includes-visible-definition.md`,
`agent-definition-inspection-exposes-state.md`,
`disable-agent-definition-transitions-to-disabled.md`,
`enable-agent-definition-transitions-to-enabled.md`,
`agent-instance-listing-includes-visible-instance.md`,
`agent-instance-inspection-exposes-definition-link-and-state.md`,
`pause-agent-instance-transitions-to-paused.md`,
`resume-agent-instance-transitions-to-ready.md`,
`terminate-agent-instance-transitions-to-terminated.md`,
`session-listing-includes-visible-session.md`,
`session-inspection-exposes-state.md`,
`close-session-transitions-to-closed.md`, and
`execution-listing-includes-visible-execution.md`,
`cancel-execution-transitions-to-canceled.md`, and
`cancel-execution-rejected-when-already-terminal.md` are conditionally required when the
implementation claims `HTTP Binding v1`.

`execution-stream-missing-target-returns-not-found.md` is conditionally required when the
implementation claims `Stream Binding v1`.

`execution-stream-disconnect-does-not-create-terminal-outcome.md` is conditionally required when
the implementation claims `Stream Binding v1`.

`execution-stream-emits-no-later-event-after-terminal.md` is conditionally required when the
implementation claims `Stream Binding v1`.

`submit-work-blocked-when-approval-required.md` and
`approval-inspection-exposes-state.md` and
`resolve-approval-approves-pending-approval.md` and
`resolve-approval-rejected-when-already-resolved.md` and
`approval-listing-includes-visible-approval.md` and
`missing-approval-inspection-returns-not-found.md` are conditionally required when the
implementation claims `Core + Approvals` or exposes approval-gated submit-work behavior or
approval inspection on the public binding.

`invoke-tool-success.md`, `invoke-tool-rejected-when-tool-disabled.md`,
`invoke-tool-rejected-when-tool-deleted.md`, and `invoke-tool-denied-by-capability.md` are
required for the `Core + Tools` target.

`delegate-execution-idempotent-replay-preserves-child.md` is conditionally required when the
implementation claims `HTTP Binding v1` and claims or exposes idempotent `delegate execution`.

`delegate-execution-terminal-approval-denial-returns-approval-denied.md` is conditionally required
when the implementation exposes visible terminal approval denial during delegation on the public
binding.

`tool-definition-listing-includes-visible-tool.md` and
`tool-definition-inspection-exposes-state.md` and
`missing-tool-definition-inspection-returns-not-found.md` are conditionally required when the
implementation claims `Core + Tools` and claims `HTTP Binding v1`, or exposes tool inspection on
the public binding.

`invoke-tool-blocked-when-approval-required.md` is conditionally required when the implementation
claims `Core + Approvals` or exposes approval-gated tool invocation on the public binding.

`invoke-tool-terminal-approval-denial-returns-approval-denied.md` is conditionally required when
the implementation exposes visible terminal approval denial during tool invocation on the public
binding.

`invoke-tool-idempotent-replay-preserves-result.md` is conditionally required when the
implementation claims `HTTP Binding v1` and claims or exposes idempotent `invoke tool`.

`artifact-record-preserves-provenance.md` is conditionally required when the implementation exposes
visible artifact emission and artifact inspection on the public binding.

`artifact-listing-includes-visible-artifact.md` is conditionally required when the implementation
claims `HTTP Binding v1` and exposes artifact inspection on the public binding.

`missing-artifact-inspection-returns-not-found.md` is conditionally required when the
implementation claims `HTTP Binding v1` and exposes artifact inspection on the public binding.

`open-channel-kind-accepted.md`, `ingress-message-preserves-routing-and-trace-fields.md`,
`delivery-request-preserves-routing-and-trace-fields.md`, and
`delivery-result-reports-outcome-and-request-linkage.md` are required for the `Core + Channels`
target.

`status-delivery-inspection-preserves-request-linkage.md` is conditionally required when the
implementation claims `HTTP Binding v1` and claims or exposes status delivery.

`proactive-delivery-without-prior-ingress.md` is conditionally required when the implementation
claims or exposes proactive delivery.

`execution-stream-replay-resumes-after-last-event-id.md` is conditionally required when the
implementation claims `Stream Binding v1` and claims or exposes execution-event replay support.

`execution-stream-replay-rejected-when-replay-unsupported.md` is conditionally required when the
implementation claims `Stream Binding v1` and does not support execution-event replay.

`execution-stream-replay-rejected-when-last-event-id-not-retained.md` is conditionally required
when the implementation claims `Stream Binding v1` and claims or exposes execution-event replay
support with retained-event replay.

`status-stream-replay-resumes-after-last-event-id.md` is conditionally required when the
implementation claims `Stream Binding v1`, claims or exposes status delivery, and claims or
exposes status-delivery replay support.

`status-stream-missing-target-returns-not-found.md` is conditionally required when the
implementation claims `Stream Binding v1` and claims or exposes status delivery.

`status-stream-replay-rejected-when-replay-unsupported.md` is conditionally required when the
implementation claims `Stream Binding v1`, claims or exposes status delivery, and does not support
status-delivery replay.

`status-stream-replay-rejected-when-last-event-id-not-retained.md` is conditionally required when
the implementation claims `Stream Binding v1`, claims or exposes status delivery, and claims or
exposes status-delivery replay support with retained-event replay.

`status-stream-emits-no-later-status-after-final-delivery-result.md` is conditionally required
when the implementation claims `Stream Binding v1` and claims or exposes status delivery.

`supervisory-child-terminal-preserves-lineage.md` is conditionally required when the implementation
exposes parent-driven supervisory child-terminal behavior on the public binding.

## Negative Paths

Required negative coverage:

- invalid request
- invalid state
- denied by capability
- denied by approval
- conflicting idempotency reuse

## Event Trace Rules

Ordered event traces MUST be judged by:

- required event presence
- required event order
- terminal event correctness
- forbidden missing or reordered events

## Conditional Traces

Conditional trace rule:

- a conditional trace becomes required when the implementation claim declares the corresponding
  optional surface
- a conditional trace becomes required when the runner observes the corresponding optional surface
  on the public binding under test

Seed traces:

- `../conformance/v1/traces/execution-completion-terminal.md`
- `../conformance/v1/traces/execution-cancel-terminal.md`
- `../conformance/v1/traces/execution-lifecycle-minimal.md`
- `../conformance/v1/traces/execution-failure-terminal.md`
- `../conformance/v1/traces/approval-gated-submit-work.md`
- `../conformance/v1/traces/approval-resolution-terminal.md`
- `../conformance/v1/traces/delegated-execution-minimal.md`
- `../conformance/v1/traces/delegated-execution-blocked-when-approval-required.md`
- `../conformance/v1/traces/delegated-blocked-child-terminal-after-supervisory-parent-stop.md`
- `../conformance/v1/traces/tool-invocation-with-artifact.md`
- `../conformance/v1/traces/tool-invocation-blocked-when-approval-required.md`
- `../conformance/v1/traces/delegated-child-terminal-after-supervisory-parent-stop.md`
- `../conformance/v1/traces/delivery-request-accepted-before-final-result.md`
- `../conformance/v1/traces/proactive-delivery-accepted-before-final-result.md`
- `../conformance/v1/traces/proactive-status-delivery-precedes-final-result.md`
- `../conformance/v1/traces/status-delivery-precedes-final-delivery-result.md`

Conditional traces:

- `../conformance/v1/traces/approval-resolution-terminal.md` becomes required when the
  implementation claims `Core + Approvals` or exposes approval resolution on the public binding
- `../conformance/v1/traces/delegated-execution-blocked-when-approval-required.md` becomes
  required when the implementation claims `Core + Approvals` or exposes approval-gated delegation
  on the public binding
- `../conformance/v1/traces/delegated-blocked-child-terminal-after-supervisory-parent-stop.md`
  becomes required when the implementation exposes parent-driven supervisory child-terminal
  behavior on the public binding and claims `Core + Approvals` or exposes approval-gated
  delegation on the public binding
- `../conformance/v1/traces/tool-invocation-blocked-when-approval-required.md` becomes required
  when the implementation claims `Core + Approvals` or exposes approval-gated tool invocation on
  the public binding
- `../conformance/v1/traces/delivery-request-accepted-before-final-result.md` becomes required
  when the implementation returns `202 Accepted` for visible delivery request submission and later
  exposes one visible final `delivery result` on the public binding
- `../conformance/v1/traces/proactive-delivery-accepted-before-final-result.md` becomes required
  when the implementation claims or exposes proactive delivery and returns `202 Accepted` for
  visible proactive delivery request submission
- `../conformance/v1/traces/proactive-status-delivery-precedes-final-result.md` becomes required
  when the implementation claims or exposes proactive delivery and claims or exposes status
  delivery
- `../conformance/v1/traces/status-delivery-precedes-final-delivery-result.md` becomes required
  when the implementation claims or exposes status delivery
- supervisory delegated-child terminal traces become required when the implementation exposes
  parent-driven supervisory child-terminal behavior on the public binding

## Reporting

An implementation report MUST declare:

- implementation name and version
- claimed `starla-protocol` version
- claimed binding versions
- claimed compliance profiles
- per-artifact pass or fail results

An implementation MUST NOT claim a profile unless every required vector, activated conditional
vector, and required trace for that profile passes.
