"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("demo@ntumba-trader.com");
  const [password, setPassword] = useState("demo123");
  const [message, setMessage] = useState("");

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();

    try {
      const response = await fetch("http://localhost:8000/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();
      if (data.status === "success") {
        localStorage.setItem("ntumba-token", data.token);
        router.push("/dashboard");
      } else {
        setMessage(data.message || "Login failed");
      }
    } catch (error) {
      setMessage("Unable to reach backend. Start the API server first.");
      console.error(error);
    }
  };

  return (
    <main className="auth-page">
      <div className="form-box">
        <h1>Login</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input id="email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input id="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          </div>
          <button className="primary-btn" type="submit">Sign in</button>
        </form>
        {message ? <p className="form-note">{message}</p> : null}
        <p className="form-note">
          No account yet? <Link href="/register">Create one</Link>
        </p>
      </div>
    </main>
  );
}
