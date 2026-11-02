from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers.analytics import router as analytics_router
from app.routers.auth import router as auth_router
from app.routers.markets import router as markets_router
from app.routers.payments import router as payments_router
from app.routers.portfolio import router as portfolio_router

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="NTUMBA TRADER — multi-market signal and trading platform API",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(markets_router)
app.include_router(portfolio_router)
app.include_router(payments_router)
app.include_router(analytics_router)


@app.get("/health")
async def health_check() -> dict[str, Any]:
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.environment,
        "version": "1.0.0",
    }


@app.get("/api/healthz")
async def healthz() -> dict[str, Any]:
    return {
        "status": "healthy",
        "message": "Everything is operational",
    }


@app.get("/")
async def root() -> dict[str, Any]:
    return {
        "project": settings.app_name,
        "status": "active",
        "features": [
            "multi-market data",
            "paper trading",
            "portfolio oversight",
            "risk controls",
            "auth and payments",
        ],
    }
