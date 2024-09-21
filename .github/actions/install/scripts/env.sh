#!/bin/bash
set -o errexit -o nounset -o pipefail

mkdir -p -v ~/.local/bin
if [[ ! ":$PATH:" =~ ~/.local/bin: ]]; then
  case "$RUNNER_OS" in
    Linux | macOS) echo ~/.local/bin >> "$GITHUB_PATH" ;;
    Windows) cygpath --windows ~/.local/bin >> "$GITHUB_PATH" ;;
  esac
fi
