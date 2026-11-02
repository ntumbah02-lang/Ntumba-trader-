from fastapi import APIRouter

from app.data import USER_ACCOUNTS
from app.schemas import UserLogin, UserRegister

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register")
async def register_user(payload: UserRegister):
    user = {
        "name": payload.name,
        "email": payload.email,
        "password": payload.password,
        "token": "demo-token",
    }
    USER_ACCOUNTS[payload.email] = user
    return {
        "status": "success",
        "message": "User registered successfully",
        "user": {"name": payload.name, "email": payload.email},
        "token": user["token"],
    }


@router.post("/login")
async def login_user(payload: UserLogin):
    stored = USER_ACCOUNTS.get(payload.email)
    if not stored or stored["password"] != payload.password:
        return {"status": "error", "message": "Invalid email or password"}

    return {
        "status": "success",
        "message": "Logged in successfully",
        "user": {"name": stored["name"], "email": stored["email"]},
        "token": stored["token"],
    }
