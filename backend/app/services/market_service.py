from __future__ import annotations

from pathlib import Path

from app.data import BACKTEST, MARKETS, ORDERS, PAYMENT_STATUS, PORTFOLIO_SUMMARY, POSITIONS, SIGNALS


class MarketService:
    def __init__(self, data_dir: str = "."):
        self.data_dir = Path(data_dir)

    def get_market_summary(self):
        return {
            "portfolio": PORTFOLIO_SUMMARY,
            "markets": MARKETS,
            "last_update": "2026-11-02T09:45:12Z",
        }

    def get_markets(self):
        return MARKETS

    def get_signals(self):
        return {"status": "paper-trading", "signals": SIGNALS}

    def get_positions(self):
        return POSITIONS

    def get_orders(self):
        return ORDERS

    def get_backtest(self):
        return BACKTEST

    def get_payment_status(self):
        return PAYMENT_STATUS
