from __future__ import annotations


class StrategyEngine:
    def calculate_position_size(self, account_balance: float, risk_percent: float, stop_distance: float) -> float:
        if stop_distance <= 0:
            return 0.0
        risk_amount = account_balance * risk_percent
        return risk_amount / stop_distance

    def expected_move(self, entry: float, stop_loss: float, take_profit: float) -> dict[str, float]:
        risk = abs(entry - stop_loss)
        reward = abs(take_profit - entry)
        return {"risk": risk, "reward": reward, "rr_ratio": reward / risk if risk else 0.0}

    def quality_score(self, confidence: int, rr_ratio: float) -> float:
        return min(100.0, (confidence * 0.7) + (rr_ratio * 20))
