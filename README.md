# starla-protocol

`starla-protocol` is a draft protocol for the transport-independent semantics of a multi-agent
harness, its transport bindings, and its conformance requirements.

Otto is the current product and reference implementation targeting it.

## Status

- Repository state: `Draft-Complete`
- Stable version: none
- Compliance claims: none
- First claim target: `Core` over `HTTP Binding v1`

## Scope

- transport-independent core specification for multi-agent harness semantics
- first-class protocol surfaces for context, tools, coordination, and channels where
  interoperability requires them
- HTTP binding
- streaming binding
- conformance requirements

## Authority Order

1. core specification
2. bindings
3. conformance

Bindings map the core specification onto transports. Conformance defines the evidence required for
claims against that specification.

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
19. `STATUS.md`

## Repository Layout

- `drafts/` — draft specification and binding docs
- `CHARTER.md` — protocol goals and modular surface boundaries
- `V1_TARGET.md` — `v1` endpoint, non-goals, and closure criteria
- `FIRST_RUST_CLAIMANT_SCOPE.md` — fixed scope for the first Rust claimant
- `WORKING_DECISIONS.md` — recurring project decisions and working sequence
- `SURFACE_MATRIX.md` — current surface ownership and completeness
- `SPEC_LIFECYCLE.md` — repository-level protocol authoring lifecycle
- `CONFORMANCE_SYSTEM.md` — black-box compliance model and artifact system
- `SPEC_METHOD.md` — classification and authoring method for protocol law
- `VOCABULARY.md` — canonical protocol terms and forbidden synonyms
- `SPEC_REVIEW_CHECKLIST.md` — review gate for protocol-law changes
- `conformance/` — versioned vectors, traces, claims, and reports
- `scripts/lint-docs.sh` — terminology and header lint
- `scripts/run-core-http-claim.py` — standalone external runner for the seeded `Core` HTTP claim
- `scripts/run-core-tools-http-claim.py` — standalone external runner for the seeded `Core + Tools` HTTP claim
- `STATUS.md` — document list and maturity state
- `CONTRIBUTING.md` — public contribution and writing rules
- `AGENTS.md` — repo-local agent instructions

## Protocol Rules

- normative text defines externally observable behavior only
- context, coordination, execution, and references belong in protocol law
- channels are a first-class protocol concern, but not part of minimal `Core v1` by default
- protocol behavior should be as concrete and deterministic as possible
- implementation detail stays implementation-defined unless interoperability requires otherwise
- implementation-defined boundaries should be named explicitly and bounded clearly
- internal memory, retrieval, ranking, and prompt-assembly strategy stay implementation-defined
- hands and device control are currently deferred and may remain application-defined
- `MUST` and `MUST NOT` should have visible conformance hooks
- examples are informative by default
- new primary terms should be registered in `VOCABULARY.md` before first normative use
