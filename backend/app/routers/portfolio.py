from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import get_db
from app.data import BACKTEST, MARKETS, SIGNALS

router = APIRouter(prefix="/api", tags=["markets"])


@router.get("/summary")
async def get_summary(db: Session = Depends(get_db)):
    return {
        "portfolio": {
            "value": 184250.7,
            "pnl": 12.45,
            "daily_change": 2.31,
            "risk": 1.8,
            "allocation": {"BTC": 38, "FOREX": 28, "STOCKS": 22, "CASH": 12},
        },
        "markets": MARKETS,
        "last_update": "2026-11-02T09:45:12Z",
    }


@router.get("/markets")
async def get_markets(db: Session = Depends(get_db)):
    return MARKETS


@router.get("/signals")
async def get_signals(db: Session = Depends(get_db)):
    return {"status": "paper-trading", "signals": SIGNALS}


@router.get("/backtest")
async def get_backtest(db: Session = Depends(get_db)):
    return BACKTEST
