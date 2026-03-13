# 0004 Conformance V1

State: Draft
Last Updated: 2026-03-12
Owner: Alan
Kind: Conformance
Related Protocol Docs: `drafts/0001-starla-protocol-core-v1.md`, `drafts/0002-http-binding-v1.md`, `drafts/0003-stream-binding-v1.md`

## Scope

This document is the draft home for `starla-protocol` conformance requirements and compliance
reporting.

It is expected to define what evidence is required before an implementation may claim compliance
with any `starla-protocol` profile.

## Compliance Targets

The first conformance pass is expected to define compliance targets for:

- `Core`
- `Core + Tools`
- `Core + Approvals`

## Required Vectors

The first conformance pass is expected to require:

- canonical HTTP fixtures
- canonical error fixtures
- canonical event traces
- profile-specific success cases

## Negative Paths

The first conformance pass is expected to require invalid-request, invalid-state, and denial-path
coverage.

## Event Trace Rules

The first conformance pass is expected to define how ordered event traces are captured and judged.

## Reporting

The first conformance pass is expected to define how an implementation reports supported version,
binding, and compliance profile claims.
