# Stream Binding v1

State: Draft
Kind: Binding Specification
Version: v1
Last Updated: 2026-03-13
Related Core Doc: `core-v1.md`
Related Channels Doc: `channels-v1.md`
Related Conformance Doc: `conformance-v1.md`
Draft Notice: This document does not yet authorize compliance claims.

## Scope

This document is the draft streaming binding specification for `Core v1` execution events and
optional `Channels v1` `status delivery`.

This binding defines:

- execution event framing
- ordering rules
- terminal event behavior
- optional `status delivery` event framing
- reconnect or replay expectations where relevant

This pass does not define:

- streaming transport for proactive delivery request submission
- streaming transport for tool events
- streaming transport for approval events
- streaming transport for channel surfaces other than optional `status delivery`

## Binding Rules

- `Stream Binding v1` MUST use Server-Sent Events.
- execution observation MUST use `GET /v1/executions/{execution_id}/events`.
- optional channel status observation, if exposed, MUST use
  `GET /v1/channel-adapters/{channel_adapter_id}/delivery-requests/{delivery_request_id}/status-events`.
- the binding MUST NOT change underlying `Core v1` or `Channels v1` semantics.
- SSE event frames MUST use:
  - `id`
  - `event`
  - `data`
- every visible stream frame MUST include `id`
- `event` MUST equal the canonical protocol event name or canonical optional surface event name
  exposed by this binding.
- `data` MUST be JSON.
- `id` MUST remain stable for the same visible event on equivalent replays of the same stream
  target.

## Resource Or Message Mapping

### Execution Events

- Route: `GET /v1/executions/{execution_id}/events`
- Success:
  - success MUST return `200 OK`
  - content type MUST be `text/event-stream`
  - every execution event frame `data` MUST include `execution_id`
  - every execution event frame `event` MUST equal one canonical execution-related event name
  - execution event order on the wire MUST match `Core v1`
- Terminal Behavior:
  - after `execution.completed`, `execution.failed`, or `execution.canceled`, the stream MAY close
  - if the stream remains open after a terminal execution event, it MUST NOT emit a later execution
    event for the same `execution`

### Status Delivery Events

- Route:
  `GET /v1/channel-adapters/{channel_adapter_id}/delivery-requests/{delivery_request_id}/status-events`
- Success:
  - success MUST return `200 OK`
  - content type MUST be `text/event-stream`
  - every visible status-delivery frame `event` MUST equal `channel.status`
  - every visible status-delivery frame `data` MUST include:
    - `delivery_request_id`
    - `channel_adapter_id`
    - `channel_kind`
    - `status`
    - `emitted_at`
- Terminal Behavior:
  - `delivery result` MUST NOT be emitted as `channel.status`
  - the status stream MAY close after the last visible status-delivery update
  - if the status stream remains open after a final visible `delivery result`, it MUST NOT emit a
    later `channel.status` frame for the same delivery attempt

## Replay / Reconnect

- reconnect requests MAY use SSE `Last-Event-ID`
- replay support MAY differ by stream target
- if `Last-Event-ID` is absent, the stream MUST begin at the next visible event available to the
  server for that stream target
- if replay is supported and `Last-Event-ID` identifies one retained visible event for the same
  stream target, the resumed stream MUST begin strictly after that event
- if replay is not supported and `Last-Event-ID` is present, the request MUST fail with
  `invalid_state`
- if replay is supported but `Last-Event-ID` does not identify one retained visible event for the
  same stream target, the request MUST fail with `invalid_state`

## Transport Errors

- missing visible stream target MUST return the normal HTTP binding `not_found` error envelope
- unsupported or invalid replay state MUST return the normal HTTP binding `invalid_state` error
  envelope
- stream disconnect, reconnect, or client timeout MUST NOT by itself imply a terminal execution
  outcome

## Versioning / Negotiation

- stream routes MUST remain under `/v1`
- `Stream Binding v1` defines no additional negotiation mechanism beyond the route and SSE content
  type

## Conformance Hooks

Streaming conformance is defined in `conformance-v1.md`.

Seed stream traces:

- `../conformance/v1/traces/execution-completion-terminal.md`
- `../conformance/v1/traces/execution-lifecycle-minimal.md`
- `../conformance/v1/traces/execution-failure-terminal.md`
- `../conformance/v1/traces/status-delivery-precedes-final-delivery-result.md`

Seed stream vectors:

- `../conformance/v1/vectors/execution-stream-missing-target-returns-not-found.md`
- `../conformance/v1/vectors/execution-stream-disconnect-does-not-create-terminal-outcome.md`
- `../conformance/v1/vectors/execution-stream-emits-no-later-event-after-terminal.md`
- `../conformance/v1/vectors/execution-stream-replay-resumes-after-last-event-id.md`
- `../conformance/v1/vectors/execution-stream-replay-rejected-when-replay-unsupported.md`
- `../conformance/v1/vectors/execution-stream-replay-rejected-when-last-event-id-not-retained.md`
- `../conformance/v1/vectors/status-stream-missing-target-returns-not-found.md`
- `../conformance/v1/vectors/status-stream-replay-resumes-after-last-event-id.md`
- `../conformance/v1/vectors/status-stream-replay-rejected-when-replay-unsupported.md`
- `../conformance/v1/vectors/status-stream-replay-rejected-when-last-event-id-not-retained.md`
- `../conformance/v1/vectors/status-stream-emits-no-later-status-after-final-delivery-result.md`
