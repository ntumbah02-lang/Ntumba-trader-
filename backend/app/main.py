from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers.auth import router as auth_router
from app.routers.markets import router as markets_router
from app.routers.payments import router as payments_router
from app.routers.portfolio import router as portfolio_router

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="NTUMBA TRADER platform API",
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


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.environment,
    }
