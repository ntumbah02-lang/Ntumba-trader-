from __future__ import annotations

from fastapi import APIRouter

from app.services.market_service import MarketService
from app.services.strategy_engine import StrategyEngine

router = APIRouter(prefix="/api", tags=["markets"])
market_service = MarketService()
strategy_engine = StrategyEngine()


@router.get("/summary")
async def get_summary():
    return market_service.get_market_summary()


@router.get("/markets")
async def get_markets():
    return market_service.get_markets()


@router.get("/signals")
async def get_signals():
    return market_service.get_signals()


@router.get("/signals/board")
async def get_signal_board():
    return {"signals": market_service.get_signal_board()}


@router.post("/signals/scan")
async def scan_signal(symbol: str = "BTC/USDT", price: float = 67240.56):
    return strategy_engine.score_signal(symbol, price)


@router.get("/backtest")
async def get_backtest():
    return market_service.get_backtest()


@router.get("/markets/live")
async def get_live_markets():
    return {
        "status": "live-simulated",
        "markets": market_service.get_markets(),
        "updated_at": "2026-11-02T09:45:12Z",
    }
