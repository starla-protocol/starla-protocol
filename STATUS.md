# Status

Repository state: `Draft-Complete`
Stable version: none
Compliance claims:
- `starla-rs` `Core` over `HTTP Binding v1` report recorded at `conformance/v1/reports/starla-rs-core-http-2026-03-13.md`
First claim target: `Core` over `HTTP Binding v1`

## Read Order

1. `CHARTER.md`
2. `V1_TARGET.md`
3. `FIRST_RUST_CLAIMANT_SCOPE.md`
4. `WORKING_DECISIONS.md`
5. `SURFACE_MATRIX.md`
6. `VOCABULARY.md`
7. `SPEC_LIFECYCLE.md`
8. `drafts/core-v1.md`
9. `drafts/context-v1.md`
10. `drafts/tools-v1.md`
11. `drafts/coordination-v1.md`
12. `drafts/channels-v1.md`
13. `drafts/http-binding-v1.md`
14. `drafts/stream-binding-v1.md`
15. `drafts/conformance-v1.md`
16. `CONFORMANCE_SYSTEM.md`
17. `SPEC_METHOD.md`
18. `SPEC_REVIEW_CHECKLIST.md`

## Drafts

- `core-v1.md` — draft core specification for resource semantics and lifecycle behavior
- `context-v1.md` — draft context specification for construction, scope, inheritance, and
  visibility behavior
- `tools-v1.md` — draft tools specification for tool identity, invocation, and results
- `coordination-v1.md` — draft coordination specification for delegation and lineage behavior
- `channels-v1.md` — draft channels specification for canonical envelopes, routing fields, and
  exclusions
- `http-binding-v1.md` — draft HTTP binding for the core specification
- `stream-binding-v1.md` — draft streaming binding for execution events and optional channel status
  delivery
- `conformance-v1.md` — draft conformance requirements and reporting rules

## Systems

- `V1_TARGET.md` — `v1` endpoint, non-goals, and closure criteria
- `FIRST_RUST_CLAIMANT_SCOPE.md` — fixed scope for the first Rust claimant
- `WORKING_DECISIONS.md` — recurring project decisions and working sequence
- `SURFACE_MATRIX.md` — current surface ownership and completeness
- `SPEC_LIFECYCLE.md` — repository-level protocol authoring lifecycle
- `CONFORMANCE_SYSTEM.md` — black-box compliance model and artifact layout
- `SPEC_METHOD.md` — specification classification and structuring method
- `VOCABULARY.md` — canonical term registry
- `SPEC_REVIEW_CHECKLIST.md` — review gate
- `scripts/lint-docs.sh` — terminology and header lint

## Planned Surfaces

- `Skill Management v1` — skill definitions, versioning, attachment, enablement, and governance,
  if standardized
- `Recall v1` — externally visible recall or memory semantics, if standardized

## Active

- None

## Current Focus

- record and review first claimant report for `Core` over `HTTP Binding v1`
- decide whether to merge or revise `starla-rs` `implement/core-http-claimant`
- keep deferred boundaries deferred unless `V1_TARGET.md` is revised explicitly

## Claim Blockers

- Otto has no runtime implementation yet
- OpenFang exposes a different northbound API family
- ZeroClaw does not expose the `starla-protocol` runtime surface

## Deferred

- hands and device control

## Archived

- None
