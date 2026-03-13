# Core Approvals HTTP Report Seed

Implementation Claim: `conformance/v1/claims/core-approvals-http-claim-seed.md`
Runner Identity:
Run Date:

## Vectors Executed

- all vectors in `core-http-report-seed.md`
- `submit-work-blocked-when-approval-required.md`
- `approval-inspection-exposes-state.md`
- `approval-listing-includes-visible-approval.md`
- `missing-approval-inspection-returns-not-found.md`
- `resolve-approval-approves-pending-approval.md`
- `resolve-approval-rejected-when-already-resolved.md`

## Traces Executed

- all traces in `core-http-report-seed.md`
- `approval-gated-submit-work.md`
- `approval-resolution-terminal.md`

## Not Executed By This Seed

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

- this seed proves `Core + Approvals` over `HTTP Binding v1`
- any observed excluded optional surface activates additional required artifacts
