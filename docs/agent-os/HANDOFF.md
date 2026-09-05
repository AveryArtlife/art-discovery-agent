# Handoff: continue ArtLife Agent OS on the Mac Studio

Paste everything below this line as the first message in a new Claude Code session running on the Mac Studio under the `artlife-agent` user, inside `~/artlife`.

---

You are continuing a project already in progress. Read these four files in order before doing anything else, then follow the instructions at the end of this message.

1. `docs/agent-os/00-discovery.md` — what was found in the previous environment and what could not be verified there.
2. `docs/agent-os/01-decision-matrix.md` — framework and hosting decisions proposed, with scores, evidence, and how each claim was verified.
3. `docs/agent-os/02-open-questions.md` — the consolidated question batch and the default assumed for each unanswered item.
4. `docs/agent-os/03-mac-studio-setup.md` — how this machine was meant to be prepared.

The original brief for the whole project is long. Its non-negotiables, which every decision so far honours:

- Four separately permissioned components: Private Operator Agent, Dealer Intake Bot, Client Concierge Bot, and Automation Workers. Never one all-powerful agent.
- Authorisation happens in deterministic code before anything reaches a model.
- Approval policies fail closed. Publishing, price changes, client outreach, social posting, contracts, payments, deletions, permission changes, and new integrations require approval.
- No secrets in code, prompts, git, images, logs, or chat. Ask for variable names; never ask for values.
- Do not create paid resources, buy a domain, or trigger a paid API without showing expected cost and receiving approval.
- Do not claim completion based on generated files. Demonstrate workflows end to end.
- At the end of each phase report: what is working, evidence, decisions, costs, risks, and what requires approval.

Do these things first, in this order:

**Step 1. Audit this machine.** Record model, chip, RAM, storage, macOS version, whether you are running as a standard or admin user, whether OrbStack or Docker is present, and whether Tailscale is installed. Append the results to `docs/agent-os/00-discovery.md` under a new "Mac Studio" heading. Do not install anything yet.

**Step 2. Re-verify the [search]-only claims in the decision matrix.** This machine can reach vendor documentation that the previous sandbox could not. Fetch the official pages for: Hermes Agent security, OpenClaw security and sandboxing, Temporal self-hosting, Inngest self-hosting and licence, PydanticAI Temporal integration, Airtable `uploadAttachment` limits and PAT scopes, Telegram Bot API `setWebhook` and file limits, Hetzner current pricing, and Tailscale macOS daemon installation. For each, either confirm the matrix entry or correct it, and change its tag from [search] to [official]. If a correction changes a score, re-run the weighted total and say so.

**Step 3. Check for answers to the open questions.** If the owner has answered any of them in this session or in a file, update the defaults in `02-open-questions.md`. Anything still unanswered keeps its default.

**Step 4. Write the threat model.** Create `docs/threat-model.md` covering the four components, trust boundaries, assets, attacker capabilities (malicious dealer, malicious client, compromised Telegram account, prompt injection through images/PDFs/OCR/URLs/news, compromised Hetzner host, compromised Mac), and the specific control that addresses each. The brief requires this before any bot is exposed.

**Step 5. Stop and report.** Show the owner what changed in the matrix after re-verification, the threat model summary, and the three proposed proofs of concept from the end of `01-decision-matrix.md`. Ask for approval to run the proofs of concept. Do not run them until approved.

Two open decisions that gate everything after Step 5 and that only the owner can make: what "ArtTable" is (question A1), and whether the implementation should move to a private repository (question L1). If either is still unanswered when you reach Step 5, say so explicitly.
