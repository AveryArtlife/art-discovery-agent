# ArtLife Agent OS: Decision Matrix

**Date:** 2026-09-05
**Phase:** 3 of 12 (Decision matrix)
**Status:** Proposed. Awaiting owner review before proofs of concept.

## How to read this

Every candidate is scored 1 to 10 on eight criteria, weighted per the brief. Scores reflect fit for *this* system, not general quality. Evidence is cited with how it was verified: **[registry]** = PyPI or npm metadata read directly, **[repo]** = in-repository documentation read from GitHub, **[search]** = web search summary only, official page blocked from this sandbox. Anything marked [search] should be re-verified from the Mac Studio.

The brief's weights:

| Criterion | Weight |
|---|---|
| Security and isolation | 25% |
| Reliability and durable execution | 20% |
| Telegram and multimodal support | 15% |
| Permission granularity | 10% |
| Maintainability | 10% |
| Observability and auditability | 10% |
| Model and provider flexibility | 5% |
| Cost and deployment complexity | 5% |

## The candidates are not interchangeable

The brief lists eight technologies as if they compete for one slot. They do not. They fall into three roles, and the right answer picks one per role:

1. **Operator agent runtime** for the private owner-only surface, where a general-purpose agent is acceptable inside a hardened boundary.
2. **Durable workflow engine** for every automation that must survive crashes, retries, and restarts.
3. **Application framework** for the dealer and client surfaces, where a general-purpose agent is the wrong tool because the counterparty is untrusted.

Scoring each candidate against the role it would actually fill is the only honest comparison. A single table would penalise Temporal for lacking a Telegram connector and reward OpenClaw for having one, when neither fact is relevant to the role each would play.

## Verified versions

| Package | Version | Released | License | Source |
|---|---|---|---|---|
| `pydantic-ai` | 2.40.0 | 2026-09-05 | MIT | [registry] |
| `temporalio` (Python SDK) | 1.32.0 | 2026-08-24 | MIT | [registry] |
| `langgraph` | 1.2.11 | 2026-08-11 | MIT | [registry] |
| `letta` | 0.16.8 | 2026-05-14 | Apache-2.0 | [registry] |
| `hermes-agent` | 0.19.0 | 2026-07-20 | MIT | [registry] |
| `openclaw` (npm) | 2026.9.1 | current | MIT | [registry] |
| `inngest` (npm / py) | 4.20.0 / 0.5.19 | current | **SSPL** with delayed Apache-2.0 | [registry] [repo] |
| `@trigger.dev/sdk` | 4.5.16 | current | MIT | [registry] |
| `n8n` | 2.37.10 | current | Sustainable Use License (proprietary) | [registry] |
| `aiogram` | 3.31.0 | 2026-08-26 | MIT | [registry] |
| `python-telegram-bot` | 22.8 | 2026-06-12 | LGPL-3.0 | [registry] |
| `pyairtable` | 3.4.2 | 2026-07-26 | MIT | [registry] |

Temporal server itself is MIT [repo].

---

## Role 1: Operator agent runtime

The private surface for the owner and authorised staff. Runs in a hardened container. Talks to business systems only through capability-allowlisted tool calls into the application service; it never holds database credentials directly.

### Evidence

**Hermes Agent 0.19.0** [repo, `website/docs/user-guide/security.md`]

- Deny-by-default authorisation: *"If no allowlists are configured and GATEWAY_ALLOW_ALL_USERS is not set, all users are denied."*
- DM pairing with one-time codes, 1-hour expiry, rate limiting, lockout after 5 failures.
- Three approval modes for dangerous commands (smart / manual / off) plus a hardline blocklist that refuses catastrophic commands *"regardless of --yolo...or user explicitly clicking allow always."*
- Secrets filtered from tool environments by name pattern; MCP subprocesses receive only a safe variable set.
- Docker backend hardening: `--cap-drop ALL`, `--security-opt no-new-privileges`, `--pids-limit 256`, no-exec tmpfs.
- SSRF protection on all URL fetches, fail-closed on DNS failure, re-validated per redirect hop.
- Prompt-injection scanning of context files (AGENTS.md, .cursorrules) before inclusion.
- Telegram: Bot API 9.4 forum topics as isolated sessions, 9.5 streaming drafts [search].
- **Stated limitation, verbatim:** *"Container backends do not guarantee isolation against deliberately adversarial processes, only honest-but-wrong agents."* And: *"Write guards apply to write_file and patch only. The terminal tool runs as the same OS user and can still cat or overwrite denied paths via shell commands."*
- Self-improving skill creation is a core feature. For a production business system, an agent that rewrites its own capabilities is a change-control problem.

**OpenClaw 2026.9.1** [repo, `docs/gateway/sandboxing.md`; security.md returned 404 on main]

- Sandbox mode defaults to `"off"`. Options: `off`, `non-main`, `all`.
- Per-role `sandbox: "required"` is immutable and *"cannot be bypassed by elevated execution or Gateway/node host overrides."* This is the one strong control.
- **Stated limitation, verbatim:** *"This is not a perfect security boundary, but it materially limits filesystem and process access when the model does something dumb."*
- `tools.elevated` is an explicit escape path out of the sandbox.
- Three `dangerouslyAllow*` flags override safety defaults.
- CVE-2026-27002: configuration injection in the Docker tool sandbox allowed bind mounts, host networking, and unconfined profiles; fixed in 2026.2.15 [search, NVD].
- Broadest messaging reach: WhatsApp, Telegram, Slack, Discord, Signal, iMessage [search].
- CalVer with very high release velocity. Surface area is large by design.

**Custom operator service on PydanticAI + Temporal** [repo, `docs/durable_execution/temporal.md`]

- Everything the operator can do is a typed tool with deterministic authorisation, no general shell.
- `TemporalDurability` capability makes model calls, tool calls, and MCP communication into Temporal activities.
- `ApprovalRequired` and `CallDeferred` exceptions implement human-in-the-loop pauses natively.
- Cost is build time: pairing, session management, and Telegram conversation UX all have to be written.

### Scores

| Criterion (weight) | Hermes | OpenClaw | Custom PydanticAI |
|---|---|---|---|
| Security and isolation (25) | 8 | 5 | 8 |
| Reliability and durability (20) | 6 | 6 | 9 |
| Telegram and multimodal (15) | 9 | 9 | 6 |
| Permission granularity (10) | 8 | 7 | 9 |
| Maintainability (10) | 6 | 5 | 7 |
| Observability (10) | 6 | 6 | 8 |
| Model flexibility (5) | 8 | 8 | 9 |
| Cost and complexity (5) | 8 | 8 | 6 |
| **Weighted total** | **7.35** | **6.45** | **7.85** |

### Recommendation for Role 1

**Hermes Agent as the conversational front, holding no authority.** Custom PydanticAI scores higher on the pure matrix because durability and deterministic permissions carry 30% of the weight. But the gap is small, and Hermes brings pairing, approvals, Telegram topic sessions, and a working operator UX that would take weeks to reproduce. The resolution is to use Hermes for what it is good at (talking to the owner) and deny it what it is bad at (holding credentials or business logic):

- Hermes runs in its Docker backend on the Mac Studio, under the dedicated non-admin user, with `HERMES_WRITE_SAFE_ROOT` set and the terminal tool disabled or restricted to a scratch volume.
- Every business capability is an MCP tool served by the Temporal-backed application service over Tailscale. Hermes sees typed tools, never a database, an API key, or a shell into production.
- High-risk tools raise `ApprovalRequired` in the application service. The approval lands in the owner's Telegram as a button, not as a Hermes "smart" auto-approve.
- Self-improvement is disabled for production. Skills are versioned in git and reviewed.

OpenClaw is rejected for the operator role: sandbox off by default, an explicit elevated escape hatch, a 2026 sandbox CVE, and a surface area sized for a personal assistant rather than a business system. Its iMessage and WhatsApp reach is real but not a requirement.

**Migration path:** if Hermes proves brittle in the pilot, the MCP tool layer is already the contract. Swapping the front for a thin custom Telegram bot on aiogram changes nothing behind the tools.

---

## Role 2: Durable workflow engine

Runs ArtTable sync, media processing, news monitoring, buyer matching, follow-up reminders, briefings, backup verification, health checks, and scheduled evaluations. Lives on Hetzner. Must survive the Mac being offline.

### Evidence

**Temporal** [repo README; PydanticAI integration docs]

- Server MIT. Python SDK 1.32.0 MIT.
- Dev: `temporal server start-dev`. Production: server + PostgreSQL + Web UI, three containers.
- PydanticAI integration is first-party: *"Model requests, tool calls that may require I/O, and MCP server communication all need to be offloaded to Temporal activities."*
- Full event history per workflow; every retry, every input, every decision is inspectable in the UI. This is the observability and audit story in one component.
- **Constraints:** streaming is buffered inside activities; every recorded payload capped at 2 MB by default. Media must be passed by reference (object storage key), never as bytes. That is the correct design anyway.
- Secondary sources describe self-hosting at $2,500 to $4,500 a month [search]. That figure is for multi-tenant scale with dedicated operators. For a single-tenant deployment at this volume it is roughly 1 GB of RAM on the same server as everything else.
- OpenAI integrated Temporal into its Agents SDK in February 2026 [search]; the pattern is now mainstream.

**Inngest 4.20 / 0.5.19** [repo README; search]

- Self-hosting since 1.0, January 2026. Single binary. SQLite or Postgres. Built-in concurrency, throttling, debounce, rate limiting.
- **License is SSPL** with delayed Apache-2.0 publication. Fine for internal use, but SSPL is not OSI-approved and constrains any future productisation. Worth knowing before adopting as the spine.
- Multi-language SDKs. Good developer ergonomics.

**Trigger.dev 4.5** [search]

- Docker Compose self-host bundles Postgres, Redis, registry, and object storage. Helm chart for Kubernetes.
- TypeScript-first. Some cloud-only features absent from self-hosted.
- Would split the codebase across Python (AI) and TypeScript (workflows), which is a maintainability tax for a two-person gallery.

**LangGraph 1.2.11 checkpointing** [search, official docs blocked]

- `AsyncPostgresSaver` for production persistence. Human-in-the-loop via interrupts.
- Persistence modes: `"exit"` (safe) or `"async"` (faster, *"small risk that LangGraph does not write checkpoints if the process crashes"*).
- This is graph-state checkpointing, not a workflow engine. No scheduler, no queue, no cron, no cross-process retry semantics. It solves resumable agent runs, not "run the news monitor every 15 minutes and retry the Airtable sync on 429."

**n8n 2.37** [search]

- Six critical and high-severity CVEs in 2026 across webhook handling, expression evaluation, and code nodes; one added to CISA's Known Exploited Vulnerabilities catalog.
- Community nodes run with the same permissions as core nodes.
- The AI Agent node processing emails, forms, or documents is a documented indirect prompt-injection surface.
- Proprietary licence.

### Scores

| Criterion (weight) | Temporal | Inngest | Trigger.dev | LangGraph ckpt | n8n |
|---|---|---|---|---|---|
| Security and isolation (25) | 8 | 7 | 7 | 6 | 3 |
| Reliability and durability (20) | 10 | 8 | 8 | 6 | 6 |
| Multimodal payload handling (15) | 6 | 7 | 7 | 7 | 7 |
| Permission granularity (10) | 7 | 6 | 6 | 5 | 4 |
| Maintainability (10) | 7 | 8 | 7 | 7 | 5 |
| Observability (10) | 9 | 8 | 8 | 6 | 6 |
| Model flexibility (5) | 9 | 8 | 8 | 9 | 8 |
| Cost and complexity (5) | 6 | 8 | 7 | 8 | 8 |
| **Weighted total** | **7.95** | **7.40** | **7.25** | **6.40** | **5.30** |

### Recommendation for Role 2

**Temporal.** It wins on the two heaviest criteria and it is the engine PydanticAI integrates with natively, which collapses the agent and workflow layers into one execution model with one audit trail. The 2 MB payload cap is a design constraint, not a blocker: media goes to object storage, workflows carry keys.

Inngest is the runner-up and a credible fallback if Temporal's operational weight proves too much for a two-person team. The SSPL licence is the reason it is not first.

n8n is excluded from any path that touches untrusted input (dealer uploads, client messages, news, email). If a visual editor is wanted for owner-only, low-stakes glue, it can be revisited behind Tailscale with community nodes disabled. Default position: not installed.

LangGraph is not rejected; it is reclassified. It is an agent-orchestration library and could sit inside a Temporal activity. It is not the workflow engine.

---

## Role 3: Application framework for untrusted-facing surfaces

The Dealer Intake Bot and Client Concierge Bot. Every input is adversarial by assumption. Authorisation happens in code before anything reaches a model.

### Evidence

**PydanticAI 2.40.0** [repo]

- Structured outputs validated against Pydantic schemas. Extraction returns a typed `ArtworkSubmission`, not free text to parse.
- Native `TemporalDurability`. A dealer's multi-message submission is one durable workflow with a session ID and idempotency key.
- `ApprovalRequired` / `CallDeferred` are first-class, which is exactly the approval-policy mechanism the brief demands.
- Model-agnostic across Anthropic, OpenAI, Google, and local providers.
- Observability via OpenTelemetry (Logfire is optional, OTel is not vendor-locked).
- Telegram transport is separate: aiogram 3.31 (MIT, asyncio-native, webhook secret token supported) is the current standard.

**LangGraph 1.2.11**

- Graph model is expressive but adds ceremony for what are essentially form-filling conversations.
- Structured output support exists but is less central to the design than in PydanticAI.
- Checkpointing is per-graph, not per-business-process; approvals and idempotency need a second system anyway.

**Hermes or OpenClaw facing dealers or clients**

- A general-purpose agent with a terminal tool, skill creation, and web fetch, pointed at an untrusted counterparty, is the threat model the brief exists to prevent. Hermes's own docs say its isolation holds against honest-but-wrong agents, not adversarial input. Scored for completeness; not a serious candidate.

### Scores

| Criterion (weight) | PydanticAI | LangGraph | Hermes | OpenClaw |
|---|---|---|---|---|
| Security and isolation (25) | 9 | 7 | 5 | 4 |
| Reliability and durability (20) | 9 | 7 | 6 | 6 |
| Telegram and multimodal (15) | 7 | 7 | 9 | 9 |
| Permission granularity (10) | 9 | 7 | 6 | 6 |
| Maintainability (10) | 8 | 7 | 6 | 5 |
| Observability (10) | 8 | 7 | 6 | 6 |
| Model flexibility (5) | 9 | 9 | 8 | 8 |
| Cost and complexity (5) | 7 | 7 | 8 | 8 |
| **Weighted total** | **8.40** | **7.10** | **6.40** | **6.00** |

### Recommendation for Role 3

**PydanticAI with aiogram, on Temporal.** Two separate services, two bots, two tokens, two database roles, two containers. Shared code lives in a library; shared credentials do not exist.

---

## Letta and memory

Letta 0.16.8 (Apache-2.0) is a serious memory framework: git-backed MemFS, self-hostable on Postgres with pgvector. It is not scored in a role because the brief is explicit that *"agent memory must not be the workflow engine or source of truth."*

Recommendation: **defer.** At this scale, consent-gated client preference tables in PostgreSQL with pgvector embeddings cover the collector-taste requirement with no additional stateful service, no additional auth surface, and no additional backup target. Revisit Letta if the Operator Agent's long-term memory becomes a real pain point in the pilot. Adding it later is additive; removing it later is not.

---

## Hosting

### Evidence

**Hetzner pricing shifted in 2026** [search, official page blocked]

- June 15, 2026: dedicated-vCPU CCX instances rose 2.1x to 2.7x; shared CX instances rose 1.3x to 1.4x. Example: US-region CCX13 went from $19.99 to $50.99 a month. A second adjustment in August 2026 is reported by one source.
- Germany and Finland locations remain cheapest and carry the largest traffic allowances (20 to 60 TB). Ashburn and Hillsboro are the US options.
- The cheapest current shared instances are €5.49 to €10.49 a month.

Consequence: the "Hetzner is nearly free" assumption is weaker than it was, but the workload here is small. A shared 4-vCPU / 8 GB instance in Falkenstein comfortably runs the API, PostgreSQL, Temporal, both bots, and the object-storage gateway. Estimated infra: **€25 to €45 a month** including object storage and off-site backup. Verify at purchase.

**Telegram constraints** [search, core.telegram.org]

- Webhook `secret_token` (1 to 256 chars) arrives as `X-Telegram-Bot-Api-Secret-Token`. Required.
- `getFile` download cap is **20 MB**. Dealer condition reports, high-resolution images, and videos will exceed this. A self-hosted Bot API server raises it to 2 GB. This is a real design decision for the Dealer Intake Bot and is asked about in Open Questions.
- Webhook ports: 443, 80, 88, 8443.

**Tailscale** [search, official docs]

- Mac as an always-on node needs the standalone `tailscaled` build, not the App Store app.
- ACLs can restrict Hetzner to reach only specific ports on the Mac and nothing else on the home network.

### Scores

| Criterion (weight) | Hetzner only | Mac only | Hybrid |
|---|---|---|---|
| Security and isolation (25) | 7 | 4 | 8 |
| Reliability and durability (20) | 9 | 4 | 8 |
| Telegram and multimodal (15) | 8 | 6 | 8 |
| Permission granularity (10) | 7 | 6 | 8 |
| Maintainability (10) | 8 | 6 | 6 |
| Observability (10) | 8 | 6 | 7 |
| Model flexibility (5) | 7 | 9 | 9 |
| Cost and complexity (5) | 8 | 9 | 6 |
| **Weighted total** | **7.75** | **5.35** | **7.65** |

### Recommendation for hosting

**Hybrid**, as the brief prefers, on a weighted score that is a tenth behind Hetzner-only. The gap is maintainability and cost of two environments. The reason to accept that cost is not in the matrix: the brief's requirement that sensitive and compute-heavy processing can stay on hardware the owner physically controls, and that a local model can run on it with no data leaving the building. Hetzner-only cannot do that. Mac-only fails the public-ingress and always-on requirements outright; residential ISPs, no static IP, and the brief's own rule against inbound ports settle it.

Split:

| Hetzner (Falkenstein unless US residency is required) | Mac Studio (dedicated non-admin user) |
|---|---|
| Public HTTPS ingress behind Cloudflare | Hermes operator agent in Docker |
| Telegram webhooks for all three bots | Local model inference (optional) |
| Application API | Sensitive document processing |
| PostgreSQL 16 with pgvector | Compute-heavy image similarity |
| Temporal server, UI, and workers | Owner-only emergency stop |
| S3-compatible object storage | Tailscale node, no inbound public ports |
| Monitoring, alerting, backups | |

Client read path (Concierge Bot, sanitised inventory API) lives entirely on Hetzner and keeps working when the Mac is off.

**Region:** Falkenstein is recommended on price and traffic. Miami to Falkenstein is roughly 110 ms; Miami to Ashburn roughly 30 ms. The Mac talks to Hetzner over Tailscale for tool calls and sync, not for interactive UI, so 110 ms is fine. If a US data-residency requirement exists, Ashburn at a higher price. Asked in Open Questions.

---

## Summary of decisions proposed

| Role | Winner | Runner-up | Rejected |
|---|---|---|---|
| Operator agent front | Hermes Agent (no authority, MCP tools only) | Custom aiogram bot | OpenClaw |
| Durable workflow engine | Temporal | Inngest | LangGraph-as-engine, n8n, Trigger.dev |
| Untrusted-facing app framework | PydanticAI + aiogram | LangGraph | Hermes, OpenClaw |
| Memory | Postgres + pgvector, consent-gated | Letta (deferred) | |
| Hosting | Hybrid, Hetzner Falkenstein + Mac Studio | Hetzner only | Mac only |
| Telegram transport | aiogram 3 | python-telegram-bot | |
| ArtTable adapter | pyairtable 3 behind an interface | direct HTTP | |

## Risks carried forward

1. Every [search]-only claim needs re-verification from the Mac Studio before code depends on it.
2. Hermes 0.19 is a 0.x project moving fast. Pin, vendor the Docker image, review upgrades.
3. Temporal's 2 MB payload cap must be enforced at the boundary; a single oversized payload fails the workflow.
4. Telegram's 20 MB download cap will bite dealer intake. Decision needed on a self-hosted Bot API server.
5. Hetzner may raise prices again. The design must be portable to any Docker host; nothing Hetzner-specific in application code.
6. If ArtTable is Artlogic, there is no public write API [search]. That changes the intake pipeline's last mile.

## Proofs of concept proposed (Phase 5, after approval)

Each is under an hour, runs on the Mac under the dedicated user with mock credentials, and produces a written result:

1. Temporal `start-dev` + PydanticAI `TemporalDurability` + a fake Airtable adapter: prove a three-message dealer submission becomes one workflow, and that a replayed Telegram update is idempotent.
2. Hermes in Docker backend with terminal disabled, one MCP tool served from a local FastAPI stub over loopback: prove the operator can call a tool and that the tool's `ApprovalRequired` surfaces as a Telegram prompt.
3. aiogram webhook receiver with `secret_token` verification and a 25 MB file: prove where the 20 MB cap actually fails and what the self-hosted Bot API server changes.
