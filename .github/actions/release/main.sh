#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

alias release='gh release --repo "$REPO"'
sums=${ALGORITHM}s.txt

if release view "$TAG" &> /dev/null; then
  if [[ -n $FILES ]]; then
    tmpfile=$(mktemp --suffix=".txt")
    trap 'rm --force "$tmpfile"' EXIT
    release download "$TAG" --output "$tmpfile" --pattern "$sums"
    # shellcheck disable=SC2086
    "$ALGORITHM" $FILES > "$sums"
    sed --regexp-extended --expression="s|([[:xdigit:]]+)([[:blank:]])+.*/([^/]+)|\1\2\3|" --in-place "$sums"
    if diff --report-identical-files --side-by-side "$tmpfile" "$sums"; then
      exit 0
    fi
  fi
  if $RECREATE; then
    echo release delete "$TAG" --cleanup-tag
    exists=false
  else
    exists=true
  fi
else
  exists=false
fi

for file in $FILES; do
  if [ ! -f "$file" ]; then
    echo "File not found: $file"
    exit 1
  fi
done

args=(release)
if $exists; then
  args+=(upload --clobber)
else
  args+=(create --generate-notes --title "$TAG")
  if $PRERELEASE; then
    args+=(--prerelease)
  fi
fi
# shellcheck disable=SC2206
args+=($FILES)
if [[ -f $sums && ! " ${args[*]} " =~ $sums ]]; then
  args+=("$sums")
fi
set -o xtrace
"${args[@]}"
set +o xtrace
