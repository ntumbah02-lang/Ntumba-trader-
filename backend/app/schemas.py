from typing import Literal

from pydantic import BaseModel, Field


class MarketAsset(BaseModel):
    name: str
    price: float
    change: float
    signal: Literal["BUY", "SELL", "HOLD"]
    confidence: int


class PortfolioSummary(BaseModel):
    value: float
    pnl: float
    daily_change: float
    risk: float
    allocation: dict[str, float] = Field(default_factory=dict)


class SignalEntry(BaseModel):
    symbol: str
    side: Literal["buy", "sell", "hold"]
    entry: float
    stop_loss: float
    take_profit: float
    confidence: int


class OrderRecord(BaseModel):
    id: str
    symbol: str
    side: str
    quantity: float
    price: float
    status: str


class UserRegister(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class PaymentCheckout(BaseModel):
    amount: float
    currency: str = "USD"
    plan: str = "premium"
