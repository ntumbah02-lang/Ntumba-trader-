export default function HomePage() {
  return (
    <main className="landing-page">
      <div className="hero-card">
        <header className="hero-header">
          <p className="kicker">NTUMBA-TRADER</p>
          <h1 className="hero-title">The real multi-market trading platform.</h1>
          <p className="hero-subtitle">
            Built from Kinshasa to the world. Track crypto, forex, and US stocks with live-style signal analysis,
            risk management, and a paper-trading engine designed for testing before real money.
          </p>

          <div className="hero-actions">
            <a href="/register" className="primary-btn">Create account</a>
            <a href="/login" className="secondary-btn">Login</a>
            <a href="/dashboard" className="secondary-btn">Open dashboard</a>
          </div>
        </header>

        <section className="hero-grid">
          <div className="metric-card">
            <p className="metric-label">Portfolio value</p>
            <h3 className="metric-value">$184,250</h3>
          </div>
          <div className="metric-card">
            <p className="metric-label">24h trend</p>
            <h3 className="metric-value text-green">+2.31%</h3>
          </div>
          <div className="metric-card">
            <p className="metric-label">Risk</p>
            <h3 className="metric-value">1.8%</h3>
          </div>
          <div className="metric-card">
            <p className="metric-label">Bot status</p>
            <h3 className="metric-value text-green">Paper mode</h3>
          </div>
        </section>
      </div>
    </main>
  );
}
