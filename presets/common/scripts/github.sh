#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

repo=$1

# https://docs.github.com/en/rest/actions/permissions#set-default-workflow-permissions-for-a-repository
gh api "/repos/$repo/actions/permissions/workflow" \
  --field default_workflow_permissions=read \
  --field can_approve_pull_request_reviews=true \
  --method PUT

# https://docs.github.com/en/rest/branches/branch-protection#update-branch-protection
gh api "/repos/$repo/branches/main/protection" \
  --input config/protection.json \
  --method PUT
