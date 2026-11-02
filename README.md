# NTUMBA-TRADER 🌍📈

The Real Multi-Market Trading Platform — from Kinshasa to the world.

Built without a PC, on Android. Testing first, selling later.

## Markets supported
- [x] Crypto (Binance API)
- [x] Forex (OANDA / TwelveData)
- [x] Stocks US (Alpaca)

## Platform architecture
- `/frontend` — Next.js trading dashboard
- `/backend` — FastAPI analytics and portfolio API
- `/bot` — Python paper-trading engine

## Core features
- market overview dashboard
- portfolio and risk summary
- multi-market signal feed
- paper-trading workflow
- Paylora-ready payment layer
- API-first backend

## Quick start

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
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

## Environment variables
Copy and customize the `.env.example` files for backend, frontend, and bot before running the app.

## MVP status
This repository now includes a working full-stack MVP scaffold covering:
- backend API
- dashboard frontend
- market signal view
- paper-trading bot
- payment-ready structure
- Docker support

## Roadmap
- live exchange integration
- authentication and user accounts
- real database persistence
- user subscriptions and Paylora checkout
- real order execution
- backtesting engine
- production deployment
