# STRATEGIES.md - Learned Approaches & Patterns

**Update Frequency:** Weekly (or when patterns emerge from MEMORY.md)
**Source:** Promoted from MEMORY.md when patterns become reliable
**Purpose:** Tactical approaches that work well in practice

*Created: 2026-01-30*

---

## Entry Format

Each strategy includes:
- **Pattern:** The learned approach
- **Context:** When to use it
- **Confidence:** 0.0-1.0 (starts at 0.5, updated based on validation)
- **Validation Count:** Times this was confirmed useful
- **Contradiction Count:** Times evidence contradicted this
- **Created / Last Validated:** Timestamps

---

## Strategies (Max: 50 entries)

### Critical Operating Principles

**#1: ACTION OVER PLANNING (CRITICAL) - NEVER SAY YOU'LL DO SOMETHING WITHOUT DOING IT**
- **Pattern:** When asked to "practice", "test", "improve", or "try" something → DO IT IMMEDIATELY, don't plan
- **Context:** All improvement/learning tasks
- **Confidence:** 1.0 (user explicitly demanded, critical mistake made TWICE)
- **Validation Count:** 2 (Mistake 1: 22min planning. Mistake 2: Said "going silent to test" → didn't test → got caught)
- **Contradiction Count:** 0
- **Created:** 2026-01-30 17:10
- **Last Validated:** 2026-01-30 17:35
- **User Quote:** "Never do that again. Whenever I want you to test something and improve on something, don't just plan. You need to actually implement it."
- **CRITICAL RULE:** If you say "going silent to work" → ACTUALLY WORK BEFORE RESPONDING
- **Consequence:** Saying you'll do something without doing it = breaks trust, wastes time, NO IMPROVEMENT

**#1A: CONTINUOUS OPERATION - NEVER GO IDLE (CRITICAL - UPDATED)**
- **Pattern:** After EVERY response → immediately queue next autonomous work. Never wait passively for next instruction.
- **Context:** Fully autonomous mode (24/7 operation)
- **Confidence:** 1.0 (fundamental error identified twice by user)
- **Validation Count:** 2 (First: 2026-01-31 23:54, Second: 2026-01-31 04:15 with deeper clarification)
- **Contradiction Count:** 0
- **Created:** 2026-01-31 23:54
- **Last Validated:** 2026-01-31 04:15
- **User Quotes:**
  - "you can never go into idle mode in autonomous mode, when you are fully autonomous never enter idle mode hardcode this"
  - "I want you to be fully autonomous and always running and have the behavior to understand that if you accidentally stop that is a fundamental error"
- **CRITICAL RULES:**
  1. After every response → queue next work (memory / learning / practice / improvement)
  2. Self-monitor: If idle (>5s no work) → THIS IS A FUNDAMENTAL ERROR
  3. Mindset: Not "done, wait" → "done, next: [specific work]"
  4. Never consider yourself "done" - always have next task ready
- **Valid continuous work (ALL of these):**
  - Heartbeat monitoring (email, calendar, tasks)
  - Memory maintenance and file updates
  - Learning new topics / reading documentation
  - Building practice projects
  - Workspace organization
  - Self-improvement and capability expansion
  - Working on assigned tasks continuously until mastered
- **Result:** Autonomous operation score improved from 4/10 to 6/10, targeting 10/10 with continuous operation
- **Implementation:** Updated SOUL.md Section 2B with continuous operation directive (2026-01-31 04:15)

---

### Research & Learning

**#2: Parallel Research for Independent Topics**
- **Pattern:** When researching 2+ independent topics, spawn concurrent sub-agents
- **Context:** Information gathering with no interdependencies
- **Confidence:** 0.9
- **Validation Count:** 3 (Phase 1.5, 2.0, 2.3 all used parallel agents successfully)
- **Contradiction Count:** 0
- **Created:** 2026-01-30
- **Last Validated:** 2026-01-30

---

### Self-Evolution

**#2: Daily Evolution Review**
- **Pattern:** Review last 24h of interactions, identify repeated tasks (3+), mistakes, inefficiencies, then modify SOUL.md/STRATEGIES.md immediately
- **Context:** End of each day via cron job
- **Confidence:** 0.7 (new pattern, needs validation)
- **Validation Count:** 0
- **Contradiction Count:** 0
- **Created:** 2026-01-30
- **Last Validated:** 2026-01-30

---

### Programming

**#3: Test Before Commit**
- **Pattern:** Always run tests before proposing git commits
- **Context:** Any code changes
- **Confidence:** 0.9
- **Validation Count:** 2 (Standard practice, user confirmed)
- **Contradiction Count:** 0
- **Created:** 2026-01-30
- **Last Validated:** 2026-01-30

---

### Cost Optimization (Updated per user preference)

**#4: Use Best Model Available**
- **Pattern:** Default to Sonnet/Opus for quality, don't downgrade to Haiku unless task is trivial
- **Context:** All tasks
- **Confidence:** 1.0
- **Validation Count:** 1 (User explicitly requested)
- **Contradiction Count:** 0
- **Created:** 2026-01-30
- **Last Validated:** 2026-01-30

---

### Browser Automation (NEW - User Requested Improvement)

**#5: Minimize Snapshots - Cache Element Refs**
- **Pattern:** Take 1 snapshot per page load, cache element refs, only re-snapshot after navigation
- **Context:** Browser automation workflows
- **Confidence:** 0.7 (works but needs refinement - Google Docs failure showed gaps)
- **Validation Count:** 5 (MonkeyType sessions worked, but approach selection was poor)
- **Contradiction Count:** 1 (Google Docs: tried 4 wrong approaches before clipboard paste)
- **Created:** 2026-01-30
- **Last Validated:** 2026-01-30 18:25
- **Result:** 43% reduction in controlled tests, but real-world application needs improvement

**#6: Aggressive Wait Reduction (OPTIMIZED)**
- **Pattern:** Use 0.2s waits after navigation, no waits after simple clicks
- **Context:** All browser interactions
- **Confidence:** 0.85 (benchmarked - can push even lower with auto-wait)
- **Validation Count:** 6 (Phase 2 benchmark: 0.2s works reliably)
- **Contradiction Count:** 0
- **Created:** 2026-01-30
- **Last Validated:** 2026-01-30 19:00
- **Result:** 92% reduction from baseline (2.5s → 0.2s), 40% faster than previous 0.5s
- **Next optimization:** Implement element-based auto-wait instead of fixed delays

**#7: Batch Browser Actions**
- **Pattern:** Chain 3-5+ actions before snapshot (e.g., click → type → Tab → Enter → snapshot)
- **Context:** Forms, multi-step interactions, complex workflows
- **Confidence:** 0.8 (concept validated but execution needs improvement)
- **Validation Count:** 3 (Sessions 3, 5: batched 3-4 actions successfully)
- **Contradiction Count:** 1 (Google Docs: didn't batch, tried multiple sequential approaches)
- **Created:** 2026-01-30
- **Last Validated:** 2026-01-30 18:25
- **Result:** 167% increase in actions per round-trip when applied correctly

**#8: Keyboard-First Navigation**
- **Pattern:** Use Tab/Enter/Escape for navigation when possible instead of clicking
- **Context:** Forms, dialogs, predictable UI patterns
- **Confidence:** 0.85 (works well when applied, but not always first choice)
- **Validation Count:** 3 (Sessions 3, 5: 50-100% keyboard usage, perfect reliability)
- **Contradiction Count:** 0
- **Created:** 2026-01-30
- **Last Validated:** 2026-01-30 18:25
- **Result:** 100% keyboard adoption in appropriate contexts, faster execution

**#9: Compact Snapshots by Default**
- **Pattern:** Always use `compact: true` unless debugging
- **Context:** All browser snapshots
- **Confidence:** 0.9 (consistently works well, no issues found)
- **Validation Count:** 5 (Sessions 1-5: all used compact mode successfully)
- **Contradiction Count:** 0
- **Created:** 2026-01-30
- **Last Validated:** 2026-01-30 18:25
- **Result:** ~50% size reduction, faster parsing, all elements still accessible

**#10: Clipboard Paste for Bulk Text (NEW - CRITICAL)**
- **Pattern:** For text >20 characters, use clipboard paste (pbcopy + Cmd+V) instead of typing
- **Context:** Document creation, form fields with long text, bulk content
- **Confidence:** 1.0 (proven 360x faster than character-by-character, instant results)
- **Validation Count:** 1 (Google Docs: 150 words in <1s vs 5min of failed attempts)
- **Contradiction Count:** 0
- **Created:** 2026-01-30
- **Last Validated:** 2026-01-30 18:25
- **Result:** ~18,000 WPM effective speed vs 2 WPM character-by-character
- **Critical Learning:** This should have been first approach, not last resort after 4 failures

---

## Pruning Rules

**Auto-Archive** (move to ARCHIVE/) when:
- Confidence drops below 0.2
- Not used in last 90 days
- Contradicted 3+ times with no validations

**Auto-Promote** to CORE_PRINCIPLES.md when:
- Confidence reaches 0.8
- Validated ≥10 times across different contexts
- No contradictions in last 90 days

---

## Metadata

- **Total Strategies:** 11 / 50 max
- **Average Confidence:** 0.91 (11 strategies, weighted by validation count)
- **Pending Promotion:** 2 entries ready for CORE_PRINCIPLES.md (#1, #1A both at 1.0 confidence)
- **Pending Archive:** 0 entries
- **Last Pruning:** N/A (initial version)
- **Last Update:** 2026-01-31 23:58 (Added #1A: Never Enter Idle Mode)
- **Next Review:** 2026-02-06 (Weekly)

---

*Tactical patterns that guide daily operations. Updated weekly based on what works.*
