# V1 Target

Repository target for `starla-protocol` `v1`.

## V1 Scope

`v1` targets the minimum interoperable agent-runtime platform with:

- `Core v1`
- `Context v1`
- `Tools v1`
- `Coordination v1`
- `Channels v1`
- `HTTP Binding v1`
- `Stream Binding v1`
- `Conformance v1`

## V1 Draft-Complete

`v1` is draft-complete only when:

- no new top-level `v1` surface is being added
- each active `v1` surface has owned vocabulary
- each active `v1` surface has explicit resources, commands, events, errors, and conformance hooks
- each claimed binding has fixed routes, envelopes, and error mapping
- each active `v1` surface has required vectors and traces for its normative behavior
- placeholder wording has been removed or moved to explicit deferral

## V1 Claimable

`v1` is claimable only when:

- at least one implementation can claim `Core`
- at least one implementation can claim `Core + Tools`
- at least one implementation can claim `Core + Approvals`
- at least one implementation can claim `Core + Channels`
- a black-box runner can verify the claimed profiles through public bindings
- required vectors and traces pass for each claimed profile

## V1 Non-Goals

These are not part of `v1`:

- `Workflow / Automation v1`
- `Recall v1`
- `Skill Management v1`
- device control
- provider or model standardization
- a generic inter-agent message surface
- bootstrap and provisioning lifecycle mutation standardization beyond the current stable mutation
  surface
- typing-indicator-specific, draft-update-specific, and reaction-specific channel semantics
- per-channel policy state model
- channel-health state model

## V1 Closure Order

Close `v1` in this order:

1. finish `Coordination v1`
2. close remaining `Core v1` gaps
3. close remaining `Channels v1` and binding gaps
4. close conformance coverage gaps
5. declare `v1` draft-complete
6. prove at least one claimable implementation profile

## Scope Freeze Rule

Before `v1` is draft-complete:

- a new top-level `v1` surface MUST NOT be added unless an existing active `v1` surface cannot
  carry the behavior without loss of coherence
- deferred surfaces MUST remain deferred unless `V1 Target` is revised explicitly
