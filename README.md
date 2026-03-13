# starla-protocol

This file is the repo-local source of truth for `starla-protocol` docs.

Protocol docs capture normative externally observable behavior. Otto may refer to this normative
content as protocol law. Protocol docs are not product-definition essays, not implementation
architecture notes, and not execution trackers.

`starla-protocol` is the protocol.
Otto is a product and reference implementation that targets it.

## Purpose

`starla-protocol` docs exist to define a versioned protocol clearly enough that:

- multiple competent teams could implement materially similar externally observable behavior
- a third party could determine compliance without asking the authors for intent

## Writing Standard

- Keep protocol docs extremely terse.
- Use the shortest wording that preserves exact meaning.
- Prefer normative rules, state tables, invariants, and binding clauses over explanatory prose.
- If text is explanatory rather than required for protocol law, move it to Otto product or design
  docs.
- Favor directional consistency across protocol docs over local elaboration.

## Law Boundary

- Enforce protocol law strictly at the semantic boundary.
- Do not over-specify implementation detail unless an external guarantee depends on it.
- If two compliant implementations can differ without breaking clients or interoperability, keep the
  detail implementation-defined by default.

## Normative Language

Use the following words literally:

- `MUST`
- `MUST NOT`
- `SHOULD`
- `SHOULD NOT`
- `MAY`

Use them only for normative requirements.

Examples are informative by default unless explicitly marked as canonical conformance vectors.
Examples should be rare.

## Conformance Depth

- `MUST` and `MUST NOT` should track visible conformance hooks such as vectors, negative paths,
  state tables, or binding tests.
- If a rule cannot yet be judged for compliance, it should usually stay out of hard law for now.
- Prefer profile-based compliance claims over one oversized compliance badge.

## Protocol Doc Kinds

`starla-protocol` docs should be classified as one of:

- `Core Law` — transport-independent semantic rules
- `Binding` — transport mapping such as HTTP or SSE
- `Conformance` — pass or fail compliance material

## Suggested Sections

### Core Law

1. `## Scope`
2. `## Compliance Profiles`
3. `## Terminology`
4. `## Semantic Model`
5. `## State Machines / Invariants`
6. `## Operations`
7. `## Event Model`
8. `## Error Model`
9. `## Security / Policy Semantics`
10. `## Versioning / Extensions`
11. `## Conformance Hooks`

### Binding

1. `## Scope`
2. `## Binding Rules`
3. `## Resource Or Message Mapping`
4. `## Transport Errors`
5. `## Versioning / Negotiation`
6. `## Conformance Hooks`

### Conformance

1. `## Scope`
2. `## Compliance Targets`
3. `## Required Vectors`
4. `## Negative Paths`
5. `## Event Trace Rules`
6. `## Reporting`

If a section does not materially apply, write `N/A — reason`.

## States

Use:

- `Draft`
- `Active`
- `Archived`

## Relationship To Other Docs

- product docs define what Otto is trying to be
- protocol docs define what compliant implementations must do
- design docs define how Otto's Rust reference implementation is structured
- plandocs define execution and migration work
