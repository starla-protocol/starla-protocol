# Specification Method

## Normative Basis

- use `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` as defined by RFC 2119 and RFC 8174
- use those words only for normative requirements
- every hard `MUST` or `MUST NOT` should have a visible conformance hook
- unspecified externally observable behavior should be treated as an under-specified defect

## Classification Model

Each primary protocol term MUST be classified as exactly one primary kind:

- `Resource` — durable or independently addressable protocol object
- `Command` — externally observable action that requests state change
- `Event` — externally observable fact emitted because state changed or execution advanced
- `Relation` — invariant association between protocol objects
- `Policy Primitive` — permission, limit, or enforcement input evaluated at the protocol boundary
- `Value Object` — structured value with stable meaning but no independent lifecycle
- `Derived View` — externally visible state computed from other protocol state

If a proposed term fits more than one primary kind, split it rather than overloading the noun.
Each new primary term MUST be registered in `VOCABULARY.md` before first normative use.

## Required Record Templates

### Resource

- definition
- identity
- ownership
- lifecycle states
- allowed transitions
- visibility
- invariants
- commands that create or change it
- events that expose it
- errors involving it
- conformance hooks

### Command

- actor
- target
- preconditions
- inputs
- side effects
- resources created or changed
- events emitted
- errors
- idempotency
- conformance hooks

### Event

- source
- trigger
- ordering constraints
- payload
- terminal meaning, if any
- conformance hooks

### Relation

- endpoints
- ownership or scope
- visibility
- invariants
- conformance hooks

### Policy Primitive

- definition
- scope
- attachment point
- enforcement outcomes
- conformance hooks

### Value Object

- definition
- shape
- validation rules
- equality or identity rules, if relevant
- visibility

### Derived View

- definition
- source state
- derivation rule
- visibility
- conformance hooks

### Implementation-Defined Boundary

- boundary name
- why the area is left implementation-defined
- fixed externally observable constraints
- allowed variability
- forbidden assumptions for clients or implementations
- non-normative implementation guidance, if useful

## Decomposition Rules

- if a concern has its own resources, commands, events, errors, or conformance claims, it should be
  reviewed as its own protocol surface
- if a concept is not durable, addressable, or independently observable, it should usually not be a
  `Resource`
- if a concept is an action, name it as a verb phrase and model it as a `Command`
- if a concept is produced by another resource or command and has no independent lifecycle, model it
  as a `Value Object`, `Relation`, or `Derived View`
- if a concept changes externally observable meaning across documents, fix the vocabulary before
  adding more law
- if a boundary is left open, describe it explicitly instead of leaving silent ambiguity
- when possible, add non-normative implementation guidance for open boundaries so independent
  implementations have a better chance of converging on successful behavior
