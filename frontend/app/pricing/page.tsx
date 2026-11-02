export default function PricingPage() {
  const plans = [
    { name: "Starter", price: "$0", features: ["Basic signal access", "Paper trading", "Limited alerts"] },
    { name: "Premium", price: "$49", features: ["Full market board", "Advanced signals", "Priority support"] },
    { name: "Pro", price: "$199", features: ["Strategy tools", "Team access", "High-priority execution"] },
  ];

  return (
    <main className="dashboard-shell">
      <header className="topbar">
        <div className="brand">PRICING</div>
        <nav className="top-actions">
          <a href="/dashboard" className="secondary-btn">Dashboard</a>
          <a href="/markets" className="secondary-btn">Markets</a>
          <a href="/login" className="secondary-btn">Login</a>
        </nav>
      </header>

      <section className="payment-grid">
        {plans.map((plan) => (
          <div key={plan.name} className="panel">
            <h3>{plan.name}</h3>
            <p className="market-price" style={{ fontSize: "2rem" }}>{plan.price}</p>
            <ul>
              {plan.features.map((feature) => (
                <li key={feature}>{feature}</li>
              ))}
            </ul>
            <button className="primary-btn mt-2">Choose {plan.name}</button>
          </div>
        ))}
      </section>
    </main>
  );
}
