#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

fail=0

error() {
  printf 'lint: %s\n' "$*" >&2
  fail=1
}

require_file() {
  local path="$1"
  [[ -f "$path" ]] || error "missing file: $path"
}

require_pattern() {
  local path="$1"
  local pattern="$2"
  local label="$3"
  rg -q "$pattern" "$path" || error "$path missing $label"
}

for path in \
  AGENTS.md \
  CHARTER.md \
  CONFORMANCE_SYSTEM.md \
  CONTRIBUTING.md \
  README.md \
  SPEC_METHOD.md \
  SPEC_REVIEW_CHECKLIST.md \
  STATUS.md \
  VOCABULARY.md \
  .github/pull_request_template.md \
  .github/workflows/docs-lint.yml \
  scripts/lint-docs.sh
do
  require_file "$path"
done

for path in drafts/*.md; do
  require_pattern "$path" '^# ' 'title'
  require_pattern "$path" '^State: ' 'State header'
  require_pattern "$path" '^Kind: ' 'Kind header'
  require_pattern "$path" '^Version: ' 'Version header'
  require_pattern "$path" '^Last Updated: ' 'Last Updated header'
  require_pattern "$path" '^Draft Notice:' 'Draft Notice header'
done

forbidden_paths=(
  README.md
  CHARTER.md
  CONFORMANCE_SYSTEM.md
  SPEC_METHOD.md
  STATUS.md
  drafts
  conformance
)

check_forbidden() {
  local pattern="$1"
  local label="$2"
  if rg -n "$pattern" "${forbidden_paths[@]}" >/tmp/starla-lint-match.$$ 2>/dev/null; then
    error "forbidden term: $label"
    cat /tmp/starla-lint-match.$$ >&2
  fi
  rm -f /tmp/starla-lint-match.$$
}

check_forbidden 'Harness Core|harness core' 'Harness Core'
check_forbidden 'context dump' 'context dump'
check_forbidden '`Agent`|struct Agent|class Agent|interface Agent' 'bare or language-specific Agent abstraction'
check_forbidden '0001-starla-protocol-core-v1\.md|0002-http-binding-v1\.md|0003-stream-binding-v1\.md|0004-conformance-v1\.md|_index\.md' 'stale internal filenames'

if (( fail != 0 )); then
  exit 1
fi

printf 'lint: ok\n'
