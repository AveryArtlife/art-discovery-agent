# ArtLife Agent OS: Discovery Audit

**Date:** 2026-09-05
**Phase:** 1 of 12 (Discovery and environment audit)
**Status:** Complete for the remote sandbox. Mac Studio audit pending (see Open Questions).

## Where this audit ran

This audit ran inside a Claude Code remote sandbox, not on the owner's Mac Studio. That matters for two reasons:

1. Nothing here describes the Mac Studio. Its model, RAM, storage, macOS version, and uptime posture are unknown and are asked for in `02-open-questions.md`.
2. The sandbox's network policy blocks direct reads of most vendor documentation. Web search works; fetching the pages it links to mostly does not. Every claim below is marked with how it was verified.

## Sandbox environment

| Item | Value |
|---|---|
| OS | Ubuntu 24.04.4 LTS, kernel 6.18 |
| CPU / RAM | 4 vCPU / 15 GB |
| Disk | 252 GB volume, ~30 GB writable allowance per session |
| Python | 3.11.15 with `uv` 0.8.17 and Poetry 2.3.3 |
| Node | 22.22.2 with npm 10.9.7 and pnpm 10.33.0 |
| Docker | 29.3.1 (daemon present) |
| Rust | 1.94.1 |
| PostgreSQL client | 16.13 |
| Redis client | 7.0.15 |
| Not present | Terraform, Ansible, Tailscale, Podman |

## Network egress

Outbound HTTPS goes through a local proxy (`127.0.0.1:41477`) with a CA bundle at `/root/.ccr/ca-bundle.crt`. The proxy reports `selective: false` but enforces a domain blocklist. Observed during this audit:

**Reachable:** `pypi.org`, `registry.npmjs.org`, `raw.githubusercontent.com`, web search.

**Blocked (EGRESS_BLOCKED):** `hermes-agent.nousresearch.com`, `docs.openclaw.ai`, `airtable.com`, `docs.temporal.io`, `www.inngest.com`, `pydantic.dev`, `www.hetzner.com`, `www.myartbroker.com`.

Consequence: framework research in this environment relies on registry metadata and in-repo documentation mirrored on GitHub. Direct doc verification should be repeated from the Mac Studio, where Claude Code runs with the owner's normal network.

## Credentials present in the sandbox

Environment variables named `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `CLOUDSDK_AUTH_ACCESS_TOKEN`, `GH_TOKEN`, and `GITHUB_TOKEN` exist. These are harness-provisioned for the sandbox itself. They are not ArtLife business credentials and were not used for anything in this audit. No values were read or recorded.

## Existing project

Repository `AveryArtlife/art-discovery-agent` (public, described as "ARTWORK SEARCH PLATFORM"):

- `README.md` (46 bytes), `LICENSE`, a Node.js-template `.gitignore`
- `docs/inquiry-audit-methodology.md` (committed on branch `claude/artlife-inquiry-audit-ex64ry`, draft PR #5)
- `audit/` (gitignored, contains client PII from the mailbox audits, delivered as private artifacts)

**There is no application code.** No schema, no services, no infrastructure. Agent OS starts from an empty repo. That is a simplification, not a problem.

**The repository is public.** Anything committed here is world-readable. All Agent OS documentation is written to be PII-free. Infrastructure code will contain no secrets by construction. If the owner wants the implementation private, that decision should be made before the first service commit.

## Connectors available in this session

These are attached to the Claude session, not to any ArtLife system. They indicate what the owner already uses and what could be wired into Agent OS later.

| Connector | Relevance |
|---|---|
| Gmail (`avery@artlife.com`) | Read access proven across three audits. Candidate ingest for news newsletters and inquiry notifications. |
| Google Drive | Candidate for document intake and cold storage of originals. |
| GitHub | Scoped to this repository only. |
| ElevenLabs | Speech transcription and generation. Candidate for dealer voice-note transcription and Instagram script voiceover. |
| Canva, Gamma | Content production. Not core. |
| LunarCrush | Crypto social data. Not relevant to Agent OS. |

## Business context established in prior sessions

Verified from the mailbox, not assumed:

- ArtLife Gallery, Miami, blue-chip secondary market. Warhol, Basquiat, Banksy, KAWS, Alec Monopoly, plus Murakami, Haring, Invader, Retna, Estevan Oriol, and others.
- Two operators: Avery Andon (CEO) and Nico Hayes (Senior Director). Shared address `info@artlife.com`.
- Inbound arrives from Artsy (per-inquiry reply tokens at `reply.artsy.net`), Artnet Gallery Network (zero inquiry notifications observed in a 14-day window despite active membership), and the artlife.com contact form (submissions do not reach `avery@`).
- Roughly 71 Artsy inquiries in 14 days. About 80 promotional emails a day. The inbox is large enough that unread state carries no signal.
- Reply matching cannot use Gmail `threadId`; the Artsy reply token is the working join key. Documented in `docs/inquiry-audit-methodology.md`.
- Artsy web-inbox replies generate no email. Whether Nico replies in-platform is unresolved.

These findings shape Agent OS directly: the Telegram surfaces exist partly because the email channel is not a reliable place to notice an inquiry.

## What was not done in this phase

Per the brief, nothing was installed, no paid resource was created, no secrets were requested, and no proof of concept was run. Proofs of concept begin after the decision matrix and threat model are accepted.
