from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    plan = Column(String(50), default="starter")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    portfolios = relationship("Portfolio", back_populates="user")
    positions = relationship("Position", back_populates="user")
    orders = relationship("TradeOrder", back_populates="user")
    payment_records = relationship("PaymentRecord", back_populates="user")


class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(120), default="Default")
    value = Column(Float, default=0.0)
    pnl = Column(Float, default=0.0)
    daily_change = Column(Float, default=0.0)
    risk = Column(Float, default=0.0)
    allocation = Column(Text, default="{}")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="portfolios")


class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    symbol = Column(String(50), nullable=False)
    side = Column(String(20), default="buy")
    quantity = Column(Float, default=0.0)
    entry_price = Column(Float, default=0.0)
    current_price = Column(Float, default=0.0)
    pnl = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="positions")


class TradeOrder(Base):
    __tablename__ = "trade_orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    symbol = Column(String(50), nullable=False)
    side = Column(String(20), nullable=False)
    quantity = Column(Float, default=0.0)
    price = Column(Float, default=0.0)
    status = Column(String(30), default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="orders")


class MarketSignalRecord(Base):
    __tablename__ = "market_signal_records"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(50), nullable=False)
    signal = Column(String(20), default="buy")
    entry = Column(Float, default=0.0)
    stop_loss = Column(Float, default=0.0)
    take_profit = Column(Float, default=0.0)
    confidence = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class PaymentRecord(Base):
    __tablename__ = "payment_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    checkout_id = Column(String(120), nullable=False)
    amount = Column(Float, default=0.0)
    currency = Column(String(10), default="USD")
    plan = Column(String(40), default="premium")
    status = Column(String(30), default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="payment_records")
