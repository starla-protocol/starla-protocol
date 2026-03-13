# Conformance System

## Purpose

This repository verifies protocol compliance by black-box observation of public bindings.

Compliance is judged from:

- wire shape
- observable behavior
- event ordering
- error semantics
- declared profile support

Internal implementation structure is not part of compliance.

## Verification Model

A conformance run should verify:

- binding schemas and envelopes
- required command and resource behavior
- forbidden state transitions
- required negative-path behavior
- required event traces
- reported protocol version, binding version, and supported profiles

## Artifact Layout

- `conformance/v1/vectors/` — canonical success and failure vectors
- `conformance/v1/traces/` — canonical ordered event traces
- `conformance/v1/claims/` — implementation claims about supported versions and profiles
- `conformance/v1/reports/` — conformance run results

## Vector Classes

- `success` — required successful behavior
- `negative` — invalid request, invalid state, denied, or conflicting input behavior
- `idempotency` — repeated command behavior under the same idempotency key
- `conditional` — required only when an optional surface is claimed or observed on the binding
- `profile` — behavior required only for a specific compliance profile

## Conditional Activation

A `conditional` vector becomes required when:

- the implementation claim declares the corresponding optional surface
- the conformance runner observes the corresponding optional surface on the public binding

## Trace Classes

- `execution lifecycle`
- `approval blocking and resolution`
- `delegation and lineage`
- `artifact emission`

## Claim Requirements

An implementation claim should declare:

- implementation name
- implementation version
- claimed `starla-protocol` version
- claimed binding versions
- claimed compliance profiles
- known unsupported optional surfaces

## Report Requirements

A conformance report should record:

- implementation claim under test
- date and runner identity
- vectors executed
- traces executed
- pass or fail result per artifact
- overall pass or fail decision

## Pass Rule

An implementation passes a claimed profile only if:

- every required vector for that profile passes
- every activated conditional vector for that profile passes
- every required trace for that profile passes
- no forbidden error or state transition is observed
- the implementation claim does not exceed the verified surface

## Failure Rule

A run fails if:

- any required vector fails
- any activated conditional vector fails
- any required trace fails
- event ordering violates the specification
- an implementation claims support for an unverified profile or binding
