# Delivery Request Accepted Before Final Result

State: Draft
Profile: `Core + Channels`
Condition: required when the implementation returns `202 Accepted` for visible delivery request
submission and later exposes one visible final `delivery result` on the public binding
Scenario: one visible delivery request is accepted first and one visible final `delivery result`
appears later for the same request
Related Spec: `drafts/channels-v1.md`, `drafts/http-binding-v1.md`,
`drafts/conformance-v1.md`

## Triggering Requests Or Commands

1. target one visible `channel adapter`
2. issue one visible `delivery request`
3. receive `202 Accepted`
4. later inspect one visible final `delivery result` for the same `delivery_request_id`

## Required Event Or Observation Order

1. visible accepted `delivery request`
2. one visible final `delivery result`

## Terminal Condition

- the visible final delivery observation is one `delivery result` linked to the accepted
  `delivery_request_id`

## Forbidden Missing Or Reordered Events

- visible final `delivery result` before visible accepted `delivery request`
- final result linked to one different `delivery_request_id`
- more than one visible final `delivery result` for the same terminal attempt

## Conformance Hooks Exercised

- accepted delivery request remains distinct from final `delivery result`
- final `delivery result` preserves request linkage
