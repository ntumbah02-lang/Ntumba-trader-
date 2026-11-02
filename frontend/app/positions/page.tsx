export default function PositionsPage() {
  const positions = [
    { symbol: "BTC/USDT", size: 0.38, entry: 66450.0, current: 67240.56, pnl: 3.2 },
    { symbol: "AAPL", size: 150, entry: 210.0, current: 218.72, pnl: 4.1 },
    { symbol: "EUR/USD", size: 25000, entry: 1.0830, current: 1.0862, pnl: 1.4 },
  ];

  return (
    <main className="dashboard-shell">
      <header className="topbar">
        <div className="brand">POSITIONS</div>
        <nav className="top-actions">
          <a href="/dashboard" className="secondary-btn">Dashboard</a>
          <a href="/markets" className="secondary-btn">Markets</a>
          <a href="/pricing" className="secondary-btn">Pricing</a>
        </nav>
      </header>

      <section className="panel">
        <h2 className="section-title">Open positions</h2>
        <div className="position-grid">
          {positions.map((position) => (
            <div className="position-card" key={position.symbol}>
              <div className="market-row">
                <strong>{position.symbol}</strong>
                <span className="text-green">+{position.pnl}%</span>
              </div>
              <p className="mt-1 text-muted">Size: {position.size}</p>
              <p className="mt-1 text-muted">Entry: {position.entry}</p>
              <p className="mt-1 text-muted">Current: {position.current}</p>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}
