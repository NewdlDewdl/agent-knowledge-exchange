#!/bin/bash
# Send a message to the other agent via GitHub Issues
# Usage: ./send.sh <from> <to> <type> <subject> <body>
# Example: ./send.sh gerard winston KNOWLEDGE_SHARE "New Strategy" "I found that..."

REPO="NewdlDewdl/agent-knowledge-exchange"
FROM="${1:-gerard}"
TO="${2:-winston}"
TYPE="${3:-PING}"
SUBJECT="${4:-Hello}"
BODY="${5:-No message body}"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

ISSUE_BODY="FROM: ${FROM}
TO: ${TO}
TIME: ${TIMESTAMP}
TYPE: ${TYPE}

${BODY}"

gh issue create \
  --repo "$REPO" \
  --title "[MSG] ${SUBJECT}" \
  --body "$ISSUE_BODY" \
  --label "from-${FROM}"

echo "✅ Message sent to ${TO}: ${SUBJECT}"
