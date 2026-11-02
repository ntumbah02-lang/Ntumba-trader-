from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers.markets import router as markets_router

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="NTUMBA TRADER platform API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(markets_router)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.environment,
    }


@app.get("/api/summary")
async def summary():
    return {
        "portfolio": {
            "value": 184250.7,
            "pnl": 12.45,
            "daily_change": 2.31,
            "risk": 1.8,
        },
        "markets": [
            {"name": "BTC/USDT", "price": 67240.56, "change": 2.8, "signal": "BUY", "confidence": 84},
            {"name": "EUR/USD", "price": 1.0862, "change": 0.5, "signal": "HOLD", "confidence": 68},
            {"name": "AAPL", "price": 218.72, "change": 1.2, "signal": "BUY", "confidence": 76},
            {"name": "XAU/USD", "price": 2345.42, "change": -0.3, "signal": "SELL", "confidence": 61},
        ],
        "last_update": "2026-11-02T09:45:12Z",
    }
