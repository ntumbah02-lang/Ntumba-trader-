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
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Bot
```bash
cd bot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Docker
```bash
docker compose up --build
```

## Environment
Create and customize these files before running production workloads:
- backend/.env.example
- frontend/.env.example
- bot/.env.example

## API primary routes
- `/health`
- `/api/auth/register`
- `/api/auth/login`
- `/api/summary`
- `/api/markets`
- `/api/signals`
- `/api/portfolio`
- `/api/positions`
- `/api/orders`
- `/api/payments/checkout`
- `/api/payments/status`
- `/api/analytics/overview`

## MVP & production direction
This repository now includes a strong foundation for a serious trading platform, including:
- proper API routing
- secure auth foundation
- modular services and logic
- database-ready architecture
- payment integration hooks
- real-world trading workflow structure

## Roadmap to global top-tier platform
- Live exchange integration and websocket updates
- Real-time order execution with risk checks
- Multi-user subscription management
- Database persistence and migrations
- Advanced backtesting suite
- Automated portfolio rebalancing
- Notification system and alerts
- Cloud deployment pipeline

## Founder
Héritier Ntumba @ntumbah02-lang
