"use client";

import { useEffect, useState } from "react";

interface SummaryData {
  portfolio: {
    value: number;
    pnl: number;
    daily_change: number;
    risk: number;
    allocation: Record<string, number>;
  };
  markets: Array<{
    name: string;
    price: number;
    change: number;
    signal: string;
    confidence: number;
  }>;
  last_update: string;
}

export default function DashboardPage() {
  const [data, setData] = useState<SummaryData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSummary = async () => {
      try {
        const response = await fetch("http://localhost:8000/api/summary", {
          method: "GET",
        });
        const payload = await response.json();
        setData(payload);
      } catch (error) {
        console.error("Failed to load market summary", error);
      } finally {
        setLoading(false);
      }
    };

    fetchSummary();
  }, []);

  if (loading) {
    return <main className="dashboard-shell"><p>Loading dashboard...</p></main>;
  }

  const summary = data ?? {
    portfolio: {
      value: 184250.7,
      pnl: 12.45,
      daily_change: 2.31,
      risk: 1.8,
      allocation: { BTC: 38, FOREX: 28, STOCKS: 22, CASH: 12 },
    },
    markets: [
      { name: "BTC/USDT", price: 67240.56, change: 2.8, signal: "BUY", confidence: 84 },
      { name: "EUR/USD", price: 1.0862, change: 0.5, signal: "HOLD", confidence: 68 },
      { name: "AAPL", price: 218.72, change: 1.2, signal: "BUY", confidence: 76 },
    ],
    last_update: "2026-11-02T09:45:12Z",
  };

  return (
    <main className="dashboard-shell">
      <header className="topbar">
        <div className="brand">NTUMBA-TRADER</div>
        <div className="top-actions">
          <a href="/" className="secondary-btn">Home</a>
          <a href="/login" className="secondary-btn">Login</a>
        </div>
      </header>

      <section className="summary-grid">
        <div className="metric-card">
          <p className="metric-label">Portfolio value</p>
          <h3 className="metric-value">${summary.portfolio.value.toLocaleString()}</h3>
        </div>
        <div className="metric-card">
          <p className="metric-label">P&amp;L</p>
          <h3 className="metric-value text-green">+{summary.portfolio.pnl}%</h3>
        </div>
        <div className="metric-card">
          <p className="metric-label">Daily change</p>
          <h3 className="metric-value text-green">+{summary.portfolio.daily_change}%</h3>
        </div>
        <div className="metric-card">
          <p className="metric-label">Risk</p>
          <h3 className="metric-value">{summary.portfolio.risk}%</h3>
        </div>
      </section>

      <section className="panel mt-2">
        <h2 className="section-title">Market overview</h2>
        <div className="market-grid">
          {summary.markets.map((market) => (
            <div className="market-card" key={market.name}>
              <div className="market-row">
                <strong>{market.name}</strong>
                <span className={`signal-tag ${market.signal === "BUY" ? "signal-buy" : market.signal === "SELL" ? "signal-sell" : "signal-hold"}`}>
                  {market.signal}
                </span>
              </div>
              <p className="market-price">
                {typeof market.price === "number" && market.price < 10 ? market.price.toFixed(4) : market.price.toLocaleString()}
              </p>
              <div className="market-meta">
                <span>{market.change > 0 ? "+" : ""}{market.change}%</span>
                <span>{market.confidence}% confidence</span>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="panel mt-2">
        <h2 className="section-title">Allocation</h2>
        <div className="position-grid">
          {Object.entries(summary.portfolio.allocation).map(([key, value]) => (
            <div className="position-card" key={key}>
              <div className="text-muted">{key}</div>
              <div className="market-price" style={{ fontSize: "1.2rem" }}>{value}%</div>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}
