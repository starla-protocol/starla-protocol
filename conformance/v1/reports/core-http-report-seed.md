# Core HTTP Report Seed

Implementation Claim: `conformance/v1/claims/core-http-claim-seed.md`
Runner Identity:
Run Date:

## Vectors Executed

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
- `delegate-execution-success.md`
- `delegate-execution-rejected-when-parent-missing.md`
- `delegate-execution-rejected-when-parent-terminal.md`
- `delegate-execution-rejected-when-target-instance-missing.md`
- `delegate-execution-rejected-when-target-instance-not-ready.md`
- `delegate-execution-rejected-when-target-instance-equals-parent-owner.md`
- `missing-execution-inspection-returns-not-found.md`
- `failed-execution-inspection-is-not-transport-error.md`
- `context-snapshot-preserves-provenance.md`
- `context-snapshot-omits-absent-contribution-sections.md`
- `inherited-lineage-material-visible-on-child-execution.md`
- `inherited-lineage-material-omitted-without-visible-lineage.md`
- `session-material-visible-on-session-attached-execution.md`
- `execution-snapshot-separates-sections.md`

## Traces Executed

- `execution-completion-terminal.md`
- `execution-cancel-terminal.md`
- `execution-lifecycle-minimal.md`
- `execution-failure-terminal.md`
- `delegated-execution-minimal.md`

## Not Executed By This Seed

- `submit-work-blocked-when-approval-required.md`
- `approval-inspection-exposes-state.md`
- `approval-listing-includes-visible-approval.md`
- `missing-approval-inspection-returns-not-found.md`
- `resolve-approval-approves-pending-approval.md`
- `resolve-approval-rejected-when-already-resolved.md`
- `delegate-execution-idempotent-replay-preserves-child.md`
- `delegate-execution-terminal-approval-denial-returns-approval-denied.md`
- `recomputed-implementation-supplied-visible-on-child-execution.md`
- supervisory delegated-child terminal vectors and traces
- all tool vectors and traces
- all channel vectors and traces
- all stream vectors

## Results

- artifact name: pass | fail

## Overall Decision

- pass | fail

## Notes

- this seed proves only `Core` over `HTTP Binding v1`
- any observed excluded optional surface activates additional required artifacts
