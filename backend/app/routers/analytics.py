from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import get_current_user, get_db
from app.data import BACKTEST, MARKETS, SIGNALS

router = APIRouter(prefix="/api/analytics", tags=["analytics"])


@router.get("/overview")
async def analytics_overview(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return {
        "owner": user.email,
        "portfolio_value": 184250.7,
        "daily_return": 2.31,
        "sharpe": 1.82,
        "volatility": 12.4,
        "drawdown": 8.7,
        "markets_tracked": len(MARKETS),
        "signals_generated": len(SIGNALS),
    }


@router.get("/risk")
async def analytics_risk(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return {
        "owner": user.email,
        "risk_level": "moderate",
        "max_risk_per_trade": 0.02,
        "daily_loss_limit": 0.05,
        "stress_test": "passed",
    }


@router.get("/backtest")
async def analytics_backtest(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return {"owner": user.email, **BACKTEST}
