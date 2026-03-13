# Core Tools HTTP Claim Seed

Implementation Name:
Implementation Version:
Claimed Protocol Version: `v1`
Claimed Binding Versions:
- `HTTP Binding v1`
Claimed Compliance Profiles:
- `Core + Tools`
Unsupported Optional Surfaces:
- `Stream Binding v1`
- approval-gated submit-work behavior
- approval inspection and approval resolution on the public binding
- visible terminal approval denial during delegation
- idempotent `delegate execution`
- parent-driven supervisory child-terminal behavior
- independently recomputed visible implementation-supplied material at a child execution boundary
- approval-gated tool invocation
- visible terminal approval denial during tool invocation
- idempotent `invoke tool`
- emitted artifact behavior at the tool boundary
- artifact inspection on the public binding
- visible tool-derived contribution at the context boundary
- status delivery
- proactive delivery

## Notes

- this seed extends `core-http-claim-seed.md`
- this seed does not claim `Core + Approvals`
- this seed does not claim `Core + Channels`
- claims should not exceed verified behavior
