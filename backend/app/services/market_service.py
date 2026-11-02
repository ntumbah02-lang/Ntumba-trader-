from __future__ import annotations

from typing import Any

from app.data import BACKTEST, MARKETS, ORDERS, PAYMENT_STATUS, PORTFOLIO_SUMMARY, POSITIONS, SIGNALS


class MarketService:
    def get_market_summary(self) -> dict[str, Any]:
        return {
            "portfolio": PORTFOLIO_SUMMARY,
            "markets": MARKETS,
            "last_update": "2026-11-02T09:45:12Z",
        }

    def get_markets(self) -> list[dict[str, Any]]:
        return MARKETS

    def get_signals(self) -> dict[str, Any]:
        return {"status": "paper-trading", "signals": SIGNALS}

    def get_positions(self) -> list[dict[str, Any]]:
        return POSITIONS

    def get_orders(self) -> list[dict[str, Any]]:
        return ORDERS

    def get_backtest(self) -> dict[str, Any]:
        return BACKTEST

    def get_payment_status(self) -> dict[str, Any]:
        return PAYMENT_STATUS

    def get_signal_board(self) -> list[dict[str, Any]]:
        return [
            {
                "symbol": item["symbol"] if "symbol" in item else item["name"],
                "side": item.get("signal", "HOLD").lower(),
                "entry": item["price"],
                "stop_loss": item["price"] * 0.97,
                "take_profit": item["price"] * 1.08,
                "confidence": item.get("confidence", 70),
            }
            for item in MARKETS
        ]
