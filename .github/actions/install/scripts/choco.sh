#!/bin/bash
set -o errexit -o nounset -o pipefail

choco install "$@"
