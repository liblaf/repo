#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

repo=$1

if [[ -n ${GH_TOKEN-} ]]; then
  gh secret set GH_TOKEN --body "$GH_TOKEN" --repo "$repo"
fi

# https://docs.github.com/en/rest/actions/permissions#set-default-workflow-permissions-for-a-repository
gh api "repos/$repo/actions/permissions/workflow" \
  --field "default_workflow_permissions"="read" \
  --field "can_approve_pull_request_reviews"=true \
  --method PUT
