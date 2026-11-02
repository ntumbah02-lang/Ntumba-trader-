from pydantic import BaseModel


class MarketSignal(BaseModel):
    symbol: str
    price: float
    change: float
    signal: str
    confidence: int


class PortfolioSummary(BaseModel):
    value: float
    pnl: float
    daily_change: float
    risk: float
