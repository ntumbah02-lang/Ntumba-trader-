from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["markets"])


@router.get("/markets")
async def get_markets():
    return [
        {"name": "BTC/USDT", "price": 67240.56, "change": 2.8, "signal": "BUY", "confidence": 84},
        {"name": "EUR/USD", "price": 1.0862, "change": 0.5, "signal": "HOLD", "confidence": 68},
        {"name": "AAPL", "price": 218.72, "change": 1.2, "signal": "BUY", "confidence": 76},
        {"name": "XAU/USD", "price": 2345.42, "change": -0.3, "signal": "SELL", "confidence": 61},
    ]


@router.get("/signals")
async def get_signals():
    return {
        "status": "paper-trading",
        "signals": [
            {"symbol": "BTC/USDT", "side": "buy", "entry": 67000.0, "stop_loss": 64200.0, "take_profit": 71000.0},
            {"symbol": "AAPL", "side": "buy", "entry": 216.0, "stop_loss": 206.0, "take_profit": 230.0},
        ],
    }
