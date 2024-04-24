#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

prefix=${1:-"$HOME/github"}

readarray -t repos < <(
  gh repo list \
    --jq ".[].nameWithOwner" \
    --json "nameWithOwner" \
    --limit 1000 \
    --no-archived \
    --source
)

for repo in "${repos[@]}"; do
  case "$repo" in
    */dotfiles) target=$HOME/.local/share/chezmoi ;;
    *) target=$prefix/$repo ;;
  esac
  if [[ -d "$target/.git" ]]; then
    git -C "$target" pull &
  else
    gh repo clone "$repo" "$target" &
  fi
done

wait
