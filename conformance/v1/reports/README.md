# Reports

Each report should record:

- implementation claim under test
- runner identity
- run date
- vectors executed
- traces executed
- pass or fail result for each artifact
- overall pass or fail result

Reports should be reproducible from the listed artifacts and bindings.

Standalone external runner:

- `scripts/run-core-http-claim.py`

Example:

```bash
python3 scripts/run-core-http-claim.py \
  --base-url http://127.0.0.1:4747 \
  --implementation-name starla-rs \
  --implementation-version d8dfccc \
  --runner-identity scripts/run-core-http-claim.py \
  --output conformance/v1/reports/starla-rs-core-http-2026-03-13.md
```

Seed artifact:

- `report-template.md`
- `core-http-report-seed.md`
- `core-tools-http-report-seed.md`

First seeded target:

- `Core` over `HTTP Binding v1`

Next seeded target:

- `Core + Tools` over `HTTP Binding v1`

Recorded reports:

- `starla-rs-core-http-2026-03-13.md`
- `starla-ex-core-http-2026-03-13.md`
