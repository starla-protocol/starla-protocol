# Vectors

Each vector should identify:

- profile
- binding
- scenario name
- preconditions
- request sequence
- expected response or error
- expected created or changed resources
- conformance hooks exercised

Vectors should be black-box executable against a public binding.

During the current draft phase, a vector MAY be semantic-first if the binding specification has not
yet fixed exact envelope or status-code assertions. In that case, the vector should name the
binding-specific assertions that remain provisional.

A `conditional` vector becomes required when the implementation claim declares the corresponding
optional surface or when the runner observes that surface on the public binding.

Seed vectors in this directory:

- `agent-definition-listing-includes-visible-definition.md`
- `agent-definition-inspection-exposes-state.md`
- `disable-agent-definition-transitions-to-disabled.md`
- `enable-agent-definition-transitions-to-enabled.md`
- `agent-instance-listing-includes-visible-instance.md`
- `agent-instance-inspection-exposes-definition-link-and-state.md`
- `pause-agent-instance-transitions-to-paused.md`
- `resume-agent-instance-transitions-to-ready.md`
- `terminate-agent-instance-transitions-to-terminated.md`
- `session-listing-includes-visible-session.md`
- `session-inspection-exposes-state.md`
- `close-session-transitions-to-closed.md`
- `submit-work-success.md`
- `execution-listing-includes-visible-execution.md`
- `cancel-execution-transitions-to-canceled.md`
- `cancel-execution-rejected-when-already-terminal.md`
- `submit-work-rejected-when-instance-paused.md`
- `submit-work-blocked-when-approval-required.md`
- `approval-inspection-exposes-state.md`
- `approval-listing-includes-visible-approval.md`
- `missing-approval-inspection-returns-not-found.md`
- `resolve-approval-approves-pending-approval.md`
- `resolve-approval-rejected-when-already-resolved.md`
- `delegate-execution-success.md`
- `delegate-execution-rejected-when-parent-missing.md`
- `delegate-execution-rejected-when-parent-terminal.md`
- `delegate-execution-rejected-when-target-instance-missing.md`
- `delegate-execution-rejected-when-target-instance-not-ready.md`
- `delegate-execution-rejected-when-target-instance-equals-parent-owner.md`
- `delegate-execution-idempotent-replay-preserves-child.md`
- `delegate-execution-terminal-approval-denial-returns-approval-denied.md`
- `tool-definition-listing-includes-visible-tool.md`
- `tool-definition-inspection-exposes-state.md`
- `missing-tool-definition-inspection-returns-not-found.md`
- `invoke-tool-success.md`
- `invoke-tool-rejected-when-tool-disabled.md`
- `invoke-tool-rejected-when-tool-deleted.md`
- `invoke-tool-denied-by-capability.md`
- `invoke-tool-blocked-when-approval-required.md`
- `invoke-tool-terminal-approval-denial-returns-approval-denied.md`
- `invoke-tool-idempotent-replay-preserves-result.md`
- `artifact-listing-includes-visible-artifact.md`
- `artifact-record-preserves-provenance.md`
- `missing-artifact-inspection-returns-not-found.md`
- `missing-execution-inspection-returns-not-found.md`
- `failed-execution-inspection-is-not-transport-error.md`
- `execution-stream-missing-target-returns-not-found.md`
- `context-snapshot-preserves-provenance.md`
- `context-snapshot-omits-absent-contribution-sections.md`
- `inherited-lineage-material-visible-on-child-execution.md`
- `inherited-lineage-material-omitted-without-visible-lineage.md`
- `recomputed-implementation-supplied-visible-on-child-execution.md`
- `session-material-visible-on-session-attached-execution.md`
- `tool-derived-material-visible-when-exposed.md`
- `event-derived-material-visible-when-exposed.md`
- `execution-snapshot-separates-sections.md`
- `open-channel-kind-accepted.md`
- `ingress-message-preserves-routing-and-trace-fields.md`
- `delivery-request-preserves-routing-and-trace-fields.md`
- `delivery-result-reports-outcome-and-request-linkage.md`
- `status-delivery-inspection-preserves-request-linkage.md`
- `proactive-delivery-without-prior-ingress.md`
- `execution-stream-disconnect-does-not-create-terminal-outcome.md`
- `execution-stream-emits-no-later-event-after-terminal.md`
- `execution-stream-replay-resumes-after-last-event-id.md`
- `execution-stream-replay-rejected-when-replay-unsupported.md`
- `execution-stream-replay-rejected-when-last-event-id-not-retained.md`
- `status-stream-missing-target-returns-not-found.md`
- `status-stream-replay-resumes-after-last-event-id.md`
- `status-stream-replay-rejected-when-replay-unsupported.md`
- `status-stream-replay-rejected-when-last-event-id-not-retained.md`
- `status-stream-emits-no-later-status-after-final-delivery-result.md`
- `supervisory-child-terminal-preserves-lineage.md`
