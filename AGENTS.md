# Protocol Doc Rules

These rules apply to files under `starla-protocol/`.

## Purpose

Protocol docs are `starla-protocol` law.

They exist to define normative externally observable behavior clearly enough for independent
implementation and compliance review.

## Style

- Keep protocol docs extremely terse.
- Prefer the shortest wording that still preserves exact meaning.
- Use literal technical language only.
- Do not write narrative explanation, persuasion, marketing, or product framing in protocol docs.
- Do not restate rationale that belongs in product docs or design docs.
- If explanatory text is not required for protocol law, remove it.

## Normative Writing

- Use `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` literally.
- Each normative statement should describe one requirement as directly as possible.
- Prefer short lists, state tables, invariants, and operation rules over long prose blocks.
- If a rule can be expressed as a state transition, invariant, or precondition, do that instead of
  narrative prose.
- Do not write a hard `MUST` or `MUST NOT` unless a visible conformance hook exists or is clearly
  intended.
- Examples are informative by default and should be rare.

## Boundaries

- Product intent belongs in Otto product docs.
- Reference-implementation structure belongs in Otto design docs.
- Execution status belongs in Otto plandocs.
- Protocol docs should contain only what compliant implementations must do, what bindings require,
  and what conformance must verify.

## Consistency

- Favor directional consistency over local completeness.
- If a section starts expanding, split the law into smaller protocol docs instead of adding more
  explanation.
- Avoid synonyms for the same protocol noun or state.
- If wording drift appears between protocol docs, normalize the wording instead of elaborating.
