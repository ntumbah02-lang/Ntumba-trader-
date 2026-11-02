from __future__ import annotations

from sqlalchemy import Boolean, Column, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./ntumba_trader.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    plan = Column(String, default="starter")


class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, nullable=False)
    value = Column(Float, default=0.0)
    pnl = Column(Float, default=0.0)
    daily_change = Column(Float, default=0.0)
    risk = Column(Float, default=0.0)
    btc_alloc = Column(Float, default=0.0)
    forex_alloc = Column(Float, default=0.0)
    stocks_alloc = Column(Float, default=0.0)
    cash_alloc = Column(Float, default=0.0)


class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    symbol = Column(String, nullable=False)
    size = Column(Float, default=0.0)
    entry = Column(Float, default=0.0)
    current = Column(Float, default=0.0)
    pnl = Column(Float, default=0.0)
    side = Column(String, default="buy")


class TradeOrder(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    order_id = Column(String, unique=True, nullable=False)
    symbol = Column(String, nullable=False)
    side = Column(String, nullable=False)
    quantity = Column(Float, default=0.0)
    price = Column(Float, default=0.0)
    status = Column(String, default="pending")


class MarketSignalRecord(Base):
    __tablename__ = "market_signals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    symbol = Column(String, nullable=False)
    side = Column(String, nullable=False)
    entry = Column(Float, default=0.0)
    stop_loss = Column(Float, default=0.0)
    take_profit = Column(Float, default=0.0)
    confidence = Column(Integer, default=0)


class PaymentRecord(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    provider = Column(String, default="Paylora")
    checkout_id = Column(String, nullable=False)
    amount = Column(Float, default=0.0)
    currency = Column(String, default="USD")
    plan = Column(String, default="premium")
    status = Column(String, default="pending")


Base.metadata.create_all(bind=engine)
