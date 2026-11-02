# NTUMBA-TRADER 🌍📈

The Real Multi-Market Trading Platform — from Kinshasa to the world.

Built without a PC, on Android. Testing first, selling later.

## Markets supported
- [x] Crypto (Binance API)
- [x] Forex (OANDA / TwelveData)
- [x] Stocks US (Alpaca)

## System architecture
- `/frontend` — Next.js dashboard (Vercel)
- `/backend` — FastAPI analytics engine (Render)
- `/bot` — Python bot + CCXT (paper trading first)

## Philosophy
No fake promises. Every signal has backtest proof + risk management (2% max, SL/TP mandatory).

Founder: Héritier Ntumba @ntumbah02-lang
Paylora integration for DRC payments.

## Quick start

### 1) Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2) Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3) Bot
```bash
cd bot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Environment variables
Copy the `.env.example` files in each app folder and adapt them to your keys.

## Current status
This repository now includes a working starter structure for the platform, including the dashboard, API, and trading bot skeleton with paper trading logic.
