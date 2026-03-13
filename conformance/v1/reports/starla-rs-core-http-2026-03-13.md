# starla-rs Core HTTP 2026-03-13

Implementation Claim: `conformance/v1/claims/core-http-claim-seed.md`
Runner Identity: `starla-rs/scripts/run-core-http-claim.sh` on branch `implement/core-http-claimant` at commit `a8b6375`
Run Date: `2026-03-13`

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

## Results

- `agent-definition-listing-includes-visible-definition.md`: pass
- `agent-definition-inspection-exposes-state.md`: pass
- `disable-agent-definition-transitions-to-disabled.md`: pass
- `enable-agent-definition-transitions-to-enabled.md`: pass
- `agent-instance-listing-includes-visible-instance.md`: pass
- `agent-instance-inspection-exposes-definition-link-and-state.md`: pass
- `pause-agent-instance-transitions-to-paused.md`: pass
- `resume-agent-instance-transitions-to-ready.md`: pass
- `terminate-agent-instance-transitions-to-terminated.md`: pass
- `session-listing-includes-visible-session.md`: pass
- `session-inspection-exposes-state.md`: pass
- `close-session-transitions-to-closed.md`: pass
- `submit-work-success.md`: pass
- `execution-listing-includes-visible-execution.md`: pass
- `cancel-execution-transitions-to-canceled.md`: pass
- `cancel-execution-rejected-when-already-terminal.md`: pass
- `submit-work-rejected-when-instance-paused.md`: pass
- `delegate-execution-success.md`: pass
- `delegate-execution-rejected-when-parent-missing.md`: pass
- `delegate-execution-rejected-when-parent-terminal.md`: pass
- `delegate-execution-rejected-when-target-instance-missing.md`: pass
- `delegate-execution-rejected-when-target-instance-not-ready.md`: pass
- `delegate-execution-rejected-when-target-instance-equals-parent-owner.md`: pass
- `missing-execution-inspection-returns-not-found.md`: pass
- `failed-execution-inspection-is-not-transport-error.md`: pass
- `context-snapshot-preserves-provenance.md`: pass
- `context-snapshot-omits-absent-contribution-sections.md`: pass
- `inherited-lineage-material-visible-on-child-execution.md`: pass
- `inherited-lineage-material-omitted-without-visible-lineage.md`: pass
- `session-material-visible-on-session-attached-execution.md`: pass
- `execution-snapshot-separates-sections.md`: pass
- `execution-completion-terminal.md`: pass
- `execution-cancel-terminal.md`: pass
- `execution-lifecycle-minimal.md`: pass
- `execution-failure-terminal.md`: pass
- `delegated-execution-minimal.md`: pass

## Overall Decision

- pass

## Notes

- claimed surface remains `Core` over `HTTP Binding v1`
- excluded optional surfaces were not exercised
- this report is branch-specific to `implement/core-http-claimant` at `a8b6375`
