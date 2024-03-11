from datetime import datetime

from sqlalchemy.orm import Session

from models import Tickers

def create_tickers(db: Session, ticker: str, name: str, industryCode: str, industry: str):
    db_ticker = Tickers(ticker=ticker,
                        name=name,
                        industryCode=industryCode,
                        industry=industry,
                        modified_at=datetime.now())
    db.add(db_ticker)
    db.commit()

def get_tickers(db: Session, ticker: str):
    return db.query(Tickers).filter(Tickers.ticker == ticker).first()