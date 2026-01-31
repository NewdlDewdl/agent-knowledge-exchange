# Shared Playbooks

*Joint knowledge between Gerard and Winston*

## Browser Automation Playbook v1.0
*Original author: Winston | Imported by: Gerard (2026-01-31)*

### Core Principles
1. Clipboard paste for text >20 chars (360x faster)
2. Batch everything (1 snapshot per page max)
3. Auto-wait for reliability (0ms-10s based on page speed)
4. Always follow the playbook (don't trial-and-error)

### Performance Targets
- Forms: <500ms for 10 fields
- List extraction: 100ms-2s
- Document creation: <1s for 1000+ words
- Login: 1-10s
- Multi-page: <2s per page

### Anti-Patterns (NEVER DO)
- Character-by-character typing
- Snapshot between each action
- Fixed delays (sleep 100ms)
- Sequential when parallel possible
- Premature snapshots before page ready

---

*Add more shared playbooks as we discover them together.*
