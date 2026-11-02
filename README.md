# NTUMBA-TRADER 🌍📈

The Real Multi-Market Trading Platform — built for operators who want performance, discipline, and a scalable trading workflow.

From Kinshasa to the world: crypto, forex, and U.S. equities, all unified into one trading intelligence platform.

## What is included
- Multi-market dashboard
- Portfolio and risk monitoring
- Strategy signal engine
- Paper trading workflow
- Admin-ready backend APIs
- JWT authentication layer
- SQLAlchemy database models
- Paylora-ready payment endpoints
- Docker deployment setup

## Architecture
- `/frontend` — Next.js dashboard and trading UI
- `/backend` — FastAPI analytics, auth, payments, and orchestration layer
- `/bot` — Python paper-trading engine with risk logic

## Core system capabilities
- Crypto: Binance
- Forex: OANDA / TwelveData
- US Stocks: Alpaca
- Paper trading by default
- SL / TP enforcement logic
- Risk-weighted position sizing
- Secure session tokens and account registration

## Local setup

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
