from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Watchlist(Base):
    __tablename__ = 'watchlist'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    stock_symbol = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)


class Trade(Base):
    __tablename__ = 'trades'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    stock_symbol = Column(String, nullable=False)
    trade_type = Column(String, nullable=False)  # Buy or Sell
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    executed_at = Column(DateTime, nullable=False)


class Alert(Base):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    stock_symbol = Column(String, nullable=False)
    alert_type = Column(String, nullable=False)  # Price alert, volume alert, etc.
    threshold = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)


class StockData(Base):
    __tablename__ = 'stock_data'
    id = Column(Integer, primary_key=True)
    stock_symbol = Column(String, nullable=False)
    open_price = Column(Float, nullable=False)
    high_price = Column(Float, nullable=False)
    low_price = Column(Float, nullable=False)
    close_price = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)
