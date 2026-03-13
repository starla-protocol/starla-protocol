# Surface Matrix

Current v1 surface ownership and completeness.

`v1` closure criteria are defined in `V1_TARGET.md`.

## Surfaces

### Core v1

- purpose: universal runtime nouns, lifecycle, ownership, errors, and core commands
- owns:
  - `agent definition`
  - `agent instance`
  - `session`
  - `execution`
  - `approval`
  - `artifact`
  - `reference`
  - `busy`
  - `submit work`
- state: active draft
- major gaps:
  - no major semantic gap currently tracked

### Context v1

- purpose: context construction, contribution classes, scope, inheritance, visibility, exclusion,
  and exported views
- owns:
  - `context`
  - `context contribution`
  - `context snapshot`
  - `execution snapshot`
- state: active draft
- major gaps:
  - no major semantic gap currently tracked

### Tools v1

- purpose: tool identity, invocation, result, failure, and policy gating
- owns:
  - `tool definition`
  - `invoke tool`
  - `tool result`
- state: active draft
- major gaps:
  - no major semantic gap currently tracked

### Coordination v1

- purpose: delegated execution, lineage, and minimal cross-agent coordination
- owns:
  - `delegate execution`
  - `execution-lineage`
- state: active draft
- major gaps:
  - no major semantic gap currently tracked

### Channels v1

- purpose: external ingress, outbound delivery, channel routing, optional status delivery, and
  optional proactive delivery
- owns:
  - `channel adapter`
  - `channel kind`
  - `ingress message`
  - `delivery request`
  - `delivery result`
  - `status delivery`
  - `reply target`
  - `thread reference`
  - `channel health`
- state: active draft
- major gaps:
  - no major semantic gap currently tracked

### Recall v1

- purpose: externally visible recall or memory semantics, if standardized
- state: planned

### Skill Management v1

- purpose: skill identity, versioning, attachment, enablement, and governance, if standardized
- state: planned

### HTTP Binding v1

- purpose: map active semantic surfaces onto HTTP
- state: active draft
- major gaps:
  - no major semantic gap currently tracked

### Stream Binding v1

- purpose: map execution-event semantics and optional channel status delivery onto a streaming
  transport
- state: active draft
- major gaps:
  - no major semantic gap currently tracked

### Conformance v1

- purpose: define claims, vectors, traces, and reporting for compliance
- state: active draft
- major gaps:
  - no major conformance-only gap currently tracked

## Current Priority

1. begin claimable-profile proof work
2. keep deferred boundaries deferred unless `V1_TARGET.md` is revised

## Next Deliverables

1. select or build first claimant for `Core` over `HTTP Binding v1`
2. use `conformance/v1/claims/core-http-claim-seed.md` and
   `conformance/v1/reports/core-http-report-seed.md` as the first proof scaffold
3. prove first claim target: `Core` over `HTTP Binding v1`

## Coherence Rules

- each primary term has exactly one owning specification
- `Core` compliance currently includes `Core v1` plus `Context v1`
- bindings and conformance must follow surface ownership
