# art-discovery-agent

## Single-Word .ai Domain Availability Checker

Comprehensive toolkit to check **every single-word .ai domain** for availability on GoDaddy. Includes a 234,000+ word dictionary covering the entire English language plus tech, business, and brandable terms.

### What's Included

| File | Description |
|------|-------------|
| `wordlist.txt` | 234,000+ unique English words (a-z, aa-zyzomys) |
| `check_ai_domains.py` | Main checker script with 4 check methods |
| `generate_wordlist.py` | Regenerate/customize the word list |
| `setup.sh` | One-command setup |

### Quick Start

```bash
# 1. Setup
chmod +x setup.sh && ./setup.sh

# 2. Run (pick a method)

# WHOIS lookup — most accurate, no account needed, ~1 domain/sec
python3 check_ai_domains.py --whois --max-length 6

# DNS check — fastest (~10/sec), but less accurate
python3 check_ai_domains.py --dns

# GoDaddy API — official, needs API key from https://developer.godaddy.com/keys
python3 check_ai_domains.py --api-key YOUR_KEY --api-secret YOUR_SECRET

# Web scrape — no account needed, moderate speed
python3 check_ai_domains.py --scrape --max-length 5
```

### Filtering Options

```bash
# Only short words (premium domains)
python3 check_ai_domains.py --whois --max-length 4

# Only words starting with a-f
python3 check_ai_domains.py --whois --start-letter a --end-letter f

# Resume after interruption
python3 check_ai_domains.py --whois --resume

# Custom delay between checks
python3 check_ai_domains.py --whois --delay 2.0
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

### Requirements

- Python 3.7+
- `requests` (`pip3 install requests`)
- `nltk` (`pip3 install nltk`) — only for regenerating word list
- `whois` command — for WHOIS method (`apt install whois` or `brew install whois`)
