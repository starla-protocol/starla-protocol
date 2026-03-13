# Status Delivery Precedes Final Delivery Result

State: Draft
Profile: `Core + Channels`
Condition: required when the implementation claims or exposes status delivery
Scenario: one visible status-delivery sequence occurs before one visible final `delivery result`
Related Spec: `drafts/channels-v1.md`, `drafts/stream-binding-v1.md`,
`drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible `channel adapter`
2. issue one visible `delivery request`
3. observe
   `GET /v1/channel-adapters/{channel_adapter_id}/delivery-requests/{delivery_request_id}/status-events`
4. allow one or more visible status-delivery updates, if supported
5. allow one visible final `delivery result`

## Required Event Or Observation Order

1. visible accepted `delivery request`
2. zero or more visible status-delivery updates
3. one visible final `delivery result`

## Terminal Condition

- the visible final delivery observation is one `delivery result`

## Forbidden Missing Or Reordered Events

- final `delivery result` treated as one status-delivery update
- status delivery treated as final `delivery result`
- more than one visible final `delivery result` for the same terminal attempt

## Conformance Hooks Exercised

- status delivery remains distinct from `delivery result`
- status delivery does not imply final delivery outcome
