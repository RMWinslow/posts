---
title: "Advisory Conflict Signals for AI-Assisted Version Control"
layout: post
date: 2026-04-04
parent: Numbers
nav_exclude: true
---

# Advisory Conflict Signals for AI-Assisted Version Control

*Idea thread from 2026-04-04, developed in conversation with Claude.
Inspired by [a post from @jonallie](https://x.com/jonallie) about needing a
better version control paradigm for AI-assisted coding.*

## The Conversation

**Me:** Why not just maintain an index file with a list of files in the repo. Each has a flag. Automatic action to change the flag to indicate which files are being worked on in a pull request. When you submit the pull request, you revert the "checkout" flags on those files. Other collaborators do frequent pulls and don't edit files that are flagged as checked out on another machine. You'd have merge conflicts for the index file, but if file has a fixed line, and new files are appended to the end, it seems like the merge conflicts would be pretty easy to automatically resolve. Criticize this idea. Identify any flaws with it...

**Claude:** [Critique of v1 — see analysis below]

**Me:** Okay. But there's an issue with real time merges he mentions, leading to a messy history. What about a second, shadow repo? Every file in the main repo has an associated text document in the shadow repo. Only large chunky changes are made in the main repo. In the shadow repo, you only ever create new shadow files or append a time-stamped message to an existing file. ("Bob checked out this file at 2pm, high priority.", "Bob unchecked the file.", "Bob is refactoring this file without making stylistic changes."). No firmly enforced checkouts, but the shadow file is frequently and automatically pushed and pulled, and the AI agents are instructed to check recent messages to see if there's a potential conflict. ("Oh, Alice and Bob both made a claim of this file an hour ago and neither has returned it". We can push, but it might result in merge conflicts.") Purely just a freeform kind of notice that can be overridden if need be. A reliable forecaster of potential merge conflicts rather than a hard blocker of them.

**Claude:** [Critique of v2 — see analysis below]

**Me:** Third version: Have synchronized logs outside of the repo with timestamped messages about intent to modify files. Instruct the AI agents to occasionally check the messages from other agents and think about if there might be conflicts.

**Claude:** [Critique of v3 — see analysis below]

**Me:** Well, the freeform nature of AI means you can respond with what you want to do. A more sophisticated system could have a second agent which gets every new message injected into its context and then decides whether to pass it on as a concern to the main agent.

**Claude:** [Discussion of v3.1 watcher agent — see analysis below]

**Me:** Going back to the original tweet... why not both? One auto-synced repo ala google docs which ends up with a messy history that's constantly monitored by the watcher, and then the main one which has chunked batch changes.

**Claude:** [Discussion of v4 — see analysis below]

**Me:** "Or just have the agents talk to each other on slack, I guess..."

---

## The Problem

AI coding agents are fast on solo/greenfield projects, but collaboration breaks
down. Either everyone exchanges huge PRs (abandoning code review, dealing with
gnarly merge conflicts) or you stick to traditional flows with reasonably sized
changes, spending a lot of time waiting for changes to land.

Old version control systems (Perforce, SVN) had file-level "checkout" locks.
Painful, but they provided a useful signal: someone is working in this area.
Git threw that signal away along with the pain. Maybe the signal still has value.

## Version 1: Checkout Index File

Maintain an index file in the repo. Each file gets a line with a flag indicating
whether it's being worked on. Agents flip the flag when they start and clear it
when they submit a PR. Other collaborators pull frequently and avoid editing
flagged files.

### Problems

- **Granularity:** Modern refactors touch dozens or hundreds of files. You'd lock
  a huge fraction of the repo or need finer granularity (functions? lines?) that's
  hard to define.
- **Doesn't solve the real problem:** The pain point is large changesets conflicting
  *semantically*, not two people editing the same file simultaneously. Two agents
  can edit completely different files and still produce incompatible changes.
- **Stale locks:** Someone checks out 30 files and goes on vacation. You need
  timeouts and overrides, and once those exist, people ignore the flags.
- **Honor system:** Nothing enforces it. You're re-implementing `git lfs lock`
  or Perforce, both of which already exist with known pain points.
- **"Easy merge conflicts" assumption is fragile:** The index file itself becomes
  the most-conflicted file in the repo.

## Version 2: Shadow Repo with Append-Only Logs

A second, shadow repository. Each file in the main repo has a corresponding text
document in the shadow repo. You only ever create new shadow files or append
timestamped messages to existing ones:

> "Bob checked out this file at 2pm, high priority."
> "Bob unchecked the file."
> "Bob is refactoring this file without making stylistic changes."

No hard locks. The shadow repo is frequently and automatically pushed/pulled.
AI agents are instructed to check recent messages and reason about potential
conflicts. A reliable forecaster of merge conflicts, not a hard blocker.

### Improvements over v1

- Soft signals instead of hard locks. Degrades gracefully.
- Freeform messages can convey intent and nuance, not just binary state.
- Main repo keeps a clean commit history.

### Remaining problems

- **Git is the wrong transport.** This is a real-time communication pattern, not
  a snapshot-of-state pattern. Append-only helps but doesn't eliminate merge
  conflicts in the shadow files. A WebSocket or pub/sub channel would deliver the
  same signal faster with less overhead.
- **One-file-to-one-shadow-file is too rigid.** Work doesn't map to files. A task
  might touch 15 files, create 3 new ones, delete 2. File renames break the
  mapping. Cross-cutting changes touch hundreds of files.
- **Unbounded growth.** Append-only means shadow files grow forever. Agents have
  to parse temporal relevance every time they check.
- **Semantic conflicts still unsolved.** File-path-based signaling can't catch two
  agents making incompatible changes to different files.

## Version 3: Shared Log with AI-Powered Conflict Detection

Drop the shadow repo entirely. Use a synchronized log outside the repo (shared
file, simple database, API endpoint, whatever) with timestamped messages about
intent to modify files. Instruct AI agents to occasionally check messages from
other agents and reason about whether there might be conflicts.

### Why this is better

- Extremely simple. Could be implemented in 20 minutes with a shared file and a
  system prompt instruction.
- No git overhead, no per-file mapping, no infrastructure to maintain.
- Leverages what LLMs are genuinely good at: reading natural language descriptions
  of intent and reasoning about whether two tasks might interact semantically.
- Freeform messages can express nuance that no schema captures: "I'm changing the
  return type of `authenticate()` but not its call signature."

### Remaining concerns

- **"Occasionally check" is underspecified.** When? Before starting? Before
  committing? Periodically during work? Each has different tradeoffs between
  freshness and overhead.
- **Detection without resolution.** Spotting a conflict is half the problem.
  What does the agent do about it? Stop? Proceed? Coordinate? Escalate?
- **Freeform means variable signal quality.** One agent writes "editing auth.py,"
  another writes a detailed architectural description. Conflict detection is only
  as good as the least informative message.

### Natural implementation

An MCP server with three endpoints: `post_intent`, `check_conflicts`,
`mark_complete`. Maybe 50 lines of code with a SQLite backend. Every AI coding
tool that supports tool use (Claude Code, Cursor, Copilot Workspace) could talk
to it without changes to the agents themselves.

## Version 3.1: Dedicated Watcher Agent

Refine v3 by separating concerns: a **watcher agent** continuously absorbs the
full firehose of log messages, while **worker agents** stay focused on their
tasks. The watcher only interrupts a worker when it identifies a genuine concern.

### What this solves

- **The timing problem.** Workers never check the log at all. Monitoring is
  someone else's full-time job.
- **The context cost problem.** Workers don't waste tokens reading 50 irrelevant
  log entries. They only receive targeted, relevant warnings.
- **Signal quality.** The watcher can maintain a running model of all active
  intents and do N-way comparison, rather than each worker independently
  evaluating pairwise conflicts.

### Interesting implications

- The watcher is doing continuous N-squared intent comparison. At scale (20+
  agents), you might need hierarchical watchers (one per module or team), which
  starts to resemble an organizational hierarchy. You've reinvented middle
  management, except the managers are cheap LLM instances.
- The watcher accumulates an *incredibly valuable* holistic view of what everyone
  is doing. This is useful beyond conflict detection: "who changed the auth flow
  recently and why?", "what's the overall trajectory of this refactor?" An
  organizational memory emerges for free as a side effect.

## The Trajectory of the Idea

Each iteration moved intelligence from the *mechanism* to the *consumer*:

| Version | Mechanism | Intelligence |
|---|---|---|
| v1: Index file | Hard locks | Deterministic (flag is set or not) |
| v2: Shadow repo | Soft signals, structured | Agent reads and interprets |
| v3: Shared log | Minimal (append-only log) | Agent reasons about conflicts |
| v3.1: Watcher | Minimal + routing | Dedicated agent reasons continuously |
| v4: Shadow + clean | Real code diffs, two repos | Watcher reasons on actual changes |

The logical endpoint: skip structured signaling entirely and have agents share
full diffs in real time, with an AI reviewer that continuously evaluates all
in-flight changesets for semantic conflicts. At that point you're not building a
version control tool --- you're building a *continuously running AI code reviewer*
that catches conflicts as a side effect. That might be the right product.

## Version 4: Shadow Repo + Clean Repo ("Why Not Both?")

Combine the shadow repo from v2 with the watcher from v3.1, but instead of a
log of intent messages, the shadow repo contains the *actual code*. Changes are
auto-committed and synced rapidly (every save, or every 30 seconds). The main
repo keeps only deliberate, reviewed, squashed commits.

The shadow repo serves two roles simultaneously:
1. **Signal source for the watcher.** The watcher reads real diffs, not natural
   language descriptions of intent. This is more reliable and more granular ---
   agents don't have to accurately describe what they're doing, because their
   actual changes speak for themselves.
2. **Time machine.** The messy history shows what agents *actually did*, in what
   order, including changes they made and then reverted. Much richer input for
   conflict reasoning than a log of stated intentions.

### Why this is the strongest version

- Collapses signaling and work into one mechanism. No separate communication
  channel to maintain.
- The watcher can do semantic conflict analysis on real code, not paraphrases.
- The main repo stays clean. Humans never see the messy history.
- The shadow repo is disposable scaffolding --- nobody cares about its integrity.

### Remaining concerns

- **Git is a bad Google Docs.** Real-time sync wants a CRDT or OT model. Git's
  merge unit is the line, and concurrent edits to the same file produce merge
  conflicts even in the shadow repo. Mitigated by very frequent auto-rebase, but
  you're fighting git's design. Maybe acceptable since no one cares about shadow
  repo integrity.
- **Tooling burden.** You need auto-commit-and-push on every save, automatic
  conflict resolution in the shadow repo, and a promotion pipeline from shadow
  to main (squash, cherry-pick, or custom flow). Each is a small project. The
  conceptual simplicity ("just two repos and a watcher") masks real
  infrastructure work.
- **Shadow repo merge conflicts could become someone's full-time job** if the
  auto-resolution isn't robust enough.

### Tweet-length summary

> Half-baked idea: Why not both?
>
> Put the signal in a "shadow repo" where changes are made rapidly and often
> synced. Stick to big chunky changes in the main repo.
>
> Have a little monitor agent who looks at the flickering shadow history and
> warns you if a conflict may arise.

### Coda

Or just have the agents talk to each other on Slack, I guess.

(This is funny because it's true --- what we arrived at across four iterations is
converging on "agents posting in a shared channel about what they're working on,
with one agent reading everything and flagging conflicts." The difference between
v4 and Slack is that the shadow repo gives the watcher actual diffs to reason
about, not just descriptions of intent. But the social architecture is the same.)

## Open Questions

- Is there a useful formal model here? Something from distributed systems
  (vector clocks, conflict-free replicated data types) that maps onto this?
- How does watcher accuracy scale with team size and codebase complexity?
- What's the right interface between the watcher and worker? Just text messages?
  Structured conflict reports? Direct modification of the worker's task plan?
- Could the watcher's accumulated context be persisted as a useful artifact
  (a living "what's happening across the codebase" document)?
- Is the economic case clear? The watcher runs continuously, consuming tokens.
  At what team size does the cost of the watcher pay for itself in avoided
  merge-conflict resolution time?
