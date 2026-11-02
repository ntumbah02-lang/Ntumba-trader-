"use client";

const summary = {
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
    { name: "ETH/USDT", price: 3520.1, change: 1.9, signal: "BUY", confidence: 81 },
    { name: "XAU/USD", price: 2345.42, change: -0.3, signal: "SELL", confidence: 61 },
  ],
};

export default function DashboardPage() {
  return (
    <main className="dashboard-shell">
      <header className="topbar">
        <div className="brand">NTUMBA-TRADER</div>
        <nav className="top-actions">
          <a href="/" className="secondary-btn">Home</a>
          <a href="/markets" className="secondary-btn">Markets</a>
          <a href="/positions" className="secondary-btn">Positions</a>
          <a href="/pricing" className="secondary-btn">Pricing</a>
          <a href="/login" className="secondary-btn">Login</a>
        </nav>
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
                {market.price < 10 ? market.price.toFixed(4) : market.price.toLocaleString()}
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
