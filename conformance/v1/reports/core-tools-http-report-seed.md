# Core Tools HTTP Report Seed

Implementation Claim: `conformance/v1/claims/core-tools-http-claim-seed.md`
Runner Identity:
Run Date:

## Vectors Executed

- all vectors in `core-http-report-seed.md`
- `tool-definition-listing-includes-visible-tool.md`
- `tool-definition-inspection-exposes-state.md`
- `missing-tool-definition-inspection-returns-not-found.md`
- `invoke-tool-success.md`
- `invoke-tool-rejected-when-tool-disabled.md`
- `invoke-tool-rejected-when-tool-deleted.md`
- `invoke-tool-denied-by-capability.md`

## Traces Executed

- all traces in `core-http-report-seed.md`

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
- `invoke-tool-blocked-when-approval-required.md`
- `invoke-tool-terminal-approval-denial-returns-approval-denied.md`
- `invoke-tool-idempotent-replay-preserves-result.md`
- `tool-derived-material-visible-when-exposed.md`
- `tool-invocation-with-artifact.md`
- `tool-invocation-blocked-when-approval-required.md`
- all channel vectors and traces
- all stream vectors

## Results

- artifact name: pass | fail

## Overall Decision

- pass | fail

## Notes

- this seed proves `Core + Tools` over `HTTP Binding v1`
- any observed excluded optional surface activates additional required artifacts
