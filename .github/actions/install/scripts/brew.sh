#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

brew update
brew install "$@"
