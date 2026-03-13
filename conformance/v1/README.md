# Conformance v1 Artifacts

This directory contains versioned conformance artifacts for `Core v1` and its bindings.

## Subdirectories

- `vectors/` — canonical success and failure vectors
- `traces/` — canonical ordered event traces
- `claims/` — implementation claims
- `reports/` — conformance run reports

## Seed Artifacts

- `vectors/submit-work-success.md`
- `vectors/submit-work-rejected-when-instance-paused.md`
- `vectors/submit-work-blocked-when-approval-required.md`
- `vectors/resolve-approval-approves-pending-approval.md`
- `vectors/resolve-approval-rejected-when-already-resolved.md`
- `vectors/delegate-execution-success.md`
- `vectors/delegate-execution-rejected-when-target-instance-not-ready.md`
- `vectors/delegate-execution-rejected-when-target-instance-equals-parent-owner.md`
- `vectors/invoke-tool-success.md`
- `vectors/invoke-tool-rejected-when-tool-disabled.md`
- `vectors/invoke-tool-denied-by-capability.md`
- `vectors/invoke-tool-blocked-when-approval-required.md`
- `vectors/artifact-record-preserves-provenance.md`
- `vectors/context-snapshot-preserves-provenance.md`
- `vectors/context-snapshot-omits-absent-contribution-sections.md`
- `vectors/inherited-lineage-material-visible-on-child-execution.md`
- `vectors/session-material-visible-on-session-attached-execution.md`
- `vectors/tool-derived-material-visible-when-exposed.md`
- `vectors/event-derived-material-visible-when-exposed.md`
- `vectors/execution-snapshot-separates-sections.md`
- `traces/execution-lifecycle-minimal.md`
- `traces/approval-gated-submit-work.md`
- `traces/delegated-execution-minimal.md`
- `traces/tool-invocation-with-artifact.md`
- `claims/claim-template.md`
- `reports/report-template.md`
