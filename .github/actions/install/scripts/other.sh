#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

for pkg in "$@"; do
  bash "$script_dir/other/$pkg.sh"
done
