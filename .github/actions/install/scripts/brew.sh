#!/bin/bash
set -o errexit -o nounset -o pipefail

brew update
brew install "$@"

for pkg in "$@"; do
  case "$pkg" in
    coreutils | make | gnu-*)
      gnubin=$(brew --prefix)/opt/$pkg/libexec/gnubin
      PATH=$gnubin:$PATH
      echo "$gnubin" >> "$GITHUB_PATH"
      ;;
  esac
done
