from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class TradeLogEntry:
    symbol: str
    side: str
    entry: float
    stop_loss: float
    take_profit: float
    confidence: int
    risk: float
    status: str


class StrategyEngine:
    def __init__(self, log_file: str = "paper_trade_log.json"):
        self.log_file = Path(log_file)

    def create_trade(self, symbol: str, price: float) -> TradeLogEntry:
        signal = TradeLogEntry(
            symbol=symbol,
            side="buy",
            entry=price,
            stop_loss=price * 0.97,
            take_profit=price * 1.08,
            confidence=84,
            risk=0.02,
            status="paper",
        )
        self.write_log(signal)
        return signal

    def write_log(self, signal: TradeLogEntry) -> None:
        payload = asdict(signal)
        with self.log_file.open("a", encoding="utf-8") as file:
            file.write(json.dumps(payload) + "\n")

    def read_log(self) -> list[dict]:
        if not self.log_file.exists():
            return []
        entries: list[dict] = []
        with self.log_file.open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    entries.append(json.loads(line))
        return entries
