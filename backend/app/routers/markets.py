from fastapi import APIRouter

from app.data import BACKTEST, MARKETS, ORDERS, PAYMENT_STATUS, PORTFOLIO_SUMMARY, POSITIONS, SIGNALS

router = APIRouter(prefix="/api", tags=["markets"])


@router.get("/summary")
async def get_summary():
    return {
        "portfolio": PORTFOLIO_SUMMARY,
        "markets": MARKETS,
        "last_update": "2026-11-02T09:45:12Z",
    }


@router.get("/markets")
async def get_markets():
    return MARKETS


@router.get("/signals")
async def get_signals():
    return {"status": "paper-trading", "signals": SIGNALS}


@router.get("/backtest")
async def get_backtest():
    return BACKTEST
