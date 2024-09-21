#!/bin/bash
set -o errexit -o nounset -o pipefail

if [[ ! ":$PATH:" =~ ~/.local/bin: ]]; then
  case "$RUNNER_OS" in
    Linux | macOS) echo ~/.local/bin >> "$GITHUB_PATH" ;;
    Windows) cygpath --windows ~/.local/bin >> "$GITHUB_PATH" ;;
  esac
fi
