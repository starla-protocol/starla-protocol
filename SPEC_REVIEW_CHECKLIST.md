# Spec Review Checklist

Use this checklist for every protocol-law change.

## Classification

- each new primary term appears in `VOCABULARY.md`
- each new primary term has exactly one primary classification
- each new primary term has exactly one owning specification

## Law Shape

- each new `Resource` defines identity, lifecycle, visibility, invariants, errors, and hooks
- each new `Command` defines actor, target, preconditions, inputs, side effects, errors, and hooks
- each new `Event` defines trigger, ordering, payload, and hooks
- each new `Relation` defines endpoints, visibility, invariants, and hooks
- each new `Value Object` or `Derived View` defines canonical shape and visibility

## Conformance

- each new `MUST` or `MUST NOT` has a visible conformance hook
- vectors or traces are added or updated for new observable behavior
- optional surfaces define activation rules
- bindings are updated if wire behavior changed

## Boundaries

- implementation-defined boundaries are named explicitly
- each implementation-defined boundary states fixed behavior and allowed variability
- non-normative guidance is labeled as guidance

## Consistency

- no non-canonical synonyms are introduced
- the owning document is the narrowest correct surface
- read order or status docs are updated if the surface set changed
