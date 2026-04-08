"""weather-edge CLI entrypoint."""
from __future__ import annotations

import click
from rich.console import Console

from . import db

console = Console()


@click.group()
def cli() -> None:
    """Find high-margin weather bets on Kalshi and Polymarket."""


@cli.command("init-db")
def init_db_cmd() -> None:
    """Create the SQLite database and tables."""
    db.init_db()
    console.print(f"[green]initialized[/green] {db.DB_PATH}")


@cli.command()
def scan() -> None:
    """Scan live markets for edge. (stub)"""
    console.print("[yellow]scan: not implemented yet — next step builds Kalshi fetcher[/yellow]")


@cli.command()
def backtest() -> None:
    """Replay historical markets to validate the strategy. (stub)"""
    console.print("[yellow]backtest: not implemented yet[/yellow]")


if __name__ == "__main__":
    cli()
