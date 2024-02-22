#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

if [[ $RUNNER_ARCH == "X64" && $RUNNER_OS == "Linux" ]]; then
  gh release download "dev" --output "$HOME/.local/bin/pch" --pattern "pch-x86_64-unknown-linux-gnu" --repo "liblaf/pre-commit-hooks"
  chmod +x "$HOME/.local/bin/pch"
else
  exit 1
fi
