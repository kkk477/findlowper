from datetime import datetime
from sqlalchemy.orm import Session
from models import Refinedstatistics

def create_rawstatistics(db: Session, ticker: str, timestamp: str, per: str, fwd_per: str, pbr: str, roe: str):
    db_refinedstatistic = Refinedstatistics(
        ticker=ticker,
        modified_at=datetime.fromtimestamp(int(timestamp) / 1000),
        refined_per=per,
        refined_forward_per=fwd_per,
        refined_pbr=pbr,
        refined_roe=roe)

    db.add(db_refinedstatistic)
    db.commit()

def get_rawstatistic(db: Session, ticker: str):
    return db.query(Refinedstatistics).order_by(Refinedstatistics.modified_at.desc()).filter(Refinedstatistics.ticker == ticker).all()

def is_rawstatistic(db: Session, ticker: str, timestamp: str):
    return db.query(Refinedstatistics).filter(ticker == Refinedstatistics.ticker , Refinedstatistics.modified_at == datetime.fromtimestamp(int(
        timestamp) / 1000)).first()