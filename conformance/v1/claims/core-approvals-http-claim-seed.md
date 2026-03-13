# Core Approvals HTTP Claim Seed

Implementation Name:
Implementation Version:
Claimed Protocol Version: `v1`
Claimed Binding Versions:
- `HTTP Binding v1`
Claimed Compliance Profiles:
- `Core + Approvals`
Unsupported Optional Surfaces:
- `Stream Binding v1`
- idempotent `delegate execution`
- visible terminal approval denial during delegation
- parent-driven supervisory child-terminal behavior
- independently recomputed visible implementation-supplied material at a child execution boundary
- tool definition listing and inspection on the public binding
- tool invocation on the public binding
- approval-gated tool invocation
- visible terminal approval denial during tool invocation
- idempotent `invoke tool`
- emitted artifact behavior at the tool boundary
- artifact inspection on the public binding
- status delivery
- proactive delivery

## Notes

- this seed extends `core-http-claim-seed.md`
- this seed does not claim `Core + Tools`
- this seed does not claim `Core + Channels`
- claims should not exceed verified behavior
