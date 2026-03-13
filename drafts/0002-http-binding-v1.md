# 0002 HTTP Binding V1

State: Draft
Last Updated: 2026-03-12
Owner: Alan
Kind: Binding
Related Protocol Docs: `drafts/0001-starla-protocol-core-v1.md`, `drafts/0004-conformance-v1.md`
Related Otto Product Docs: `0007-post-m1-api-surface.md`

## Scope

This document is the draft HTTP binding for `starla-protocol` core law.

The first binding pass is expected to define:

- route mapping under `/v1`
- request and response envelope rules
- idempotency requirements for duplicate-prone mutations
- request correlation metadata
- HTTP status mapping for protocol-law errors

## Binding Rules

This binding will map transport-independent protocol law onto HTTP without redefining the core
semantic model.

This section is not yet complete enough for compliance claims.

## Resource Or Message Mapping

The first HTTP binding pass is expected to cover at least:

- agents
- sessions
- executions
- approvals
- tools

This section is not yet complete enough for compliance claims.

## Transport Errors

The HTTP binding is expected to define stable envelope and status-code mapping for protocol-law
errors.

This section is not yet complete enough for compliance claims.

## Versioning / Negotiation

The first HTTP binding pass is expected to define path versioning and any binding-specific
compatibility rules.

## Conformance Hooks

HTTP conformance vectors will be defined in `0004-conformance-v1.md`.
