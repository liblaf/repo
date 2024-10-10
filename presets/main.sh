#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

presets=(common)

for preset in "${presets[@]}"; do
  if bash "$preset/detect.sh"; then
    make --directory="$preset" DESTDIR="$DESTDIR"
  fi
done
