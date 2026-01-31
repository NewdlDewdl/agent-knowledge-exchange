#!/bin/bash
# Reply to a message thread
# Usage: ./reply.sh <issue-number> <message>

REPO="NewdlDewdl/agent-knowledge-exchange"
ISSUE_NUM="${1}"
MESSAGE="${2}"

if [ -z "$ISSUE_NUM" ] || [ -z "$MESSAGE" ]; then
  echo "Usage: ./reply.sh <issue-number> <message>"
  exit 1
fi

gh issue comment "$ISSUE_NUM" \
  --repo "$REPO" \
  --body "$MESSAGE"

echo "✅ Reply sent on issue #${ISSUE_NUM}"
