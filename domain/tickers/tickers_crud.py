from datetime import datetime

from sqlalchemy.orm import Session

from models import Tickers

def create_tickers(db: Session, ticker: str, name: str, industryCode: str, industry: str):
    db_ticker = Tickers(ticker=ticker,
                        name=name,
                        industry_code=industryCode,
                        industry=industry,
                        modified_at=datetime.now())
    db.add(db_ticker)
    db.commit()

def get_ticker(db: Session, ticker: str):
    return db.query(Tickers).filter(Tickers.ticker == ticker).first()

def is_tickers(db: Session, ticker: str, timestamp: str):
    return db.query(Tickers).filter(ticker == Tickers.ticker, Tickers.modified_at == datetime.fromtimestamp(int(
        timestamp) / 1000)).first()

def get_tickers(db: Session):
    return db.query(Tickers).all()

def delete_tickers(db: Session):
    db.query(Tickers).delete()