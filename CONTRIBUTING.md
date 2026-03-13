# Contributing

This repository is a standards repository.

Use `SPEC_METHOD.md` as the classification and structuring method for protocol law.
Use `CHARTER.md` as the scope and modularization guide while the specification set is still taking
shape.
Use `SPEC_LIFECYCLE.md` as the repository-level authoring lifecycle.
Use `WORKING_DECISIONS.md` for recurring project decisions and sequencing.
Use `VOCABULARY.md` as the canonical term registry.
Use `SPEC_REVIEW_CHECKLIST.md` as the review gate.

## Document Kinds

- `Core Specification` — transport-independent semantic rules
- `Binding Specification` — transport mappings such as HTTP or streaming
- `Conformance Specification` — evidence and reporting rules for compliance claims

## Naming

- use `Core v1` as the formal name of the primary specification
- use `multi-agent harness` only as a scope phrase, not as a document family name
- do not use `Harness Core` as a formal layer name

## Writing Rules

- keep protocol text extremely terse
- prefer state tables, invariants, and operation clauses over explanatory prose
- define semantics, not implementation structure
- make externally observable behavior as deterministic as possible
- if a boundary is implementation-defined, say so explicitly and bound it
- non-normative guidance for implementation-defined areas is allowed if clearly labeled as guidance
- do not write a hard `MUST` or `MUST NOT` without a visible conformance hook
- treat examples as informative unless explicitly marked otherwise

## Draft Discipline

- draft documents do not authorize compliance claims
- move text out of protocol law if it is product explanation or implementation rationale
- keep naming stable across documents

## Guardrails

- add each new primary term to `VOCABULARY.md` before first normative use
- run `./scripts/lint-docs.sh` before merge
- use `.github/pull_request_template.md` for protocol-law changes
