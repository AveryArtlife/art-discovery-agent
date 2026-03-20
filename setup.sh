#!/bin/bash
# Setup script for .ai Domain Availability Checker
set -e

echo "=== .ai Domain Availability Checker Setup ==="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: python3 is required but not installed."
    exit 1
fi

echo "Python: $(python3 --version)"

# Install dependencies
echo "Installing Python dependencies..."
pip3 install requests nltk 2>/dev/null || pip install requests nltk

# Generate word list if not present
if [ ! -f "wordlist.txt" ]; then
    echo "Generating word list from NLTK corpus..."
    python3 generate_wordlist.py
else
    echo "Word list already exists ($(wc -l < wordlist.txt) words)"
fi

# Create results directory
mkdir -p results

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Quick start:"
echo ""
echo "  # Method 1: WHOIS lookup (no account needed, most accurate)"
echo "  python3 check_ai_domains.py --whois --max-length 6"
echo ""
echo "  # Method 2: DNS check (fastest, less accurate)"
echo "  python3 check_ai_domains.py --dns --max-length 8"
echo ""
echo "  # Method 3: GoDaddy API (need API key from https://developer.godaddy.com/keys)"
echo "  python3 check_ai_domains.py --api-key YOUR_KEY --api-secret YOUR_SECRET"
echo ""
echo "  # Method 4: Web scraping (no account needed)"
echo "  python3 check_ai_domains.py --scrape --max-length 5"
echo ""
echo "Results will be saved to results/ directory."
