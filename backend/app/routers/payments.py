from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import get_current_user, get_db
from app.data import PAYMENT_STATUS

router = APIRouter(prefix="/api/payments", tags=["payments"])


@router.post("/checkout")
async def checkout_payment(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return {
        "status": "pending",
        "checkout_id": "NTB-CHK-2026-2",
        "amount": 49.0,
        "currency": "USD",
        "plan": "premium",
        "provider": "Paylora",
        "checkout_url": "https://paylora.demo/checkout/NTB-CHK-2026-2",
        "owner": user.email,
    }


@router.get("/status")
async def get_payment_status(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return {**PAYMENT_STATUS, "owner": user.email}


@router.get("/plans")
async def get_payment_plans():
    return {
        "plans": [
            {"name": "Starter", "price": 0, "features": ["basic market access", "paper mode", "limited alerts"]},
            {"name": "Premium", "price": 49, "features": ["full market board", "advanced signals", "priority support"]},
            {"name": "Pro", "price": 199, "features": ["team access", "strategy deck", "risk tools"]},
        ]
    }
