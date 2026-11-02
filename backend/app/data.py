PORTFOLIO_SUMMARY = {
    "value": 184250.7,
    "pnl": 12.45,
    "daily_change": 2.31,
    "risk": 1.8,
    "allocation": {
        "BTC": 38,
        "FOREX": 28,
        "STOCKS": 22,
        "CASH": 12,
    },
}

MARKETS = [
    {"name": "BTC/USDT", "price": 67240.56, "change": 2.8, "signal": "BUY", "confidence": 84},
    {"name": "EUR/USD", "price": 1.0862, "change": 0.5, "signal": "HOLD", "confidence": 68},
    {"name": "AAPL", "price": 218.72, "change": 1.2, "signal": "BUY", "confidence": 76},
    {"name": "XAU/USD", "price": 2345.42, "change": -0.3, "signal": "SELL", "confidence": 61},
    {"name": "ETH/USDT", "price": 3520.1, "change": 1.9, "signal": "BUY", "confidence": 81},
]

SIGNALS = [
    {
        "symbol": "BTC/USDT",
        "side": "buy",
        "entry": 67000.0,
        "stop_loss": 64200.0,
        "take_profit": 71000.0,
        "confidence": 84,
    },
    {
        "symbol": "AAPL",
        "side": "buy",
        "entry": 216.0,
        "stop_loss": 206.0,
        "take_profit": 230.0,
        "confidence": 76,
    },
    {
        "symbol": "EUR/USD",
        "side": "hold",
        "entry": 1.0850,
        "stop_loss": 1.0780,
        "take_profit": 1.0950,
        "confidence": 68,
    },
]

POSITIONS = [
    {"symbol": "BTC/USDT", "size": 0.38, "entry": 66450.0, "current": 67240.56, "pnl": 3.2},
    {"symbol": "AAPL", "size": 150, "entry": 210.0, "current": 218.72, "pnl": 4.1},
    {"symbol": "EUR/USD", "size": 25000, "entry": 1.0830, "current": 1.0862, "pnl": 1.4},
]

ORDERS = [
    {"id": "NTB-1001", "symbol": "BTC/USDT", "side": "buy", "quantity": 0.12, "price": 66800.0, "status": "filled"},
    {"id": "NTB-1002", "symbol": "AAPL", "side": "buy", "quantity": 80, "price": 214.5, "status": "filled"},
    {"id": "NTB-1003", "symbol": "EUR/USD", "side": "sell", "quantity": 15000, "price": 1.0880, "status": "pending"},
]

USER_ACCOUNTS = {
    "demo@ntumba-trader.com": {
        "name": "Demo User",
        "email": "demo@ntumba-trader.com",
        "password": "demo123",
        "token": "demo-token",
    }
}

BACKTEST = {
    "strategy": "Momentum + Risk Control",
    "period": "2024-01 to 2024-12",
    "total_return": 26.4,
    "sharpe_ratio": 1.82,
    "max_drawdown": 8.7,
    "win_rate": 63.2,
}

PAYMENT_STATUS = {
    "status": "approved",
    "method": "Paylora",
    "checkout_id": "NTB-CHK-2026-1",
    "amount": 49.0,
    "currency": "USD",
    "plan": "premium",
}
