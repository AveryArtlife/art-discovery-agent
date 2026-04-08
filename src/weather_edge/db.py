"""SQLite schema and connection helper for weather-edge."""
from __future__ import annotations

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[2] / "data" / "weather_edge.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS markets (
    ticker TEXT PRIMARY KEY,
    source TEXT NOT NULL,            -- 'kalshi' | 'polymarket'
    series TEXT,                     -- e.g. 'KXHIGH'
    location TEXT,                   -- airport / station code
    threshold REAL,                  -- temperature threshold
    direction TEXT,                  -- 'above' | 'below' | 'between'
    open_date TEXT,
    close_date TEXT,
    settle_date TEXT,
    yes_price REAL,
    no_price REAL,
    fetched_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS forecasts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    market_ticker TEXT NOT NULL,
    model TEXT NOT NULL,             -- 'gfs' | 'ecmwf' | 'best_match'
    forecast_value REAL,             -- predicted high temp
    prob_yes REAL,                   -- model probability of YES
    fetched_at TEXT NOT NULL,
    FOREIGN KEY (market_ticker) REFERENCES markets(ticker)
);

CREATE TABLE IF NOT EXISTS opportunities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    market_ticker TEXT NOT NULL,
    model_prob REAL NOT NULL,
    market_prob REAL NOT NULL,
    edge REAL NOT NULL,              -- model_prob - market_prob
    kelly_fraction REAL,
    recommended_size REAL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (market_ticker) REFERENCES markets(ticker)
);

CREATE TABLE IF NOT EXISTS bets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    market_ticker TEXT NOT NULL,
    side TEXT NOT NULL,              -- 'yes' | 'no'
    size REAL NOT NULL,
    entry_price REAL NOT NULL,
    status TEXT NOT NULL,            -- 'open' | 'settled' | 'cancelled'
    resolved_price REAL,
    pnl REAL,
    placed_at TEXT NOT NULL,
    settled_at TEXT
);

-- Historical data for backtesting
CREATE TABLE IF NOT EXISTS historical_markets (
    ticker TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    location TEXT,
    threshold REAL,
    direction TEXT,
    close_date TEXT,
    settle_date TEXT,
    final_yes_price REAL,            -- last traded YES price before close
    outcome INTEGER,                 -- 1 if YES won, 0 if NO won
    forecast_snapshots TEXT          -- JSON array of {ts, model, value, prob}
);
"""


def connect(path: Path | None = None) -> sqlite3.Connection:
    p = path or DB_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(p)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(path: Path | None = None) -> None:
    conn = connect(path)
    try:
        conn.executescript(SCHEMA)
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    print(f"Initialized {DB_PATH}")
