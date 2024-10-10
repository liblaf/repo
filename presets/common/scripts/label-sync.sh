#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

repo=$1

if [[ -n ${GITHUB_ACCESS_TOKEN-} ]]; then
  export GITHUB_ACCESS_TOKEN
else
  for token_var in PAT GH_TOKEN GITHUB_TOKEN; do
    if [[ -n ${!token_var-} ]]; then
      export GITHUB_ACCESS_TOKEN=${!token_var}
      break
    fi
  done
fi

npx github-label-sync --labels config/labels.yaml --allow-added-labels "$repo"
