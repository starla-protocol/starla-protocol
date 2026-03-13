# Traces

Each trace should identify:

- profile
- scenario name
- triggering requests or commands
- required event order
- terminal condition
- forbidden reordered or missing events

Traces verify observable sequencing, not internal implementation steps.

A trace MAY be conditional when the corresponding optional surface is claimed or observed.

Seed traces in this directory:

- `execution-completion-terminal.md`
- `execution-cancel-terminal.md`
- `execution-lifecycle-minimal.md`
- `execution-failure-terminal.md`
- `approval-gated-submit-work.md`
- `approval-resolution-terminal.md`
- `delegated-execution-minimal.md`
- `delegated-execution-blocked-when-approval-required.md`
- `delegated-blocked-child-terminal-after-supervisory-parent-stop.md`
- `tool-invocation-with-artifact.md`
- `tool-invocation-blocked-when-approval-required.md`
- `delegated-child-terminal-after-supervisory-parent-stop.md`
- `delivery-request-accepted-before-final-result.md`
- `proactive-delivery-accepted-before-final-result.md`
- `proactive-status-delivery-precedes-final-result.md`
- `status-delivery-precedes-final-delivery-result.md`
