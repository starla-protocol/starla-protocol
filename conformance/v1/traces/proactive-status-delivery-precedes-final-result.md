# Proactive Status Delivery Precedes Final Result

State: Draft
Profile: `Core + Channels`
Condition: required when the implementation claims or exposes proactive delivery and claims or
exposes status delivery
Scenario: one visible proactive delivery request is accepted without prior visible ingress, zero or
more visible status-delivery updates occur, and one visible final `delivery result` appears later
for the same request
Related Spec: `drafts/channels-v1.md`, `drafts/stream-binding-v1.md`,
`drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible `channel adapter`
2. issue one visible proactive `delivery request`
3. provide no prior visible `ingress message` for the scenario
4. receive `202 Accepted`
5. observe zero or more visible status-delivery updates for the same `delivery_request_id`
6. later inspect one visible final `delivery result` for the same `delivery_request_id`

## Required Event Or Observation Order

1. visible accepted proactive `delivery request`
2. zero or more visible status-delivery updates
3. one visible final `delivery result`

## Terminal Condition

- the visible final delivery observation is one `delivery result` linked to the accepted proactive
  `delivery_request_id`

## Forbidden Missing Or Reordered Events

- proactive delivery rejection solely because no prior visible `ingress message` exists
- visible final `delivery result` before visible accepted proactive `delivery request`
- final `delivery result` treated as one status-delivery update
- status delivery treated as final `delivery result`
- more than one visible final `delivery result` for the same terminal attempt

## Conformance Hooks Exercised

- proactive delivery does not require prior visible ingress
- status delivery remains distinct from `delivery result`
- status delivery does not imply final delivery outcome
