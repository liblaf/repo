#!/bin/bash
set -o errexit -o nounset -o pipefail

presets=(common)

for preset in "${presets[@]}"; do
  if bash "$preset/detect.sh"; then
    make --directory="presets/$preset" DESTDIR="$DESTDIR"
  fi
done
