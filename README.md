# art-discovery-agent

## Single-Word .ai Domain Availability Checker

Comprehensive toolkit to check **every single-word .ai domain** for availability across **6 providers**. Includes a 234,000+ word dictionary covering the entire English language plus tech, business, and brandable terms.

### Supported Providers

| Provider | Auth Required? | Pricing Info? | Speed | Accuracy |
|----------|---------------|---------------|-------|----------|
| **RDAP** | No (free) | No | ~2/sec | Excellent |
| **Porkbun** | API key (free account) | Yes | ~0.1/sec | Excellent |
| **Namecheap** | API key (free sandbox) | Yes | ~1/sec | Excellent |
| **GoDaddy** | API key (50+ domains) | Yes | ~1/sec | Excellent |
| **WHOIS** | No (free) | No | ~1/sec | Good |
| **DNS** | No (free) | No | ~10/sec | Low |

### Quick Start

```bash
# 1. Setup
chmod +x setup.sh && ./setup.sh

# 2. Run — pick a provider:

# RDAP — RECOMMENDED: free, no account needed, most reliable
python3 check_ai_domains.py --rdap --max-length 6

# Porkbun — free account, includes pricing
python3 check_ai_domains.py --porkbun-key YOUR_KEY --porkbun-secret YOUR_SECRET

# Namecheap sandbox — free test account
python3 check_ai_domains.py --namecheap-key KEY --namecheap-user USER --namecheap-ip YOUR_IP --namecheap-sandbox

# GoDaddy — needs 50+ domains on account
python3 check_ai_domains.py --godaddy-key KEY --godaddy-secret SECRET

# WHOIS — free, needs whois command installed
python3 check_ai_domains.py --whois --max-length 6

# DNS — fastest, least accurate
python3 check_ai_domains.py --dns
```

### Where to Get API Keys

| Provider | Signup | API Keys |
|----------|--------|----------|
| Porkbun | [porkbun.com](https://porkbun.com) | [porkbun.com/account/api](https://porkbun.com/account/api) |
| Namecheap (sandbox) | [sandbox.namecheap.com](https://www.sandbox.namecheap.com/) | Profile > Tools > API Access |
| GoDaddy | [godaddy.com](https://godaddy.com) | [developer.godaddy.com/keys](https://developer.godaddy.com/keys) |

### Filtering Options

```bash
# Only short words (premium domains)
python3 check_ai_domains.py --rdap --max-length 4

# Only words starting with a-f
python3 check_ai_domains.py --rdap --start-letter a --end-letter f

# Resume after interruption
python3 check_ai_domains.py --rdap --resume

# Custom delay between checks
python3 check_ai_domains.py --rdap --delay 2.0
```

### Output

Results are saved to `results/`:

- **`available.csv`** — Available .ai domains with prices
- **`taken.csv`** — Already registered domains
- **`all_results.csv`** — Every check result
- **`progress.json`** — Resume checkpoint

### Word Count by Length

| Max Length | Word Count | Examples |
|-----------|-----------|---------|
| 1 char | 26 | a.ai, x.ai, z.ai |
| 2 chars | 166 | ai.ai, go.ai, up.ai |
| 3 chars | 1,493 | art.ai, zen.ai, hub.ai |
| 4 chars | 6,497 | code.ai, data.ai, flux.ai |
| 5 chars | 16,489 | dream.ai, spark.ai, cloud.ai |
| 6 chars | 33,966 | oracle.ai, vision.ai, neural.ai |
| 7 chars | 57,688 | quantum.ai, phoenix.ai, diamond.ai |
| 8 chars | 87,533 | infinity.ai, spectrum.ai, paradigm.ai |
| All | 234,000+ | Every English word |

### Files

| File | Description |
|------|-------------|
| `wordlist.txt` | 234,000+ unique English words |
| `check_ai_domains.py` | Main checker (6 providers) |
| `generate_wordlist.py` | Regenerate/customize the word list |
| `setup.sh` | One-command setup |

### Requirements

- Python 3.7+
- `requests` (`pip3 install requests`)
- `nltk` (`pip3 install nltk`) — only for regenerating word list
- `whois` command — for WHOIS method (`apt install whois` or `brew install whois`)
