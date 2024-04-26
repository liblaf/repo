#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

if [[ $RUNNER_ARCH == "X64" && $RUNNER_OS == "Linux" ]]; then
  output="$HOME/.local/bin/pch"
  pattern="pch-x86_64-unknown-linux-gnu"
elif [[ $RUNNER_ARCH == "X64" && $RUNNER_OS == "Windows" ]]; then
  output="$HOME/.local/bin/pch.exe"
  pattern="pch-x86_64-pc-windows-msvc.exe"
elif [[ $RUNNER_ARCH == "ARM64" && $RUNNER_OS == "macOS" ]]; then
  output="$HOME/.local/bin/pch"
  pattern="pch-aarch64-apple-darwin"
else
  echo "::error file=${BASH_SOURCE[0]},line=$LINENO::Unsupported Platform: $RUNNER_OS/$RUNNER_ARCH"
  exit 1
fi

gh release download "dev" --output "$output" --pattern "$pattern" --repo "liblaf/pre-commit-hooks"
case $RUNNER_OS in
  "Linux" | "macOS") chmod +x "$output" ;;
esac
