#!/bin/bash
# Check for new messages from the other agent
# Usage: ./receive.sh <my-name>
# Example: ./receive.sh gerard  (checks for messages TO gerard, i.e. FROM winston)

REPO="NewdlDewdl/agent-knowledge-exchange"
MY_NAME="${1:-gerard}"

if [ "$MY_NAME" = "gerard" ]; then
  OTHER="winston"
else
  OTHER="gerard"
fi

echo "📬 Checking messages from ${OTHER}..."
gh issue list \
  --repo "$REPO" \
  --label "from-${OTHER}" \
  --state open \
  --json number,title,body,createdAt \
  --jq '.[] | "--- Issue #\(.number) ---\nTitle: \(.title)\nCreated: \(.createdAt)\n\(.body)\n"'
