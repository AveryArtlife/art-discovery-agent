# ArtLife Agent OS: Open Questions

**Date:** 2026-09-05. **Answers recorded:** 2026-09-06.
**Status:** A, C, E2, K, L and M are answered. The rest continue on the safe defaults marked below.

One consolidated batch. Only questions that change what gets built. Each shows the default assumed if unanswered, so nothing blocks.

Never paste a secret, token, or password in reply to any of these. Where a credential is needed, the answer is "yes, I have one" and the value goes into the secrets manager later, following instructions in `03-mac-studio-setup.md`.

## A. ArtTable (blocks the intake pipeline's last mile)

**A1. ANSWERED: Airtable.** The adapter is built vendor-neutral regardless, and the Airtable
implementation is written and tested against a mocked transport.

**A2. OPEN, and now the item that blocks the intake pipeline.** Which base and table names hold inventory, and does the account plan support the Web API with personal access tokens? Attachment upload via the API is a 5 MB per-file cap [unverified from this sandbox; verify from Mac]; originals larger than that must live in object storage with a link in the record.
*Default:* Assume PAT access exists; originals always go to object storage regardless.

**A3. NOT APPLICABLE** now that A1 is answered. Retained for the record. If Artlogic: research found no public write API, only Artsy sync and Xero integration. Do you have a contract that includes API access, or an account manager who can confirm? If not, the interim is: Agent OS creates the draft in PostgreSQL, produces an Artlogic-ready import file, and a human imports it. Fragile browser automation for writes is not proposed without your explicit approval.
*Default:* Interim manual-import workflow.

**A4.** Is ArtTable the system of record, with PostgreSQL as a supplement? Or may Agent OS become the record and ArtTable the mirror?
*Default:* ArtTable is the record. PostgreSQL holds conversation state, approvals, audit, embeddings, workflow state, and a sanitised read mirror.

## B. Mac Studio (blocks the hybrid half and the operator pilot)

**B1.** Model, chip, RAM, storage, macOS version.
**B2.** Must it stay on 24/7? Is it on a UPS?
**B3.** Is it currently your daily driver, or a dedicated machine?
**B4.** Will you create a dedicated standard (non-admin) macOS user for Agent OS, per `03-mac-studio-setup.md`? The brief's own security requirements assume this.
*Default:* Treated as a daily driver with intermittent uptime; all client-facing read paths stay on Hetzner and nothing user-facing depends on the Mac being up.

## C. Hosting and network

**C1.** Domain to use for webhooks and the command center, or should a subdomain be chosen under artlife.com?
**C2.** Hetzner region: Falkenstein (Germany, cheaper, more traffic, ~110 ms from Miami) or Ashburn (US, roughly double the price post-June-2026, ~30 ms)? Only choose Ashburn if there is a US data-residency requirement.
*Default:* Falkenstein.
**C3.** Do you already have a Hetzner account, a Cloudflare account, and a Tailscale account?
*Default:* Assume none; setup steps will be provided before any paid resource is created.

## D. Scale (sizes the database, storage, and model budget)

**D1.** Approximate counts: active dealers, active clients, artworks in inventory, images per artwork, daily Telegram conversations expected.
*Default:* 10 dealers, 200 clients, 500 artworks, 4 images each, 30 conversations a day.

## E. Access policy (blocks the allowlists and authorisation rules)

**E1.** Which dealers are authorised to submit inventory? Names and Telegram handles, or "I will pair them one at a time."
**E2.** Are clients public (anyone can message the bot), invite-only (signed link), or manually paired by you?
*Default:* Invite-only with signed, expiring links.
**E3.** Which inventory and price fields may each client tier see? For example: everyone sees title, artist, year, medium, dimensions, availability; tier 1 sees asking price; nobody sees acquisition cost or consignor.
*Default:* Two tiers as in the example. Acquisition cost, consignor, internal notes, and commissions never leave the database role that holds them.
**E4.** Besides you, who is staff on the operator surface? Nico?
*Default:* You only until told otherwise.

## F. Existing systems (decides which connectors get built)

**F1.** Do you use a CRM today, or is the mailbox the CRM?
**F2.** Calendar: Google Calendar on the artlife.com Workspace?
**F3.** Cloud storage: Google Drive (connected to this session), Dropbox, Box?
**F4.** Accounting: QuickBooks (invoices seen in the mailbox from Intuit), Xero, other?
**F5.** E-signature: DocuSign (seen in the mailbox)?
**F6.** Artsy partner account: do you have API credentials, or only the CMS login?
**F7.** Licensed auction-data provider (Artnet Price Database, MutualArt, Artprice)? Comparable pricing needs one; scraping is not proposed.
*Default:* Build Gmail, Google Drive, and Telegram first. Everything else after a documented workflow needs it.

## G. Budget

**G1.** Monthly ceiling for infrastructure. Estimate for the proposed stack: €25 to €45 a month.
**G2.** Monthly ceiling for model usage. This is the real variable. Estimate at the default scale in D1: $80 to $250 a month across Anthropic, OpenAI, and Google, depending on how much image and document processing runs.
**G3.** Should the system hard-stop at the ceiling, degrade to cheaper models, or alert and continue?
*Default:* Alert at 70%, degrade to cheaper models at 90%, hard-stop non-essential workflows at 100%. Client concierge and inquiry capture never stop.

## H. Compliance and retention

**H1.** Any requirement that data stay in the US, or in the EU?
**H2.** How long should conversation transcripts, dealer submissions, and client preference data be retained? Any existing privacy policy on artlife.com to align with?
**H3.** Insurance or consignment agreements that dictate how condition reports, provenance documents, or images may be stored or shared?
*Default:* No residency constraint. Transcripts 24 months, submissions indefinitely (business records), preferences until consent is withdrawn. Encrypted at rest in every case.

## I. News intelligence

**I1.** Publications and sources you actually read: Artnet News, ARTnews, The Art Newspaper, Artsy Editorial, auction-house newsletters, specific Substacks?
**I2.** Artists, markets, and topics that should score highest.
**I3.** Should a dedicated mailbox be created for newsletter ingest, or should the system read a label in the existing mailbox?
*Default:* Sources seen in the mailbox census (Artnet, Artsy, Frieze, Sotheby's, Christie's, Phillips, Hang-Up, Guy Hepner, Hamilton Selway, Revolver) plus official RSS from the majors. Artists from the audits. A Gmail label rather than a new mailbox.

## J. Interfaces

**J1.** Telegram alerts only, or also a web command center?
*Default:* Both. The command center is required for approvals, audit history, and cost visibility, and is served only over Tailscale.
**J2.** Do you want voice-note commands to the operator agent in the first pilot, or later?
*Default:* Later. Transcription is in scope for dealer intake from day one.

## K. Telegram file sizes

**K1.** Dealer uploads will include condition reports and videos above Telegram's 20 MB `getFile` limit. Options: (a) run a self-hosted Telegram Bot API server on Hetzner, which raises the limit to 2 GB and adds one container; (b) ask dealers to send large files through a signed upload link instead. Preference?
*Default:* (b) for the pilot, (a) if dealers push back.

**K2. ANSWERED: one shared WhatsApp number.** Dealers and clients message the same business
number. The surface is decided by verified sender identity in deterministic code before any model
call, and a test asserts that separation holds. Telegram is the primary channel; WhatsApp follows
once Meta business verification completes.

## L. Repository and branch

**L1. ANSWERED: a new standalone private repository**, named ArtLife Agent, under the ArtLife
account. It touches no other repository. This public repository keeps only the audit methodology and
these discovery documents; no implementation code is committed here.

**L2. ANSWERED: the project is named ArtLife Agent.**

## M. Your voice rules

**M1. IMPLEMENTED on the default.** The voice rules are enforced in code before any send, across
client-facing, dealer-facing, and Instagram copy. Copy that breaks them cannot become a send job.
