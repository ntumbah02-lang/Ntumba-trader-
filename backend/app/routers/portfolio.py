from fastapi import APIRouter

from app.data import ORDERS, POSITIONS

router = APIRouter(prefix="/api", tags=["portfolio"])


@router.get("/portfolio")
async def get_portfolio():
    return {
        "portfolio": {
            "value": 184250.7,
            "pnl": 12.45,
            "daily_change": 2.31,
            "risk": 1.8,
            "allocation": {"BTC": 38, "FOREX": 28, "STOCKS": 22, "CASH": 12},
        }
    }


@router.get("/positions")
async def get_positions():
    return POSITIONS


@router.get("/orders")
async def get_orders():
    return ORDERS
