export default function HomePage() {
  return (
    <main className="landing-page">
      <div className="hero-card">
        <header className="hero-header">
          <p className="kicker">NTUMBA TRADER</p>
          <h1 className="hero-title">A global multi-market trading platform built for performance.</h1>
          <p className="hero-subtitle">
            Built for disciplined operators and serious portfolio management. Track crypto, forex, and U.S. stocks,
            monitor risk in real time, and test execution ideas before any live commitment.
          </p>
          <div className="hero-actions">
            <a href="/register" className="primary-btn">Create account</a>
            <a href="/login" className="secondary-btn">Login</a>
            <a href="/dashboard" className="secondary-btn">Dashboard</a>
          </div>
        </header>

        <section className="hero-grid">
          <div className="metric-card">
            <p className="metric-label">Portfolio value</p>
            <h3 className="metric-value">$184,250</h3>
          </div>
          <div className="metric-card">
            <p className="metric-label">Daily performance</p>
            <h3 className="metric-value text-green">+2.31%</h3>
          </div>
          <div className="metric-card">
            <p className="metric-label">Risk framework</p>
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
