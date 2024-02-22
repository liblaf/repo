#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

readarray -t repos < <(
  gh repo list \
    --jq ".[].nameWithOwner" \
    --json "nameWithOwner" \
    --limit 1000 \
    --no-archived \
    --source \
    --visibility public
)

function _sync() {
  repo=$1
  gh repo clone "$repo" "$repo" -- --depth 1
  make --always-make DEST_DIR="$(realpath "$repo")"
  git -C "$repo" add --all
  if git -C "$repo" diff --cached --exit-code; then
    echo "[$repo] already up to date"
  else
    git -C "$repo" commit \
      --author="github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>" \
      --message="ci(repo): sync with template"
    git -C "$repo" push
  fi
}

for repo in "${repos[@]}"; do
  _sync "$repo" &
done

while
  wait -fn || exitcode=$?
  ((exitcode != 127))
do
  if ((exitcode)); then
    exit "$exitcode"
  fi
done
