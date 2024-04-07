from datetime import datetime
from sqlalchemy.orm import Session
from models import Refinedstatistics
from sqlalchemy import select

def create_refinedstatistic(db: Session, ticker: str, per: str, fwd_per: str, pbr: str, roe: str, current_ratio: str,
                            quick_ratio: str):
    db_refinedstatistic = Refinedstatistics(
        ticker=ticker,
        modified_at=datetime.today(),
        refined_per=per,
        refined_forward_per=fwd_per,
        refined_pbr=pbr,
        refined_roe=roe,
        current_ratio=current_ratio,
        quick_ratio=quick_ratio)

    db.add(db_refinedstatistic)
    db.commit()

def get_refinedstatistic(db: Session, ticker: str):
    return db.query(Refinedstatistics).order_by(Refinedstatistics.modified_at.desc()).filter(Refinedstatistics.ticker == ticker).all()

def is_refinedstatistic(db: Session, ticker: str, timestamp: str):
    return db.query(Refinedstatistics).filter(ticker == Refinedstatistics.ticker, Refinedstatistics.modified_at == datetime.fromtimestamp(int(
        timestamp) / 1000)).first()

def find_recommendations(db: Session):
    stmt = (select(Refinedstatistics)
            .select_from(Refinedstatistics)
            .filter(Refinedstatistics.modified_at =='2024-04-08'
                    , Refinedstatistics.refined_per <= -0.52
                    ,Refinedstatistics.refined_forward_per <= -0.52
                    , Refinedstatistics.refined_pbr <= -0.52
                    , Refinedstatistics.refined_roe >= 0.52
                    , Refinedstatistics.current_ratio >= 2.0
                    , Refinedstatistics.quick_ratio >= 1.0))
    return db.execute(stmt).scalars().all()