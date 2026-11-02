from fastapi import APIRouter

from app.data import PAYMENT_STATUS

router = APIRouter(prefix="/api/payments", tags=["payments"])


@router.post("/checkout")
async def checkout_payment():
    return {
        "status": "pending",
        "checkout_id": "NTB-CHK-2026-2",
        "amount": 49.0,
        "currency": "USD",
        "plan": "premium",
        "provider": "Paylora",
        "checkout_url": "https://paylora.demo/checkout/NTB-CHK-2026-2",
    }


@router.get("/status")
async def get_payment_status():
    return PAYMENT_STATUS
