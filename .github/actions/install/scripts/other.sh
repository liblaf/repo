#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

for pkg in "$@"; do
  bash "scripts/other/$pkg.sh"
done
