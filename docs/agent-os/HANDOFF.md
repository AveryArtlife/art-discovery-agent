# Handoff: build ArtLife Agent OS on the Mac Studio

**Superseded.** The message that used to live here has been replaced by `04-master-build-prompt.md`, the self-contained Master Build Prompt v2. Use that file.

The sequence, in full:

1. Prepare the Mac Studio and create the new private `artlife-agent-os` repository under the ArtLife GitHub account, following `03-mac-studio-setup.md`. Agent OS never lives in this repository and never touches any GemBreak repository.
2. In the new repository, place `04-master-build-prompt.md` as `docs/00-master-build-prompt.md` and, optionally, the four discovery documents under `docs/prior/`.
3. Start Codex or Claude Code inside the clone as the dedicated non-admin user.
4. Paste everything below the first horizontal rule of the build prompt as the first message.
5. The agent stops at the Phase 1 approval gate. Nothing is installed, deployed, or paid for before you approve.

Decisions settled since this file was written: the project is named **ArtLife Agent**; ArtTable is
**Airtable**; the implementation lives in a **new standalone private repository** that touches no
other; **Telegram is the primary channel** with three bots; **WhatsApp uses one shared business
number**, with dealers and clients separated by verified sender identity in code.

A working prototype now exists against those decisions, so a session starting from this handoff
should treat the build prompt's Phase 1 as largely done and read the implementation's own
`STATUS.md` first. The remaining open questions are asked by the agent in one batch.
