#!/bin/bash
set -o errexit -o nounset -o pipefail

cd ~/.local/bin
curl https://zyedidia.github.io/eget.sh | sh
for target in "$@"; do
  case "$target" in
    liblaf/pre-commit-hooks) ./eget --to="pch" "$target" ;;
    *) ./eget "$target" ;;
  esac
done
