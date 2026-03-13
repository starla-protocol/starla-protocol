# HTTP Binding v1

State: Draft
Kind: Binding Specification
Version: v1
Last Updated: 2026-03-13
Related Core Doc: `core-v1.md`
Related Context Doc: `context-v1.md`
Related Tools Doc: `tools-v1.md`
Related Coordination Doc: `coordination-v1.md`
Related Channels Doc: `channels-v1.md`
Related Conformance Doc: `conformance-v1.md`
Draft Notice: This document does not yet authorize compliance claims.

## Scope

This document defines the draft HTTP binding for `Core v1`, `Context v1`, `Tools v1`,
`Coordination v1`, and `Channels v1`.

This binding defines:

- route mapping under `/v1`
- JSON request and response mapping
- idempotency header mapping for `submit work`
- idempotency header mapping for `delegate execution`
- idempotency header mapping for `invoke tool`
- HTTP status mapping for protocol-law errors
- canonical HTTP export surfaces for `context snapshot` and `execution snapshot`
- canonical JSON member preservation for channel envelopes when `Channels v1` is exposed over HTTP

This pass does not define:

- broader execution mutation routing beyond the current stable mutation surface
- tool-definition lifecycle mutation routing on the current `v1` public surface
- direct HTTP mapping for future coordination surfaces beyond `delegate execution`
- direct HTTP mapping for future optional channel capability surfaces beyond `status delivery`

## Binding Rules

This binding maps `Core v1`, `Context v1`, `Tools v1`, `Coordination v1`, and `Channels v1` onto
HTTP.

- HTTP MUST NOT redefine `Core v1`, `Context v1`, `Tools v1`, `Coordination v1`, or `Channels v1`
  semantics.
- `Core v1`, `Context v1`, `Tools v1`, `Coordination v1`, and `Channels v1` request and response
  bodies MUST use `application/json`.
- path versioning MUST use `/v1`.
- `submit work` idempotent retry MUST use the `Idempotency-Key` header.
- `delegate execution` idempotent retry MUST use the `Idempotency-Key` header when an idempotency
  key is exposed.
- `invoke tool` idempotent retry MUST use the `Idempotency-Key` header when an idempotency key is
  exposed.
- caller authentication mechanism is outside `Core v1`.
- transport-level rejection before protocol-law evaluation is not yet a conformance target.

## Resource And Command Mapping

### Agent Definition List

- Route: `GET /v1/agent-definitions`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON array
  - every array item MUST include:
    - `agent_definition_id`
    - `state`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Agent Definition

- Route: `GET /v1/agent-definitions/{agent_definition_id}`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `agent_definition_id`
    - `state`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Disable Agent Definition

- Route: `POST /v1/agent-definitions/{agent_definition_id}/disable`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `agent_definition_id`
    - `state`
  - `state` MUST equal `disabled`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Enable Agent Definition

- Route: `POST /v1/agent-definitions/{agent_definition_id}/enable`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `agent_definition_id`
    - `state`
  - `state` MUST equal `enabled`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Agent Instance List

- Route: `GET /v1/agent-instances`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON array
  - every array item MUST include:
    - `agent_instance_id`
    - `agent_definition_id`
    - `state`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Agent Instance

- Route: `GET /v1/agent-instances/{agent_instance_id}`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `agent_instance_id`
    - `agent_definition_id`
    - `state`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Pause Agent Instance

- Route: `POST /v1/agent-instances/{agent_instance_id}/pause`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `agent_instance_id`
    - `state`
  - `state` MUST equal `paused`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Resume Agent Instance

- Route: `POST /v1/agent-instances/{agent_instance_id}/resume`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `agent_instance_id`
    - `state`
  - `state` MUST equal `ready`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Terminate Agent Instance

- Route: `POST /v1/agent-instances/{agent_instance_id}/terminate`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `agent_instance_id`
    - `state`
  - `state` MUST equal `terminated`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Session List

- Route: `GET /v1/sessions`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON array
  - every array item MUST include:
    - `session_id`
    - `state`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Session

- Route: `GET /v1/sessions/{session_id}`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `session_id`
    - `state`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Close Session

- Route: `POST /v1/sessions/{session_id}/close`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `session_id`
    - `state`
  - `state` MUST equal `closed`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Submit Work

- Route: `POST /v1/agent-instances/{agent_instance_id}/submit-work`
- Request Body:
  - `input`
  - optional `session_id`
  - optional `references`
- Success:
  - fresh execution creation MUST return `201 Created`
  - idempotent replay of the same semantic request MUST return `200 OK`
  - the response body MUST include:
    - `execution_id`
    - `state`
    - optional `session_id`
    - optional `approval_ids`
  - if unresolved approval blocks progress before command completion, `state` MUST equal `blocked`
  - if unresolved approval blocks progress before command completion, `approval_ids` MUST be
    present and identify visible `pending` approvals created for the new `execution`
  - if no approval is created before command completion, `approval_ids` MUST be absent
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Execution List

- Route: `GET /v1/executions`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON array
  - every array item MUST include:
    - `execution_id`
    - `agent_instance_id`
    - `state`
  - if one listed execution has one visible parent, the listed item MAY include
    `parent_execution_id`
  - if one listed execution has one visible session, the listed item MAY include `session_id`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Cancel Execution

- Route: `POST /v1/executions/{execution_id}/cancel`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `execution_id`
    - `agent_instance_id`
    - `state`
  - `state` MUST equal `canceled`
  - if the canceled execution has one visible parent, the response MAY include `parent_execution_id`
  - if the canceled execution has one visible session, the response MAY include `session_id`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Approval

- Route: `GET /v1/approvals/{approval_id}`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `approval_id`
    - `state`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Approval List

- Route: `GET /v1/approvals`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON array
  - every array item MUST include:
    - `approval_id`
    - `state`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Resolve Approval

- Route: `POST /v1/approvals/{approval_id}/resolve`
- Request Body:
  - `decision`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `approval_id`
    - `state`
  - `state` MUST equal `approved` or `denied`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Delegate Execution

- Route: `POST /v1/executions/{execution_id}/delegate`
- Request Body:
  - `target_agent_instance_id`
  - `input`
  - optional `references`
- Success:
  - fresh child execution creation MUST return `201 Created`
  - idempotent replay of the same semantic request MUST return `200 OK`
  - the response body MUST include:
    - `execution_id`
    - `parent_execution_id`
    - `agent_instance_id`
    - `state`
    - optional `session_id`
    - optional `approval_ids`
  - `parent_execution_id` MUST equal the delegated parent execution identifier
  - if the parent execution has visible session membership, `session_id` MUST equal the parent
    session identifier
  - if unresolved approval blocks delegated child progress before command completion, `state` MUST
    equal `blocked`
  - if unresolved approval blocks delegated child progress before command completion,
    `approval_ids` MUST be present and identify visible pending approvals created for the child
    execution
  - if no approval is created before delegated command completion, `approval_ids` MUST be absent
- Failure:
  - visible terminal approval denial MUST return `403 Forbidden` with `error.code` equal to
    `approval_denied`
  - failure body MUST use the error envelope defined in `Transport Errors`

### Artifact

- Route: `GET /v1/artifacts/{artifact_id}`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `artifact_id`
    - `source_execution_id`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Artifact List

- Route: `GET /v1/artifacts`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON array
  - every array item MUST include:
    - `artifact_id`
    - `source_execution_id`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Tool Definition

- Route: `GET /v1/tools/{tool_id}`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `tool_id`
    - `state`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Tool Definition List

- Route: `GET /v1/tools`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON array
  - every array item MUST include:
    - `tool_id`
    - `state`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Invoke Tool

- Route: `POST /v1/executions/{execution_id}/tools/{tool_id}/invoke`
- Request Body:
  - `input`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `tool_id`
    - `outcome`
    - optional `approval_ids`
  - `outcome` MUST be one of `completed`, `failed`, or `blocked`
  - optional `result`
  - optional `artifact_ids`
  - if `outcome` is `blocked`, `result` MUST be absent
  - if `outcome` is `blocked`, `artifact_ids` MUST be absent
  - if unresolved approval blocks tool execution before visible command completion, `approval_ids`
    MUST be present and identify visible pending approvals created or attached for the invocation
  - if no visible approval is created or attached before command completion, `approval_ids` MUST be
    absent
  - `artifact_ids`, if present, MUST identify artifacts emitted by the invoking `execution` during
    the same accepted invocation
  - unresolved approval requirement MUST return `200 OK` with `outcome` equal to `blocked`
- Failure:
  - visible terminal approval denial MUST return `403 Forbidden` with `error.code` equal to
    `approval_denied`
  - failure body MUST use the error envelope defined in `Transport Errors`

### Context Snapshot

- Route: `GET /v1/executions/{execution_id}/context`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON `context snapshot`
  - the response body MUST use these members:
    - `execution_id`
    - `agent_instance_id`
    - optional `session_id`
    - `explicit_input`
    - `explicit_references`
    - optional `session_material`
    - optional `inherited_lineage_material`
    - optional `tool_derived_material`
    - optional `event_derived_material`
    - optional `implementation_supplied`
  - optional members omitted by the implementation MUST be absent
  - `explicit_references` MUST NOT be flattened into `explicit_input`
  - `inherited_lineage_material` MUST NOT be relabeled as `session_material`
  - `tool_derived_material` MUST NOT be relabeled as `implementation_supplied`
  - `event_derived_material` MUST NOT be relabeled as `implementation_supplied`
  - `implementation_supplied` MUST NOT be relabeled as caller input
  - independently recomputed child-boundary implementation-supplied material, if exposed, MUST
    appear only in `implementation_supplied`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Execution Snapshot

- Route: `GET /v1/executions/{execution_id}`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON `execution snapshot`
  - the response body MUST use these members:
    - `execution_id`
    - `state`
    - `agent_instance_id`
    - optional `parent_execution_id`
    - optional `session_id`
    - `context`
    - optional `approvals`
    - optional `available_tools`
    - optional `artifacts`
    - optional `recent_events`
  - `context` MUST satisfy the `context snapshot` shape
  - optional members omitted by the implementation MUST be absent
  - `approvals`, `available_tools`, `artifacts`, and `recent_events` MUST NOT be embedded within
    `context`
  - visible `failed` or `canceled` execution state MUST still return `200 OK`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Channel Adapter

- Route: `GET /v1/channel-adapters/{channel_adapter_id}`
- Success:
  - success MUST return `200 OK`
  - the response body MUST include:
    - `channel_adapter_id`
    - `channel_kind`
  - optional `health`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Ingress Message Acceptance

- Route: `POST /v1/channel-adapters/{channel_adapter_id}/ingress-messages`
- Request Body:
  - a JSON `ingress message`
  - request `channel_adapter_id` MUST equal the path `channel_adapter_id`
- Success:
  - successful acceptance MUST return `202 Accepted`
  - the response body MUST include:
    - `channel_adapter_id`
    - `channel_kind`
    - `message_id`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Ingress Message Inspection

- Route: `GET /v1/channel-adapters/{channel_adapter_id}/ingress-messages/{message_id}`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON `ingress message`
  - response `channel_adapter_id` MUST equal the path `channel_adapter_id`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Delivery Request

- Route: `POST /v1/channel-adapters/{channel_adapter_id}/delivery-requests`
- Request Body:
  - a JSON `delivery request`
  - request `channel_adapter_id` MUST equal the path `channel_adapter_id`
- Success:
  - if no visible `delivery result` is available at command completion, success MUST return
    `202 Accepted`
  - if a visible `delivery result` is available at command completion, success MUST return
    `200 OK`
  - a `202 Accepted` response body MUST include:
    - `delivery_request_id`
    - `channel_adapter_id`
    - `channel_kind`
  - a `200 OK` response body MUST be a JSON `delivery result`
  - when proactive delivery is exposed, absence of `in_reply_to_message_id` MUST NOT by itself
    cause failure
  - if the request is proactive rather than reply-driven, `in_reply_to_message_id` MAY be absent
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Delivery Result

- Route: `GET /v1/channel-adapters/{channel_adapter_id}/delivery-results/{delivery_request_id}`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON `delivery result`
  - response `channel_adapter_id` MUST equal the path `channel_adapter_id`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Status Delivery Inspection

- if `status delivery` is exposed over HTTP, the route MUST be
  `GET /v1/channel-adapters/{channel_adapter_id}/delivery-requests/{delivery_request_id}/status-deliveries`
- Success:
  - success MUST return `200 OK`
  - the response body MUST be a JSON array of canonical `status delivery`
  - every array item MUST include:
    - `delivery_request_id`
    - `channel_adapter_id`
    - `channel_kind`
    - `status`
    - `emitted_at`
  - every array item `delivery_request_id` MUST equal the path `delivery_request_id`
  - every array item `channel_adapter_id` MUST equal the path `channel_adapter_id`
- Failure:
  - failure body MUST use the error envelope defined in `Transport Errors`

### Channel Envelopes

- when HTTP exposes `ingress message`, `delivery request`, or `delivery result`, the JSON body MUST
  preserve the member names defined in `channels-v1.md`
- when HTTP exposes `status delivery`, the JSON body MUST preserve the member names defined in
  `channels-v1.md`
- HTTP MUST NOT rename `reply_target` to a thread field
- HTTP MUST NOT rename `thread_reference` to a reply-routing field
- HTTP MUST NOT replace `channel_kind` with a closed protocol enum

## Transport Errors

HTTP transport errors MUST use this envelope:

- `error`
  - `code`

HTTP status mapping:

- `not_found` -> `404 Not Found`
- `invalid_state` -> `409 Conflict`
- `capability_denied` -> `403 Forbidden`
- `approval_denied` -> `403 Forbidden`
- `idempotency_conflict` -> `409 Conflict`

Binding rules:

- `error.code` MUST equal the protocol-law error class.
- the binding MUST NOT map two different protocol-law error classes to the same `error.code`.

## Versioning / Negotiation

- HTTP versioning MUST use the `/v1` path prefix.
- `HTTP Binding v1` defines no additional content-negotiation mechanism.

## Conformance Hooks

HTTP conformance vectors are defined in `conformance-v1.md`.

Seed HTTP vectors:

- `../conformance/v1/vectors/agent-definition-listing-includes-visible-definition.md`
- `../conformance/v1/vectors/agent-definition-inspection-exposes-state.md`
- `../conformance/v1/vectors/disable-agent-definition-transitions-to-disabled.md`
- `../conformance/v1/vectors/enable-agent-definition-transitions-to-enabled.md`
- `../conformance/v1/vectors/agent-instance-listing-includes-visible-instance.md`
- `../conformance/v1/vectors/agent-instance-inspection-exposes-definition-link-and-state.md`
- `../conformance/v1/vectors/pause-agent-instance-transitions-to-paused.md`
- `../conformance/v1/vectors/resume-agent-instance-transitions-to-ready.md`
- `../conformance/v1/vectors/terminate-agent-instance-transitions-to-terminated.md`
- `../conformance/v1/vectors/session-listing-includes-visible-session.md`
- `../conformance/v1/vectors/session-inspection-exposes-state.md`
- `../conformance/v1/vectors/close-session-transitions-to-closed.md`
- `../conformance/v1/vectors/submit-work-success.md`
- `../conformance/v1/vectors/execution-listing-includes-visible-execution.md`
- `../conformance/v1/vectors/cancel-execution-transitions-to-canceled.md`
- `../conformance/v1/vectors/cancel-execution-rejected-when-already-terminal.md`
- `../conformance/v1/vectors/submit-work-rejected-when-instance-paused.md`
- `../conformance/v1/vectors/submit-work-blocked-when-approval-required.md`
- `../conformance/v1/vectors/approval-listing-includes-visible-approval.md`
- `../conformance/v1/vectors/resolve-approval-approves-pending-approval.md`
- `../conformance/v1/vectors/resolve-approval-rejected-when-already-resolved.md`
- `../conformance/v1/vectors/delegate-execution-success.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-parent-missing.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-parent-terminal.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-target-instance-missing.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-target-instance-not-ready.md`
- `../conformance/v1/vectors/delegate-execution-rejected-when-target-instance-equals-parent-owner.md`
- `../conformance/v1/vectors/delegate-execution-idempotent-replay-preserves-child.md`
- `../conformance/v1/vectors/delegate-execution-terminal-approval-denial-returns-approval-denied.md`
- `../conformance/v1/vectors/tool-definition-listing-includes-visible-tool.md`
- `../conformance/v1/vectors/tool-definition-inspection-exposes-state.md`
- `../conformance/v1/vectors/missing-tool-definition-inspection-returns-not-found.md`
- `../conformance/v1/vectors/invoke-tool-success.md`
- `../conformance/v1/vectors/invoke-tool-rejected-when-tool-disabled.md`
- `../conformance/v1/vectors/invoke-tool-rejected-when-tool-deleted.md`
- `../conformance/v1/vectors/invoke-tool-denied-by-capability.md`
- `../conformance/v1/vectors/invoke-tool-blocked-when-approval-required.md`
- `../conformance/v1/vectors/invoke-tool-terminal-approval-denial-returns-approval-denied.md`
- `../conformance/v1/vectors/invoke-tool-idempotent-replay-preserves-result.md`
- `../conformance/v1/vectors/artifact-listing-includes-visible-artifact.md`
- `../conformance/v1/vectors/artifact-record-preserves-provenance.md`
- `../conformance/v1/vectors/missing-execution-inspection-returns-not-found.md`
- `../conformance/v1/vectors/failed-execution-inspection-is-not-transport-error.md`
- `../conformance/v1/vectors/context-snapshot-preserves-provenance.md`
- `../conformance/v1/vectors/context-snapshot-omits-absent-contribution-sections.md`
- `../conformance/v1/vectors/inherited-lineage-material-visible-on-child-execution.md`
- `../conformance/v1/vectors/session-material-visible-on-session-attached-execution.md`
- `../conformance/v1/vectors/tool-derived-material-visible-when-exposed.md`
- `../conformance/v1/vectors/event-derived-material-visible-when-exposed.md`
- `../conformance/v1/vectors/execution-snapshot-separates-sections.md`
- `../conformance/v1/vectors/open-channel-kind-accepted.md`
- `../conformance/v1/vectors/ingress-message-preserves-routing-and-trace-fields.md`
- `../conformance/v1/vectors/delivery-request-preserves-routing-and-trace-fields.md`
- `../conformance/v1/vectors/delivery-result-reports-outcome-and-request-linkage.md`
- `../conformance/v1/vectors/status-delivery-inspection-preserves-request-linkage.md`
- `../conformance/v1/vectors/proactive-delivery-without-prior-ingress.md`
