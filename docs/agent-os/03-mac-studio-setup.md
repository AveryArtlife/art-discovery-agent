# Mac Studio Setup for Agent OS Development

**Purpose:** prepare the Mac Studio to host Claude Code sessions and, later, the private operator agent, without granting either one access to your personal account, keychain, files, or browser.

**Why this matters:** the brief requires that the Mac Studio run Agent OS under a dedicated non-admin account, mount only explicitly required directories, and never grant broad access to your home directory, passwords, keychains, messages, photos, or cloud drives. Running Claude Code as your everyday admin user to build that system would violate its own threat model on day one. Twenty minutes now prevents that.

**Time:** about 25 minutes. **Cost:** none. **Scope:** nothing is built by following this guide; it prepares the machine and the repository, then hands the build prompt to Codex or Claude Code, which stops at an approval gate.

## 1. Create a dedicated standard user

System Settings, Users & Groups, Add User.

- Account type: **Standard**, not Administrator.
- Name: `artlife-agent` (or similar).
- Strong password stored in your password manager. This account has no reason to know your personal password.
- Do **not** sign this user into iCloud. Skip Apple ID sign-in at first login.
- Do not enable Screen Sharing or Remote Login for this user unless you specifically need it later; Tailscale SSH will handle remote access when the time comes.

## 2. Install tooling as that user

Log in as `artlife-agent`. Everything below installs to that user's home directory only.

```bash
# Homebrew (per-user install, no sudo required for this path)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Core tooling
brew install git uv node@22 tailscale
brew install --cask orbstack        # Docker-compatible runtime, lighter than Docker Desktop

# Claude Code
npm install -g @anthropic-ai/claude-code
```

If Homebrew asks for an administrator password during install, that is the one-time prerequisite for `/opt/homebrew`. Provide it, then never run anything else with sudo under this user.

Verify:

```bash
git --version && uv --version && node --version && docker --version && claude --version
```

## 3. Create a new private repository for Agent OS and clone it with a deploy key

Agent OS lives in its own private repository under the ArtLife GitHub account. It does not live in this repository, and it never touches any GemBreak repository.

On GitHub, signed in as the ArtLife account: New repository, name `artlife-agent-os` (or similar), visibility **Private**, no template, no README (the agent creates one). Then, as `artlife-agent` on the Mac:

```bash
ssh-keygen -t ed25519 -C "artlife-agent@mac-studio" -f ~/.ssh/artlife_deploy
cat ~/.ssh/artlife_deploy.pub
```

Add the public key at the new repository's Settings, Deploy keys, with **Allow write access** enabled, since this machine will push Agent OS commits. Your personal GitHub SSH key stays in your personal account.

```bash
cat >> ~/.ssh/config <<'EOF'
Host github.com-artlife
  HostName github.com
  IdentityFile ~/.ssh/artlife_deploy
  IdentitiesOnly yes
EOF

git clone git@github.com-artlife:AveryArtlife/artlife-agent-os.git ~/artlife
cd ~/artlife
```

Now bring the build prompt in. Download the two files you need from the discovery branch of `art-discovery-agent` and place them in the new repository:

```bash
mkdir -p docs/prior
BASE=https://raw.githubusercontent.com/AveryArtlife/art-discovery-agent/claude/artlife-inquiry-audit-ex64ry/docs/agent-os
curl -fsSL "$BASE/04-master-build-prompt.md" -o docs/00-master-build-prompt.md
for f in 00-discovery 01-decision-matrix 02-open-questions 03-mac-studio-setup; do
  curl -fsSL "$BASE/$f.md" -o "docs/prior/$f.md"
done
git add docs && git commit -m "Add master build prompt and prior discovery documents"
git push -u origin main
```

If the discovery branch has been merged or deleted by then, use `main` in the URL instead. If `art-discovery-agent` is private at that point, download the files through the GitHub web interface and copy them in.

## 4. Do not put secrets in files Claude Code can read

For the discovery and proof-of-concept phases, no real credentials are needed. Mock values only.

When real credentials are eventually needed:

- Store them in the macOS Keychain under the `artlife-agent` user via `security add-generic-password`, or in a `.env` file **outside** the repository at `~/.config/artlife/.env` with permissions `600`.
- The repository's `.gitignore` already excludes `.env` and `.env.*` inside the repo, but the safer habit is to never create one there.
- Claude Code will be told the variable *names* it needs. It will never be given the values in chat.

## 5. Sign in to Claude Code

```bash
cd ~/artlife
claude
```

Sign in with your Anthropic account when prompted. Connectors (Gmail, Google Drive) are per-Anthropic-account, so they carry over. The Mac session will have your normal network, which means it can read the vendor documentation this sandbox could not.

## 6. Paste the build prompt

Open `docs/00-master-build-prompt.md` in the new repository. Copy everything below its first horizontal rule and paste it as your first message. The agent audits the Mac, researches from official sources, scores the frameworks and hosting, writes the threat model and cost proposal, asks you one batch of questions, and stops for your approval. It installs nothing and pays for nothing before that gate.

## 7. Later, when the operator agent goes live (not now)

Recorded here so the account is set up right from the start:

- Tailscale runs as this user with the standalone daemon, not the App Store app, so it survives logout.
- Hermes runs in OrbStack with its Docker backend, `HERMES_WRITE_SAFE_ROOT` pointed at `~/artlife-data`, and the terminal tool disabled.
- Only `~/artlife` and `~/artlife-data` are ever mounted into a container. Never `~`, never `~/Desktop`, never `~/Documents`.
- An owner-only stop command lives at `~/artlife/bin/stop-all` and is also reachable through the operator Telegram bot.

## What this setup does not do

- It does not expose any inbound port on the Mac.
- It does not give the agent user access to your files, photos, messages, or browser profiles. macOS enforces this between standard users.
- It does not install anything system-wide beyond Homebrew's own prefix.
- It does not create any paid resource.
