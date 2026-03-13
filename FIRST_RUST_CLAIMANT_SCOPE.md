# First Rust Claimant Scope

This document fixes the scope for the first `starla-protocol` Rust implementation claimant.

## Claim Target

- language: `Rust`
- claimed protocol version: `v1`
- claimed binding versions:
  - `HTTP Binding v1`
- claimed compliance profiles:
  - `Core`
- conformance seed:
  - `conformance/v1/claims/core-http-claim-seed.md`
  - `conformance/v1/reports/core-http-report-seed.md`

## Purpose

The first Rust claimant exists to prove that `Core` over `HTTP Binding v1` is implementable and
claimable.

It does not exist to prove the full `v1` surface.

## Required Public Surface

The first Rust claimant MUST expose the public HTTP behavior required by the seeded `Core` claim.

That includes:

- `agent definition` inspection, listing, enable, and disable
- `agent instance` inspection, listing, pause, resume, and terminate
- `session` inspection, listing, and close
- `submit work`
- `execution` inspection, listing, and cancel
- `delegate execution`
- `context snapshot`
- `execution snapshot`

## Allowed Implementation Shortcuts

The first Rust claimant MAY:

- keep all state in memory
- run as a single local process
- use a deterministic synthetic execution engine instead of a model provider
- omit `Stream Binding v1`
- omit approval-gated behavior
- omit tool surfaces
- omit channel surfaces
- omit artifact inspection surfaces
- omit persistence across restart

## Explicit Exclusions

The first Rust claimant MUST NOT claim:

- `Core + Approvals`
- `Core + Tools`
- `Core + Channels`
- `Stream Binding v1`

The first Rust claimant SHOULD avoid exposing optional behavior that would activate additional
conditional conformance artifacts.

That includes:

- approval-gated `submit work`
- approval inspection or resolution
- visible terminal approval denial during delegation
- idempotent `delegate execution`
- parent-driven supervisory child-terminal behavior
- independently recomputed visible implementation-supplied material at a child execution boundary
- tool inspection or invocation
- artifact inspection
- status delivery
- proactive delivery

## Success Condition

The first Rust claimant succeeds only when:

- the seeded `Core` claim remains honest
- every required artifact in the seeded `Core` report passes
- no excluded optional surface is claimed

## Non-Goals

The first Rust claimant is not:

- the Otto product
- a durable production runtime
- a full `v1` claimant
- a provider or model integration target
- a workflow or automation runtime
