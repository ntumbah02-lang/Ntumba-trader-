from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import get_current_user, get_db
from app.data import ORDERS, POSITIONS

router = APIRouter(prefix="/api", tags=["portfolio"])


@router.get("/portfolio")
async def get_portfolio(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return {
        "portfolio": {
            "value": 184250.7,
            "pnl": 12.45,
            "daily_change": 2.31,
            "risk": 1.8,
            "allocation": {"BTC": 38, "FOREX": 28, "STOCKS": 22, "CASH": 12},
            "owner": user.email,
        }
    }


@router.get("/positions")
async def get_positions(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return {"positions": POSITIONS, "owner": user.email}


@router.get("/orders")
async def get_orders(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return {"orders": ORDERS, "owner": user.email}


@router.get("/risk")
async def get_risk_summary(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return {
        "owner": user.email,
        "risk": 1.8,
        "max_daily_loss": 0.02,
        "stop_loss_required": True,
        "exposure": 0.42,
    }
