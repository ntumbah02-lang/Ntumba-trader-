export default function MarketsPage() {
  const markets = [
    { symbol: "BTC/USDT", price: 67240.56, signal: "BUY", confidence: 84 },
    { symbol: "ETH/USDT", price: 3520.1, signal: "BUY", confidence: 81 },
    { symbol: "EUR/USD", price: 1.0862, signal: "HOLD", confidence: 68 },
    { symbol: "AAPL", price: 218.72, signal: "BUY", confidence: 76 },
    { symbol: "XAU/USD", price: 2345.42, signal: "SELL", confidence: 61 },
  ];

  return (
    <main className="dashboard-shell">
      <header className="topbar">
        <div className="brand">MARKETS</div>
        <nav className="top-actions">
          <a href="/dashboard" className="secondary-btn">Dashboard</a>
          <a href="/positions" className="secondary-btn">Positions</a>
          <a href="/pricing" className="secondary-btn">Pricing</a>
        </nav>
      </header>

      <section className="panel">
        <h2 className="section-title">Live market board</h2>
        <div className="market-grid">
          {markets.map((market) => (
            <div className="market-card" key={market.symbol}>
              <div className="market-row">
                <strong>{market.symbol}</strong>
                <span className={`signal-tag ${market.signal === "BUY" ? "signal-buy" : market.signal === "SELL" ? "signal-sell" : "signal-hold"}`}>
                  {market.signal}
                </span>
              </div>
              <p className="market-price">
                {market.price < 10 ? market.price.toFixed(4) : market.price.toLocaleString()}
              </p>
              <div className="market-meta">
                <span>Confidence</span>
                <span>{market.confidence}%</span>
              </div>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}
