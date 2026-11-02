# NTUMBA-TRADER 🌍📈
The Real Multi-Market Trading Platform - From Kinshasa to the World.

> Built without a PC, on Android. Testing first, selling later.

## Markets Supported
- [x] Crypto (Binance API)
- [x] Forex (OANDA / TwelveData)
- [x] Stocks US (Alpaca)

## Production stack
- Frontend: Next.js dashboard on Vercel
- Backend: FastAPI analysis engine on Render or VPS
- Database: PostgreSQL + Redis
- Bot: Python + CCXT paper trading
- Security: JWT + risk controls + environment-based config

## Philosophy
No fake promises. Every signal has backtest proof + Risk Management (2% max, SL/TP mandatory).

Founder: Héritier Ntumba @ntumbah02-lang
Paylora Integration for DRC Payments

## Run locally
```bash
docker compose up --build
```

## Production notes
- Set `SECRET_KEY` and `DATABASE_URL` in environment variables.
- Use Postgres in production instead of SQLite.
- Keep maximum risk per trade below 2%.
