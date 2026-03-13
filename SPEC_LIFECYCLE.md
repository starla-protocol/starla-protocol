# Specification Lifecycle

Use this file for the repository-level protocol authoring lifecycle.

`CHARTER.md` defines scope and boundaries.
`SPEC_METHOD.md` defines how protocol law is written.
This file defines how protocol surfaces move from idea to usable draft.

## Lifecycle

1. justify the surface
   - the surface MUST protect at least one real downstream product capability
   - the surface MUST satisfy `CHARTER.md`
2. assign ownership
   - the surface MUST have one owning specification
   - each primary term MUST be registered in `VOCABULARY.md` before first normative use
3. write semantic law
   - define nouns, commands, relations, invariants, errors, and event rules first
   - name implementation-defined boundaries explicitly
4. write the binding
   - map the semantic law onto HTTP or streaming without redefining meaning
5. add conformance artifacts
   - add vectors, traces, or clearly intended hooks for every hard normative rule
6. tighten coverage
   - remove duplicate ownership
   - remove silent ambiguity
   - normalize vocabulary drift
7. promote only when ready
   - a surface remains `Draft` until semantic law, binding coverage, and conformance coverage are
     materially present

## Admission Rules

- no new surface without downstream capability justification
- no new primary term without `VOCABULARY.md`
- no `MUST` or `MUST NOT` without a visible conformance hook
- no binding rule without a vector, trace, or clearly intended hook
- no composition surface before the substrate surfaces it composes are stable enough

## Surface Order

Preferred order:

1. substrate and boundary control
   - `CHARTER.md`
   - `VOCABULARY.md`
   - `SURFACE_MATRIX.md`
2. semantic draft
3. binding draft
4. conformance artifacts
5. promotion review

## Review Questions

- is the surface core, extension, or application-defined
- does the surface have one owning specification
- does the law define externally observable behavior only
- are implementation-defined boundaries named and bounded
- can black-box conformance verify the hard rules
- does the surface map to a real downstream capability

## Deferral Rule

Defer a surface when:

- it mainly composes still-unstable lower surfaces
- the downstream capability can be described without standardizing it yet
- the protocol would otherwise encode product or implementation assumptions too early
