#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

sums=${ALGORITHM}s.txt

for file in $FILES; do
  if [[ -f $file ]]; then
    files+=("$file")
  else
    echo "::warning file=${BASH_SOURCE[0]},line=$LINENO::File not found: $file"
  fi
done

if gh release view "$TAG" --repo "$REPO" &> /dev/null; then
  if [[ -n $FILES ]]; then
    tmpfile=$(mktemp --suffix=".txt")
    trap 'rm --force "$tmpfile"' EXIT
    gh release download "$TAG" --output "$tmpfile" --pattern "$sums" --repo "$REPO" || true
    "$ALGORITHM" "${files[@]}" > "$sums"
    sed --regexp-extended --expression="s|([[:xdigit:]]+)([[:blank:]])+.*/([^/]+)|\1\2\3|" --in-place "$sums"
    if diff --report-identical-files "$tmpfile" "$sums"; then
      exit 0
    fi
  fi
  if $RECREATE; then
    gh release delete "$TAG" --cleanup-tag --repo "$REPO"
    echo "::notice file=${BASH_SOURCE[0]},line=$LINENO::Delete GitHub Release: $TAG"
    exists=false
  else
    exists=true
  fi
else
  exists=false
fi

args=(gh release --repo "$REPO")
if $exists; then
  args+=(upload --clobber)
else
  args+=(create --generate-notes --title "$TAG")
  if $PRERELEASE; then
    args+=(--prerelease)
  fi
fi
args+=("$TAG")
args+=("${files[@]}")
if [[ -f $sums ]]; then
  args+=("$sums")
fi
set -o xtrace
"${args[@]}"
set +o xtrace
echo "::notice file=${BASH_SOURCE[0]},line=$LINENO::Create GitHub Release: $TAG"
