"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";

export default function RegisterPage() {
  const router = useRouter();
  const [name, setName] = useState("Ntumba User");
  const [email, setEmail] = useState("user@ntumba-trader.com");
  const [password, setPassword] = useState("securepass123");
  const [message, setMessage] = useState("");

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/api/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password }),
      });
      const data = await response.json();
      if (data.status === "success") {
        localStorage.setItem("ntumba-token", data.token);
        router.push("/dashboard");
      } else {
        setMessage(data.detail || data.message || "Registration failed");
      }
    } catch (error) {
      console.error(error);
      setMessage("Unable to reach backend. Start the API server first.");
    }
  };

  return (
    <main className="auth-page">
      <div className="form-box">
        <h1>Create account</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="name">Full name</label>
            <input id="name" type="text" value={name} onChange={(e) => setName(e.target.value)} required />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input id="email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input id="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          </div>
          <button className="primary-btn" type="submit">Create account</button>
        </form>
        {message ? <p className="form-note">{message}</p> : null}
        <p className="form-note">
          Already registered? <Link href="/login">Login</Link>
        </p>
      </div>
    </main>
  );
}
